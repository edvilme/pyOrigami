"""Internal arrow representation ported from the DOODLE C++ codebase.

Derived from ``doodle/src/arrow.h`` / ``arrow.cpp``.
DOODLE — https://doodle.sourceforge.net/ — by Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .constants import SIMPLE_ARROW_ANGLE


class ArrowType(Enum):
    VALLEY = 0
    MOUNTAIN = 1
    UNFOLD = 2
    NONE = 3


class ArrowSideInternal(Enum):
    LEFT = 0
    RIGHT = 1


class TurnType(Enum):
    NONE = 0
    VERTICAL = 1
    HORIZONTAL = 2


@dataclass
class InternalArrow:
    v1: str = ""
    v2: str = ""
    v1_type: ArrowType = ArrowType.NONE
    v2_type: ArrowType = ArrowType.NONE
    side: ArrowSideInternal = ArrowSideInternal.LEFT
    simple: bool = True
    shape: int = SIMPLE_ARROW_ANGLE
