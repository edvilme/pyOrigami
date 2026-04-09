"""Arrow commands (simple, return, open, push, repeat).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..types import ArrowHead, ArrowSide, Edge


@dataclass
class SimpleArrow:
    """Draws a circular-arc arrow associated with a fold.

    The arrow goes from *src* toward *dst* (a vertex or an ``Edge`` to
    cross).  The arc is drawn proportionally to the distance between
    points but always remains at a defined circle-arc length (default
    60 degrees).  *src_arrow* / *dst_arrow* set head types at each end;
    *side* controls whether the arc bows left or right.
    Maps to ``\\simple_arrow(src, dst, src_arrow, dst_arrow[, side[, arc]]);``.
    """

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


@dataclass
class ReturnArrow:
    """Draws a curved (Bézier) return arrow, often used for mountain or back folds.

    The arrow starts near the midpoint of *edge1* (typically the fold
    line), curves along its mediator, and returns near the intersection
    with *edge2*.  *ratio* (0–100, default 50) controls how far the
    arrow extends beyond *edge2*.
    Maps to ``\\return_arrow(edge1, edge2, src_arrow, dst_arrow[, side[, ratio]]);``.
    """

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


@dataclass
class OpenArrow:
    """Draws an "open" symbol — a white-filled truncated arrow indicating to open the model.

    Drawn at the midpoint of the given edge.  The edge order matters for
    determining left/right side.
    Maps to ``\\open_arrow(edge[, side]);``.
    """

    edge: Edge
    side: ArrowSide = ArrowSide.RIGHT

    def to_doo(self) -> str:
        return f"\\open_arrow({self.edge.to_doo()}, {self.side})"


@dataclass
class PushArrow:
    """Draws a filled arrow head indicating a push action.

    Placed at *vertex* with an optional orientation *angle* (degrees,
    absolute) and *distance* (mm) from the vertex.  If *angle* is
    omitted, it is computed to point toward the step centre.
    Maps to ``\\push_arrow(vertex[, angle[, distance]]);``.
    """

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


@dataclass
class RepeatArrow:
    """Draws a repeat symbol — a straight arrow with tick marks.

    Indicates that certain folds should be repeated.  *number* sets the
    repeat count; *label1*/*label2* optionally reference step labels
    (defined with ``Label``) to display the step range in a box.
    *angle* and *distance* adjust positioning.
    Maps to ``\\repeat_arrow(vertex[, number[, angle[, distance]]]);``
    or ``\\repeat_arrow(vertex, label1, label2[, ...]);``.
    """

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
