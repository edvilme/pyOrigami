"""High-level statement matcher — maps .doo text to command objects."""

from __future__ import annotations

from .base import REGISTRY
from .statement import (
    parse_statement,
    ParsedStmt,
    CommentStmt,
    BlockCloseStmt,
    BlockOpenStmt,
    CommandStmt,
    AssignStmt,
    AssignPairStmt,
)


def _build_command(parsed: CommandStmt | AssignStmt | AssignPairStmt):
    """Build a command object from a parsed statement with a keyword.

    Returns the command (possibly wrapped in ``Assign`` or ``AssignPair``),
    or ``None`` if the keyword is not registered.
    """
    cls = REGISTRY.get(parsed.keyword)
    if cls is None:
        return None

    obj = cls.from_doo_args(parsed.args)

    if isinstance(parsed, AssignStmt):
        from ..commands.structure import Assign

        return Assign(name=parsed.name, expr=obj)

    if isinstance(parsed, AssignPairStmt):
        from ..commands.structure import AssignPair

        return AssignPair(names=parsed.names, expr=obj)

    return obj


def match_statement(text: str):
    """Parse a .doo statement and return the corresponding command object.

    Handles standalone commands, assignments (wrapped in ``Assign`` /
    ``AssignPair``), comments (``DooComment``), and block boundaries
    (``DiagramHeader``, ``Step``).

    Returns ``None`` for closing braces or unrecognised text.
    """
    parsed = parse_statement(text)
    if parsed is None:
        return None

    if isinstance(parsed, CommentStmt):
        from ..commands.structure import DooComment

        return DooComment(text=parsed.text)

    if isinstance(parsed, BlockCloseStmt):
        return None

    if isinstance(parsed, BlockOpenStmt):
        if parsed.keyword == "diagram_header":
            from ..commands.structure import DiagramHeader

            return DiagramHeader()
        if parsed.keyword == "step":
            from ..commands.structure import Step

            return Step()
        return None

    return _build_command(parsed)
