"""Arrow commands (simple, return, open, push, repeat).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..parsing import DoodleParseableCommand
from ..types import ArrowHead, ArrowSide, Edge


@dataclass
class SimpleArrow(DoodleParseableCommand):
    """Draws a circular-arc arrow associated with a fold.

    The arrow goes from *src* toward *dst* (a vertex or an ``Edge`` to
    cross).  The arc is drawn proportionally to the distance between
    points but always remains at a defined circle-arc length (default
    60 degrees).  *src_arrow* / *dst_arrow* set head types at each end;
    *side* controls whether the arc bows left or right.
    Maps to ``\\simple_arrow(src, dst, src_arrow, dst_arrow[, side[, arc]]);``.
    """

    DOO_KEYWORD = "simple_arrow"

    src: str
    dst: str | Edge
    src_arrow: ArrowHead
    dst_arrow: ArrowHead
    side: ArrowSide = ArrowSide.RIGHT
    arc: int | None = None

    def to_doo(self) -> str:
        d = self.dst.to_doo() if isinstance(self.dst, Edge) else self.dst
        args = [self.src, d, str(self.src_arrow), str(self.dst_arrow), str(self.side)]
        if self.arc is not None:
            args.append(str(self.arc))
        return f"\\simple_arrow({', '.join(args)})"

    @classmethod
    def from_doo_args(cls, args: list) -> SimpleArrow:
        side = ArrowSide(args[4]) if len(args) > 4 else ArrowSide.RIGHT
        arc = int(args[5]) if len(args) > 5 else None
        return cls(
            src=args[0],
            dst=args[1],
            src_arrow=ArrowHead(args[2]),
            dst_arrow=ArrowHead(args[3]),
            side=side,
            arc=arc,
        )


@dataclass
class ReturnArrow(DoodleParseableCommand):
    """Draws a curved (Bézier) return arrow, often used for mountain or back folds.

    The arrow starts near the midpoint of *edge1* (typically the fold
    line), curves along its mediator, and returns near the intersection
    with *edge2*.  *ratio* (0–100, default 50) controls how far the
    arrow extends beyond *edge2*.
    Maps to ``\\return_arrow(edge1, edge2, src_arrow, dst_arrow[, side[, ratio]]);``.
    """

    DOO_KEYWORD = "return_arrow"

    edge1: Edge
    edge2: Edge
    src_arrow: ArrowHead
    dst_arrow: ArrowHead
    side: ArrowSide = ArrowSide.RIGHT
    ratio: int | None = None

    def to_doo(self) -> str:
        args = [
            self.edge1.to_doo(),
            self.edge2.to_doo(),
            str(self.src_arrow),
            str(self.dst_arrow),
            str(self.side),
        ]
        if self.ratio is not None:
            args.append(str(self.ratio))
        return f"\\return_arrow({', '.join(args)})"

    @classmethod
    def from_doo_args(cls, args: list) -> ReturnArrow:
        side = ArrowSide(args[4]) if len(args) > 4 else ArrowSide.RIGHT
        ratio = int(args[5]) if len(args) > 5 else None
        return cls(
            edge1=args[0],
            edge2=args[1],
            src_arrow=ArrowHead(args[2]),
            dst_arrow=ArrowHead(args[3]),
            side=side,
            ratio=ratio,
        )


@dataclass
class OpenArrow(DoodleParseableCommand):
    """Draws an "open" symbol — a white-filled truncated arrow indicating to open the model.

    Drawn at the midpoint of the given edge.  The edge order matters for
    determining left/right side.
    Maps to ``\\open_arrow(edge[, side]);``.
    """

    DOO_KEYWORD = "open_arrow"

    edge: Edge
    side: ArrowSide = ArrowSide.RIGHT

    def to_doo(self) -> str:
        return f"\\open_arrow({self.edge.to_doo()}, {self.side})"

    @classmethod
    def from_doo_args(cls, args: list) -> OpenArrow:
        side = ArrowSide(args[1]) if len(args) > 1 else ArrowSide.RIGHT
        return cls(edge=args[0], side=side)


@dataclass
class PushArrow(DoodleParseableCommand):
    """Draws a filled arrow head indicating a push action.

    Placed at *vertex* with an optional orientation *angle* (degrees,
    absolute) and *distance* (mm) from the vertex.  If *angle* is
    omitted, it is computed to point toward the step centre.
    Maps to ``\\push_arrow(vertex[, angle[, distance]]);``.
    """

    DOO_KEYWORD = "push_arrow"

    vertex: str
    angle: int | None = None
    distance: int | None = None

    def to_doo(self) -> str:
        args = [self.vertex]
        if self.angle is not None:
            args.append(str(self.angle))
            if self.distance is not None:
                args.append(str(self.distance))
        return f"\\push_arrow({', '.join(args)})"

    @classmethod
    def from_doo_args(cls, args: list) -> PushArrow:
        angle = int(args[1]) if len(args) > 1 else None
        distance = int(args[2]) if len(args) > 2 else None
        return cls(vertex=args[0], angle=angle, distance=distance)


@dataclass
class RepeatArrow(DoodleParseableCommand):
    """Draws a repeat symbol — a straight arrow with tick marks.

    Indicates that certain folds should be repeated.  *number* sets the
    repeat count; *label1*/*label2* optionally reference step labels
    (defined with ``Label``) to display the step range in a box.
    *angle* and *distance* adjust positioning.
    Maps to ``\\repeat_arrow(vertex[, number[, angle[, distance]]]);``
    or ``\\repeat_arrow(vertex, label1, label2[, ...]);``.
    """

    DOO_KEYWORD = "repeat_arrow"

    vertex: str
    number: int | None = None
    label1: str | None = None
    label2: str | None = None
    angle: int | None = None
    distance: int | None = None

    def to_doo(self) -> str:
        args = [self.vertex]
        if self.label1 is not None and self.label2 is not None:
            args.extend([self.label1, self.label2])
        if self.number is not None:
            args.append(str(self.number))
        if self.angle is not None:
            args.append(str(self.angle))
            if self.distance is not None:
                args.append(str(self.distance))
        return f"\\repeat_arrow({', '.join(args)})"

    @classmethod
    def from_doo_args(cls, args: list) -> RepeatArrow:
        vertex = args[0]
        # Disambiguate: if arg[1] and arg[2] are both str (identifiers),
        # they are label1 and label2; otherwise arg[1] is the number.
        if len(args) >= 3 and isinstance(args[1], str) and isinstance(args[2], str):
            label1, label2 = args[1], args[2]
            rest = args[3:]
            number = int(rest[0]) if rest else None
            angle = int(rest[1]) if len(rest) > 1 else None
            distance = int(rest[2]) if len(rest) > 2 else None
            return cls(vertex=vertex, label1=label1, label2=label2, number=number, angle=angle, distance=distance)
        number = int(args[1]) if len(args) > 1 else None
        angle = int(args[2]) if len(args) > 2 else None
        distance = int(args[3]) if len(args) > 3 else None
        return cls(vertex=vertex, number=number, angle=angle, distance=distance)
