from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Scale:
    """Scales subsequent steps by the given percentage.

    100 is the default (no change); values above 100 zoom in, below 100
    zoom out.  Fold line styles are not affected by scaling.
    Appears **outside** step blocks.
    Maps to ``\\scale(percent);``.
    """

    percent: int

    def to_doo(self) -> str:
        return f"\\scale({self.percent})"


@dataclass
class Rotate:
    """Rotates subsequent steps by the given angle in degrees.

    Applied globally — must appear **outside** step blocks.
    Maps to ``\\rotate(degrees);``.
    """

    degrees: int | float

    def to_doo(self) -> str:
        d = (
            str(int(self.degrees))
            if isinstance(self.degrees, float) and self.degrees == int(self.degrees)
            else str(self.degrees)
        )
        return f"\\rotate({d})"


@dataclass
class Clip:
    """Enables clipping: hides graphics that extend beyond the step bounding box.

    Maps to ``\\clip;``.
    """

    def to_doo(self) -> str:
        return "\\clip"


@dataclass
class Unclip:
    """Disables clipping, allowing graphics to extend beyond step limits.

    Maps to ``\\unclip;``.
    """

    def to_doo(self) -> str:
        return "\\unclip"


@dataclass
class VisibleAreaCenter:
    """Sets the centre of the visible drawing area to a specific vertex.

    The step diagram will be re-centred so that *vertex* appears at the
    middle of the step box.
    Maps to ``\\visible_area_center(vertex);``.
    """

    vertex: str

    def to_doo(self) -> str:
        return f"\\visible_area_center({self.vertex})"


@dataclass
class VisibleAreaHeight:
    """Sets the height (in mm) of the visible drawing area for subsequent steps.

    Maps to ``\\visible_area_height(value);``.
    """

    value: int

    def to_doo(self) -> str:
        return f"\\visible_area_height({self.value})"


@dataclass
class VisibleAreaWidth:
    """Sets the width (in mm) of the visible drawing area for subsequent steps.

    Maps to ``\\visible_area_width(value);``.
    """

    value: int

    def to_doo(self) -> str:
        return f"\\visible_area_width({self.value})"


@dataclass
class TurnOverVertical:
    """Turns the paper over around the vertical axis (left–right flip).

    All subsequent steps reflect the model horizontally.  Must appear
    **outside** step blocks.
    Maps to ``\\turn_over_vertical;``.
    """

    def to_doo(self) -> str:
        return "\\turn_over_vertical"


@dataclass
class TurnOverHorizontal:
    """Turns the paper over around the horizontal axis (top–bottom flip).

    All subsequent steps reflect the model vertically.  Must appear
    **outside** step blocks.
    Maps to ``\\turn_over_horizontal;``.
    """

    def to_doo(self) -> str:
        return "\\turn_over_horizontal"
