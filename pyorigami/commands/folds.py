"""Fold and edge commands (valley, mountain, xray, border, cut).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..parsing import DoodleParseableCommand
from ..types import Edge, Limit


def _parse_fold_args(cls, args: list):
    """Common parser for fold-like commands: (v1, v2[, limit1, limit2])."""
    v1, v2 = args[0], args[1]
    limit1 = args[2] if len(args) > 2 else None
    limit2 = args[3] if len(args) > 3 else None
    return cls(v1=v1, v2=v2, limit1=limit1, limit2=limit2)


@dataclass
class ValleyFold(DoodleParseableCommand):
    """Marks a valley fold between two vertices — drawn as a dashed line.

    The implicit result is a new valley edge in the global edge
    structure.  Optional *limit1*/*limit2* control how much of the line
    is drawn (percentage of blank or intersection edge).  Negative
    percentages extend the line beyond the endpoint.

    The operator is "opportunist": it only creates a new edge if one
    does not already exist between the two vertices.
    Maps to ``\\valley_fold(v1, v2[, limit1, limit2]);``.
    """

    DOO_KEYWORD = "valley_fold"

    v1: str
    v2: str
    limit1: Limit | None = None
    limit2: Limit | None = None

    def to_doo(self) -> str:
        args = [self.v1, self.v2]
        for lim in (self.limit1, self.limit2):
            if lim is not None:
                args.append(lim.to_doo() if isinstance(lim, Edge) else str(lim))
        return f"\\valley_fold({', '.join(args)})"

    @classmethod
    def from_doo_args(cls, args: list) -> ValleyFold:
        return _parse_fold_args(cls, args)


@dataclass
class MountainFold(DoodleParseableCommand):
    """Marks a mountain fold between two vertices — drawn as a dot-dot-dash line.

    Behaves identically to ``ValleyFold`` but uses mountain line style.
    Optional *limit1*/*limit2* control the visible portion of the line.
    Maps to ``\\mountain_fold(v1, v2[, limit1, limit2]);``.
    """

    DOO_KEYWORD = "mountain_fold"

    v1: str
    v2: str
    limit1: Limit | None = None
    limit2: Limit | None = None

    def to_doo(self) -> str:
        args = [self.v1, self.v2]
        for lim in (self.limit1, self.limit2):
            if lim is not None:
                args.append(lim.to_doo() if isinstance(lim, Edge) else str(lim))
        return f"\\mountain_fold({', '.join(args)})"

    @classmethod
    def from_doo_args(cls, args: list) -> MountainFold:
        return _parse_fold_args(cls, args)


@dataclass
class XrayFold(DoodleParseableCommand):
    """Marks an x-ray fold between two vertices — drawn as a dotted line.

    Used to show a fold line that is hidden by paper layers.
    Optional *limit1*/*limit2* control the visible portion of the line.
    Maps to ``\\xray_fold(v1, v2[, limit1, limit2]);``.
    """

    DOO_KEYWORD = "xray_fold"

    v1: str
    v2: str
    limit1: Limit | None = None
    limit2: Limit | None = None

    def to_doo(self) -> str:
        args = [self.v1, self.v2]
        for lim in (self.limit1, self.limit2):
            if lim is not None:
                args.append(lim.to_doo() if isinstance(lim, Edge) else str(lim))
        return f"\\xray_fold({', '.join(args)})"

    @classmethod
    def from_doo_args(cls, args: list) -> XrayFold:
        return _parse_fold_args(cls, args)


@dataclass
class Fold(DoodleParseableCommand):
    """Marks an existing crease between two vertices — drawn as a thin short line.

    Fold edges are displayed as incomplete thin lines that don't reach
    the vertices.  Usually created automatically at the start of a step
    when valley/mountain folds from the previous step are carried
    forward, but can also be set explicitly.
    Optional *limit1*/*limit2* control the visible portion of the line.
    Maps to ``\\fold(v1, v2[, limit1, limit2]);``.
    """

    DOO_KEYWORD = "fold"

    v1: str
    v2: str
    limit1: Limit | None = None
    limit2: Limit | None = None

    def to_doo(self) -> str:
        args = [self.v1, self.v2]
        for lim in (self.limit1, self.limit2):
            if lim is not None:
                args.append(lim.to_doo() if isinstance(lim, Edge) else str(lim))
        return f"\\fold({', '.join(args)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Fold:
        return _parse_fold_args(cls, args)


@dataclass
class Border(DoodleParseableCommand):
    """Draws a border line between two vertices — displayed as a thick plain line.

    Represents paper edges.  Like other line operators, optional
    *limit1*/*limit2* control the visible portion (percentage or
    intersection edge).
    Maps to ``\\border(v1, v2[, limit1, limit2]);``.
    """

    DOO_KEYWORD = "border"

    v1: str
    v2: str
    limit1: Limit | None = None
    limit2: Limit | None = None

    def to_doo(self) -> str:
        args = [self.v1, self.v2]
        for lim in (self.limit1, self.limit2):
            if lim is not None:
                args.append(lim.to_doo() if isinstance(lim, Edge) else str(lim))
        return f"\\border({', '.join(args)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Border:
        return _parse_fold_args(cls, args)


@dataclass
class Cut(DoodleParseableCommand):
    """Breaks an existing edge into two sub-edges at an intermediate vertex.

    The original edge is removed from internal storage and replaced by
    two new edges: [edge.v1, vertex] and [vertex, edge.v2].  The cut
    vertex need not geometrically belong to the edge.  Often used
    together with ``Hide`` to conceal parts of an edge after a fold.
    Maps to ``\\cut(edge, vertex);``.
    """

    DOO_KEYWORD = "cut"

    edge: Edge
    vertex: str

    def to_doo(self) -> str:
        return f"\\cut({self.edge.to_doo()}, {self.vertex})"

    @classmethod
    def from_doo_args(cls, args: list) -> Cut:
        return cls(edge=args[0], vertex=args[1])
