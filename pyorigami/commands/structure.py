from __future__ import annotations

from dataclasses import dataclass, field


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
