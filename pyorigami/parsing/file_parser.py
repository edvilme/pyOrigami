"""Parse a complete .doo file into a ``Diagram`` command tree."""

from __future__ import annotations

from pathlib import Path

from .matcher import _build_command
from .statement import (
    parse_statement,
    CommentStmt,
    BlockOpenStmt,
    BlockCloseStmt,
)


def parse_text(source: str) -> "Diagram":
    """Parse raw ``.doo`` text and return a :class:`~pyorigami.commands.structure.Diagram`.

    Lines that cannot be parsed (e.g. ``\\define`` macros) are silently
    skipped.
    """
    from ..commands.structure import (
        Diagram,
        DiagramHeader,
        DooComment,
        Step,
    )

    # Ensure the command registry is populated.
    import pyorigami.commands  # noqa: F401

    header: DiagramHeader | None = None
    body: list = []

    # Stack: when we enter a block_open we push the current collector list
    # and start a fresh one.  On block_close we pop.
    stack: list[list] = []
    current: list = body

    for line in source.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        parsed = parse_statement(stripped)
        if parsed is None:
            continue

        if isinstance(parsed, BlockOpenStmt):
            if parsed.keyword == "diagram_header":
                obj = DiagramHeader()
                stack.append(current)
                current = obj.body
                header = obj
            elif parsed.keyword == "step":
                obj = Step()
                stack.append(current)
                current = obj.body
                stack[-1].append(obj)
            continue

        if isinstance(parsed, BlockCloseStmt):
            if stack:
                current = stack.pop()
            continue

        if isinstance(parsed, CommentStmt):
            current.append(DooComment(text=parsed.text))
            continue

        obj = _build_command(parsed)
        if obj is not None:
            current.append(obj)

    if header is None:
        header = DiagramHeader()

    return Diagram(header=header, body=body)


def parse_file(path: str | Path) -> "Diagram":
    """Parse a ``.doo`` file from disk and return a :class:`~pyorigami.commands.structure.Diagram`.

    Tries UTF-8 first, falls back to Latin-1 for older files.
    """
    p = Path(path)
    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = p.read_text(encoding="latin-1")
    return parse_text(text)
