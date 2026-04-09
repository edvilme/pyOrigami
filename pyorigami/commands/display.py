from __future__ import annotations

from dataclasses import dataclass, field

from ..types import Edge, Side, string_quote


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
