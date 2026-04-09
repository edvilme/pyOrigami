"""Miscellaneous commands (debug, reset, include).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..types import string_quote


@dataclass
class Debug:
    """Displays all visible point names and edge names for the current step.

    A diagnostic aid; combines the effects of ``DebugPoint`` and
    ``DebugLine``.
    Maps to ``\\debug;``.
    """

    def to_doo(self) -> str:
        return "\\debug"


@dataclass
class DebugLine:
    """Displays visible edge names for the current step.

    Maps to ``\\debug_line;``.
    """

    def to_doo(self) -> str:
        return "\\debug_line"


@dataclass
class DebugPoint:
    """Displays visible vertex names for the current step.

    Maps to ``\\debug_point;``.
    """

    def to_doo(self) -> str:
        return "\\debug_point"


@dataclass
class Reset:
    """Resets all internal data structures to their initial state.

    Maps to ``\\reset;``.
    """

    def to_doo(self) -> str:
        return "\\reset"


@dataclass
class Include:
    """Includes another Doodle source file at the current position.

    Maps to ``\\include("filename");``.
    """

    filename: str

    def to_doo(self) -> str:
        return f"\\include({string_quote(self.filename)})"
