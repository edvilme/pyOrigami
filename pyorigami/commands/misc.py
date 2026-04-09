"""Miscellaneous commands (debug, reset, include).

Based on the `DOODLE <https://doodle.sourceforge.net/>`_ project by
Olivier Bettens.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..parsing import DoodleParseableCommand
from ..types import string_quote


@dataclass
class Debug(DoodleParseableCommand):
    """Displays all visible point names and edge names for the current step.

    A diagnostic aid; combines the effects of ``DebugPoint`` and
    ``DebugLine``.
    Maps to ``\\debug;``.
    """

    DOO_KEYWORD = "debug"

    def to_doo(self) -> str:
        return "\\debug"

    @classmethod
    def from_doo_args(cls, args: list) -> Debug:
        return cls()


@dataclass
class DebugLine(DoodleParseableCommand):
    """Displays visible edge names for the current step.

    Maps to ``\\debug_line;``.
    """

    DOO_KEYWORD = "debug_line"

    def to_doo(self) -> str:
        return "\\debug_line"

    @classmethod
    def from_doo_args(cls, args: list) -> DebugLine:
        return cls()


@dataclass
class DebugPoint(DoodleParseableCommand):
    """Displays visible vertex names for the current step.

    Maps to ``\\debug_point;``.
    """

    DOO_KEYWORD = "debug_point"

    def to_doo(self) -> str:
        return "\\debug_point"

    @classmethod
    def from_doo_args(cls, args: list) -> DebugPoint:
        return cls()


@dataclass
class Reset(DoodleParseableCommand):
    """Resets all internal data structures to their initial state.

    Maps to ``\\reset;``.
    """

    DOO_KEYWORD = "reset"

    def to_doo(self) -> str:
        return "\\reset"

    @classmethod
    def from_doo_args(cls, args: list) -> Reset:
        return cls()


@dataclass
class Include(DoodleParseableCommand):
    """Includes another Doodle source file at the current position.

    Maps to ``\\include("filename");``.
    """

    DOO_KEYWORD = "include"

    filename: str

    def to_doo(self) -> str:
        return f"\\include({string_quote(self.filename)})"

    @classmethod
    def from_doo_args(cls, args: list) -> Include:
        return cls(filename=args[0])
