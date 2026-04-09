from __future__ import annotations

import math
from dataclasses import dataclass

from .constants import EPSILON
from .vec2 import Vec2

_TEXT_MARKER = "\x01"


@dataclass
class Vertex:
    name: str = "null"
    x: float = 0.0
    y: float = 0.0
    dx: float = 0.0
    dy: float = 0.0
    debug: bool = False

    def copy(self) -> Vertex:
        return Vertex(self.name, self.x, self.y, self.dx, self.dy, self.debug)

    def get_name(self) -> str:
        idx = self.name.find(_TEXT_MARKER)
        return self.name[:idx] if idx != -1 else self.name

    def has_text(self) -> bool:
        return _TEXT_MARKER in self.name

    def add_text(self, s: str) -> None:
        self.name += _TEXT_MARKER + s

    def get_text(self) -> str:
        idx = self.name.find(_TEXT_MARKER)
        return self.name[idx + 1 :] if idx != -1 else ""

    def clear_text(self) -> None:
        idx = self.name.find(_TEXT_MARKER)
        if idx != -1:
            self.name = self.name[:idx]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vertex):
            return NotImplemented
        n = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return -EPSILON < n < EPSILON

    def __hash__(self) -> int:
        return id(self)

    def equivalent(self, other: Vertex) -> bool:
        n1 = math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        n2 = math.sqrt((other.dx - self.dx) ** 2 + (other.dy - self.dy) ** 2)
        return (-EPSILON < n1 < EPSILON) and (-EPSILON < n2 < EPSILON)

    def apply_shift(self, angle: float, scale: float) -> Vertex:
        """Compute visual point incorporating shift data.

        *angle* in degrees, *scale* in percent.
        """
        rad = angle * math.pi / 180.0
        mm_to_unit = 5.0
        new_x = self.x + 100.0 / scale * (mm_to_unit * (self.dx * math.cos(rad) + self.dy * math.sin(rad)))
        new_y = self.y + 100.0 / scale * (mm_to_unit * (-self.dx * math.sin(rad) + self.dy * math.cos(rad)))
        return Vertex(self.name, new_x, new_y)

    def get_angle_from_horizontal(self, v: Vertex, angle: float, scale: float) -> float:
        self.apply_shift(angle, scale)
        v.apply_shift(angle, scale)
        if self == v:
            return 0.0
        res = math.atan2(v.y - self.y, v.x - self.x)
        if res < 0:
            res += 2 * math.pi
        return 180 * res / math.pi

    # -- geometric operations -----------------------------------------------

    def middle(self, v: Vertex) -> Vertex:
        return self.fraction(v, 1, 2)

    def fraction(self, v: Vertex, n: int, d: int) -> Vertex:
        vr = Vertex("null", self.x + n * (v.x - self.x) / d, self.y + n * (v.y - self.y) / d)
        if not (self == v):
            vr.dx = (d - n) / d * self.dx + n / d * v.dx
            vr.dy = (d - n) / d * self.dy + n / d * v.dy
        return vr

    def _basic_symmetry(self, a: Vertex, b: Vertex) -> Vertex:
        u = Vec2.between(a, b)
        n = u.norm()
        u = u / n
        # Q = projection of self onto line AB
        v_a_self = Vec2.between(a, self)
        proj_len = v_a_self.dot(u)
        q = Vertex("null", a.x + proj_len * u.x, a.y + proj_len * u.y)
        # P = self + 2*(Q - self)
        return Vertex("null", self.x + 2 * (q.x - self.x), self.y + 2 * (q.y - self.y))

    def symmetry(self, a: Vertex, b: Vertex, angle: float, scale: float) -> Vertex:
        if a == b:
            raise ValueError(f"{a.get_name()} equivalent to {b.get_name()}")
        p = self._basic_symmetry(a, b)

        s = self.apply_shift(angle, scale)
        a_bis = a.apply_shift(angle, scale)
        b_bis = b.apply_shift(angle, scale)
        if not (a_bis == b_bis):
            p_bis = s._basic_symmetry(a_bis, b_bis)
        else:
            p_bis = p.copy()

        v = Vec2.between(p, p_bis)
        rad = angle * math.pi / 180.0
        unit_to_mm = 1.0 / 5.0
        p.dx = scale / 100.0 * unit_to_mm * (math.cos(rad) * v.x - math.sin(rad) * v.y)
        p.dy = scale / 100.0 * unit_to_mm * (math.sin(rad) * v.x + math.cos(rad) * v.y)
        return p

    def _basic_intersection(self, a: Vertex, b: Vertex, c: Vertex) -> Vertex:
        a1 = self.y - a.y
        b1 = a.x - self.x
        c1 = a1 * self.x + b1 * self.y
        a2 = b.y - c.y
        b2 = c.x - b.x
        c2 = a2 * c.x + b2 * c.y
        det = a1 * b2 - a2 * b1
        if det == 0:
            raise ValueError("Lines are parallel (det=0)")
        _x = (c1 * b2 - b1 * c2) / det
        _y = (a1 * c2 - a2 * c1) / det
        return Vertex("null", _x, _y)

    def intersection(self, a: Vertex, b: Vertex, c: Vertex, angle: float, scale: float) -> Vertex:
        i = self._basic_intersection(a, b, c)
        v1 = self.apply_shift(angle, scale)
        v2 = a.apply_shift(angle, scale)
        v3 = b.apply_shift(angle, scale)
        v4 = c.apply_shift(angle, scale)
        try:
            i_bis = v1._basic_intersection(v2, v3, v4)
        except ValueError:
            i_bis = i.copy()
        v = Vec2.between(i, i_bis)
        rad = angle * math.pi / 180.0
        unit_to_mm = 1.0 / 5.0
        i.dx = scale / 100.0 * unit_to_mm * (math.cos(rad) * v.x - math.sin(rad) * v.y)
        i.dy = scale / 100.0 * unit_to_mm * (math.sin(rad) * v.x + math.cos(rad) * v.y)
        return i

    def bissector(self, a: Vertex, b: Vertex, angle: float, scale: float) -> Vertex:
        u = Vec2.between(self, a)
        v = Vec2.between(self, b)
        nu = u.norm()
        nv = v.norm()
        if nu < EPSILON or nv < EPSILON:
            raise ValueError("Undefined bissector")
        u = u / nu
        v = v / nv
        w = u + v
        if w.sqr_norm() < EPSILON:
            w = u.ortho()
        q = Vertex("null", self.x + w.x, self.y + w.y)
        return self.intersection(q, a, b, angle, scale)

    def mediator(self, a: Vertex, b: Vertex, c: Vertex, angle: float, scale: float) -> Vertex:
        m = self.middle(a)
        u = Vec2.between(self, a)
        v = u.ortho()
        mp = Vertex("null", m.x + v.x, m.y + v.y)
        return m.intersection(mp, b, c, angle, scale)

    def projection(self, a: Vertex, b: Vertex) -> Vertex:
        u = Vec2.between(a, b)
        n = u.norm()
        u = u / n
        v_a_self = Vec2.between(a, self)
        proj_len = v_a_self.dot(u)
        return Vertex("null", a.x + proj_len * u.x, a.y + proj_len * u.y)

    def vertex_to_line(
        self,
        pivot: Vertex,
        b: Vertex,
        c: Vertex,
        d: Vertex,
        e: Vertex,
        first: bool,
        angle: float,
        scale: float,
    ) -> Vertex:
        """Fold vertex *self* onto line (B,C) around *pivot*, return intersection with (D,E)."""
        bc = Vec2.between(b, c)
        a_coeff = -bc.y
        b_coeff = bc.x
        c_coeff = a_coeff * b.x + b_coeff * b.y
        r2 = Vec2.between(pivot, self).sqr_norm()

        if a_coeff == 0:
            if b_coeff == 0:
                raise ValueError("Equal points in vertex_to_line")
            y1 = c_coeff / b_coeff
            s = r2 - (y1 - pivot.y) ** 2
            if s < 0:
                raise ValueError("No intersections in vertex_to_line")
            p1 = Vertex("null", pivot.x + math.sqrt(s), y1)
            p2 = Vertex("null", pivot.x - math.sqrt(s), y1)
        else:
            a0 = (b_coeff / a_coeff) ** 2 + 1
            b0 = 2 * ((pivot.x - c_coeff / a_coeff) * b_coeff / a_coeff - pivot.y)
            c0 = (-(pivot.x) + c_coeff / a_coeff) ** 2 + pivot.y**2 - r2
            delta = b0**2 - 4 * a0 * c0
            if delta < 0:
                raise ValueError("No intersections in vertex_to_line")
            y1 = (-b0 - math.sqrt(delta)) / (2 * a0)
            y2 = (-b0 + math.sqrt(delta)) / (2 * a0)
            x1 = (c_coeff - b_coeff * y1) / a_coeff
            x2 = (c_coeff - b_coeff * y2) / a_coeff
            p1 = Vertex("null", x1, y1)
            p2 = Vertex("null", x2, y2)

        v = Vec2.between(pivot, self)
        v1 = Vec2.between(pivot, p1)
        v2 = Vec2.between(pivot, p2)
        angle1 = math.atan2(v1.y, v1.x) - math.atan2(v.y, v.x)
        angle2 = math.atan2(v2.y, v2.x) - math.atan2(v.y, v.x)
        if angle1 < 0:
            angle1 += 2 * math.pi
        if angle2 < 0:
            angle2 += 2 * math.pi
        if first:
            chosen = p1 if angle1 < angle2 else p2
        else:
            chosen = p2 if angle1 < angle2 else p1

        q = pivot.bissector(self, chosen, angle, scale)
        return pivot.intersection(q, d, e, angle, scale)

    def distance_to_line(self, a: Vertex, b: Vertex) -> float:
        proj = self.projection(a, b)
        return Vec2.between(self, proj).norm()

    def is_parallel(self, a: Vertex, b: Vertex, c: Vertex) -> bool:
        v1 = Vec2.between(self, a)
        v2 = Vec2.between(b, c)
        ps = v1.dot(v2)
        n = v1.norm() * v2.norm()
        ps = abs(ps)
        return ps > 0.99 * n and ps < 1.01 * n

    def is_orthogonal(self, a: Vertex, b: Vertex, c: Vertex) -> bool:
        v1 = Vec2.between(self, a)
        v2 = Vec2.between(b, c)
        ps = v1.dot(v2)
        n = v1.norm() * v2.norm()
        return -0.01 * n < ps < 0.01 * n
