from __future__ import annotations

from dataclasses import dataclass, field

from .types import (
    ArrowHead,
    ArrowSide,
    Color,
    Edge,
    Limit,
    PaperFormat,
    Side,
    Which,
    string_quote,
)

# ── Comments ──────────────────────────────────────────────────────────


@dataclass
class DooComment:
    """A Doodle source comment line.

    Doodle uses ``%`` as a line-comment character.  Everything after
    ``%`` until the end of the line is ignored by the parser.
    """

    text: str = ""

    def to_doo(self) -> str:
        if self.text:
            return f"% {self.text}"
        return "%"


# ── Assignments ───────────────────────────────────────────────────────


@dataclass
class Assign:
    """Single variable assignment, mapping to Doodle's ``name = \\op(...);``.

    Many Doodle geometrical operators return a new vertex that is stored
    under a symbolic name.  ``Assign`` captures that pattern::

        Assign("o", Middle("a", "b"))   →   o = \\middle(a, b);
    """

    name: str
    expr: object

    def to_doo(self) -> str:
        return f"{self.name} = {self.expr.to_doo()}"


@dataclass
class AssignPair:
    """Pair variable assignment, mapping to Doodle's ``[n1, n2] = \\op(...);``.

    Operators like ``\\point_to_point`` and ``\\line_to_line`` return two
    vertices at once.  ``AssignPair`` captures that pattern::

        AssignPair(("i1", "i2"), PointToPoint(...))
        →  [i1, i2] = \\point_to_point(...);
    """

    names: tuple[str, str]
    expr: object

    def to_doo(self) -> str:
        n1, n2 = self.names
        return f"[{n1}, {n2}] = {self.expr.to_doo()}"


# ── Structure ─────────────────────────────────────────────────────────


@dataclass
class DiagramHeader:
    """Top-level block containing general diagram information.

    A Doodle file begins with a ``\\diagram_header { ... }`` block that
    holds metadata such as designer name, title, dates, paper colours
    and page-layout settings.  All header-specific operators (Designer,
    Title, Diagrammer, etc.) go inside *body*.
    """

    body: list = field(default_factory=list)

    def to_doo(self, indent: int = 0) -> str:
        pfx = "\t" * indent
        inner = "\t" * (indent + 1)
        lines = [f"{pfx}\\diagram_header {{"]
        for item in self.body:
            # Comments are bare lines; all other items need a trailing semicolon.
            suffix = "" if isinstance(item, DooComment) else ";"
            lines.append(f"{inner}{item.to_doo()}{suffix}")
        lines.append(f"{pfx}}}")
        return "\n".join(lines)


@dataclass
class Step:
    """Defines a single step of an origami diagram.

    A ``\\step { ... }`` block describes the operations for one step of the
    model.  Steps are automatically numbered starting from 1.  At the
    beginning of each step (after the first), points and edges from
    previous steps are carried forward.  Valley/mountain folds from the
    previous step become plain fold (crease) lines.  At the end of each
    step an automatic diagram output is produced.
    """

    body: list = field(default_factory=list)

    def to_doo(self, indent: int = 0) -> str:
        pfx = "\t" * indent
        inner = "\t" * (indent + 1)
        lines = [f"{pfx}\\step {{"]
        for item in self.body:
            # Comments are bare lines; all other items need a trailing semicolon.
            suffix = "" if isinstance(item, DooComment) else ";"
            lines.append(f"{inner}{item.to_doo()}{suffix}")
        lines.append(f"{pfx}}}")
        return "\n".join(lines)


@dataclass
class Diagram:
    """Root node of a complete Doodle diagram.

    A Doodle source file is composed of a ``\\diagram_header`` followed by
    a sequence of ``\\step`` blocks interleaved with top-level operators
    such as ``\\scale``, ``\\rotate``, ``\\turn_over_vertical``, etc.
    """

    header: DiagramHeader
    body: list = field(default_factory=list)

    def to_doo(self) -> str:
        parts = [self.header.to_doo(), ""]
        for item in self.body:
            # Steps and comments are self-contained; other items need a trailing semicolon.
            suffix = "" if isinstance(item, (Step, DooComment)) else ";"
            parts.append(f"{item.to_doo()}{suffix}")
            parts.append("")
        while parts and parts[-1] == "":
            parts.pop()
        return "\n".join(parts)


# ── Header operators ──────────────────────────────────────────────────


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


# ── Paper shapes ──────────────────────────────────────────────────────


@dataclass
class Square:
    """Defines four border edges forming a square and names the four corners.

    The first vertex is the upper-left corner; the remaining three follow
    clockwise: upper-right, lower-right, lower-left.
    Maps to ``\\square(v1, v2, v3, v4);``.
    """

    v1: str
    v2: str
    v3: str
    v4: str

    def to_doo(self) -> str:
        return f"\\square({self.v1}, {self.v2}, {self.v3}, {self.v4})"


@dataclass
class Diamond:
    """Defines four border edges forming a diamond (rotated square).

    The first vertex is the upper corner; the remaining three follow
    clockwise: right, bottom, left.  A diamond is a common starting shape.
    Maps to ``\\diamond(v1, v2, v3, v4);``.
    """

    v1: str
    v2: str
    v3: str
    v4: str

    def to_doo(self) -> str:
        return f"\\diamond({self.v1}, {self.v2}, {self.v3}, {self.v4})"


@dataclass
class HorizontalRectangle:
    """Defines four border edges forming a horizontal rectangle.

    Corners are named upper-left clockwise.  The fifth parameter is the
    width-to-height ratio as a percentage (e.g. 200 = twice as wide as
    tall) or a named paper format symbol (``"A"``, ``"dollar"``).
    Maps to ``\\horizontal_rectangle(v1, v2, v3, v4, ratio);``.
    """

    v1: str
    v2: str
    v3: str
    v4: str
    ratio: int | PaperFormat | None = None

    def to_doo(self) -> str:
        args = [self.v1, self.v2, self.v3, self.v4]
        if self.ratio is not None:
            args.append(str(self.ratio))
        return f"\\horizontal_rectangle({', '.join(args)})"


@dataclass
class VerticalRectangle:
    """Defines four border edges forming a vertical rectangle.

    Corners are named upper-left clockwise.  The fifth parameter is the
    height-to-width ratio as a percentage (e.g. 200 = twice as tall as
    wide) or a named paper format symbol (``"A"``, ``"dollar"``).
    Maps to ``\\vertical_rectangle(v1, v2, v3, v4, ratio);``.
    """

    v1: str
    v2: str
    v3: str
    v4: str
    ratio: int | PaperFormat | None = None

    def to_doo(self) -> str:
        args = [self.v1, self.v2, self.v3, self.v4]
        if self.ratio is not None:
            args.append(str(self.ratio))
        return f"\\vertical_rectangle({', '.join(args)})"


# ── Geometrical operators (produce new vertices) ─────────────────────


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
            parts.append(
                self.arg4.to_doo() if isinstance(self.arg4, Edge) else self.arg4
            )
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


# ── Geometrical operators (no return value) ──────────────────────────


@dataclass
class Move:
    """Moves a vertex to a new position.

    Changes the internal coordinates of *src*.

    * **Syntax 1:** *dest* is a vertex name — *src* gets the coordinates
      of *dest*.
    * **Syntax 2:** *dest* is an ``Edge`` — *src* is reflected (mirrored)
      through that edge, simulating the result of folding along the edge.

    Maps to ``\\move(src, dest);`` or ``\\move(src, edge);``.
    """

    src: str
    dest: str | Edge

    def to_doo(self) -> str:
        d = self.dest.to_doo() if isinstance(self.dest, Edge) else self.dest
        return f"\\move({self.src}, {d})"


@dataclass
class Shift:
    """Visually displaces a vertex for pseudo-3D diagrams.

    The shift does **not** alter the internal geometric coordinates; it
    only offsets the rendering position by *(dx, dy)* millimetres.
    However, future geometric operations on the shifted point will use
    the shifted coordinates to maintain visual consistency.
    Maps to ``\\shift(vertex, dx, dy);``.
    """

    vertex: str
    dx: int | float
    dy: int | float

    def to_doo(self) -> str:
        dx = (
            str(int(self.dx))
            if isinstance(self.dx, float) and self.dx == int(self.dx)
            else str(self.dx)
        )
        dy = (
            str(int(self.dy))
            if isinstance(self.dy, float) and self.dy == int(self.dy)
            else str(self.dy)
        )
        return f"\\shift({self.vertex}, {dx}, {dy})"


@dataclass
class Unshift:
    """Resets all previously applied shifts on a vertex.

    Maps to ``\\unshift(vertex);``.
    """

    vertex: str

    def to_doo(self) -> str:
        return f"\\unshift({self.vertex})"


# ── Line / fold operators ────────────────────────────────────────────


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


# ── Arrow operators ──────────────────────────────────────────────────


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


# ── Edge management ──────────────────────────────────────────────────


@dataclass
class Hide:
    """Hides previously drawn graphical elements.

    * If *targets* is an ``Edge``, that specific edge is hidden.
    * If *targets* is a list of vertex names, **all edges containing any
      of those vertices** are hidden.

    Maps to ``\\hide(edge);`` or ``\\hide(v1, v2, ...);``.
    """

    targets: Edge | list[str]

    def to_doo(self) -> str:
        if isinstance(self.targets, Edge):
            return f"\\hide({self.targets.to_doo()})"
        return f"\\hide({', '.join(self.targets)})"


@dataclass
class Show:
    """Re-shows previously hidden graphical elements (dual of ``Hide``).

    Accepts the same target forms as ``Hide``.
    Maps to ``\\show(edge);`` or ``\\show(v1, v2, ...);``.
    """

    targets: Edge | list[str]

    def to_doo(self) -> str:
        if isinstance(self.targets, Edge):
            return f"\\show({self.targets.to_doo()})"
        return f"\\show({', '.join(self.targets)})"


@dataclass
class SpaceFold:
    """Overrides the blank percentage at each extremity of an existing edge.

    Useful to fine-tune the visual gap at fold endpoints after automatic
    style changes.
    Maps to ``\\space_fold(edge, pct1, pct2);``.
    """

    edge: Edge
    pct1: int
    pct2: int

    def to_doo(self) -> str:
        return f"\\space_fold({self.edge.to_doo()}, {self.pct1}, {self.pct2})"


# ── Faces coloring ───────────────────────────────────────────────────


@dataclass
class Fill:
    """Fills a polygonal area with the front or back paper colour.

    *vertices* must be given in circular order; the polygon is
    automatically closed between the first and last vertex.  Filled
    areas are drawn in chronological order (first defined, first drawn).
    Maps to ``\\fill(side, v1, v2, ...);``.
    """

    side: Side
    vertices: list[str]

    def to_doo(self) -> str:
        args = [str(self.side)] + self.vertices
        return f"\\fill({', '.join(args)})"


@dataclass
class Unfill:
    """Clears a previously filled area.

    If *vertices* is empty then **all** previously filled faces are
    cleared.  Otherwise, the face matching the given vertex set
    (order-independent) is removed.
    Maps to ``\\unfill(v1, v2, ...);`` or ``\\unfill;``.
    """

    vertices: list[str] = field(default_factory=list)

    def to_doo(self) -> str:
        if self.vertices:
            return f"\\unfill({', '.join(self.vertices)})"
        return "\\unfill"


@dataclass
class Darker:
    """Decreases the lightness of the given paper side colour.

    *amount* controls the darkening degree.
    Maps to ``\\darker(side, amount);``.
    """

    side: Side
    amount: int

    def to_doo(self) -> str:
        return f"\\darker({self.side}, {self.amount})"


@dataclass
class Lighter:
    """Increases the lightness of the given paper side colour.

    *amount* controls the lightening degree.
    Maps to ``\\lighter(side, amount);``.
    """

    side: Side
    amount: int

    def to_doo(self) -> str:
        return f"\\lighter({self.side}, {self.amount})"


# ── Text operators ───────────────────────────────────────────────────


@dataclass
class Caption:
    """Adds an explanatory text line beneath the current step.

    Multiple captions per step are stacked in order.
    Maps to ``\\caption("text");``.
    """

    text: str

    def to_doo(self) -> str:
        return f"\\caption({string_quote(self.text)})"


@dataclass
class Label:
    """Defines a named label bound to the current step number.

    Labels are used by ``RepeatArrow`` and ``Ref`` to reference step
    numbers symbolically.  Label identifiers live in a separate symbol
    table from vertex identifiers.
    Maps to ``\\label(name);``.
    """

    name: str

    def to_doo(self) -> str:
        return f"\\label({self.name})"


@dataclass
class Ref:
    """Substitutes a step number into a string (used inside ``\\caption``).

    Maps to ``\\ref(label);``.
    """

    step: int

    def to_doo(self) -> str:
        return f"\\ref({self.step})"


@dataclass
class Text:
    """Draws annotation text at a vertex position.

    Maps to ``\\text(vertex, "text");``.
    """

    vertex: str
    text: str

    def to_doo(self) -> str:
        return f"\\text({self.vertex}, {string_quote(self.text)})"


# ── Step / page layout ───────────────────────────────────────────────


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


# ── Model manipulation ───────────────────────────────────────────────


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


# ── Debugging ────────────────────────────────────────────────────────


@dataclass
class Debug:
    """Displays all visible point names and edge names for the current step.

    A diagnostic aid; combines the effects of ``DebugPoint`` and
    ``DebugLine``.
    Maps to ``\\debug;``.
    """

    def to_doo(self) -> str:
        return "\\debug"


@dataclass
class DebugLine:
    """Displays visible edge names for the current step.

    Maps to ``\\debug_line;``.
    """

    def to_doo(self) -> str:
        return "\\debug_line"


@dataclass
class DebugPoint:
    """Displays visible vertex names for the current step.

    Maps to ``\\debug_point;``.
    """

    def to_doo(self) -> str:
        return "\\debug_point"


# ── Miscellaneous ────────────────────────────────────────────────────


@dataclass
class Reset:
    """Resets all internal data structures to their initial state.

    Maps to ``\\reset;``.
    """

    def to_doo(self) -> str:
        return "\\reset"


@dataclass
class Include:
    """Includes another Doodle source file at the current position.

    Maps to ``\\include("filename");``.
    """

    filename: str

    def to_doo(self) -> str:
        return f"\\include({string_quote(self.filename)})"
