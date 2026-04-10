"""Display commands (hide, show, fill, caption, label, text, etc.).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from ..parsing import DoodleParseableCommand
from ..types import Edge, Side, string_quote


@dataclass
class Hide(DoodleParseableCommand):
    """Hides previously drawn graphical elements.

    * If *targets* is an ``Edge``, that specific edge is hidden.
    * If *targets* is a list of vertex names, **all edges containing any
      of those vertices** are hidden.

    Maps to ``\\hide(edge);`` or ``\\hide(v1, v2, ...);``.
    """

    DOO_KEYWORD = "hide"

    targets: Edge | list[str]

    def to_doo(self) -> str:
        if isinstance(self.targets, Edge):
            return f"\\hide({self.targets.to_doo()})"
        return f"\\hide({', '.join(self.targets)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Hide:
        if len(args) == 1 and isinstance(args[0], Edge):
            return cls(targets=args[0])
        return cls(targets=[a for a in args if isinstance(a, str)])


@dataclass
class Show(DoodleParseableCommand):
    """Re-shows previously hidden graphical elements (dual of ``Hide``).

    Accepts the same target forms as ``Hide``.
    Maps to ``\\show(edge);`` or ``\\show(v1, v2, ...);``.
    """

    DOO_KEYWORD = "show"

    targets: Edge | list[str]

    def to_doo(self) -> str:
        if isinstance(self.targets, Edge):
            return f"\\show({self.targets.to_doo()})"
        return f"\\show({', '.join(self.targets)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Show:
        if len(args) == 1 and isinstance(args[0], Edge):
            return cls(targets=args[0])
        return cls(targets=[a for a in args if isinstance(a, str)])


@dataclass
class SpaceFold(DoodleParseableCommand):
    """Overrides the blank percentage at each extremity of an existing edge.

    Useful to fine-tune the visual gap at fold endpoints after automatic
    style changes.
    Maps to ``\\space_fold(edge, pct1, pct2);``.
    """

    DOO_KEYWORD = "space_fold"

    edge: Edge
    pct1: int
    pct2: int

    def to_doo(self) -> str:
        return f"\\space_fold({self.edge.to_doo()}, {self.pct1}, {self.pct2})"

    @classmethod
    def from_doo_args(cls, args: list) -> SpaceFold:
        return cls(edge=args[0], pct1=int(args[1]), pct2=int(args[2]))


@dataclass
class Fill(DoodleParseableCommand):
    """Fills a polygonal area with the front or back paper colour.

    *vertices* must be given in circular order; the polygon is
    automatically closed between the first and last vertex.  Filled
    areas are drawn in chronological order (first defined, first drawn).
    Maps to ``\\fill(side, v1, v2, ...);``.
    """

    DOO_KEYWORD = "fill"

    side: Side
    vertices: list[str]

    def to_doo(self) -> str:
        args = [str(self.side)] + self.vertices
        return f"\\fill({', '.join(args)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Fill:
        return cls(side=Side(args[0]), vertices=list(args[1:]))


@dataclass
class Unfill(DoodleParseableCommand):
    """Clears a previously filled area.

    If *vertices* is empty then **all** previously filled faces are
    cleared.  Otherwise, the face matching the given vertex set
    (order-independent) is removed.
    Maps to ``\\unfill(v1, v2, ...);`` or ``\\unfill;``.
    """

    DOO_KEYWORD = "unfill"

    vertices: list[str] = field(default_factory=list)

    def to_doo(self) -> str:
        if self.vertices:
            return f"\\unfill({', '.join(self.vertices)})"
        return "\\unfill"

    @classmethod
    def from_doo_args(cls, args: list) -> Unfill:
        return cls(vertices=list(args))


@dataclass
class Darker(DoodleParseableCommand):
    """Decreases the lightness of the given paper side colour.

    *amount* controls the darkening degree.
    Maps to ``\\darker(side, amount);``.
    """

    DOO_KEYWORD = "darker"

    side: Side
    amount: int

    def to_doo(self) -> str:
        return f"\\darker({self.side}, {self.amount})"

    @classmethod
    def from_doo_args(cls, args: list) -> Darker:
        return cls(side=Side(args[0]), amount=int(args[1]))


@dataclass
class Lighter(DoodleParseableCommand):
    """Increases the lightness of the given paper side colour.

    *amount* controls the lightening degree.
    Maps to ``\\lighter(side, amount);``.
    """

    DOO_KEYWORD = "lighter"

    side: Side
    amount: int

    def to_doo(self) -> str:
        return f"\\lighter({self.side}, {self.amount})"

    @classmethod
    def from_doo_args(cls, args: list) -> Lighter:
        return cls(side=Side(args[0]), amount=int(args[1]))


@dataclass
class Caption(DoodleParseableCommand):
    """Adds an explanatory text line beneath the current step.

    Multiple captions per step are stacked in order.
    Maps to ``\\caption("text");``.
    """

    DOO_KEYWORD = "caption"

    text: str

    def to_doo(self) -> str:
        return f"\\caption({string_quote(self.text)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Caption:
        return cls(text=args[0])


@dataclass
class Label(DoodleParseableCommand):
    """Defines a named label bound to the current step number.

    Labels are used by ``RepeatArrow`` and ``Ref`` to reference step
    numbers symbolically.  Label identifiers live in a separate symbol
    table from vertex identifiers.
    Maps to ``\\label(name);``.
    """

    DOO_KEYWORD = "label"

    name: str

    def to_doo(self) -> str:
        return f"\\label({self.name})"

    @classmethod
    def from_doo_args(cls, args: list) -> Label:
        return cls(name=args[0])


@dataclass
class Ref(DoodleParseableCommand):
    """Substitutes a step number into a string (used inside ``\\caption``).

    Maps to ``\\ref(label);``.
    """

    DOO_KEYWORD = "ref"

    step: int

    def to_doo(self) -> str:
        return f"\\ref({self.step})"

    @classmethod
    def from_doo_args(cls, args: list) -> Ref:
        return cls(step=int(args[0]))


@dataclass
class Text(DoodleParseableCommand):
    """Draws annotation text at a vertex position.

    Maps to ``\\text(vertex, "text");``.
    """

    DOO_KEYWORD = "text"

    vertex: str
    text: str

    def to_doo(self) -> str:
        return f"\\text({self.vertex}, {string_quote(self.text)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Text:
        return cls(vertex=args[0], text=args[1])
