"""Internal edge representation ported from the DOODLE C++ codebase.

Derived from ``doodle/src/edge.h`` / ``edge.cpp``.
DOODLE — https://doodle.sourceforge.net/ — by Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class EdgeType(Enum):
    BORDER = 0
    VALLEY = 1
    MOUNTAIN = 2
    FOLD = 3
    XRAY = 4


class LimitType(Enum):
    ALL_PERCENT = 0
    ALL_LIMIT = 3
    LIMIT_V1 = 2
    LIMIT_V2 = 1


@dataclass
class InternalEdge:
    v1: str
    v2: str
    type: EdgeType = EdgeType.BORDER
    visible: bool = True
    limits: int = 0  # bit field: bit 1 = v1 is limit-index, bit 0 = v2 is limit-index
    limit_v1: int = 0  # percent or edge-index
    limit_v2: int = 0
    debug: bool = False

    def copy(self) -> InternalEdge:
        return InternalEdge(
            self.v1, self.v2, self.type, self.visible, self.limits, self.limit_v1, self.limit_v2, self.debug
        )

    def equal(self, s1: str, s2: str) -> bool:
        return (self.v1 == s1 and self.v2 == s2) or (self.v1 == s2 and self.v2 == s1)

    def has_limit_v1(self) -> bool:
        return (self.limits >> 1) != 0

    def has_limit_v2(self) -> bool:
        return (self.limits & 1) != 0

    def set_space_v1(self, p: int) -> None:
        self.limit_v1 = p
        self.limits &= 1  # clear bit 1

    def set_space_v2(self, p: int) -> None:
        self.limit_v2 = p
        self.limits &= 2  # clear bit 0

    def set_limit_v1(self, idx: int) -> None:
        self.limit_v1 = idx
        self.limits |= 2  # set bit 1

    def set_limit_v2(self, idx: int) -> None:
        self.limit_v2 = idx
        self.limits |= 1  # set bit 0

    def get_space_v1(self) -> int:
        return self.limit_v1

    def get_space_v2(self) -> int:
        return self.limit_v2
