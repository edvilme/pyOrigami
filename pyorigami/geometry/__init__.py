"""Internal geometric data model for the Doodle origami engine.

These classes mirror the C++ ``vertex``, ``edge``, ``face``, ``arrow``
and ``step`` types used by the Doodle renderer.  They are *computed*
representations populated by :mod:`pyorigami.engine` from the high-level
command dataclasses in :mod:`pyorigami.commands`.

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens — a tool for creating origami diagrams using the
DOODLE (Description Of Origami by Drawing Little Elements) markup
language.  See ``doodle/src/`` for the original C++ sources.
"""

from .constants import (
    ARROWHEADANGLE,
    ARROWLG,
    ARROWSPC,
    BOTTOM_MARGIN,
    CAPTION_HEIGHT_MM,
    CLIP_HEIGHT,
    CLIP_WIDTH,
    DIAMOND_EDGE,
    EPSILON,
    FIRST_TOP_MARGIN,
    FOLDSPC,
    HSPACE,
    LEFT_MARGIN,
    PAGE_HEIGHT,
    PAGE_WIDTH,
    PS_BORDER_WIDTH,
    PS_FOLD_WIDTH,
    PS_MOUNTAIN_WIDTH,
    PS_VALLEY_WIDTH,
    PS_XRAY_WIDTH,
    RETURN_ARROW_RATIO,
    RIGHT_MARGIN,
    SIMPLE_ARROW_ANGLE,
    SQUARE_EDGE,
    TOP_MARGIN,
    VSPACE,
    is_null,
    to_ps,
)
from .vec2 import Vec2
from .vertex import Vertex
from .edge import EdgeType, InternalEdge, LimitType
from .arrow import ArrowSideInternal, ArrowType, InternalArrow, TurnType
from .face import InternalColor, InternalFace
from .symbols import ArrowSymbol, OpenArrowSymbol, PushArrowSymbol, RepeatArrowSymbol
from .model import ComputedHeader, ComputedStep
