from __future__ import annotations

import math
from dataclasses import dataclass, field

from .constants import (
    BOTTOM_MARGIN,
    CLIP_HEIGHT,
    CLIP_WIDTH,
    FOLDSPC,
    HSPACE,
    LEFT_MARGIN,
    RIGHT_MARGIN,
    TOP_MARGIN,
    VSPACE,
    is_null,
)
from .vertex import Vertex
from .edge import EdgeType, InternalEdge
from .arrow import InternalArrow, TurnType
from .face import InternalColor, InternalFace
from .symbols import ArrowSymbol


@dataclass
class ComputedHeader:
    title: str = ""
    designer: str = ""
    diagrammer: str = ""
    design_date_year: int = 0
    diagram_date_year: int = 0
    top_margin: int = TOP_MARGIN
    bottom_margin: int = BOTTOM_MARGIN
    left_margin: int = LEFT_MARGIN
    right_margin: int = RIGHT_MARGIN
    v_space: int = VSPACE
    h_space: int = HSPACE
    front_color: InternalColor = field(default_factory=lambda: InternalColor(100, 100, 100))
    back_color: InternalColor = field(default_factory=lambda: InternalColor(100, 100, 100))
    comment1: str = ""
    comment2: str = ""
    comment3: str = ""


@dataclass
class ComputedStep:
    index: str = ""
    captions: list[str] = field(default_factory=list)
    vertices: list[Vertex] = field(default_factory=list)
    lines: list[InternalEdge] = field(default_factory=list)
    arrows: list[InternalArrow] = field(default_factory=list)
    faces: list[InternalFace] = field(default_factory=list)
    arrow_symbols: list[ArrowSymbol] = field(default_factory=list)
    turn: TurnType = TurnType.NONE
    rotate: float = 0.0
    clip_width: int = CLIP_WIDTH
    clip_height: int = CLIP_HEIGHT
    visible_center_x: float = 0.0
    visible_center_y: float = 0.0
    scale: int = 100
    clip: bool = False

    def symbol_exists(self, name: str) -> bool:
        for v in self.vertices:
            if v.get_name() == name:
                return True
        return False

    def get_vertex(self, name: str) -> Vertex:
        for v in self.vertices:
            if v.get_name() == name:
                return v
        raise KeyError(f"Vertex {name!r} not found")

    def ref_vertex(self, name: str) -> Vertex:
        """Return vertex by name (mutable reference)."""
        return self.get_vertex(name)

    def search_edge(self, s1: str, s2: str) -> int:
        for i, e in enumerate(self.lines):
            if e.equal(s1, s2):
                return i
        return -1

    def fill_update(self, prev: ComputedStep) -> None:
        """Inherit state from previous step (faces, vertices, lines)."""
        for f in prev.faces:
            self.faces.append(f.copy())
        for v in prev.vertices:
            new_v = v.copy()
            new_v.debug = False
            new_v.clear_text()
            self.vertices.append(new_v)
        for i, e in enumerate(prev.lines):
            new_e = e.copy()
            if e.type == EdgeType.XRAY:
                new_e.visible = False
            elif e.type in (EdgeType.VALLEY, EdgeType.MOUNTAIN):
                new_e.type = EdgeType.FOLD
                new_e.set_space_v1(FOLDSPC)
                new_e.set_space_v2(FOLDSPC)
            new_e.debug = False
            self.lines.append(new_e)
        # Update dx/dy for rotation and scale changes
        if not is_null(prev.rotate) or prev.scale != self.scale:
            resize_factor = 1.0
            if prev.scale != self.scale:
                resize_factor = self.scale / prev.scale
            alpha = prev.rotate * math.pi / 180.0
            for v in self.vertices:
                dx, dy = v.dx, v.dy
                v.dx = resize_factor * (math.cos(alpha) * dx - math.sin(alpha) * dy)
                v.dy = resize_factor * (math.sin(alpha) * dx + math.cos(alpha) * dy)

    def turn_vertices(self, t: TurnType) -> None:
        if t == TurnType.VERTICAL:
            for v in self.vertices:
                v.x = -v.x
                v.dx = -v.dx
        elif t == TurnType.HORIZONTAL:
            for v in self.vertices:
                v.y = -v.y
                v.dy = -v.dy
