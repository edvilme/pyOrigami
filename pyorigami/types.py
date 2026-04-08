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

    def __str__(self) -> str:
        return self.value


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

    def __str__(self) -> str:
        return self.value


class ArrowSide(Enum):
    """Orientation side of an arrow relative to its direction.

    Along the arrow direction, the arc or curve can be drawn to the
    ``LEFT`` or ``RIGHT``.  Default is ``RIGHT`` for most operators.
    """

    LEFT = "left"
    RIGHT = "right"

    def __str__(self) -> str:
        return self.value


class Which(Enum):
    """Selector for ``\\point_to_line`` when two solutions exist.

    A segment can have up to two intersections with the moving circle.
    ``FIRST`` keeps the first intersection found; ``SECOND`` keeps the
    other one.  Default is ``FIRST``.
    """

    FIRST = "first"
    SECOND = "second"

    def __str__(self) -> str:
        return self.value


class PaperFormat(Enum):
    """Named paper format for rectangle aspect ratios.

    Used by ``\\horizontal_rectangle`` and ``\\vertical_rectangle`` as
    an alternative to specifying a numeric ratio percentage.

    * ``A`` — ISO A-series proportion (1 : √2 ≈ 141%).
    * ``DOLLAR`` — US dollar bill proportion.
    """

    A = "A"
    DOLLAR = "dollar"

    def __str__(self) -> str:
        return self.value


class OutputFormat(Enum):
    """Output format for rendered diagrams.

    * ``PS``  — PostScript (native C++ output).
    * ``PDF`` — PDF (converted from PostScript via Ghostscript).
    * ``PNG`` — PNG (converted from PostScript via Ghostscript).
    * ``SVG`` — SVG (converted from PostScript via Ghostscript).
    """

    PS = "ps"
    PDF = "pdf"
    PNG = "png"
    SVG = "svg"

    def __str__(self) -> str:
        return self.value

    @staticmethod
    def from_string(value: str) -> "OutputFormat":
        """Convert a string to an :class:`OutputFormat` member (case-insensitive).

        Raises
        ------
        ValueError
            If *value* does not match any known format.
        """
        try:
            return OutputFormat(value.lower())
        except ValueError:
            valid = ", ".join(repr(f.value) for f in OutputFormat)
            raise ValueError(f"Unsupported format {value!r}; expected one of {valid}") from None


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


def string_quote(s: str) -> str:
    """Wrap *s* in double quotes, escaping characters that would break .doo syntax."""
    s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
    return f'"{s}"'
