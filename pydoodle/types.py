from __future__ import annotations

from enum import Enum
from typing import NamedTuple


class Edge(NamedTuple):
    """A pair of vertex identifiers representing a Doodle edge.

    In Doodle syntax edges are written as ``[v1, v2]``.  An edge references
    two vertices but does **not** require that a physical edge has been
    defined between them — it is often used simply to designate a line
    passing through two known points.
    """
    v1: str
    v2: str

    def to_doo(self) -> str:
        return f"[{self.v1},{self.v2}]"


class Side(Enum):
    """Indicates which colour (front or back of the paper) to use.

    Doodle models a sheet of paper with two differently-coloured sides.
    ``FRONT`` selects the front-side colour and ``BACK`` selects the
    back-side colour, as set by ``\\color_front`` / ``\\color_back``.
    """
    FRONT = "front"
    BACK = "back"


class ArrowHead(Enum):
    """Type of arrow head drawn at an arrow extremity.

    Used by ``\\simple_arrow``, ``\\return_arrow`` and related operators.

    * ``VALLEY``   — filled triangular head (valley fold symbol).
    * ``MOUNTAIN`` — open triangular head (mountain fold symbol).
    * ``UNFOLD``   — half-filled head indicating an unfold action.
    * ``NONE``     — no arrow head drawn.
    """
    VALLEY = "valley"
    MOUNTAIN = "mountain"
    UNFOLD = "unfold"
    NONE = "none"


class ArrowSide(Enum):
    """Orientation side of an arrow relative to its direction.

    Along the arrow direction, the arc or curve can be drawn to the
    ``LEFT`` or ``RIGHT``.  Default is ``RIGHT`` for most operators.
    """
    LEFT = "left"
    RIGHT = "right"


class Which(Enum):
    """Selector for ``\\point_to_line`` when two solutions exist.

    A segment can have up to two intersections with the moving circle.
    ``FIRST`` keeps the first intersection found; ``SECOND`` keeps the
    other one.  Default is ``FIRST``.
    """
    FIRST = "first"
    SECOND = "second"


Limit = int | Edge
"""A fold / line visual-limit parameter.

All line operators (``\\valley_fold``, ``\\mountain_fold``, ``\\border``,
``\\fold``, ``\\xray_fold``) accept two optional limit parameters that
control how much of the line is actually drawn:

* **int** — a percentage of total edge length left blank near the vertex.
  Negative values extend the line beyond the real endpoint.
* **Edge** — the drawn portion ends at the intersection of the fold line
  with the given edge, useful when a paper layer hides part of the line.
"""

Color = tuple[int, int, int] | str
"""Paper colour specification.

Either an ``(R, G, B)`` tuple with integer components (Doodle uses a
percentage-like scale) or a named colour string such as ``"white"``.
"""
