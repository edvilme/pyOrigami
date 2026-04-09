"""Command registry and DoodleParseableCommand base class for .doo commands."""

from __future__ import annotations

from typing import ClassVar

from .statement import parse_statement, CommandStmt

REGISTRY: dict[str, type] = {}
"""Maps .doo keyword strings to their command dataclasses."""


def register(*classes: type) -> None:
    """Register command classes by their ``DOO_KEYWORD`` attribute."""
    for cls in classes:
        REGISTRY[cls.DOO_KEYWORD] = cls


class DoodleParseableCommand:
    """Mixin that adds ``.match()`` to command dataclasses.

    Subclasses must define:

    * ``DOO_KEYWORD``: class-level string with the .doo keyword
      (without the leading backslash).
    * ``from_doo_args(cls, args)``: classmethod that constructs an
      instance from a list of tokenized arguments (as returned by
      :func:`~pyorigami.parsing.tokenizer.tokenize_args`).
    """

    DOO_KEYWORD: ClassVar[str]

    @classmethod
    def from_doo_args(cls, args: list) -> DoodleParseableCommand:
        """Construct an instance from tokenized .doo argument list."""
        raise NotImplementedError

    @classmethod
    def match(cls, text: str) -> DoodleParseableCommand | None:
        """Try to parse a .doo statement as this command type.

        Returns an instance if *text* matches this command's keyword,
        or ``None`` otherwise.  For assignment-wrapped commands
        (``name = \\op(...)``), use :func:`match_statement` instead.
        """
        parsed = parse_statement(text)
        if not isinstance(parsed, CommandStmt):
            return None
        if parsed.keyword != cls.DOO_KEYWORD:
            return None
        return cls.from_doo_args(parsed.args)
