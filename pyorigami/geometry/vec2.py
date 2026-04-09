"""2-D vector helper ported from the DOODLE C++ codebase.

Derived from ``doodle/src/vect.h`` / ``vect.cpp``.
DOODLE — https://doodle.sourceforge.net/ — by Olivier Bettens.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .vertex import Vertex


@dataclass
class Vec2:
    x: float = 0.0
    y: float = 0.0

    def __add__(self, other: Vec2) -> Vec2:
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vec2) -> Vec2:
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> Vec2:
        return Vec2(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> Vec2:
        return Vec2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float) -> Vec2:
        return Vec2(self.x / scalar, self.y / scalar)

    def __neg__(self) -> Vec2:
        return Vec2(-self.x, -self.y)

    def dot(self, other: Vec2) -> float:
        return self.x * other.x + self.y * other.y

    def norm(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def sqr_norm(self) -> float:
        return self.x * self.x + self.y * self.y

    def ortho(self) -> Vec2:
        return Vec2(-self.y, self.x)

    @staticmethod
    def between(v1: Vertex, v2: Vertex) -> Vec2:
        return Vec2(v2.x - v1.x, v2.y - v1.y)
