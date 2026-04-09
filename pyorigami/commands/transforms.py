"""Vertex transform commands (move, shift, unshift).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..types import Edge


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
        dx = str(int(self.dx)) if isinstance(self.dx, float) and self.dx == int(self.dx) else str(self.dx)
        dy = str(int(self.dy)) if isinstance(self.dy, float) and self.dy == int(self.dy) else str(self.dy)
        return f"\\shift({self.vertex}, {dx}, {dy})"


@dataclass
class Unshift:
    """Resets all previously applied shifts on a vertex.

    Maps to ``\\unshift(vertex);``.
    """

    vertex: str

    def to_doo(self) -> str:
        return f"\\unshift({self.vertex})"
