from __future__ import annotations

from dataclasses import dataclass

from ..types import Edge, Which


@dataclass
class Middle:
    """Creates a new vertex at the midpoint of two existing vertices.

    The two given vertices need not have a physical edge between them.
    Maps to ``\\middle(v1, v2)``.  Wrap in ``Assign`` to capture the result.
    """

    v1: str
    v2: str

    def to_doo(self) -> str:
        return f"\\middle({self.v1}, {self.v2})"


@dataclass
class Fraction:
    """Creates a new vertex at a fractional position along a segment.

    An extension of ``\\middle``; the new vertex is located at
    ``numerator / denominator`` of the distance from *v1* to *v2*.
    Values outside [0, 1] place the point beyond the segment endpoints.
    Maps to ``\\fraction(v1, v2, numerator, denominator)``.  Wrap in
    ``Assign`` to capture the result.
    """

    v1: str
    v2: str
    numerator: int
    denominator: int

    def to_doo(self) -> str:
        return f"\\fraction({self.v1}, {self.v2}, {self.numerator}, {self.denominator})"


@dataclass
class Intersection:
    """Returns the intersection vertex of two edges (lines).

    The intersection is computed between the full lines through each pair
    of vertices, so the result may not lie on the physical segments.
    Accepts either two ``Edge`` objects or four vertices via the
    ``from_vertices`` class method.
    Maps to ``\\intersection(edge1, edge2)``
    or ``\\intersection(v1, v2, v3, v4)``.  Wrap in ``Assign`` to
    capture the result.
    """

    edge1: Edge
    edge2: Edge

    @classmethod
    def from_vertices(cls, v1: str, v2: str, v3: str, v4: str) -> Intersection:
        return cls(Edge(v1, v2), Edge(v3, v4))

    def to_doo(self) -> str:
        return f"\\intersection({self.edge1.v1}, {self.edge1.v2}, {self.edge2.v1}, {self.edge2.v2})"


@dataclass
class InterCut:
    """Computes the intersection of two edges and cuts the first edge at that point.

    A shortcut combining ``\\intersection`` and ``\\cut``.  After this
    operation the first edge is split into two new sub-edges at the
    returned vertex, and the original edge no longer exists.
    Maps to ``\\inter_cut(edge1, edge2)``.  Wrap in ``Assign`` to
    capture the result.
    """

    edge1: Edge
    edge2: Edge

    def to_doo(self) -> str:
        return f"\\inter_cut({self.edge1.to_doo()}, {self.edge2.to_doo()})"


@dataclass
class PointToPoint:
    """Computes fold-line vertices for bringing one point onto another.

    Given a *moving* vertex and a *dest* vertex, returns the two
    intersection points of the fold line (perpendicular bisector) with
    *edge1* and *edge2* respectively.
    Maps to ``\\point_to_point(moving, dest, edge1, edge2)``.  Wrap in
    ``AssignPair`` to capture both results.
    """

    moving: str
    dest: str
    edge1: Edge
    edge2: Edge

    def to_doo(self) -> str:
        return f"\\point_to_point({self.moving}, {self.dest}, {self.edge1.to_doo()}, {self.edge2.to_doo()})"


@dataclass
class PointToLine:
    """Computes the fold-line vertex for bringing a point onto a line.

    Given a *moving* vertex and a *pivot*, finds where the fold line
    intersects *edge*.  *limit_edge* is the edge on which the point must
    arrive.  When two solutions exist, *which* selects ``FIRST`` or
    ``SECOND``.
    Maps to ``\\point_to_line(moving, pivot, limit_edge, edge[, which])``.
    Wrap in ``Assign`` to capture the result.
    """

    moving: str
    pivot: str
    limit_edge: Edge
    edge: Edge
    which: Which = Which.FIRST

    def to_doo(self) -> str:
        args = [self.moving, self.pivot, self.limit_edge.to_doo(), self.edge.to_doo()]
        if self.which != Which.FIRST:
            args.append(str(self.which))
        return f"\\point_to_line({', '.join(args)})"


@dataclass
class LineToLine:
    """Computes vertices where one edge meets another via their median or bisector.

    **Syntax 1 (median, 4 edges):** computes the median line between
    *arg1* and *arg2*, then returns its intersections with *arg3* and
    *arg4*.  Use with ``AssignPair``.

    **Syntax 2 (bisector, 3 vertices + 1 edge):** computes the bisector
    of the angle at *arg1* (common vertex) through *arg2* and *arg3*,
    returning its intersection with *arg4* (an edge).

    Maps to ``\\line_to_line(e1, e2, e3, e4)``
    or ``\\line_to_line(v1, v2, v3, edge)``.  Wrap in ``AssignPair``
    or ``Assign`` depending on the syntax used.
    """

    arg1: Edge | str
    arg2: Edge | str
    arg3: Edge | str
    arg4: Edge | None = None

    def to_doo(self) -> str:
        parts = [
            self.arg1.to_doo() if isinstance(self.arg1, Edge) else self.arg1,
            self.arg2.to_doo() if isinstance(self.arg2, Edge) else self.arg2,
            self.arg3.to_doo() if isinstance(self.arg3, Edge) else self.arg3,
        ]
        if self.arg4 is not None:
            parts.append(self.arg4.to_doo() if isinstance(self.arg4, Edge) else self.arg4)
        return f"\\line_to_line({', '.join(parts)})"


@dataclass
class Symmetry:
    """Creates a new vertex as the mirror image of a point through an axis.

    The axis is given as an ``Edge`` (pair of vertices); the edge need
    not physically exist.
    Maps to ``\\symmetry(vertex, edge)``.  Wrap in ``Assign`` to
    capture the result.
    """

    vertex: str
    edge: Edge

    def to_doo(self) -> str:
        return f"\\symmetry({self.vertex}, {self.edge.to_doo()})"


@dataclass
class Parallel:
    """Creates a vertex where a line parallel to *edge* through *vertex* meets *limit_edge*.

    Maps to ``\\parallel(edge, vertex, limit_edge)``.  Wrap in
    ``Assign`` to capture the result.
    """

    edge: Edge
    vertex: str
    limit_edge: Edge

    def to_doo(self) -> str:
        return f"\\parallel({self.edge.to_doo()}, {self.vertex}, {self.limit_edge.to_doo()})"


@dataclass
class Perpendicular:
    """Creates a vertex where a line perpendicular to *edge* from *vertex* meets another line.

    Without *limit_edge*, the returned point lies on the reference edge
    itself (i.e. is the foot of the perpendicular).  With *limit_edge*,
    the perpendicular is extended until it intersects that edge.
    Maps to ``\\perpendicular(edge, vertex[, limit_edge])``.  Wrap in
    ``Assign`` to capture the result.
    """

    edge: Edge
    vertex: str
    limit_edge: Edge | None = None

    def to_doo(self) -> str:
        if self.limit_edge is not None:
            return f"\\perpendicular({self.edge.to_doo()}, {self.vertex}, {self.limit_edge.to_doo()})"
        return f"\\perpendicular({self.edge.to_doo()}, {self.vertex})"


@dataclass
class RabbitEar:
    """Computes vertices for a rabbit-ear fold on a triangle.

    The rabbit-ear fold uses three valley folds from each corner to a
    common intersection, plus one inverse (mountain) fold.

    **Regular syntax:** three corner vertices are given; the common centre
    is computed as the intersection of the three bisectors and returned
    alongside the result vertex.  Use with ``AssignPair``.

    **"Goofy" syntax:** the common centre is given explicitly as
    *center_or_edge*; only one vertex is returned.

    An optional *edge* parameter constrains where the result vertex is
    found (defaults to ``[moving, dest]``).

    Maps to ``\\rabbit_ear(moving, dest, v3[, edge])``
    or ``\\rabbit_ear(moving, dest, v3, center[, edge])``.  Wrap in
    ``AssignPair`` or ``Assign`` depending on the syntax used.
    """

    moving: str
    dest: str
    v3: str
    center_or_edge: str | Edge | None = None
    edge: Edge | None = None

    def to_doo(self) -> str:
        args = [self.moving, self.dest, self.v3]
        if self.center_or_edge is not None:
            c = self.center_or_edge
            args.append(c.to_doo() if isinstance(c, Edge) else c)
        if self.edge is not None:
            args.append(self.edge.to_doo())
        return f"\\rabbit_ear({', '.join(args)})"
