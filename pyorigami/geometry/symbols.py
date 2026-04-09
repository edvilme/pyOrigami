"""Arrow symbol dataclasses ported from the DOODLE C++ codebase.

Derived from ``doodle/src/open_arrow.h``, ``push_arrow.h``, and
``repeat_arrow.h``.
DOODLE — https://doodle.sourceforge.net/ — by Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class OpenArrowSymbol:
    v1: str
    v2: str
    right: bool = True


@dataclass
class PushArrowSymbol:
    point: str
    angle: int = 0
    distance: int = 0


@dataclass
class RepeatArrowSymbol:
    point: str
    angle: int = 0
    distance: int = 0
    number: int = 0
    first_label: str = ""
    second_label: str = ""


ArrowSymbol = OpenArrowSymbol | PushArrowSymbol | RepeatArrowSymbol
