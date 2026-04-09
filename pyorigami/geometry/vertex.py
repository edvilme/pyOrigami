"""Vertex dataclass ported from the DOODLE C++ codebase.

Derived from ``doodle/src/vertex.h`` / ``vertex.cpp``.
DOODLE — https://doodle.sourceforge.net/ — by Olivier Bettens.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .constants import EPSILON
from .vector import Vector

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

    __hash__ = None

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
        a = self.apply_shift(angle, scale)
        b = v.apply_shift(angle, scale)
        if a == b:
            return 0.0
        res = math.atan2(b.y - a.y, b.x - a.x)
        if res < 0:
            res += 2 * math.pi
        return 180 * res / math.pi
