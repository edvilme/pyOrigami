"""Serializes pydoodle command trees into Doodle .doo text format."""

from __future__ import annotations

from . import commands as cmd


def write(diagram: cmd.Diagram) -> str:
    """Serialize a ``Diagram`` tree to a Doodle ``.doo`` format string."""
    return diagram.to_doo()


def write_file(diagram: cmd.Diagram, path: str) -> None:
    """Serialize a ``Diagram`` tree and write it to a file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(write(diagram))
        f.write("\n")
