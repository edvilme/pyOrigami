"""Constants and helpers ported from the DOODLE C++ codebase.

Derived from ``doodle/src/global_def.h``.
DOODLE — https://doodle.sourceforge.net/ — by Olivier Bettens.
"""

from __future__ import annotations

import math

EPSILON = 1e-6
SQUARE_EDGE = 100.0
DIAMOND_EDGE = SQUARE_EDGE * math.sqrt(2)

PS_BORDER_WIDTH = 1
PS_FOLD_WIDTH = 0
PS_VALLEY_WIDTH = PS_BORDER_WIDTH
PS_MOUNTAIN_WIDTH = PS_BORDER_WIDTH
PS_XRAY_WIDTH = PS_BORDER_WIDTH

PAGE_HEIGHT = 297
PAGE_WIDTH = 210
CLIP_WIDTH = 65
CLIP_HEIGHT = 65
FIRST_TOP_MARGIN = 60
TOP_MARGIN = 20
BOTTOM_MARGIN = 20
LEFT_MARGIN = 20
RIGHT_MARGIN = 20
VSPACE = 5
HSPACE = 5
CAPTION_HEIGHT_MM = 5

SIMPLE_ARROW_ANGLE = 60
RETURN_ARROW_RATIO = 50
FOLDSPC = 5

ARROWSPC = 5
ARROWLG = 10
ARROWHEADANGLE = 40


def to_ps(x: float) -> float:
    """Convert internal units to PS cm.  50 units = 1 cm."""
    return x / 50.0


def is_null(a: float) -> bool:
    return -EPSILON <= a < EPSILON
