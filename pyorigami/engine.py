"""Interpreter that evaluates a Diagram command tree into computed geometry.

Walks the ``Diagram`` dataclass tree produced by the user and executes
every geometric operation, building up a list of ``ComputedStep`` objects
that contain fully resolved vertex positions, edges, arrows, and faces
ready for PostScript rendering.

Derived from ``doodle/src/read_instruction.cpp`` in the
`DOODLE <https://doodle.sourceforge.net/>`_ project by Olivier Bettens.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from . import commands as cmd
from .types import ArrowHead, ArrowSide, Edge, PaperFormat, Side, Which
from .geometry import (
    CLIP_HEIGHT,
    CLIP_WIDTH,
    DIAMOND_EDGE,
    FOLDSPC,
    RETURN_ARROW_RATIO,
    SIMPLE_ARROW_ANGLE,
    SQUARE_EDGE,
    ArrowSymbol,
    ComputedHeader,
    ComputedStep,
    EdgeType,
    Arrow,
    InternalColor,
    InternalEdge,
    Face,
    OpenArrowSymbol,
    PushArrowSymbol,
    RepeatArrowSymbol,
    TurnType,
    Vec2,
    Vertex,
)

if TYPE_CHECKING:
    pass


def _resolve_color(c, header: ComputedHeader) -> InternalColor:
    """Resolve a Color value (tuple or 'front'/'back') to InternalColor."""
    if isinstance(c, tuple):
        return InternalColor(*c)
    if isinstance(c, str):
        if c == "front":
            return header.front_color
        if c == "back":
            return header.back_color
    return InternalColor(100, 100, 100)


def _gen_sym(step: ComputedStep, base: str) -> str:
    s = base
    while step.symbol_exists("_" + s):
        s = "_" + s
    return "_" + s


# ---------------------------------------------------------------------------
# Engine
# ---------------------------------------------------------------------------


class Engine:
    """Evaluate a ``Diagram`` into computed geometry."""

    def __init__(self) -> None:
        self.header = ComputedHeader()
        self.steps: list[ComputedStep] = []
        self._current_step = 0
        self._current_index = 1
        self._visible_height = CLIP_HEIGHT
        self._visible_width = CLIP_WIDTH
        self._scale = 100
        self._center = ""
        self._clip = False
        self._labels: dict[str, int] = {}

    # -- public API ---------------------------------------------------------

    def evaluate(self, diagram: cmd.Diagram) -> tuple[ComputedHeader, list[ComputedStep]]:
        """Process a full Diagram and return ``(header, steps)``."""
        self._process_header(diagram.header)
        for item in diagram.body:
            self._process_top_level(item)
        return self.header, self.steps

    # -- header -------------------------------------------------------------

    def _process_header(self, hdr: cmd.DiagramHeader) -> None:
        comment_idx = 0
        for item in hdr.body:
            if isinstance(item, cmd.DooComment):
                continue
            elif isinstance(item, cmd.Designer):
                self.header.designer = item.name
            elif isinstance(item, cmd.Title):
                self.header.title = item.name
            elif isinstance(item, cmd.Diagrammer):
                self.header.diagrammer = item.name
            elif isinstance(item, cmd.DiagramDate):
                self.header.diagram_date_year = item.year
            elif isinstance(item, cmd.DesignDate):
                self.header.design_date_year = item.year
            elif isinstance(item, cmd.Comment):
                comment_idx += 1
                if comment_idx == 1:
                    self.header.comment1 = item.text
                elif comment_idx == 2:
                    self.header.comment2 = item.text
                elif comment_idx == 3:
                    self.header.comment3 = item.text
            elif isinstance(item, cmd.ColorFront):
                if isinstance(item.color, tuple):
                    self.header.front_color = InternalColor(*item.color)
                elif isinstance(item.color, str):
                    self.header.front_color = _resolve_color(item.color, self.header)
            elif isinstance(item, cmd.ColorBack):
                if isinstance(item.color, tuple):
                    self.header.back_color = InternalColor(*item.color)
                elif isinstance(item.color, str):
                    self.header.back_color = _resolve_color(item.color, self.header)
            elif isinstance(item, cmd.BottomMargin):
                self.header.bottom_margin = item.value
            elif isinstance(item, cmd.TopMargin):
                self.header.top_margin = item.value
            elif isinstance(item, cmd.LeftMargin):
                self.header.left_margin = item.value
            elif isinstance(item, cmd.RightMargin):
                self.header.right_margin = item.value
            elif isinstance(item, cmd.HorizontalSpace):
                self.header.h_space = item.value
            elif isinstance(item, cmd.VerticalSpace):
                self.header.v_space = item.value

    # -- top-level items (steps + inter-step commands) ----------------------

    def _process_top_level(self, item: object) -> None:
        if isinstance(item, cmd.Step):
            self._new_step()
            for child in item.body:
                self._process_step_item(child)
        elif isinstance(item, cmd.TurnOverVertical):
            if self.steps:
                self.steps[-1].turn = TurnType.VERTICAL
        elif isinstance(item, cmd.TurnOverHorizontal):
            if self.steps:
                self.steps[-1].turn = TurnType.HORIZONTAL
        elif isinstance(item, cmd.Rotate):
            if self.steps:
                self.steps[-1].rotate += item.degrees
        elif isinstance(item, cmd.Scale):
            self._scale = item.percent
        elif isinstance(item, cmd.VisibleAreaHeight):
            self._visible_height = item.value
        elif isinstance(item, cmd.VisibleAreaWidth):
            self._visible_width = item.value
        elif isinstance(item, cmd.VisibleAreaCenter):
            self._center = item.vertex
        elif isinstance(item, cmd.Clip):
            self._clip = True
        elif isinstance(item, cmd.Unclip):
            self._clip = False
        elif isinstance(item, cmd.DooComment):
            pass

    # -- create a new computed step -----------------------------------------

    def _new_step(self) -> None:
        cx, cy = 0.0, 0.0
        if self._center and self.steps:
            v = self.steps[-1].get_vertex(self._center)
            cx, cy = v.x, v.y

        s = ComputedStep(
            clip_width=self._visible_width,
            clip_height=self._visible_height,
            scale=self._scale,
            visible_center_x=cx,
            visible_center_y=cy,
            clip=self._clip,
        )
        s.index = str(self._current_index)

        if self.steps:
            prev = self.steps[-1]
            s.fill_update(prev)
            if prev.turn != TurnType.NONE:
                s.turn_vertices(prev.turn)

        self.steps.append(s)
        self._current_step = len(self.steps) - 1
        self._current_index += 1

    # -- helpers ------------------------------------------------------------

    @property
    def _step(self) -> ComputedStep:
        return self.steps[self._current_step]

    def _prev_rotate(self) -> float:
        if self._current_step > 0:
            return self.steps[self._current_step - 1].rotate
        return 0.0

    def _angle_scale(self) -> tuple[float, int]:
        return self._prev_rotate(), self._step.scale

    def _search_edge(self, s1: str, s2: str) -> int:
        return self._step.search_edge(s1, s2)

    def _search_edge_and_hide_equivalent(self, s1: str, s2: str) -> int:
        """Find edge (s1,s2). Also hide any edge with equivalent vertex coords."""
        v1 = self._step.get_vertex(s1)
        v2 = self._step.get_vertex(s2)
        found = -1
        for i, e in enumerate(self._step.lines):
            if e.equal(s1, s2):
                found = i
            else:
                vl1 = self._step.get_vertex(e.v1)
                vl2 = self._step.get_vertex(e.v2)
                if (vl1.equivalent(v1) and vl2.equivalent(v2)) or (vl1.equivalent(v2) and vl2.equivalent(v1)):
                    e.visible = False
        return found

    # -- process a single step-level item -----------------------------------

    def _process_step_item(self, item: object) -> None:  # noqa: C901, PLR0912
        s = self._step

        if isinstance(item, cmd.DooComment):
            return

        # -- assignments --
        if isinstance(item, cmd.Assign):
            self._process_assign(item)
            return
        if isinstance(item, cmd.AssignPair):
            self._process_assign_pair(item)
            return

        # -- paper shapes --
        if isinstance(item, cmd.Square):
            self._read_square(item)
            return
        if isinstance(item, cmd.Diamond):
            self._read_diamond(item)
            return
        if isinstance(item, (cmd.HorizontalRectangle, cmd.VerticalRectangle)):
            self._read_rectangle(item)
            return

        # -- folds --
        if isinstance(item, cmd.ValleyFold):
            self._read_fold(item.v1, item.v2, EdgeType.VALLEY, item.limit1, item.limit2)
            return
        if isinstance(item, cmd.MountainFold):
            self._read_fold(item.v1, item.v2, EdgeType.MOUNTAIN, item.limit1, item.limit2)
            return
        if isinstance(item, cmd.XrayFold):
            self._read_fold(item.v1, item.v2, EdgeType.XRAY, item.limit1, item.limit2)
            return
        if isinstance(item, cmd.Fold):
            self._read_fold(item.v1, item.v2, EdgeType.FOLD, item.limit1, item.limit2)
            return
        if isinstance(item, cmd.Border):
            self._read_fold(item.v1, item.v2, EdgeType.BORDER, item.limit1, item.limit2)
            return

        # -- edge management --
        if isinstance(item, cmd.Hide):
            self._read_hide_show(item.targets, visible=False)
            return
        if isinstance(item, cmd.Show):
            self._read_hide_show(item.targets, visible=True)
            return
        if isinstance(item, cmd.SpaceFold):
            self._read_space_fold(item)
            return
        if isinstance(item, cmd.Cut):
            self._read_cut(item)
            return

        # -- fill --
        if isinstance(item, cmd.Fill):
            self._read_fill(item)
            return
        if isinstance(item, cmd.Unfill):
            self._read_unfill(item)
            return
        if isinstance(item, cmd.Darker):
            self._read_darker_lighter(item, darken=True)
            return
        if isinstance(item, cmd.Lighter):
            self._read_darker_lighter(item, darken=False)
            return

        # -- arrows --
        if isinstance(item, cmd.SimpleArrow):
            self._read_simple_arrow(item)
            return
        if isinstance(item, cmd.ReturnArrow):
            self._read_return_arrow(item)
            return
        if isinstance(item, cmd.OpenArrow):
            self._read_open_arrow(item)
            return
        if isinstance(item, cmd.PushArrow):
            self._read_push_arrow(item)
            return
        if isinstance(item, cmd.RepeatArrow):
            self._read_repeat_arrow(item)
            return

        # -- text / caption / label --
        if isinstance(item, cmd.Caption):
            s.captions.append(item.text)
            return
        if isinstance(item, cmd.Label):
            self._labels[item.name] = self._current_index - 1
            return
        if isinstance(item, cmd.Text):
            v = s.get_vertex(item.vertex)
            v.add_text(item.text)
            return

        # -- move / shift --
        if isinstance(item, cmd.Move):
            self._read_move(item)
            return
        if isinstance(item, cmd.Shift):
            v = s.get_vertex(item.vertex)
            v.dx = item.dx
            v.dy = item.dy
            return
        if isinstance(item, cmd.Unshift):
            v = s.get_vertex(item.vertex)
            v.dx = 0.0
            v.dy = 0.0
            return

        # -- step layout --
        if isinstance(item, cmd.VisibleAreaCenter):
            v = s.get_vertex(item.vertex)
            s.visible_center_x = v.x
            s.visible_center_y = v.y
            return
        if isinstance(item, cmd.VisibleAreaHeight):
            s.clip_height = item.value
            return
        if isinstance(item, cmd.VisibleAreaWidth):
            s.clip_width = item.value
            return
        if isinstance(item, cmd.Scale):
            s.scale = item.percent
            return
        if isinstance(item, cmd.Clip):
            s.clip = True
            return
        if isinstance(item, cmd.Unclip):
            s.clip = False
            return

        # -- debug --
        if isinstance(item, cmd.Debug):
            for v in s.vertices:
                v.debug = True
            for e in s.lines:
                e.debug = True
            return
        if isinstance(item, cmd.DebugPoint):
            for v in s.vertices:
                v.debug = True
            return
        if isinstance(item, cmd.DebugLine):
            for e in s.lines:
                e.debug = True
            return

        if isinstance(item, cmd.Reset):
            s.vertices.clear()
            s.lines.clear()
            s.faces.clear()
            return

    # -- paper shapes -------------------------------------------------------

    def _read_square(self, sq: cmd.Square) -> None:
        s = self._step
        v1 = Vertex(sq.v1, -SQUARE_EDGE, SQUARE_EDGE)
        v2 = Vertex(sq.v2, SQUARE_EDGE, SQUARE_EDGE)
        v3 = Vertex(sq.v3, SQUARE_EDGE, -SQUARE_EDGE)
        v4 = Vertex(sq.v4, -SQUARE_EDGE, -SQUARE_EDGE)
        s.vertices.extend([v1, v2, v3, v4])
        s.lines.append(InternalEdge(sq.v1, sq.v2))
        s.lines.append(InternalEdge(sq.v2, sq.v3))
        s.lines.append(InternalEdge(sq.v3, sq.v4))
        s.lines.append(InternalEdge(sq.v4, sq.v1))

    def _read_diamond(self, dm: cmd.Diamond) -> None:
        s = self._step
        v1 = Vertex(dm.v1, 0, DIAMOND_EDGE)
        v2 = Vertex(dm.v2, DIAMOND_EDGE, 0)
        v3 = Vertex(dm.v3, 0, -DIAMOND_EDGE)
        v4 = Vertex(dm.v4, -DIAMOND_EDGE, 0)
        s.vertices.extend([v1, v2, v3, v4])
        s.lines.append(InternalEdge(dm.v1, dm.v2))
        s.lines.append(InternalEdge(dm.v2, dm.v3))
        s.lines.append(InternalEdge(dm.v3, dm.v4))
        s.lines.append(InternalEdge(dm.v4, dm.v1))

    def _read_rectangle(self, rect: cmd.HorizontalRectangle | cmd.VerticalRectangle) -> None:
        s = self._step
        ratio: int
        if rect.ratio is None:
            ratio = 100
        elif isinstance(rect.ratio, PaperFormat):
            ratio = rect.ratio.ratio
        else:
            ratio = rect.ratio

        is_horizontal = isinstance(rect, cmd.HorizontalRectangle)
        if is_horizontal:
            expand_x = ratio > 100
        else:
            expand_x = ratio < 100

        if expand_x:
            v1 = Vertex(rect.v1, -ratio * (SQUARE_EDGE / 100.0), SQUARE_EDGE)
            v2 = Vertex(rect.v2, ratio * (SQUARE_EDGE / 100.0), SQUARE_EDGE)
            v3 = Vertex(rect.v3, ratio * (SQUARE_EDGE / 100.0), -SQUARE_EDGE)
            v4 = Vertex(rect.v4, -ratio * (SQUARE_EDGE / 100.0), -SQUARE_EDGE)
        else:
            v1 = Vertex(rect.v1, -SQUARE_EDGE, ratio * (SQUARE_EDGE / 100.0))
            v2 = Vertex(rect.v2, SQUARE_EDGE, ratio * (SQUARE_EDGE / 100.0))
            v3 = Vertex(rect.v3, SQUARE_EDGE, -ratio * (SQUARE_EDGE / 100.0))
            v4 = Vertex(rect.v4, -SQUARE_EDGE, -ratio * (SQUARE_EDGE / 100.0))

        s.vertices.extend([v1, v2, v3, v4])
        s.lines.append(InternalEdge(rect.v1, rect.v2))
        s.lines.append(InternalEdge(rect.v2, rect.v3))
        s.lines.append(InternalEdge(rect.v3, rect.v4))
        s.lines.append(InternalEdge(rect.v4, rect.v1))

    # -- assignments (geometric operators) ----------------------------------

    def _process_assign(self, a: cmd.Assign) -> None:
        expr = a.expr
        angle, sc = self._angle_scale()
        s = self._step

        if isinstance(expr, cmd.Middle):
            v1 = s.get_vertex(expr.v1)
            v2 = s.get_vertex(expr.v2)
            v = v1.middle(v2)
            v.name = a.name
            s.vertices.append(v)

        elif isinstance(expr, cmd.Fraction):
            v1 = s.get_vertex(expr.v1)
            v2 = s.get_vertex(expr.v2)
            v = v1.fraction(v2, expr.numerator, expr.denominator)
            v.name = a.name
            s.vertices.append(v)

        elif isinstance(expr, cmd.Intersection):
            v1 = s.get_vertex(expr.edge1.v1)
            v2 = s.get_vertex(expr.edge1.v2)
            v3 = s.get_vertex(expr.edge2.v1)
            v4 = s.get_vertex(expr.edge2.v2)
            v = v1.intersection(v2, v3, v4, angle, sc)
            v.name = a.name
            s.vertices.append(v)

        elif isinstance(expr, cmd.InterCut):
            e1v1 = s.get_vertex(expr.edge1.v1)
            e1v2 = s.get_vertex(expr.edge1.v2)
            e2v1 = s.get_vertex(expr.edge2.v1)
            e2v2 = s.get_vertex(expr.edge2.v2)
            v = e1v1.intersection(e1v2, e2v1, e2v2, angle, sc)
            v.name = a.name
            s.vertices.append(v)
            self._cut_edge(v, e1v1, e1v2, a.name, expr.edge1.v1, expr.edge1.v2)

        elif isinstance(expr, cmd.Symmetry):
            vo = s.get_vertex(expr.vertex)
            va = s.get_vertex(expr.edge.v1)
            vb = s.get_vertex(expr.edge.v2)
            vr = vo.symmetry(va, vb, angle, sc)
            vr.name = a.name
            s.vertices.append(vr)

        elif isinstance(expr, cmd.Perpendicular):
            vo = s.get_vertex(expr.vertex)
            v1 = s.get_vertex(expr.edge.v1)
            v2 = s.get_vertex(expr.edge.v2)
            if expr.limit_edge is not None:
                v3 = s.get_vertex(expr.limit_edge.v1)
                v4 = s.get_vertex(expr.limit_edge.v2)
                p = vo.projection(v1, v2)
                if p == vo:
                    u = Vec2.between(v1, v2).ortho()
                    auxi = Vertex("null", vo.x + u.x, vo.y + u.y)
                    vr = p.intersection(auxi, v3, v4, angle, sc)
                else:
                    vr = p.intersection(vo, v3, v4, angle, sc)
            else:
                vr = vo.projection(v1, v2)
            vr.name = a.name
            s.vertices.append(vr)

        elif isinstance(expr, cmd.Parallel):
            vo = s.get_vertex(expr.vertex)
            v1 = s.get_vertex(expr.edge.v1)
            v2 = s.get_vertex(expr.edge.v2)
            v3 = s.get_vertex(expr.limit_edge.v1)
            v4 = s.get_vertex(expr.limit_edge.v2)
            u = Vec2.between(v1, v2)
            p = Vertex("null", vo.x + u.x, vo.y + u.y)
            vr = p.intersection(vo, v3, v4, angle, sc)
            vr.name = a.name
            s.vertices.append(vr)

        elif isinstance(expr, cmd.PointToLine):
            mv = s.get_vertex(expr.moving)
            pvt = s.get_vertex(expr.pivot)
            va = s.get_vertex(expr.limit_edge.v1)
            vb = s.get_vertex(expr.limit_edge.v2)
            vc = s.get_vertex(expr.edge.v1)
            vd = s.get_vertex(expr.edge.v2)
            first = expr.which == Which.FIRST
            v = mv.vertex_to_line(pvt, va, vb, vc, vd, first, angle, sc)
            v.name = a.name
            s.vertices.append(v)

        elif isinstance(expr, cmd.LineToLine):
            # 3-arg form: bisector
            if isinstance(expr.arg1, str) and isinstance(expr.arg2, str) and isinstance(expr.arg3, str):
                raise ValueError("LineToLine 3-vertex form must be used with AssignPair or have an edge arg4")
            elif isinstance(expr.arg1, str) and isinstance(expr.arg2, str) and isinstance(expr.arg3, Edge):
                # bisector: arg1=common vertex, arg2=vertex, arg3=edge
                va = s.get_vertex(expr.arg1)
                vb = s.get_vertex(expr.arg2)
                if expr.arg4 is None:
                    raise ValueError("LineToLine bisector form requires arg4 (edge)")
                # Actually the 5-arg form: \line_to_line(a, b, c, [d,e])
                # arg1=a, arg2=b, arg3=c (vertex), arg4=[d,e]
                pass
            # Handle line_to_line(a, b, c, [d,e]) -- bisector form
            if (
                isinstance(expr.arg1, str)
                and isinstance(expr.arg2, str)
                and isinstance(expr.arg3, str)
                and isinstance(expr.arg4, Edge)
            ):
                va = s.get_vertex(expr.arg1)
                vb = s.get_vertex(expr.arg2)
                vc = s.get_vertex(expr.arg3)
                vd = s.get_vertex(expr.arg4.v1)
                ve = s.get_vertex(expr.arg4.v2)
                v_biss = va.bisector(vb, vc, angle, sc)
                vr = va.intersection(v_biss, vd, ve, angle, sc)
                vr.name = a.name
                s.vertices.append(vr)

        elif isinstance(expr, cmd.RabbitEar):
            self._read_rabbit_ear_assign(a.name, expr)

    def _process_assign_pair(self, ap: cmd.AssignPair) -> None:
        expr = ap.expr
        n1, n2 = ap.names
        angle, sc = self._angle_scale()
        s = self._step

        if isinstance(expr, cmd.PointToPoint):
            vsrc = s.get_vertex(expr.moving)
            vdst = s.get_vertex(expr.dest)
            va = s.get_vertex(expr.edge1.v1)
            vb = s.get_vertex(expr.edge1.v2)
            vc = s.get_vertex(expr.edge2.v1)
            vd = s.get_vertex(expr.edge2.v2)
            v1 = vsrc.mediator(vdst, va, vb, angle, sc)
            v2 = vsrc.mediator(vdst, vc, vd, angle, sc)
            v1.name = n1
            v2.name = n2
            s.vertices.append(v1)
            s.vertices.append(v2)

        elif isinstance(expr, cmd.LineToLine):
            # 4-edge form: median/bisector returning two intersection points
            if (
                isinstance(expr.arg1, Edge)
                and isinstance(expr.arg2, Edge)
                and isinstance(expr.arg3, Edge)
                and isinstance(expr.arg4, Edge)
            ):
                va = s.get_vertex(expr.arg1.v1)
                vb = s.get_vertex(expr.arg1.v2)
                vc = s.get_vertex(expr.arg2.v1)
                vd = s.get_vertex(expr.arg2.v2)
                ve = s.get_vertex(expr.arg3.v1)
                vf = s.get_vertex(expr.arg3.v2)
                vg = s.get_vertex(expr.arg4.v1)
                vh = s.get_vertex(expr.arg4.v2)

                if va.is_parallel(vb, vc, vd):
                    pa = va.projection(vc, vd)
                    v1 = va.mediator(pa, ve, vf, angle, sc)
                    v2 = va.mediator(pa, vg, vh, angle, sc)
                else:
                    in_v = va.intersection(vb, vc, vd, angle, sc)
                    va1 = vb if in_v == va else va
                    vc1 = vd if in_v == vc else vc
                    v0 = in_v.bisector(va1, vc1, angle, sc)
                    v1 = in_v.intersection(v0, ve, vf, angle, sc)
                    v2 = in_v.intersection(v0, vg, vh, angle, sc)

                v1.name = n1
                v2.name = n2
                s.vertices.append(v1)
                s.vertices.append(v2)

        elif isinstance(expr, cmd.RabbitEar):
            self._read_rabbit_ear_assign_pair(n1, n2, expr)

    # -- rabbit ear ---------------------------------------------------------

    def _read_rabbit_ear_assign(self, name: str, expr: cmd.RabbitEar) -> None:
        s = self._step
        angle, sc = self._angle_scale()

        v1 = s.get_vertex(expr.moving)
        v2 = s.get_vertex(expr.dest)
        v3 = s.get_vertex(expr.v3)

        # Determine edge
        if expr.edge is not None:
            e1 = s.get_vertex(expr.edge.v1)
            e2 = s.get_vertex(expr.edge.v2)
        else:
            e1 = v1.copy()
            e2 = v2.copy()

        if isinstance(expr.center_or_edge, str):
            center = s.get_vertex(expr.center_or_edge)
            # Goofy rabbit ear with given center
            a1 = v1.symmetry(v2, center, angle, sc)
            b1 = v2.intersection(center, v1, v3, angle, sc)
            a2 = a1.symmetry(v3, center, angle, sc)
            b2 = b1.symmetry(v3, center, angle, sc)
            a3 = a2.symmetry(b2, center, angle, sc)
            a4 = a1.mediator(a3, v2, v3, angle, sc)
            a5 = a4.symmetry(v2, center, angle, sc)
            v = a5.intersection(center, e1, e2, angle, sc)
            v.name = name
            s.vertices.append(v)
        elif isinstance(expr.center_or_edge, Edge):
            # Edge given instead of center
            e1 = s.get_vertex(expr.center_or_edge.v1)
            e2 = s.get_vertex(expr.center_or_edge.v2)
            # Compute center from bisectors
            p = v1.bisector(v2, v3, angle, sc)
            q = v2.bisector(v1, v3, angle, sc)
            center = v1.intersection(p, v2, q, angle, sc)
            temp = center.projection(v1, v2)
            v = center.intersection(temp, e1, e2, angle, sc)
            v.name = name
            s.vertices.append(v)

    def _read_rabbit_ear_assign_pair(self, n1: str, n2: str, expr: cmd.RabbitEar) -> None:
        s = self._step
        angle, sc = self._angle_scale()

        v1 = s.get_vertex(expr.moving)
        v2 = s.get_vertex(expr.dest)
        v3 = s.get_vertex(expr.v3)

        if expr.edge is not None:
            e1 = s.get_vertex(expr.edge.v1)
            e2 = s.get_vertex(expr.edge.v2)
        else:
            e1 = v1.copy()
            e2 = v2.copy()

        p = v1.bisector(v2, v3, angle, sc)
        q = v2.bisector(v1, v3, angle, sc)
        center = v1.intersection(p, v2, q, angle, sc)

        temp = center.projection(v1, v2)
        v = center.intersection(temp, e1, e2, angle, sc)

        center.name = n1
        v.name = n2
        s.vertices.append(center)
        s.vertices.append(v)

    # -- folds/edges --------------------------------------------------------

    def _read_fold(self, v1_name: str, v2_name: str, etype: EdgeType, lim1, lim2) -> None:
        s = self._step

        # Determine limit types
        sp1: int = 0
        sp2: int = 0
        lim1_edge: Edge | None = None
        lim2_edge: Edge | None = None

        if lim1 is None:
            sp1 = 0
        elif isinstance(lim1, int):
            sp1 = lim1
        elif isinstance(lim1, Edge):
            lim1_edge = lim1

        if lim2 is None:
            sp2 = 0
        elif isinstance(lim2, int):
            sp2 = lim2
        elif isinstance(lim2, Edge):
            lim2_edge = lim2

        if lim1_edge is None and lim2_edge is None:
            # Both percent
            self._read_fold_percent(v1_name, v2_name, etype, sp1, sp2)
        elif lim1_edge is not None and lim2_edge is not None:
            # Both limits
            self._read_fold_limit(v1_name, v2_name, etype, lim1_edge, lim2_edge)
        elif lim1_edge is not None:
            # lim1 is edge, lim2 is percent
            self._read_fold_both(v1_name, v2_name, etype, sp2, lim1_edge, is_limit_v1=True)
        else:
            # lim1 is percent, lim2 is edge
            self._read_fold_both(v1_name, v2_name, etype, sp1, lim2_edge, is_limit_v1=False)

    def _read_fold_percent(self, s1: str, s2: str, t: EdgeType, sp1: int, sp2: int) -> None:
        s = self._step
        idx = self._search_edge_and_hide_equivalent(s1, s2)
        if idx != -1:
            e = s.lines[idx]
            e.type = t
            if e.v1 == s1:
                e.set_space_v1(sp1)
            else:
                e.set_space_v2(sp1)
            if e.v2 == s2:
                e.set_space_v2(sp2)
            else:
                e.set_space_v1(sp2)
            e.visible = True
        else:
            s.lines.append(InternalEdge(s1, s2, t, True, 0, sp1, sp2))

    def _read_fold_limit(self, s1: str, s2: str, t: EdgeType, lim1: Edge, lim2: Edge) -> None:
        s = self._step
        l1_idx = self._search_edge(lim1.v1, lim1.v2)
        l2_idx = self._search_edge(lim2.v1, lim2.v2)
        idx = self._search_edge_and_hide_equivalent(s1, s2)
        if idx != -1:
            e = s.lines[idx]
            e.type = t
            if s1 == e.v1:
                e.set_limit_v1(l1_idx)
                if l2_idx != -1:
                    e.set_limit_v2(l2_idx)
            else:
                e.set_limit_v2(l1_idx)
                if l2_idx != -1:
                    e.set_limit_v1(l2_idx)
            e.visible = True
        else:
            if l2_idx != -1:
                s.lines.append(InternalEdge(s1, s2, t, True, 3, l1_idx, l2_idx))
            else:
                s.lines.append(InternalEdge(s1, s2, t, True, 2, l1_idx))

    def _read_fold_both(self, s1: str, s2: str, t: EdgeType, sp: int, lim_edge: Edge, *, is_limit_v1: bool) -> None:
        s = self._step
        lim_idx = self._search_edge(lim_edge.v1, lim_edge.v2)
        idx = self._search_edge_and_hide_equivalent(s1, s2)
        if idx != -1:
            e = s.lines[idx]
            if (s1 == e.v1 and is_limit_v1) or (s1 != e.v1 and not is_limit_v1):
                e.set_limit_v1(lim_idx)
                e.set_space_v2(sp)
            else:
                e.set_space_v1(sp)
                e.set_limit_v2(lim_idx)
            e.type = t
            e.visible = True
        else:
            if is_limit_v1:
                s.lines.append(InternalEdge(s1, s2, t, True, 2, lim_idx, sp))
            else:
                s.lines.append(InternalEdge(s1, s2, t, True, 1, sp, lim_idx))

    # -- cut ----------------------------------------------------------------

    def _cut_edge(self, v: Vertex, v1: Vertex, v2: Vertex, sname: str, s1: str, s2: str) -> None:
        s = self._step
        norm_total = Vec2.between(v1, v2).norm()
        norm1 = Vec2.between(v1, v).norm()
        norm2 = Vec2.between(v, v2).norm()

        for i, e in enumerate(s.lines):
            if e.equal(s1, s2):
                if e.v1 == s1:
                    sv2 = s2
                else:
                    sv2 = s1
                    norm1, norm2 = norm2, norm1

                sp = e.get_space_v2()
                e.v2 = sname
                e.set_space_v2(0)
                if norm1 > 0:
                    e.set_space_v1(int(e.get_space_v1() * norm_total / norm1))
                t = e.type
                # Add second edge part
                sp2 = int(sp * norm_total / norm2) if norm2 > 0 else 0
                s.lines.append(InternalEdge(sname, sv2, t, True, 0, 0, sp2))
                break

    def _read_cut(self, item: cmd.Cut) -> None:
        s = self._step
        v1 = s.get_vertex(item.edge.v1)
        v2 = s.get_vertex(item.edge.v2)
        v = s.get_vertex(item.vertex)
        self._cut_edge(v, v1, v2, item.vertex, item.edge.v1, item.edge.v2)

    # -- hide/show ----------------------------------------------------------

    def _read_hide_show(self, targets: Edge | list[str], *, visible: bool) -> None:
        s = self._step
        if isinstance(targets, Edge):
            for e in s.lines:
                if e.equal(targets.v1, targets.v2):
                    e.visible = visible
        else:
            for vname in targets:
                for e in s.lines:
                    if e.v1 == vname or e.v2 == vname:
                        e.visible = visible

    # -- space fold ---------------------------------------------------------

    def _read_space_fold(self, item: cmd.SpaceFold) -> None:
        s = self._step
        for e in s.lines:
            if e.equal(item.edge.v1, item.edge.v2):
                if e.v1 == item.edge.v1:
                    e.set_space_v1(item.pct1)
                    e.set_space_v2(item.pct2)
                else:
                    e.set_space_v1(item.pct2)
                    e.set_space_v2(item.pct1)
                break

    # -- fill ---------------------------------------------------------------

    def _read_fill(self, item: cmd.Fill) -> None:
        s = self._step
        color = _resolve_color(str(item.side), self.header)
        f = Face(list(item.vertices), color)
        s.faces.append(f)

    def _read_unfill(self, item: cmd.Unfill) -> None:
        s = self._step
        if not item.vertices:
            s.faces.clear()
        else:
            target_set = set(item.vertices)
            for i, f in enumerate(s.faces):
                if target_set.issubset(set(f.symbols)):
                    s.faces.pop(i)
                    break

    def _read_darker_lighter(self, item: cmd.Darker | cmd.Lighter, *, darken: bool) -> None:
        """Adjust front/back color by amount."""
        factor = 1.0 - item.amount / 100.0 if darken else 1.0 + item.amount / 100.0
        if item.side == Side.FRONT:
            c = self.header.front_color
        else:
            c = self.header.back_color
        c.r = max(0, min(100, int(c.r * factor)))
        c.g = max(0, min(100, int(c.g * factor)))
        c.b = max(0, min(100, int(c.b * factor)))

    # -- move ---------------------------------------------------------------

    def _read_move(self, item: cmd.Move) -> None:
        s = self._step
        vsrc = s.get_vertex(item.src)
        if isinstance(item.dest, Edge):
            v1 = s.get_vertex(item.dest.v1)
            v2 = s.get_vertex(item.dest.v2)
            angle, sc = self._angle_scale()
            sym = vsrc.symmetry(v1, v2, angle, sc)
            vsrc.x = sym.x
            vsrc.y = sym.y
            vsrc.dx = 0.0
            vsrc.dy = 0.0
        else:
            vdst = s.get_vertex(item.dest)
            vsrc.x = vdst.x
            vsrc.y = vdst.y
            vsrc.dx = 0.0
            vsrc.dy = 0.0

    # -- arrows -------------------------------------------------------------

    def _read_simple_arrow(self, item: cmd.SimpleArrow) -> None:
        s = self._step
        angle, sc = self._angle_scale()
        arc = item.arc if item.arc is not None else SIMPLE_ARROW_ANGLE

        if isinstance(item.dst, Edge):
            # Arrow across an edge: compute destination as symmetry
            v = s.get_vertex(item.src)
            va = s.get_vertex(item.dst.v1)
            vb = s.get_vertex(item.dst.v2)
            r = v.symmetry(va, vb, angle, sc)
            r.name = _gen_sym(s, v.get_name())
            s.vertices.append(r)
            s.arrows.append(Arrow(item.src, r.get_name(), item.src_arrow, item.dst_arrow, item.side, True, arc))
        else:
            s.arrows.append(Arrow(item.src, item.dst, item.src_arrow, item.dst_arrow, item.side, True, arc))

    def _read_return_arrow(self, item: cmd.ReturnArrow) -> None:
        s = self._step
        angle, sc = self._angle_scale()
        v1 = s.get_vertex(item.edge1.v1)
        v2 = s.get_vertex(item.edge1.v2)
        v3 = s.get_vertex(item.edge2.v1)
        v4 = s.get_vertex(item.edge2.v2)

        mid12 = v1.middle(v2)
        end = v1.mediator(v2, v3, v4, angle, sc)
        begin = mid12.middle(end)

        ratio = item.ratio if item.ratio is not None else RETURN_ARROW_RATIO

        begin.name = _gen_sym(s, "bra")
        end.name = _gen_sym(s, "era")
        s.vertices.append(begin)
        s.vertices.append(end)
        s.arrows.append(Arrow(begin.get_name(), end.get_name(), item.src_arrow, item.dst_arrow, item.side, False, ratio))

    def _read_open_arrow(self, item: cmd.OpenArrow) -> None:
        s = self._step
        right = item.side == ArrowSide.RIGHT
        s.arrow_symbols.append(OpenArrowSymbol(item.edge.v1, item.edge.v2, right))

    def _read_push_arrow(self, item: cmd.PushArrow) -> None:
        s = self._step
        angle, sc = self._angle_scale()
        if item.angle is not None:
            a = item.angle
            d = item.distance if item.distance is not None else 0
        else:
            v = s.get_vertex(item.vertex)
            o = Vertex("null", 0.0, 0.0)
            a = o.get_angle_from_horizontal(v, self._prev_rotate(), sc)
            a += self._prev_rotate()
            d = 0
        s.arrow_symbols.append(PushArrowSymbol(item.vertex, int(a), d))

    def _read_repeat_arrow(self, item: cmd.RepeatArrow) -> None:
        s = self._step
        angle, sc = self._angle_scale()
        nb = item.number if item.number is not None else 0

        lab1 = ""
        lab2 = ""
        if item.label1 and item.label2:
            if item.label1 in self._labels:
                lab1 = str(self._labels[item.label1])
            if item.label2 in self._labels:
                lab2 = str(self._labels[item.label2])

        if item.angle is not None:
            a = item.angle
            d = item.distance if item.distance is not None else 0
        else:
            v = s.get_vertex(item.vertex)
            o = Vertex("null", 0.0, 0.0)
            a = o.get_angle_from_horizontal(v, self._prev_rotate(), sc)
            a += self._prev_rotate()
            d = 0

        s.arrow_symbols.append(RepeatArrowSymbol(item.vertex, int(a), d, nb, lab1, lab2))


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def evaluate(diagram: cmd.Diagram) -> tuple[ComputedHeader, list[ComputedStep]]:
    """Process a Diagram tree and return ``(header, steps)``."""
    return Engine().evaluate(diagram)
