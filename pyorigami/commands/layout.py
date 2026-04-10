"""Layout and orientation commands (scale, rotate, clip, turn-over).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..parsing import DoodleParseableCommand


@dataclass
class Scale(DoodleParseableCommand):
    """Scales subsequent steps by the given percentage.

    100 is the default (no change); values above 100 zoom in, below 100
    zoom out.  Fold line styles are not affected by scaling.
    Appears **outside** step blocks.
    Maps to ``\\scale(percent);``.
    """

    DOO_KEYWORD = "scale"

    percent: int

    def to_doo(self) -> str:
        return f"\\scale({self.percent})"

    @classmethod
    def from_doo_args(cls, args: list) -> Scale:
        return cls(percent=int(args[0]))


@dataclass
class Rotate(DoodleParseableCommand):
    """Rotates subsequent steps by the given angle in degrees.

    Applied globally — must appear **outside** step blocks.
    Maps to ``\\rotate(degrees);``.
    """

    DOO_KEYWORD = "rotate"

    degrees: int | float

    def to_doo(self) -> str:
        d = (
            str(int(self.degrees))
            if isinstance(self.degrees, float) and self.degrees == int(self.degrees)
            else str(self.degrees)
        )
        return f"\\rotate({d})"

    @classmethod
    def from_doo_args(cls, args: list) -> Rotate:
        return cls(degrees=args[0])


@dataclass
class Clip(DoodleParseableCommand):
    """Enables clipping: hides graphics that extend beyond the step bounding box.

    Maps to ``\\clip;``.
    """

    DOO_KEYWORD = "clip"

    def to_doo(self) -> str:
        return "\\clip"

    @classmethod
    def from_doo_args(cls, args: list) -> Clip:
        return cls()


@dataclass
class Unclip(DoodleParseableCommand):
    """Disables clipping, allowing graphics to extend beyond step limits.

    Maps to ``\\unclip;``.
    """

    DOO_KEYWORD = "unclip"

    def to_doo(self) -> str:
        return "\\unclip"

    @classmethod
    def from_doo_args(cls, args: list) -> Unclip:
        return cls()


@dataclass
class VisibleAreaCenter(DoodleParseableCommand):
    """Sets the centre of the visible drawing area to a specific vertex.

    The step diagram will be re-centred so that *vertex* appears at the
    middle of the step box.
    Maps to ``\\visible_area_center(vertex);``.
    """

    DOO_KEYWORD = "visible_area_center"

    vertex: str

    def to_doo(self) -> str:
        return f"\\visible_area_center({self.vertex})"

    @classmethod
    def from_doo_args(cls, args: list) -> VisibleAreaCenter:
        return cls(vertex=args[0])


@dataclass
class VisibleAreaHeight(DoodleParseableCommand):
    """Sets the height (in mm) of the visible drawing area for subsequent steps.

    Maps to ``\\visible_area_height(value);``.
    """

    DOO_KEYWORD = "visible_area_height"

    value: int

    def to_doo(self) -> str:
        return f"\\visible_area_height({self.value})"

    @classmethod
    def from_doo_args(cls, args: list) -> VisibleAreaHeight:
        return cls(value=int(args[0]))


@dataclass
class VisibleAreaWidth(DoodleParseableCommand):
    """Sets the width (in mm) of the visible drawing area for subsequent steps.

    Maps to ``\\visible_area_width(value);``.
    """

    DOO_KEYWORD = "visible_area_width"

    value: int

    def to_doo(self) -> str:
        return f"\\visible_area_width({self.value})"

    @classmethod
    def from_doo_args(cls, args: list) -> VisibleAreaWidth:
        return cls(value=int(args[0]))


@dataclass
class TurnOverVertical(DoodleParseableCommand):
    """Turns the paper over around the vertical axis (left–right flip).

    All subsequent steps reflect the model horizontally.  Must appear
    **outside** step blocks.
    Maps to ``\\turn_over_vertical;``.
    """

    DOO_KEYWORD = "turn_over_vertical"

    def to_doo(self) -> str:
        return "\\turn_over_vertical"

    @classmethod
    def from_doo_args(cls, args: list) -> TurnOverVertical:
        return cls()


@dataclass
class TurnOverHorizontal(DoodleParseableCommand):
    """Turns the paper over around the horizontal axis (top–bottom flip).

    All subsequent steps reflect the model vertically.  Must appear
    **outside** step blocks.
    Maps to ``\\turn_over_horizontal;``.
    """

    DOO_KEYWORD = "turn_over_horizontal"

    def to_doo(self) -> str:
        return "\\turn_over_horizontal"

    @classmethod
    def from_doo_args(cls, args: list) -> TurnOverHorizontal:
        return cls()
