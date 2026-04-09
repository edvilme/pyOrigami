"""Vertex transform commands (move, shift, unshift).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..parsing import DoodleParseableCommand
from ..types import Edge


@dataclass
class Move(DoodleParseableCommand):
    """Moves a vertex to a new position.

    Changes the internal coordinates of *src*.

    * **Syntax 1:** *dest* is a vertex name — *src* gets the coordinates
      of *dest*.
    * **Syntax 2:** *dest* is an ``Edge`` — *src* is reflected (mirrored)
      through that edge, simulating the result of folding along the edge.

    Maps to ``\\move(src, dest);`` or ``\\move(src, edge);``.
    """

    DOO_KEYWORD = "move"

    src: str
    dest: str | Edge

    def to_doo(self) -> str:
        d = self.dest.to_doo() if isinstance(self.dest, Edge) else self.dest
        return f"\\move({self.src}, {d})"

    @classmethod
    def from_doo_args(cls, args: list) -> Move:
        return cls(src=args[0], dest=args[1])


@dataclass
class Shift(DoodleParseableCommand):
    """Visually displaces a vertex for pseudo-3D diagrams.

    The shift does **not** alter the internal geometric coordinates; it
    only offsets the rendering position by *(dx, dy)* millimetres.
    However, future geometric operations on the shifted point will use
    the shifted coordinates to maintain visual consistency.
    Maps to ``\\shift(vertex, dx, dy);``.
    """

    DOO_KEYWORD = "shift"

    vertex: str
    dx: int | float
    dy: int | float

    def to_doo(self) -> str:
        dx = str(int(self.dx)) if isinstance(self.dx, float) and self.dx == int(self.dx) else str(self.dx)
        dy = str(int(self.dy)) if isinstance(self.dy, float) and self.dy == int(self.dy) else str(self.dy)
        return f"\\shift({self.vertex}, {dx}, {dy})"

    @classmethod
    def from_doo_args(cls, args: list) -> Shift:
        return cls(vertex=args[0], dx=args[1], dy=args[2])


@dataclass
class Unshift(DoodleParseableCommand):
    """Resets all previously applied shifts on a vertex.

    Maps to ``\\unshift(vertex);``.
    """

    DOO_KEYWORD = "unshift"

    vertex: str

    def to_doo(self) -> str:
        return f"\\unshift({self.vertex})"

    @classmethod
    def from_doo_args(cls, args: list) -> Unshift:
        return cls(vertex=args[0])
