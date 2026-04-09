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
    BOTTOM_MARGIN,
    CLIP_HEIGHT,
    CLIP_WIDTH,
    DIAMOND_EDGE,
    EPSILON,
    FOLDSPC,
    HSPACE,
    LEFT_MARGIN,
    RETURN_ARROW_RATIO,
    RIGHT_MARGIN,
    SIMPLE_ARROW_ANGLE,
    SQUARE_EDGE,
    TOP_MARGIN,
    VSPACE,
    is_null,
)
from .vector import Vector
from .vertex import Vertex
from . import operations
from .edge import EdgeType, InternalEdge
from .arrow import Arrow
from .face import InternalColor, Face
from .symbols import ArrowSymbol, OpenArrowSymbol, PushArrowSymbol, RepeatArrowSymbol
from .model import ComputedHeader, ComputedStep, TurnType

__all__ = [
    # constants
    "BOTTOM_MARGIN",
    "CLIP_HEIGHT",
    "CLIP_WIDTH",
    "DIAMOND_EDGE",
    "EPSILON",
    "FOLDSPC",
    "HSPACE",
    "LEFT_MARGIN",
    "RETURN_ARROW_RATIO",
    "RIGHT_MARGIN",
    "SIMPLE_ARROW_ANGLE",
    "SQUARE_EDGE",
    "TOP_MARGIN",
    "VSPACE",
    "is_null",
    # vec2
    "Vector",
    # vertex
    "Vertex",
    # operations
    "operations",
    # edge
    "EdgeType",
    "InternalEdge",
    # arrow
    "Arrow",
    # face
    "InternalColor",
    "Face",
    # symbols
    "ArrowSymbol",
    "OpenArrowSymbol",
    "PushArrowSymbol",
    "RepeatArrowSymbol",
    # model
    "ComputedHeader",
    "ComputedStep",
    "TurnType",
]
