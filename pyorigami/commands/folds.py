from __future__ import annotations

from dataclasses import dataclass

from ..types import Edge, Limit


@dataclass
class ValleyFold:
    """Marks a valley fold between two vertices — drawn as a dashed line.

    The implicit result is a new valley edge in the global edge
    structure.  Optional *limit1*/*limit2* control how much of the line
    is drawn (percentage of blank or intersection edge).  Negative
    percentages extend the line beyond the endpoint.

    The operator is "opportunist": it only creates a new edge if one
    does not already exist between the two vertices.
    Maps to ``\\valley_fold(v1, v2[, limit1, limit2]);``.
    """

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


@dataclass
class MountainFold:
    """Marks a mountain fold between two vertices — drawn as a dot-dot-dash line.

    Behaves identically to ``ValleyFold`` but uses mountain line style.
    Optional *limit1*/*limit2* control the visible portion of the line.
    Maps to ``\\mountain_fold(v1, v2[, limit1, limit2]);``.
    """

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


@dataclass
class XrayFold:
    """Marks an x-ray fold between two vertices — drawn as a dotted line.

    Used to show a fold line that is hidden by paper layers.
    Optional *limit1*/*limit2* control the visible portion of the line.
    Maps to ``\\xray_fold(v1, v2[, limit1, limit2]);``.
    """

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


@dataclass
class Fold:
    """Marks an existing crease between two vertices — drawn as a thin short line.

    Fold edges are displayed as incomplete thin lines that don't reach
    the vertices.  Usually created automatically at the start of a step
    when valley/mountain folds from the previous step are carried
    forward, but can also be set explicitly.
    Optional *limit1*/*limit2* control the visible portion of the line.
    Maps to ``\\fold(v1, v2[, limit1, limit2]);``.
    """

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


@dataclass
class Border:
    """Draws a border line between two vertices — displayed as a thick plain line.

    Represents paper edges.  Like other line operators, optional
    *limit1*/*limit2* control the visible portion (percentage or
    intersection edge).
    Maps to ``\\border(v1, v2[, limit1, limit2]);``.
    """

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


@dataclass
class Cut:
    """Breaks an existing edge into two sub-edges at an intermediate vertex.

    The original edge is removed from internal storage and replaced by
    two new edges: [edge.v1, vertex] and [vertex, edge.v2].  The cut
    vertex need not geometrically belong to the edge.  Often used
    together with ``Hide`` to conceal parts of an edge after a fold.
    Maps to ``\\cut(edge, vertex);``.
    """

    edge: Edge
    vertex: str

    def to_doo(self) -> str:
        return f"\\cut({self.edge.to_doo()}, {self.vertex})"
