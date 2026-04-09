"""Low-level statement parser for .doo files.

Decomposes a single .doo statement line into a typed result object
describing its kind, keyword, and tokenized arguments.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .tokenizer import tokenize_args

# ---------------------------------------------------------------------------
# Parsed statement types
# ---------------------------------------------------------------------------


@dataclass
class CommentStmt:
    """A ``% ...`` comment line."""

    text: str


@dataclass
class BlockOpenStmt:
    """A ``\\keyword {`` or ``\\keyword(...) {`` block opener."""

    keyword: str
    args: list


@dataclass
class BlockCloseStmt:
    """A lone ``}`` closing brace."""


@dataclass
class CommandStmt:
    """A standalone ``\\keyword(...)`` command."""

    keyword: str
    args: list


@dataclass
class AssignStmt:
    """A ``name = \\keyword(...)`` assignment."""

    name: str
    keyword: str
    args: list


@dataclass
class AssignPairStmt:
    """A ``[n1, n2] = \\keyword(...)`` pair assignment."""

    names: tuple[str, str]
    keyword: str
    args: list


ParsedStmt = CommentStmt | BlockOpenStmt | BlockCloseStmt | CommandStmt | AssignStmt | AssignPairStmt


_CMD_RE = re.compile(r"\\(\w+)\s*\(")
_ASSIGN_RE = re.compile(r"([A-Za-z_]\w*)\s*=\s*\\(\w+)\s*\(")
_PAIR_ASSIGN_RE = re.compile(r"\[\s*([A-Za-z_]\w*)\s*,\s*([A-Za-z_]\w*)\s*\]\s*=\s*\\(\w+)\s*\(")


def _find_matching_paren(text: str, open_idx: int) -> int:
    """Return index of the ``')'`` matching the ``'('`` at *open_idx*."""
    depth = 1
    i = open_idx + 1
    in_string = False
    while i < len(text) and depth > 0:
        c = text[i]
        if in_string:
            if c == "\\":
                i += 2
                continue
            if c == '"':
                in_string = False
        else:
            if c == '"':
                in_string = True
            elif c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
        i += 1
    return i - 1


def _strip_trailing_comment(text: str) -> str:
    """Remove a trailing ``% ...`` comment that isn't inside a string."""
    in_str = False
    for idx in range(len(text)):
        c = text[idx]
        if in_str:
            if c == "\\":
                continue
            if c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "%":
                return text[:idx].rstrip()
    return text


def parse_statement(text: str) -> ParsedStmt | None:
    """Parse a single .doo statement into a typed result object.

    Returns one of :class:`CommentStmt`, :class:`BlockOpenStmt`,
    :class:`BlockCloseStmt`, :class:`CommandStmt`, :class:`AssignStmt`,
    or :class:`AssignPairStmt`.

    Returns ``None`` if *text* is empty or cannot be parsed.
    """
    text = text.strip()
    if not text:
        return None

    if text.startswith("%"):
        return CommentStmt(text=text[1:].strip())

    if text == "}":
        return BlockCloseStmt()

    text = _strip_trailing_comment(text)
    stmt = text.rstrip(";").strip()

    # Block open: \keyword { or \keyword(args) {
    if stmt.endswith("{"):
        inner = stmt[:-1].strip()
        m = re.match(r"\\(\w+)(?:\s*\((.+)\))?\s*$", inner)
        if m:
            args = tokenize_args(m.group(2)) if m.group(2) else []
            return BlockOpenStmt(keyword=m.group(1), args=args)

    # Pair assignment: [n1, n2] = \op(...)
    m = _PAIR_ASSIGN_RE.match(stmt)
    if m:
        n1, n2, keyword = m.group(1), m.group(2), m.group(3)
        paren_idx = stmt.index("(", m.end() - 1)
        close_idx = _find_matching_paren(stmt, paren_idx)
        args = tokenize_args(stmt[paren_idx + 1 : close_idx])
        return AssignPairStmt(names=(n1, n2), keyword=keyword, args=args)

    # Single assignment: name = \op(...)
    m = _ASSIGN_RE.match(stmt)
    if m:
        name, keyword = m.group(1), m.group(2)
        paren_idx = stmt.index("(", m.end() - 1)
        close_idx = _find_matching_paren(stmt, paren_idx)
        args = tokenize_args(stmt[paren_idx + 1 : close_idx])
        return AssignStmt(name=name, keyword=keyword, args=args)

    # Standalone command with args: \keyword(...)
    m = _CMD_RE.match(stmt)
    if m:
        keyword = m.group(1)
        paren_idx = stmt.index("(", m.start())
        close_idx = _find_matching_paren(stmt, paren_idx)
        args = tokenize_args(stmt[paren_idx + 1 : close_idx])
        return CommandStmt(keyword=keyword, args=args)

    # Bare command without args: \keyword
    m = re.match(r"\\(\w+)\s*$", stmt)
    if m:
        return CommandStmt(keyword=m.group(1), args=[])

    return None
