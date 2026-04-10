"""Geometric operator commands (middle, intersection, symmetry, etc.).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..parsing import DoodleParseableCommand
from ..types import Edge, Which


@dataclass
class Middle(DoodleParseableCommand):
    """Creates a new vertex at the midpoint of two existing vertices.

    The two given vertices need not have a physical edge between them.
    Maps to ``\\middle(v1, v2)``.  Wrap in ``Assign`` to capture the result.
    """

    DOO_KEYWORD = "middle"

    v1: str
    v2: str

    def to_doo(self) -> str:
        return f"\\middle({self.v1}, {self.v2})"

    @classmethod
    def from_doo_args(cls, args: list) -> Middle:
        return cls(v1=args[0], v2=args[1])


@dataclass
class Fraction(DoodleParseableCommand):
    """Creates a new vertex at a fractional position along a segment.

    An extension of ``\\middle``; the new vertex is located at
    ``numerator / denominator`` of the distance from *v1* to *v2*.
    Values outside [0, 1] place the point beyond the segment endpoints.
    Maps to ``\\fraction(v1, v2, numerator, denominator)``.  Wrap in
    ``Assign`` to capture the result.
    """

    DOO_KEYWORD = "fraction"

    v1: str
    v2: str
    numerator: int
    denominator: int

    def to_doo(self) -> str:
        return f"\\fraction({self.v1}, {self.v2}, {self.numerator}, {self.denominator})"

    @classmethod
    def from_doo_args(cls, args: list) -> Fraction:
        return cls(v1=args[0], v2=args[1], numerator=int(args[2]), denominator=int(args[3]))


@dataclass
class Intersection(DoodleParseableCommand):
    """Returns the intersection vertex of two edges (lines).

    The intersection is computed between the full lines through each pair
    of vertices, so the result may not lie on the physical segments.
    Accepts either two ``Edge`` objects or four vertices via the
    ``from_vertices`` class method.
    Maps to ``\\intersection(edge1, edge2)``
    or ``\\intersection(v1, v2, v3, v4)``.  Wrap in ``Assign`` to
    capture the result.
    """

    DOO_KEYWORD = "intersection"

    edge1: Edge
    edge2: Edge

    @classmethod
    def from_vertices(cls, v1: str, v2: str, v3: str, v4: str) -> Intersection:
        return cls(Edge(v1, v2), Edge(v3, v4))

    def to_doo(self) -> str:
        return f"\\intersection({self.edge1.v1}, {self.edge1.v2}, {self.edge2.v1}, {self.edge2.v2})"

    @classmethod
    def from_doo_args(cls, args: list) -> Intersection:
        if len(args) == 2 and isinstance(args[0], Edge) and isinstance(args[1], Edge):
            return cls(edge1=args[0], edge2=args[1])
        return cls(edge1=Edge(args[0], args[1]), edge2=Edge(args[2], args[3]))


@dataclass
class InterCut(DoodleParseableCommand):
    """Computes the intersection of two edges and cuts the first edge at that point.

    A shortcut combining ``\\intersection`` and ``\\cut``.  After this
    operation the first edge is split into two new sub-edges at the
    returned vertex, and the original edge no longer exists.
    Maps to ``\\inter_cut(edge1, edge2)``.  Wrap in ``Assign`` to
    capture the result.
    """

    DOO_KEYWORD = "inter_cut"

    edge1: Edge
    edge2: Edge

    def to_doo(self) -> str:
        return f"\\inter_cut({self.edge1.to_doo()}, {self.edge2.to_doo()})"

    @classmethod
    def from_doo_args(cls, args: list) -> InterCut:
        return cls(edge1=args[0], edge2=args[1])


@dataclass
class PointToPoint(DoodleParseableCommand):
    """Computes fold-line vertices for bringing one point onto another.

    Given a *moving* vertex and a *dest* vertex, returns the two
    intersection points of the fold line (perpendicular bisector) with
    *edge1* and *edge2* respectively.
    Maps to ``\\point_to_point(moving, dest, edge1, edge2)``.  Wrap in
    ``AssignPair`` to capture both results.
    """

    DOO_KEYWORD = "point_to_point"

    moving: str
    dest: str
    edge1: Edge
    edge2: Edge

    def to_doo(self) -> str:
        return f"\\point_to_point({self.moving}, {self.dest}, {self.edge1.to_doo()}, {self.edge2.to_doo()})"

    @classmethod
    def from_doo_args(cls, args: list) -> PointToPoint:
        return cls(moving=args[0], dest=args[1], edge1=args[2], edge2=args[3])


@dataclass
class PointToLine(DoodleParseableCommand):
    """Computes the fold-line vertex for bringing a point onto a line.

    Given a *moving* vertex and a *pivot*, finds where the fold line
    intersects *edge*.  *limit_edge* is the edge on which the point must
    arrive.  When two solutions exist, *which* selects ``FIRST`` or
    ``SECOND``.
    Maps to ``\\point_to_line(moving, pivot, limit_edge, edge[, which])``.
    Wrap in ``Assign`` to capture the result.
    """

    DOO_KEYWORD = "point_to_line"

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

    @classmethod
    def from_doo_args(cls, args: list) -> PointToLine:
        which = Which.FIRST
        if len(args) > 4:
            try:
                which = Which(args[4])
            except ValueError:
                pass
        return cls(moving=args[0], pivot=args[1], limit_edge=args[2], edge=args[3], which=which)


@dataclass
class LineToLine(DoodleParseableCommand):
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

    DOO_KEYWORD = "line_to_line"

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

    @classmethod
    def from_doo_args(cls, args: list) -> LineToLine:
        arg4 = args[3] if len(args) > 3 else None
        return cls(arg1=args[0], arg2=args[1], arg3=args[2], arg4=arg4)


@dataclass
class Symmetry(DoodleParseableCommand):
    """Creates a new vertex as the mirror image of a point through an axis.

    The axis is given as an ``Edge`` (pair of vertices); the edge need
    not physically exist.
    Maps to ``\\symmetry(vertex, edge)``.  Wrap in ``Assign`` to
    capture the result.
    """

    DOO_KEYWORD = "symmetry"

    vertex: str
    edge: Edge

    def to_doo(self) -> str:
        return f"\\symmetry({self.vertex}, {self.edge.to_doo()})"

    @classmethod
    def from_doo_args(cls, args: list) -> Symmetry:
        return cls(vertex=args[0], edge=args[1])


@dataclass
class Parallel(DoodleParseableCommand):
    """Creates a vertex where a line parallel to *edge* through *vertex* meets *limit_edge*.

    Maps to ``\\parallel(edge, vertex, limit_edge)``.  Wrap in
    ``Assign`` to capture the result.
    """

    DOO_KEYWORD = "parallel"

    edge: Edge
    vertex: str
    limit_edge: Edge

    def to_doo(self) -> str:
        return f"\\parallel({self.edge.to_doo()}, {self.vertex}, {self.limit_edge.to_doo()})"

    @classmethod
    def from_doo_args(cls, args: list) -> Parallel:
        return cls(edge=args[0], vertex=args[1], limit_edge=args[2])


@dataclass
class Perpendicular(DoodleParseableCommand):
    """Creates a vertex where a line perpendicular to *edge* from *vertex* meets another line.

    Without *limit_edge*, the returned point lies on the reference edge
    itself (i.e. is the foot of the perpendicular).  With *limit_edge*,
    the perpendicular is extended until it intersects that edge.
    Maps to ``\\perpendicular(edge, vertex[, limit_edge])``.  Wrap in
    ``Assign`` to capture the result.
    """

    DOO_KEYWORD = "perpendicular"

    edge: Edge
    vertex: str
    limit_edge: Edge | None = None

    def to_doo(self) -> str:
        if self.limit_edge is not None:
            return f"\\perpendicular({self.edge.to_doo()}, {self.vertex}, {self.limit_edge.to_doo()})"
        return f"\\perpendicular({self.edge.to_doo()}, {self.vertex})"

    @classmethod
    def from_doo_args(cls, args: list) -> Perpendicular:
        limit = args[2] if len(args) > 2 else None
        return cls(edge=args[0], vertex=args[1], limit_edge=limit)


@dataclass
class RabbitEar(DoodleParseableCommand):
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

    DOO_KEYWORD = "rabbit_ear"

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

    @classmethod
    def from_doo_args(cls, args: list) -> RabbitEar:
        moving, dest, v3 = args[0], args[1], args[2]
        center_or_edge = args[3] if len(args) > 3 else None
        edge = args[4] if len(args) > 4 else None
        return cls(moving=moving, dest=dest, v3=v3, center_or_edge=center_or_edge, edge=edge)
