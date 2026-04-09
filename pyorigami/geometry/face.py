"""Internal face and colour representation ported from the DOODLE C++ codebase.

Derived from ``doodle/src/face.h`` / ``face.cpp`` and
``doodle/src/color.h`` / ``color.cpp``.
DOODLE — https://doodle.sourceforge.net/ — by Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class InternalColor:
    r: int = 0
    g: int = 0
    b: int = 0

    def copy(self) -> InternalColor:
        return InternalColor(self.r, self.g, self.b)


@dataclass
class InternalFace:
    symbols: list[str] = field(default_factory=list)
    color: InternalColor = field(default_factory=InternalColor)

    def copy(self) -> InternalFace:
        return InternalFace(list(self.symbols), self.color.copy())
