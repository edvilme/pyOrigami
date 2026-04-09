"""Paper shape commands (square, diamond, rectangles).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..types import PaperFormat


@dataclass
class Square:
    """Defines four border edges forming a square and names the four corners.

    The first vertex is the upper-left corner; the remaining three follow
    clockwise: upper-right, lower-right, lower-left.
    Maps to ``\\square(v1, v2, v3, v4);``.
    """

    v1: str
    v2: str
    v3: str
    v4: str

    def to_doo(self) -> str:
        return f"\\square({self.v1}, {self.v2}, {self.v3}, {self.v4})"


@dataclass
class Diamond:
    """Defines four border edges forming a diamond (rotated square).

    The first vertex is the upper corner; the remaining three follow
    clockwise: right, bottom, left.  A diamond is a common starting shape.
    Maps to ``\\diamond(v1, v2, v3, v4);``.
    """

    v1: str
    v2: str
    v3: str
    v4: str

    def to_doo(self) -> str:
        return f"\\diamond({self.v1}, {self.v2}, {self.v3}, {self.v4})"


@dataclass
class HorizontalRectangle:
    """Defines four border edges forming a horizontal rectangle.

    Corners are named upper-left clockwise.  The fifth parameter is the
    width-to-height ratio as a percentage (e.g. 200 = twice as wide as
    tall) or a named paper format symbol (``"A"``, ``"dollar"``).
    Maps to ``\\horizontal_rectangle(v1, v2, v3, v4, ratio);``.
    """

    v1: str
    v2: str
    v3: str
    v4: str
    ratio: int | PaperFormat | None = None

    def to_doo(self) -> str:
        args = [self.v1, self.v2, self.v3, self.v4]
        if self.ratio is not None:
            args.append(str(self.ratio))
        return f"\\horizontal_rectangle({', '.join(args)})"


@dataclass
class VerticalRectangle:
    """Defines four border edges forming a vertical rectangle.

    Corners are named upper-left clockwise.  The fifth parameter is the
    height-to-width ratio as a percentage (e.g. 200 = twice as tall as
    wide) or a named paper format symbol (``"A"``, ``"dollar"``).
    Maps to ``\\vertical_rectangle(v1, v2, v3, v4, ratio);``.
    """

    v1: str
    v2: str
    v3: str
    v4: str
    ratio: int | PaperFormat | None = None

    def to_doo(self) -> str:
        args = [self.v1, self.v2, self.v3, self.v4]
        if self.ratio is not None:
            args.append(str(self.ratio))
        return f"\\vertical_rectangle({', '.join(args)})"
