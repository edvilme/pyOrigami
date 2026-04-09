"""Diagram header commands (metadata, colours, margins).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..parsing import DoodleParseableCommand
from ..types import Color, string_quote


def _parse_color(args: list) -> Color:
    """Build a Color from tokenized args: (R,G,B) tuple or name string."""
    if len(args) == 3 and all(isinstance(a, int) for a in args):
        return (args[0], args[1], args[2])
    return args[0]


@dataclass
class Designer(DoodleParseableCommand):
    """Specifies the origami model designer's name.

    Appears on the first page of the generated diagram.
    Maps to ``\\designer("name");`` inside a ``\\diagram_header`` block.
    """

    DOO_KEYWORD = "designer"

    name: str

    def to_doo(self) -> str:
        return f"\\designer({string_quote(self.name)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Designer:
        return cls(name=args[0])


@dataclass
class Title(DoodleParseableCommand):
    """Specifies the model title.

    Appears centred on the first page of the generated diagram.
    Maps to ``\\title("name");``.
    """

    DOO_KEYWORD = "title"

    name: str

    def to_doo(self) -> str:
        return f"\\title({string_quote(self.name)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Title:
        return cls(name=args[0])


@dataclass
class Diagrammer(DoodleParseableCommand):
    """Specifies the diagram author's name (the person who wrote the Doodle file).

    Maps to ``\\diagrammer("name");``.
    """

    DOO_KEYWORD = "diagrammer"

    name: str

    def to_doo(self) -> str:
        return f"\\diagrammer({string_quote(self.name)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Diagrammer:
        return cls(name=args[0])


@dataclass
class DiagramDate(DoodleParseableCommand):
    """Specifies the diagram creation date (year).

    The date appears on the first page.
    Maps to ``\\diagram_date(year);``.
    """

    DOO_KEYWORD = "diagram_date"

    year: int

    def to_doo(self) -> str:
        return f"\\diagram_date({self.year})"

    @classmethod
    def from_doo_args(cls, args: list) -> DiagramDate:
        return cls(year=int(args[0]))


@dataclass
class DesignDate(DoodleParseableCommand):
    """Specifies the original design date (year).

    Maps to ``\\design_date(year);``.
    """

    DOO_KEYWORD = "design_date"

    year: int

    def to_doo(self) -> str:
        return f"\\design_date({self.year})"

    @classmethod
    def from_doo_args(cls, args: list) -> DesignDate:
        return cls(year=int(args[0]))


@dataclass
class Comment(DoodleParseableCommand):
    """Free-form comment text that appears on the first page of the diagram.

    Multiple ``Comment`` entries are allowed and displayed in order.
    Maps to ``\\comment("text");``.
    """

    DOO_KEYWORD = "comment"

    text: str

    def to_doo(self) -> str:
        return f"\\comment({string_quote(self.text)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Comment:
        return cls(text=args[0])


@dataclass
class ColorFront(DoodleParseableCommand):
    """Defines the colour of the front side of the paper.

    Accepts an ``(R, G, B)`` tuple or a named colour string.
    Maps to ``\\color_front(R, G, B);`` or ``\\color_front(name);``.
    """

    DOO_KEYWORD = "color_front"

    color: Color

    def to_doo(self) -> str:
        if type(self.color) is tuple:
            r, g, b = self.color
            return f"\\color_front({r}, {g}, {b})"
        return f"\\color_front({self.color})"

    @classmethod
    def from_doo_args(cls, args: list) -> ColorFront:
        return cls(color=_parse_color(args))


@dataclass
class ColorBack(DoodleParseableCommand):
    """Defines the colour of the back side of the paper.

    Accepts an ``(R, G, B)`` tuple or a named colour string.
    Maps to ``\\color_back(R, G, B);`` or ``\\color_back(name);``.
    """

    DOO_KEYWORD = "color_back"

    color: Color

    def to_doo(self) -> str:
        if type(self.color) is tuple:
            r, g, b = self.color
            return f"\\color_back({r}, {g}, {b})"
        return f"\\color_back({self.color})"

    @classmethod
    def from_doo_args(cls, args: list) -> ColorBack:
        return cls(color=_parse_color(args))


@dataclass
class BottomMargin(DoodleParseableCommand):
    """Defines the bottom margin (in mm) of each page.

    Maps to ``\\bottom_margin(value);``.
    """

    DOO_KEYWORD = "bottom_margin"

    value: int

    def to_doo(self) -> str:
        return f"\\bottom_margin({self.value})"

    @classmethod
    def from_doo_args(cls, args: list) -> BottomMargin:
        return cls(value=int(args[0]))


@dataclass
class TopMargin(DoodleParseableCommand):
    """Defines the top margin (in mm) of each page.

    Maps to ``\\top_margin(value);``.
    """

    DOO_KEYWORD = "top_margin"

    value: int

    def to_doo(self) -> str:
        return f"\\top_margin({self.value})"

    @classmethod
    def from_doo_args(cls, args: list) -> TopMargin:
        return cls(value=int(args[0]))


@dataclass
class LeftMargin(DoodleParseableCommand):
    """Defines the left margin (in mm) of each page.

    Maps to ``\\left_margin(value);``.
    """

    DOO_KEYWORD = "left_margin"

    value: int

    def to_doo(self) -> str:
        return f"\\left_margin({self.value})"

    @classmethod
    def from_doo_args(cls, args: list) -> LeftMargin:
        return cls(value=int(args[0]))


@dataclass
class RightMargin(DoodleParseableCommand):
    """Defines the right margin (in mm) of each page.

    Maps to ``\\right_margin(value);``.
    """

    DOO_KEYWORD = "right_margin"

    value: int

    def to_doo(self) -> str:
        return f"\\right_margin({self.value})"

    @classmethod
    def from_doo_args(cls, args: list) -> RightMargin:
        return cls(value=int(args[0]))


@dataclass
class HorizontalSpace(DoodleParseableCommand):
    """Specifies the horizontal spacing (in mm) between adjacent steps.

    Maps to ``\\horizontal_space(value);``.
    """

    DOO_KEYWORD = "horizontal_space"

    value: int

    def to_doo(self) -> str:
        return f"\\horizontal_space({self.value})"

    @classmethod
    def from_doo_args(cls, args: list) -> HorizontalSpace:
        return cls(value=int(args[0]))


@dataclass
class VerticalSpace(DoodleParseableCommand):
    """Specifies the vertical spacing (in mm) between step rows.

    Maps to ``\\vertical_space(value);``.
    """

    DOO_KEYWORD = "vertical_space"

    value: int

    def to_doo(self) -> str:
        return f"\\vertical_space({self.value})"

    @classmethod
    def from_doo_args(cls, args: list) -> VerticalSpace:
        return cls(value=int(args[0]))
