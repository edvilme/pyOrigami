"""Pure geometric operations on vertices.

Each function takes :class:`Vertex` instances as arguments and returns
new :class:`Vertex` results, keeping algorithmic logic separate from
the :class:`Vertex` data model.

Derived from ``doodle/src/vertex.cpp`` in the
`DOODLE <https://doodle.sourceforge.net/>`_ project by Olivier Bettens.
"""

from __future__ import annotations

import math

from .constants import EPSILON
from .vector import Vector
from .vertex import Vertex

# ---------------------------------------------------------------------------
# Basic (no shift) helpers
# ---------------------------------------------------------------------------


def _basic_symmetry(point: Vertex, a: Vertex, b: Vertex) -> Vertex:
    u = Vector.between(a, b)
    n = u.norm()
    u = u / n
    v_a_self = Vector.between(a, point)
    proj_len = v_a_self.dot(u)
    q = Vertex("null", a.x + proj_len * u.x, a.y + proj_len * u.y)
    return Vertex("null", point.x + 2 * (q.x - point.x), point.y + 2 * (q.y - point.y))


def _basic_intersection(v1: Vertex, v2: Vertex, v3: Vertex, v4: Vertex) -> Vertex:
    a1 = v1.y - v2.y
    b1 = v2.x - v1.x
    c1 = a1 * v1.x + b1 * v1.y
    a2 = v3.y - v4.y
    b2 = v4.x - v3.x
    c2 = a2 * v4.x + b2 * v4.y
    det = a1 * b2 - a2 * b1
    if det == 0:
        raise ValueError("Lines are parallel (det=0)")
    _x = (c1 * b2 - b1 * c2) / det
    _y = (a1 * c2 - a2 * c1) / det
    return Vertex("null", _x, _y)


def _compute_shift(base: Vertex, shifted: Vertex, angle: float, scale: float) -> None:
    """Set *base*.dx, *base*.dy from the displacement to *shifted*."""
    v = Vector.between(base, shifted)
    rad = angle * math.pi / 180.0
    unit_to_mm = 1.0 / 5.0
    base.dx = scale / 100.0 * unit_to_mm * (math.cos(rad) * v.x - math.sin(rad) * v.y)
    base.dy = scale / 100.0 * unit_to_mm * (math.sin(rad) * v.x + math.cos(rad) * v.y)


# ---------------------------------------------------------------------------
# Public operations
# ---------------------------------------------------------------------------


def middle(a: Vertex, b: Vertex) -> Vertex:
    """Midpoint of *a* and *b*."""
    return fraction(a, b, 1, 2)


def fraction(a: Vertex, b: Vertex, n: int, d: int) -> Vertex:
    """Point dividing segment *a*–*b* in ratio *n*/*d*."""
    vr = Vertex("null", a.x + n * (b.x - a.x) / d, a.y + n * (b.y - a.y) / d)
    if not (a == b):
        vr.dx = (d - n) / d * a.dx + n / d * b.dx
        vr.dy = (d - n) / d * a.dy + n / d * b.dy
    return vr


def symmetry(point: Vertex, a: Vertex, b: Vertex, angle: float, scale: float) -> Vertex:
    """Reflect *point* across line (*a*, *b*)."""
    if a == b:
        raise ValueError(f"{a.get_name()} equivalent to {b.get_name()}")
    p = _basic_symmetry(point, a, b)

    s = point.apply_shift(angle, scale)
    a_bis = a.apply_shift(angle, scale)
    b_bis = b.apply_shift(angle, scale)
    if not (a_bis == b_bis):
        p_bis = _basic_symmetry(s, a_bis, b_bis)
    else:
        p_bis = p.copy()

    _compute_shift(p, p_bis, angle, scale)
    return p


def intersection(v1: Vertex, v2: Vertex, v3: Vertex, v4: Vertex, angle: float, scale: float) -> Vertex:
    """Intersection of lines (*v1*, *v2*) and (*v3*, *v4*)."""
    i = _basic_intersection(v1, v2, v3, v4)
    s1 = v1.apply_shift(angle, scale)
    s2 = v2.apply_shift(angle, scale)
    s3 = v3.apply_shift(angle, scale)
    s4 = v4.apply_shift(angle, scale)
    try:
        i_bis = _basic_intersection(s1, s2, s3, s4)
    except ValueError:
        i_bis = i.copy()
    _compute_shift(i, i_bis, angle, scale)
    return i


def bisector(pivot: Vertex, a: Vertex, b: Vertex, angle: float, scale: float) -> Vertex:
    """Point on the bisector of angle *a*–*pivot*–*b*."""
    u = Vector.between(pivot, a)
    v = Vector.between(pivot, b)
    nu = u.norm()
    nv = v.norm()
    if nu < EPSILON or nv < EPSILON:
        raise ValueError("Undefined bisector")
    u = u / nu
    v = v / nv
    w = u + v
    if w.sqr_norm() < EPSILON:
        w = u.ortho()
    q = Vertex("null", pivot.x + w.x, pivot.y + w.y)
    return intersection(pivot, q, a, b, angle, scale)


def mediator(v1: Vertex, v2: Vertex, v3: Vertex, v4: Vertex, angle: float, scale: float) -> Vertex:
    """Intersection of the perpendicular bisector of (*v1*, *v2*) with line (*v3*, *v4*)."""
    m = middle(v1, v2)
    u = Vector.between(v1, v2)
    v = u.ortho()
    mp = Vertex("null", m.x + v.x, m.y + v.y)
    return intersection(m, mp, v3, v4, angle, scale)


def projection(point: Vertex, a: Vertex, b: Vertex) -> Vertex:
    """Orthogonal projection of *point* onto line (*a*, *b*)."""
    u = Vector.between(a, b)
    n = u.norm()
    u = u / n
    v_a_self = Vector.between(a, point)
    proj_len = v_a_self.dot(u)
    return Vertex("null", a.x + proj_len * u.x, a.y + proj_len * u.y)


def vertex_to_line(
    moving: Vertex,
    pivot: Vertex,
    b: Vertex,
    c: Vertex,
    d: Vertex,
    e: Vertex,
    first: bool,
    angle: float,
    scale: float,
) -> Vertex:
    """Fold *moving* onto line (*b*, *c*) around *pivot*, return intersection with (*d*, *e*)."""
    bc = Vector.between(b, c)
    a_coeff = -bc.y
    b_coeff = bc.x
    c_coeff = a_coeff * b.x + b_coeff * b.y
    r2 = Vector.between(pivot, moving).sqr_norm()

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

    v = Vector.between(pivot, moving)
    v1 = Vector.between(pivot, p1)
    v2 = Vector.between(pivot, p2)
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

    q = bisector(pivot, moving, chosen, angle, scale)
    return intersection(pivot, q, d, e, angle, scale)


def distance_to_line(point: Vertex, a: Vertex, b: Vertex) -> float:
    """Distance from *point* to line (*a*, *b*)."""
    proj = projection(point, a, b)
    return Vector.between(point, proj).norm()


def is_parallel(v1: Vertex, v2: Vertex, v3: Vertex, v4: Vertex) -> bool:
    """Check whether lines (*v1*, *v2*) and (*v3*, *v4*) are approximately parallel."""
    u1 = Vector.between(v1, v2)
    u2 = Vector.between(v3, v4)
    ps = u1.dot(u2)
    n = u1.norm() * u2.norm()
    ps = abs(ps)
    return ps > 0.99 * n and ps < 1.01 * n


def is_orthogonal(v1: Vertex, v2: Vertex, v3: Vertex, v4: Vertex) -> bool:
    """Check whether lines (*v1*, *v2*) and (*v3*, *v4*) are approximately orthogonal."""
    u1 = Vector.between(v1, v2)
    u2 = Vector.between(v3, v4)
    ps = u1.dot(u2)
    n = u1.norm() * u2.norm()
    return -0.01 * n < ps < 0.01 * n
