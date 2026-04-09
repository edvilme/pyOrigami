"""Constants and helpers ported from the DOODLE C++ codebase.

Derived from ``doodle/src/global_def.h``.
DOODLE — https://doodle.sourceforge.net/ — by Olivier Bettens.
"""

from __future__ import annotations

import math

EPSILON = 1e-6
SQUARE_EDGE = 100.0
DIAMOND_EDGE = SQUARE_EDGE * math.sqrt(2)

CLIP_WIDTH = 65
CLIP_HEIGHT = 65
TOP_MARGIN = 20
BOTTOM_MARGIN = 20
LEFT_MARGIN = 20
RIGHT_MARGIN = 20
VSPACE = 5
HSPACE = 5

SIMPLE_ARROW_ANGLE = 60
RETURN_ARROW_RATIO = 50
FOLDSPC = 5


def is_null(a: float) -> bool:
    return -EPSILON <= a < EPSILON
