"""Pure-Python PostScript output writer for Doodle origami diagrams.

Generates PostScript output matching the C++ ``ps_output.cpp`` and
``ps_prologue.cpp``, operating entirely on the computed geometry
produced by :func:`pyorigami.engine.evaluate`.

Derived from ``doodle/src/ps_output.cpp`` and ``doodle/src/ps_prologue.cpp``
in the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

import math
import random
from io import StringIO
from pathlib import Path
from string import Template

from .types import ArrowHead, ArrowSide
from .geometry import (
    ComputedHeader,
    ComputedStep,
    EdgeType,
    Arrow,
    InternalEdge,
    Face,
    OpenArrowSymbol,
    PushArrowSymbol,
    RepeatArrowSymbol,
    TurnType,
    Vec2,
    Vertex,
)

# ---------------------------------------------------------------------------
# PS rendering constants (from C++ global_def.h)
# ---------------------------------------------------------------------------

PS_BORDER_WIDTH = 1
PS_FOLD_WIDTH = 0
PS_VALLEY_WIDTH = PS_BORDER_WIDTH
PS_MOUNTAIN_WIDTH = PS_BORDER_WIDTH
PS_XRAY_WIDTH = PS_BORDER_WIDTH

PAGE_HEIGHT = 297
PAGE_WIDTH = 210
FIRST_TOP_MARGIN = 60
CAPTION_HEIGHT_MM = 5

ARROWSPC = 5
ARROWLG = 10
ARROWHEADANGLE = 40


def to_ps(x: float) -> float:
    """Convert internal units to PS cm.  50 units = 1 cm."""
    return x / 50.0


# Width of the random angle range for debug symbol placement.
_DEBUG_ARC = 120

_PROLOGUE_PATH = Path(__file__).parent / "prologue.ps"


# ---------------------------------------------------------------------------
# PS prologue
# ---------------------------------------------------------------------------


def _write_prologue(out: StringIO) -> None:
    raw = _PROLOGUE_PATH.read_text(encoding="utf-8")
    out.write(Template(raw).substitute(PAGE_WIDTH=PAGE_WIDTH, PAGE_HEIGHT=PAGE_HEIGHT))


# ---------------------------------------------------------------------------
# PS string helper
# ---------------------------------------------------------------------------


def _ps_string(s: str) -> str:
    """Escape and wrap *s* as a PostScript string literal."""
    escaped = s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    return f"({escaped})"


# ---------------------------------------------------------------------------
# Vertex coordinate writer
# ---------------------------------------------------------------------------


def _write_vertex_coords(out: StringIO, v: Vertex, current_rotate: float, current_scale: float) -> None:
    if v.dx == 0 and v.dy == 0:
        out.write(f"{to_ps(v.x)} cm {to_ps(v.y)} cm ")
    else:
        out.write(f"{to_ps(v.x)} {to_ps(v.y)} " f"{v.dx} {v.dy} " f"{current_rotate} {current_scale} add_shift ")


def _compute_vertex_percent(v1: Vertex, v2: Vertex, sp: int) -> Vertex:
    vec = Vec2.between(v1, v2)
    norm = vec.norm()
    if norm < 1e-12:
        return v1.copy()
    u = vec / norm
    frac = sp / 100.0
    vshift = Vertex(
        "null",
        v1.x + frac * norm * u.x,
        v1.y + frac * norm * u.y,
    )
    vshift.dx = v1.dx * (1 - frac) + v2.dx * frac
    vshift.dy = v1.dy * (1 - frac) + v2.dy * frac
    return vshift


# ---------------------------------------------------------------------------
# Line style
# ---------------------------------------------------------------------------


def _write_line_style(out: StringIO, e: InternalEdge, current_scale: float) -> None:
    if e.type == EdgeType.BORDER:
        out.write(f"{PS_BORDER_WIDTH / current_scale} setlinewidth % set border width\n")
        out.write("[] 0 setdash   % set solid line for border\n")
    elif e.type == EdgeType.VALLEY:
        out.write(f"{PS_VALLEY_WIDTH / current_scale} setlinewidth % set valley width\n")
        out.write(f"[5 {current_scale} div] 0 setdash  % set dashed line for valley fold\n")
    elif e.type == EdgeType.MOUNTAIN:
        out.write(f"{PS_MOUNTAIN_WIDTH / current_scale} setlinewidth % set mountain width\n")
        out.write(
            f"[5 {current_scale} div 3 {current_scale} div 1 {current_scale}"
            f" div 3 {current_scale} div 1 {current_scale} div 3 "
            f"{current_scale} div] 0 setdash  % set dotted-dashed line for mountain fold\n"
        )
    elif e.type == EdgeType.FOLD:
        out.write(f"{PS_FOLD_WIDTH / current_scale} setlinewidth % set fold width\n")
        out.write("[] 0 setdash  % set solid line for existing fold\n")
    elif e.type == EdgeType.XRAY:
        out.write(f"{PS_XRAY_WIDTH / current_scale} setlinewidth % set xray width\n")
        out.write(f"[1 {current_scale} div 2 {current_scale} div] 0 setdash" "  % set dotted line for xray fold\n")
    else:
        out.write(f"{PS_FOLD_WIDTH / current_scale} setlinewidth % set fold width\n")
        out.write("[] 0 setdash  % set solid line for existing fold\n")


# ---------------------------------------------------------------------------
# Debug vertex
# ---------------------------------------------------------------------------


def _write_debug_vertex(out: StringIO, v: Vertex, current_scale: float, current_rotate: float) -> None:
    if v.debug:
        out.write("gsave 0 0 1 setrgbcolor % blue\n")
        _write_vertex_coords(out, v, current_rotate, current_scale)
        out.write(f"\n{current_scale} {current_rotate} ")
        out.write(_ps_string(v.get_name()))
        out.write(f" {random.randint(-_DEBUG_ARC // 2, _DEBUG_ARC // 2)} draw_symbol grestore\n")
        v.debug = False


# ---------------------------------------------------------------------------
# Line drawing
# ---------------------------------------------------------------------------


def _write_line(out: StringIO, step: ComputedStep, e: InternalEdge, cr: float, cs: float) -> None:
    v1 = step.get_vertex(e.v1)
    v2 = step.get_vertex(e.v2)
    if v1 == v2:
        return

    # First point
    if e.has_limit_v1():
        _write_vertex_coords(out, v1, cr, cs)
        _write_vertex_coords(out, v2, cr, cs)
        lim_edge = step.lines[e.limit_v1]
        _write_vertex_coords(out, step.get_vertex(lim_edge.v1), cr, cs)
        _write_vertex_coords(out, step.get_vertex(lim_edge.v2), cr, cs)
        out.write("intersection ")
    else:
        _write_vertex_coords(out, _compute_vertex_percent(v1, v2, e.get_space_v1()), cr, cs)
    out.write("moveto \n")

    # Second point
    if e.has_limit_v2():
        _write_vertex_coords(out, v1, cr, cs)
        _write_vertex_coords(out, v2, cr, cs)
        lim_edge = step.lines[e.limit_v2]
        _write_vertex_coords(out, step.get_vertex(lim_edge.v1), cr, cs)
        _write_vertex_coords(out, step.get_vertex(lim_edge.v2), cr, cs)
        out.write("intersection ")
    else:
        _write_vertex_coords(out, _compute_vertex_percent(v2, v1, e.get_space_v2()), cr, cs)
    out.write("lineto stroke \n")

    _write_debug_vertex(out, v1, cs, cr)
    _write_debug_vertex(out, v2, cs, cr)


def _write_edge(out: StringIO, step: ComputedStep, e: InternalEdge, cr: float, cs: float) -> None:
    if not e.visible:
        return
    if e.debug:
        out.write("\ngsave 1 0 0 setrgbcolor % red\n")
        v1 = step.get_vertex(e.v1)
        v2 = step.get_vertex(e.v2)
        if e.has_limit_v1():
            _write_vertex_coords(out, v1, cr, cs)
            _write_vertex_coords(out, v2, cr, cs)
            lim_edge = step.lines[e.limit_v1]
            _write_vertex_coords(out, step.get_vertex(lim_edge.v1), cr, cs)
            _write_vertex_coords(out, step.get_vertex(lim_edge.v2), cr, cs)
            out.write("intersection ")
        else:
            _write_vertex_coords(out, _compute_vertex_percent(v1, v2, e.get_space_v1()), cr, cs)
        if e.has_limit_v2():
            _write_vertex_coords(out, v1, cr, cs)
            _write_vertex_coords(out, v2, cr, cs)
            lim_edge = step.lines[e.limit_v2]
            _write_vertex_coords(out, step.get_vertex(lim_edge.v1), cr, cs)
            _write_vertex_coords(out, step.get_vertex(lim_edge.v2), cr, cs)
            out.write("intersection ")
        else:
            _write_vertex_coords(out, _compute_vertex_percent(v2, v1, e.get_space_v2()), cr, cs)
        out.write(
            f"{cs} {cr} ([{e.v1}, {e.v2}]) "
            f"{random.randint(-_DEBUG_ARC // 2, _DEBUG_ARC // 2)}"
            " draw_symbol_at_middle grestore\n"
        )
    _write_line_style(out, e, cs)
    _write_line(out, step, e, cr, cs)


# ---------------------------------------------------------------------------
# Face
# ---------------------------------------------------------------------------


def _write_face(out: StringIO, step: ComputedStep, f: Face, cr: float, cs: float) -> None:
    if not f.symbols:
        return
    out.write("gsave % begin fill face\n")
    out.write(f"{f.color.r / 100.0} {f.color.g / 100.0} {f.color.b / 100.0} setrgbcolor\n")
    _write_vertex_coords(out, step.get_vertex(f.symbols[0]), cr, cs)
    out.write("moveto")
    for sym in f.symbols[1:]:
        out.write("\n")
        _write_vertex_coords(out, step.get_vertex(sym), cr, cs)
        out.write("lineto")
    out.write(" fill\n")
    out.write("grestore % end fill face\n")


# ---------------------------------------------------------------------------
# Arrow head helpers
# ---------------------------------------------------------------------------


def _write_head_simple_arrow(
    out: StringIO,
    atype: ArrowHead,
    angle: float,
    reverse: bool,
    cx: float,
    cy: float,
    r: float,
    headsize: float,
) -> tuple[float]:
    """Write arrow head and return (possibly modified) angle."""
    out.write("gsave\n")
    px = cx + r * math.cos(angle * math.pi / 180)
    py = cy + r * math.sin(angle * math.pi / 180)
    angle2 = angle + 180 if reverse else angle
    out.write(f"{to_ps(px)} cm {to_ps(py)} cm translate\n")

    ha = ARROWHEADANGLE * math.pi / 360
    hrx = headsize * math.sin(ha)
    hry = headsize * math.cos(ha)
    hlx = -headsize * math.sin(ha)
    hly = headsize * math.cos(ha)
    out.write(f"{angle2} rotate\n")

    if atype == ArrowHead.VALLEY:
        out.write(f"{to_ps(hrx)} cm {to_ps(hry)} cm moveto\n")
        out.write(f"0 0 lineto {to_ps(hlx)} cm {to_ps(hly)} cm lineto stroke\n")
    elif atype == ArrowHead.UNFOLD:
        out.write("1 1 1 setrgbcolor\n")
        out.write(f"0 0 moveto {to_ps(hrx)} cm {to_ps(hry)} cm lineto\n")
        out.write(f"{to_ps(hlx)} cm {to_ps(hly)} cm lineto closepath fill\n")
        out.write("0 0 0 setrgbcolor\n")
        out.write(f"0 0 moveto {to_ps(hrx)} cm {to_ps(hry)} cm lineto\n")
        out.write(f"{to_ps(hlx)} cm {to_ps(hly)} cm lineto closepath stroke\n")
        dangle = headsize * 180.0 / (r * math.pi)
        if reverse:
            angle -= dangle
        else:
            angle += dangle
    elif atype == ArrowHead.NONE:
        pass
    elif atype == ArrowHead.MOUNTAIN:
        if not reverse:
            out.write(f"0 0 moveto {to_ps(hrx)} cm {to_ps(hry)} cm lineto\n")
            out.write(f"{to_ps((hlx + hrx) / 2)} cm {to_ps((hly + hry) / 2)} cm lineto stroke\n")
        else:
            out.write(f"0 0 moveto {to_ps(hlx)} cm {to_ps(hly)} cm lineto stroke\n")
            out.write(f"{to_ps((hlx + hrx) / 2)} cm {to_ps((hly + hry) / 2)} cm lineto stroke\n")

    out.write("grestore\n")
    return (angle,)


def _write_head_return_arrow(
    out: StringIO,
    vx: float,
    vy: float,
    ux: float,
    uy: float,
    head_size: float,
    atype: ArrowHead,
    right_side: bool,
) -> None:
    out.write("gsave\n")
    out.write(f"{to_ps(vx)} cm {to_ps(vy)} cm translate\n")
    out.write(f"{math.atan2(-ux, uy) * 180 / math.pi} rotate\n")
    head_length = head_size / 4
    ha = ARROWHEADANGLE * math.pi / 360
    prx = head_length * math.sin(ha)
    pry = head_length * math.cos(ha)
    plx = -head_length * math.sin(ha)
    ply = head_length * math.cos(ha)
    pt = (prx, pry) if right_side else (plx, ply)

    if atype == ArrowHead.VALLEY:
        out.write(f"{to_ps(prx)} cm {to_ps(pry)} cm moveto\n")
        out.write(f"0 0 lineto {to_ps(plx)} cm {to_ps(ply)} cm lineto stroke\n")
    elif atype == ArrowHead.UNFOLD:
        out.write("1 1 1 setrgbcolor\n")
        out.write(f"0 0 moveto {to_ps(prx)} cm {to_ps(pry)} cm lineto\n")
        out.write(f"{to_ps(plx)} cm {to_ps(ply)} cm lineto closepath fill\n")
        out.write("0 0 0 setrgbcolor\n")
        out.write(f"0 0 moveto {to_ps(prx)} cm {to_ps(pry)} cm lineto\n")
        out.write(f"{to_ps(plx)} cm {to_ps(ply)} cm lineto closepath stroke\n")
    elif atype == ArrowHead.MOUNTAIN:
        out.write(f"0 0 moveto {to_ps(pt[0])} cm {to_ps(pt[1])} cm lineto\n")
        out.write(f"{to_ps((prx + plx) / 2)} cm {to_ps((pry + ply) / 2)} cm lineto stroke\n")
    # arrowNone: nothing

    out.write("grestore\n")


# ---------------------------------------------------------------------------
# Simple arrow
# ---------------------------------------------------------------------------


def _write_simple_arrow(out: StringIO, step: ComputedStep, a: Arrow, cr: float, cs: float) -> None:
    v1_raw = step.get_vertex(a.v1)
    v2_raw = step.get_vertex(a.v2)
    v1 = v1_raw.apply_shift(cr, cs * 100.0)
    v2 = v2_raw.apply_shift(cr, cs * 100.0)

    out.write(f"{PS_BORDER_WIDTH / cs} setlinewidth % set arrow width\n")
    out.write("[] 0 setdash   % set solid line for arrow\n")

    px = (v1.x + v2.x) / 2
    py = (v1.y + v2.y) / 2
    u = Vec2.between(v1, v2)
    alpha_r = a.shape * math.pi / 180
    d = u.norm()
    if d < 1e-12:
        return
    u = u / d
    r = d / (2 * math.sin(alpha_r / 2))

    v = u.ortho()
    if a.side == ArrowSide.RIGHT:
        cx = px + r * math.cos(alpha_r / 2) * v.x
        cy = py + r * math.cos(alpha_r / 2) * v.y
    else:
        cx = px - r * math.cos(alpha_r / 2) * v.x
        cy = py - r * math.cos(alpha_r / 2) * v.y

    w = Vec2(v1.x - cx, v1.y - cy)
    a1 = math.atan2(w.y, w.x) * 180 / math.pi
    if a.side == ArrowSide.RIGHT:
        a2 = a1 + a.shape
    else:
        a2 = a1
        a1 = a2 - a.shape

    # Adjustments
    a1 += a.shape * (ARROWSPC / 100.0)
    a2 -= a.shape * (ARROWSPC / 100.0)

    # Arrow heads
    headsize = (ARROWLG) * (a2 - a1) * math.pi * r / (180 * 100)

    if (a.v1_type != ArrowHead.NONE and a.side == ArrowSide.RIGHT) or (
        a.v2_type != ArrowHead.NONE and a.side == ArrowSide.LEFT
    ):
        t = a.v1_type if a.side == ArrowSide.RIGHT else a.v2_type
        (a1,) = _write_head_simple_arrow(out, t, a1, False, cx, cy, r, headsize)

    if (a.v2_type != ArrowHead.NONE and a.side == ArrowSide.RIGHT) or (
        a.v1_type != ArrowHead.NONE and a.side == ArrowSide.LEFT
    ):
        t = a.v2_type if a.side == ArrowSide.RIGHT else a.v1_type
        (a2,) = _write_head_simple_arrow(out, t, a2, True, cx, cy, r, headsize)

    # Arrow body
    out.write(f"{to_ps(cx)} cm {to_ps(cy)} cm {to_ps(r)} cm {a1} {a2} arc stroke\n")


# ---------------------------------------------------------------------------
# Return arrow
# ---------------------------------------------------------------------------


def _write_return_arrow(out: StringIO, step: ComputedStep, a: Arrow, cr: float, cs: float) -> None:
    begin = step.get_vertex(a.v1).apply_shift(cr, cs * 100.0)
    end = step.get_vertex(a.v2).apply_shift(cr, cs * 100.0)
    be = Vec2.between(begin, end)
    u = be / 10
    v = u.ortho()
    if a.side == ArrowSide.RIGHT:
        v = Vec2(-v.x, -v.y)

    u_prop1 = Vec2(50.0 / (100.0 - a.shape) * u.x, 50.0 / (100.0 - a.shape) * u.y)
    u_prop2 = Vec2(a.shape / (100.0 - a.shape) * u.x, a.shape / (100.0 - a.shape) * u.y)
    v_prop2 = Vec2(a.shape / (100.0 - a.shape) * v.x, a.shape / (100.0 - a.shape) * v.y)

    def _add(base: Vertex, *vecs: tuple[float, Vec2]) -> Vertex:
        x, y = base.x, base.y
        for scale, vec in vecs:
            x += scale * vec.x
            y += scale * vec.y
        return Vertex("null", x, y)

    c1 = _add(begin, (8, u_prop1), (5, v))
    c2 = _add(begin, (20, u_prop1), (3, v))
    c3 = _add(begin, (20, u_prop1), (1, v))
    c4 = _add(begin, (20, u_prop1), (-1, v))
    c5 = _add(begin, (10, u), (5, u_prop2), (-2, v_prop2))
    c6 = _add(begin, (10, u), (1, u_prop2), (-1, v_prop2))

    out.write(f"{PS_BORDER_WIDTH / cs} setlinewidth % set arrow width\n")
    out.write("[] 0 setdash   % set solid line for arrow\n")

    # Arrow body
    out.write(f"{to_ps(begin.x)} cm {to_ps(begin.y)} cm moveto\n")
    out.write(f"{to_ps(c1.x)} cm {to_ps(c1.y)} cm\n")
    out.write(f"{to_ps(c2.x)} cm {to_ps(c2.y)} cm\n")
    out.write(f"{to_ps(c3.x)} cm {to_ps(c3.y)} cm curveto \n")
    out.write(f"{to_ps(c4.x)} cm {to_ps(c4.y)} cm\n")
    out.write(f"{to_ps(c5.x)} cm {to_ps(c5.y)} cm\n")
    out.write(f"{to_ps(c6.x)} cm {to_ps(c6.y)} cm curveto stroke % return arrow\n")

    # Arrow heads
    right_side = a.side == ArrowSide.RIGHT
    be_norm = be.norm()
    bc1 = Vec2.between(begin, c1)
    _write_head_return_arrow(out, begin.x, begin.y, bc1.x, bc1.y, be_norm, a.v1_type, right_side)
    c6c5 = Vec2.between(c6, c5)
    _write_head_return_arrow(out, c6.x, c6.y, c6c5.x, c6c5.y, be_norm, a.v2_type, not right_side)


# ---------------------------------------------------------------------------
# Arrow symbols (open, push, repeat)
# ---------------------------------------------------------------------------


def _write_arrow_symbol(out: StringIO, step: ComputedStep, sym, cr: float, cs: float) -> None:
    if isinstance(sym, OpenArrowSymbol):
        v1 = step.get_vertex(sym.v1)
        v2 = step.get_vertex(sym.v2)
        mid = v1.middle(v2)
        angle = v1.get_angle_from_horizontal(v2, cr, cs * 100.0)
        if sym.right:
            angle -= 90
        else:
            angle += 90
        _write_vertex_coords(out, mid, cr, cs)
        out.write(f"{angle} {cs} open_arrow\n")

    elif isinstance(sym, PushArrowSymbol):
        v = step.get_vertex(sym.point)
        _write_vertex_coords(out, v, cr, cs)
        out.write(f"{sym.angle} {sym.distance} {cr} {cs} push_arrow\n")

    elif isinstance(sym, RepeatArrowSymbol):
        v = step.get_vertex(sym.point)
        _write_vertex_coords(out, v, cr, cs)
        label = ""
        if sym.first_label and sym.second_label:
            label = f"{sym.first_label} - {sym.second_label}"
        out.write(f"{sym.number} ({label}) {sym.angle} {sym.distance} {cr} {cs} repeat_arrow\n")


# ---------------------------------------------------------------------------
# Turn / rotate symbols
# ---------------------------------------------------------------------------


def _write_turn(out: StringIO, urx: float, ury: float) -> None:
    out.write(f"{urx} mm {ury} mm turn_over\n")


def _write_rotate_symbol(out: StringIO, urx: float, ury: float, a: float, cr_ref: list[float]) -> None:
    out.write("% begin rotate\n")
    out.write(f"{urx} mm {ury} mm ({abs(a)}) ")
    if a > 0:
        out.write("true rotate_step\n")
    else:
        out.write("false rotate_step\n")
    cr_ref[0] += a


# ---------------------------------------------------------------------------
# Caption
# ---------------------------------------------------------------------------


def _write_caption(out: StringIO, step: ComputedStep, urx: float, ury: float) -> None:
    # Declare font
    out.write(
        "/Times-Roman findfont % Get basic font\n"
        "11 scalefont          % 11 points font\n"
        "setfont               % Make it the current font\n\n"
    )
    out.write("/hline {0 (Mj) width_height exch pop} def\n")
    out.write(f"{urx * 2} mm -0.4 mul " f"{-ury} mm interline hline add sub moveto\n" f"({step.index}-) show\n")
    for i, caption in enumerate(step.captions, 1):
        out.write(f"{urx * 2} mm -0.3 mul " f"{-ury} mm interline hline add " f"{i} mul sub moveto\n")
        out.write(f"{_ps_string(caption)} show\n")


# ---------------------------------------------------------------------------
# Full step writer
# ---------------------------------------------------------------------------


def _write_step(
    out: StringIO,
    step: ComputedStep,
    cr_ref: list[float],
    cs_ref: list[float],
    urx: float,
    ury: float,
    *,
    with_caption: bool = True,
) -> None:
    out.write("gsave % begin figure\n")

    cr = cr_ref[0]
    if cr:
        out.write(f"{cr} rotate\n")

    # Font for debug
    out.write(
        "/Times-Roman findfont % Get basic font\n"
        "12 scalefont          % 12 points font\n"
        "setfont               % Make it the current font\n\n"
    )

    # Scaling
    cs_ref[0] = step.scale / 100.0
    cs = cs_ref[0]
    if cs != 1.0:
        out.write(f"{cs} {cs} scale % scaling the step\n")

    # Re-centering
    out.write(
        f"{to_ps(-step.visible_center_x)} cm " f"{to_ps(-step.visible_center_y)} cm translate % recentering the step\n"
    )

    # Draw faces
    for f in step.faces:
        _write_face(out, step, f, cr, cs)

    # Draw edges
    for e in step.lines:
        _write_edge(out, step, e, cr, cs)

    # Draw arrows
    for a in step.arrows:
        if a.simple:
            _write_simple_arrow(out, step, a, cr, cs)
        else:
            _write_return_arrow(out, step, a, cr, cs)

    # Write text of vertices
    for v in step.vertices:
        if v.has_text():
            _write_vertex_coords(out, v, cr, cs)
            out.write("\ngsave 0 0 0 setrgbcolor % black\n")
            out.write(f"{cs} {cr} ")
            out.write(_ps_string(v.get_text()))
            out.write(f" {random.randint(-_DEBUG_ARC // 2, _DEBUG_ARC // 2)} draw_symbol grestore\n")

    # Arrow symbols
    for sym in step.arrow_symbols:
        _write_arrow_symbol(out, step, sym, cr, cs)

    out.write("grestore % end figure\n")
    if step.clip:
        out.write("grestore % end clip\n")

    # Caption
    if with_caption:
        _write_caption(out, step, urx, ury)

    # Turn symbol
    if step.turn != TurnType.NONE:
        _write_turn(out, urx, ury)

    # Rotate symbol
    r = step.rotate
    if r:
        if step.turn != TurnType.NONE:
            ury -= 15
        _write_rotate_symbol(out, urx, ury, r, cr_ref)


# ---------------------------------------------------------------------------
# Page layout
# ---------------------------------------------------------------------------


def _write_first_page_header(out: StringIO, info: ComputedHeader) -> None:
    out.write(_ps_string(info.title))
    out.write("\n")
    ss = f"Design: {info.designer}"
    if info.design_date_year:
        ss += f" - Copyright {info.design_date_year}"
    out.write(_ps_string(ss))
    out.write("\n")
    ss = f"Diagrams: {info.diagrammer}"
    if info.diagram_date_year:
        ss += f" - Copyright {info.diagram_date_year}"
    out.write(_ps_string(ss))
    out.write("\n")
    out.write(_ps_string(info.comment1))
    out.write("\n")
    out.write(_ps_string(info.comment2))
    out.write("\n")
    out.write(_ps_string(info.comment3))
    out.write(f"\n{info.left_margin} mm {info.right_margin} mm make_first_page_header\n")


def _write_page_header(out: StringIO, info: ComputedHeader) -> None:
    out.write("gsave % begin page header\n")
    out.write("/Helvetica-Bold findfont 16 scalefont setfont\n")
    out.write(f"{info.left_margin} mm {PAGE_HEIGHT - info.top_margin} mm 3 mm add moveto ")
    out.write(_ps_string(info.title))
    out.write(" show\n")
    out.write("/Helvetica findfont 12 scalefont setfont\n")
    out.write(
        f"{PAGE_WIDTH - info.right_margin} mm 0 "
        f"({info.designer}) width_height pop sub "
        f"{PAGE_HEIGHT - info.top_margin} mm 3 mm add moveto "
    )
    out.write(_ps_string(info.designer))
    out.write(" show stroke\n")
    out.write("3 setlinewidth [] 0 setdash\n")
    out.write(
        f"{info.left_margin} mm {PAGE_HEIGHT - info.top_margin} mm moveto "
        f"{PAGE_WIDTH - info.right_margin} mm "
        f"{PAGE_HEIGHT - info.top_margin} mm lineto stroke\n"
    )
    out.write("grestore % end page header\n")


def _write_page_footer(out: StringIO, info: ComputedHeader, page_nb: int) -> None:
    out.write("gsave % begin page footer\n")
    out.write("3 setlinewidth [] 0 setdash\n")
    out.write(
        f"{info.left_margin} mm {info.bottom_margin} mm moveto "
        f"{PAGE_WIDTH - info.right_margin} mm "
        f"{info.bottom_margin} mm lineto stroke\n"
    )
    out.write("/Times-Roman findfont 12 scalefont setfont\n")
    out.write(
        f"{PAGE_WIDTH} mm 0 ({page_nb}) width_height\n"
        f"3 1 roll sub 2 div exch {info.bottom_margin} mm exch sub 3 mm sub moveto\n"
        f"({page_nb}) show\n"
    )
    out.write("grestore % end page footer\n")
    out.write("showpage\n")


# ---------------------------------------------------------------------------
# Main entry: write all steps across pages
# ---------------------------------------------------------------------------


def generate_ps(info: ComputedHeader, steps: list[ComputedStep]) -> str:
    """Generate a complete PostScript document from computed diagram data."""
    random.seed(42)  # Fixed seed for reproducible output

    out = StringIO()

    # PS header
    out.write(
        "%!PS-Adobe-3.0\n"
        "%%Creator: pyorigami — https://github.com/pyorigami\n"
        "%%Title: Origami Diagram\n"
        "%%DocumentPaperSizes: A4\n"
    )
    pages_marker = out.tell()
    out.write("%%Pages: 000\n%%EndComments\n\n")

    # Prologue
    _write_prologue(out)

    nb_steps = len(steps)
    step_id = 0
    top_margin_min = FIRST_TOP_MARGIN
    bottom_margin_min = info.bottom_margin
    left_margin_min = info.left_margin
    right_margin_min = info.right_margin
    v_space = info.v_space
    h_space = info.h_space
    page_id = 1

    current_rotate = [0.0]  # mutable ref
    current_scale = [1.0]

    if nb_steps == 0:
        _write_first_page_header(out, info)
        _write_page_footer(out, info, page_id)
        page_id += 1
    else:
        while step_id < nb_steps:
            sum_height = 0
            num_line = 0
            max_heights: list[int] = []
            nb_steps_by_line: list[int] = []
            sum_width: list[int] = []
            next_page = False
            step_id_2_write = step_id

            out.write(f"\n%%Page: {page_id} {page_id}\n")

            while not next_page:
                sw = 0
                next_line = False
                mh = 0
                nsbl = 0

                while not next_line:
                    avail = PAGE_WIDTH - left_margin_min - right_margin_min - max(0, nsbl - 1) * h_space
                    if sw + steps[step_id].clip_width < avail:
                        sw += steps[step_id].clip_width
                        cap_h = len(steps[step_id].captions) * CAPTION_HEIGHT_MM
                        mh = max(mh, steps[step_id].clip_height + cap_h)
                        step_id += 1
                        nsbl += 1
                        if step_id >= nb_steps:
                            next_line = True
                            next_page = True
                    else:
                        next_line = True

                if page_id > 1:
                    top_margin_min = info.top_margin

                if sum_height + mh + top_margin_min + bottom_margin_min + (num_line + 1) * v_space < PAGE_HEIGHT:
                    sum_height += mh
                    max_heights.append(mh)
                    nb_steps_by_line.append(nsbl)
                    sum_width.append(sw)
                    num_line += 1
                else:
                    step_id -= nsbl
                    next_page = True

            # Write the page
            if page_id > 1:
                _write_page_header(out, info)
            else:
                _write_first_page_header(out, info)

            current_height = 0
            for line in range(num_line):
                current_width = 0
                if step_id_2_write != nb_steps:
                    inter_v = (PAGE_HEIGHT - top_margin_min - bottom_margin_min - sum_height) // max(num_line, 1)
                else:
                    inter_v = v_space
                y = PAGE_HEIGHT - int(top_margin_min + max_heights[line] / 2 + current_height + (line + 0.5) * inter_v)
                current_height += max_heights[line]

                for col in range(nb_steps_by_line[line]):
                    if nb_steps_by_line[line] == 1:
                        x = PAGE_WIDTH // 2
                    else:
                        inter_h = (PAGE_WIDTH - left_margin_min - right_margin_min - sum_width[line]) // (
                            nb_steps_by_line[line] - 1
                        )
                        x = left_margin_min + current_width + col * inter_h + steps[step_id_2_write].clip_width // 2
                        current_width += steps[step_id_2_write].clip_width

                    out.write("gsave % begin step\n")
                    out.write(f"{x} mm {y} mm translate\n")

                    w = steps[step_id_2_write].clip_width
                    h = steps[step_id_2_write].clip_height
                    upper_right_x = w / 2
                    upper_right_y = h / 2

                    if steps[step_id_2_write].clip:
                        out.write("gsave % begin clip\n")
                        out.write("newpath % begin of clipping zone\n")
                        out.write(f"{-w // 2} mm {h // 2} mm moveto\n")
                        out.write(f"{w // 2} mm {h // 2} mm lineto\n")
                        out.write(f"{w // 2} mm {-h // 2} mm lineto\n")
                        out.write(f"{-w // 2} mm {-h // 2} mm lineto closepath clip")
                        out.write(" newpath % end of clipping zone\n")

                    _write_step(
                        out,
                        steps[step_id_2_write],
                        current_rotate,
                        current_scale,
                        upper_right_x,
                        upper_right_y,
                    )
                    out.write("grestore % end step\n")
                    step_id_2_write += 1

            _write_page_footer(out, info, page_id)
            page_id += 1

    # Patch page count
    content = out.getvalue()
    content = content.replace("%%Pages: 000", f"%%Pages: {page_id - 1:3d}", 1)

    return content
