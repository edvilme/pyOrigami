"""Internal arrow representation ported from the DOODLE C++ codebase.

Derived from ``doodle/src/arrow.h`` / ``arrow.cpp``.
DOODLE — https://doodle.sourceforge.net/ — by Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..types import ArrowHead, ArrowSide
from .constants import SIMPLE_ARROW_ANGLE


@dataclass
class Arrow:
    v1: str = ""
    v2: str = ""
    v1_type: ArrowHead = ArrowHead.NONE
    v2_type: ArrowHead = ArrowHead.NONE
    side: ArrowSide = ArrowSide.LEFT
    simple: bool = True
    shape: int = SIMPLE_ARROW_ANGLE
