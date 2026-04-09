from __future__ import annotations

from dataclasses import dataclass

from ..types import Color, string_quote


@dataclass
class Designer:
    """Specifies the origami model designer's name.

    Appears on the first page of the generated diagram.
    Maps to ``\\designer("name");`` inside a ``\\diagram_header`` block.
    """

    name: str

    def to_doo(self) -> str:
        return f"\\designer({string_quote(self.name)})"


@dataclass
class Title:
    """Specifies the model title.

    Appears centred on the first page of the generated diagram.
    Maps to ``\\title("name");``.
    """

    name: str

    def to_doo(self) -> str:
        return f"\\title({string_quote(self.name)})"


@dataclass
class Diagrammer:
    """Specifies the diagram author's name (the person who wrote the Doodle file).

    Maps to ``\\diagrammer("name");``.
    """

    name: str

    def to_doo(self) -> str:
        return f"\\diagrammer({string_quote(self.name)})"


@dataclass
class DiagramDate:
    """Specifies the diagram creation date (year).

    The date appears on the first page.
    Maps to ``\\diagram_date(year);``.
    """

    year: int

    def to_doo(self) -> str:
        return f"\\diagram_date({self.year})"


@dataclass
class DesignDate:
    """Specifies the original design date (year).

    Maps to ``\\design_date(year);``.
    """

    year: int

    def to_doo(self) -> str:
        return f"\\design_date({self.year})"


@dataclass
class Comment:
    """Free-form comment text that appears on the first page of the diagram.

    Multiple ``Comment`` entries are allowed and displayed in order.
    Maps to ``\\comment("text");``.
    """

    text: str

    def to_doo(self) -> str:
        return f"\\comment({string_quote(self.text)})"


@dataclass
class ColorFront:
    """Defines the colour of the front side of the paper.

    Accepts an ``(R, G, B)`` tuple or a named colour string.
    Maps to ``\\color_front(R, G, B);`` or ``\\color_front(name);``.
    """

    color: Color

    def to_doo(self) -> str:
        if type(self.color) is tuple:
            r, g, b = self.color
            return f"\\color_front({r}, {g}, {b})"
        return f"\\color_front({self.color})"


@dataclass
class ColorBack:
    """Defines the colour of the back side of the paper.

    Accepts an ``(R, G, B)`` tuple or a named colour string.
    Maps to ``\\color_back(R, G, B);`` or ``\\color_back(name);``.
    """

    color: Color

    def to_doo(self) -> str:
        if type(self.color) is tuple:
            r, g, b = self.color
            return f"\\color_back({r}, {g}, {b})"
        return f"\\color_back({self.color})"


@dataclass
class BottomMargin:
    """Defines the bottom margin (in mm) of each page.

    Maps to ``\\bottom_margin(value);``.
    """

    value: int

    def to_doo(self) -> str:
        return f"\\bottom_margin({self.value})"


@dataclass
class TopMargin:
    """Defines the top margin (in mm) of each page.

    Maps to ``\\top_margin(value);``.
    """

    value: int

    def to_doo(self) -> str:
        return f"\\top_margin({self.value})"


@dataclass
class LeftMargin:
    """Defines the left margin (in mm) of each page.

    Maps to ``\\left_margin(value);``.
    """

    value: int

    def to_doo(self) -> str:
        return f"\\left_margin({self.value})"


@dataclass
class RightMargin:
    """Defines the right margin (in mm) of each page.

    Maps to ``\\right_margin(value);``.
    """

    value: int

    def to_doo(self) -> str:
        return f"\\right_margin({self.value})"


@dataclass
class HorizontalSpace:
    """Specifies the horizontal spacing (in mm) between adjacent steps.

    Maps to ``\\horizontal_space(value);``.
    """

    value: int

    def to_doo(self) -> str:
        return f"\\horizontal_space({self.value})"


@dataclass
class VerticalSpace:
    """Specifies the vertical spacing (in mm) between step rows.

    Maps to ``\\vertical_space(value);``.
    """

    value: int

    def to_doo(self) -> str:
        return f"\\vertical_space({self.value})"
