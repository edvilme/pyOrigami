"""Parsing infrastructure for .doo origami diagram files.

Submodules:

* :mod:`.tokenizer` — tokenizes comma-separated argument strings.
* :mod:`.statement` — decomposes a single .doo line into typed result objects.
* :mod:`.base` — command registry and :class:`DoodleParseableCommand` base class.
* :mod:`.matcher` — high-level dispatcher that builds command objects.
* :mod:`.file_parser` — parses a complete .doo file into a ``Diagram`` tree.
"""

from .tokenizer import tokenize_args
from .statement import (
    parse_statement,
    ParsedStmt,
    CommentStmt,
    BlockOpenStmt,
    BlockCloseStmt,
    CommandStmt,
    AssignStmt,
    AssignPairStmt,
)
from .base import REGISTRY, DoodleParseableCommand, register
from .matcher import match_statement
from .file_parser import parse_file, parse_text

__all__ = [
    "tokenize_args",
    "parse_statement",
    "ParsedStmt",
    "CommentStmt",
    "BlockOpenStmt",
    "BlockCloseStmt",
    "CommandStmt",
    "AssignStmt",
    "AssignPairStmt",
    "REGISTRY",
    "DoodleParseableCommand",
    "register",
    "match_statement",
    "parse_file",
    "parse_text",
]
