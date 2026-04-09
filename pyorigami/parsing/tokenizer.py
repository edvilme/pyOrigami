"""Tokenizer for .doo argument strings."""

from __future__ import annotations

import re

from ..types import Edge


def tokenize_args(text: str) -> list[str | int | float | Edge]:
    """Tokenize a comma-separated .doo argument string.

    Returns a flat list of typed tokens:

    - ``Edge(v1, v2)`` for ``[v1, v2]``
    - ``str`` for identifiers and quoted strings (quotes stripped)
    - ``int`` for integer literals
    - ``float`` for floating-point literals
    """
    tokens: list[str | int | float | Edge] = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        # Skip whitespace and commas
        if c in " \t\n\r,":
            i += 1
            continue
        # Edge: [v1, v2]
        if c == "[":
            j = text.index("]", i)
            parts = [p.strip() for p in text[i + 1 : j].split(",")]
            tokens.append(Edge(parts[0], parts[1]))
            i = j + 1
        # Quoted string
        elif c == '"':
            j = i + 1
            chars: list[str] = []
            while j < n:
                if text[j] == "\\" and j + 1 < n:
                    chars.append(text[j + 1])
                    j += 2
                elif text[j] == '"':
                    break
                else:
                    chars.append(text[j])
                    j += 1
            tokens.append("".join(chars))
            i = j + 1
        # Number (int or float, possibly negative)
        elif c == "-" or c.isdigit():
            m = re.match(r"-?\d+(?:\.\d+)?", text[i:])
            if m:
                val = m.group()
                tokens.append(float(val) if "." in val else int(val))
                i += len(val)
            else:
                i += 1
        # Identifier / symbol / keyword
        elif c.isalpha() or c == "_":
            m = re.match(r"[A-Za-z_][A-Za-z0-9_]*", text[i:])
            if m:
                tokens.append(m.group())
                i += len(m.group())
            else:
                i += 1
        else:
            i += 1
    return tokens
