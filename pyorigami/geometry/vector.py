"""2-D vector helper ported from the DOODLE C++ codebase.

Derived from ``doodle/src/vect.h`` / ``vect.cpp``.
DOODLE — https://doodle.sourceforge.net/ — by Olivier Bettens.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from .vertex import Vertex


class Vector:
    """2-D vector backed by a NumPy array for accurate and efficient operations."""

    __slots__ = ("_data",)

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self._data = np.array([x, y], dtype=float)

    @property
    def x(self) -> float:
        return float(self._data[0])

    @property
    def y(self) -> float:
        return float(self._data[1])

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return bool(np.array_equal(self._data, other._data))

    def __add__(self, other: Vector) -> Vector:
        r = self._data + other._data
        return Vector(r[0], r[1])

    def __sub__(self, other: Vector) -> Vector:
        r = self._data - other._data
        return Vector(r[0], r[1])

    def __mul__(self, scalar: float) -> Vector:
        r = self._data * scalar
        return Vector(r[0], r[1])

    def __rmul__(self, scalar: float) -> Vector:
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> Vector:
        r = self._data / scalar
        return Vector(r[0], r[1])

    def __neg__(self) -> Vector:
        r = -self._data
        return Vector(r[0], r[1])

    def dot(self, other: Vector) -> float:
        return float(np.dot(self._data, other._data))

    def norm(self) -> float:
        return float(np.linalg.norm(self._data))

    def sqr_norm(self) -> float:
        return float(np.dot(self._data, self._data))

    def ortho(self) -> Vector:
        return Vector(-self._data[1], self._data[0])

    @staticmethod
    def between(v1: Vertex, v2: Vertex) -> Vector:
        return Vector(v2.x - v1.x, v2.y - v1.y)
