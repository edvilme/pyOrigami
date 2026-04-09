"""Serialization and rendering of pyorigami Diagram trees.

``write`` / ``write_file`` convert a Diagram to the textual ``.doo``
format.  ``render`` goes further and produces PostScript (either via
the C++ engine or the pure-Python engine) and optionally converts it
to PDF, PNG or SVG output files.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

from . import commands as cmd
from .converters import CONVERTERS, OutputFormat

try:
    from ._doodle import render_to_ps as _render_to_ps
    from ._doodle import render_step_to_ps as _render_step_to_ps

    _HAS_NATIVE = True
except ImportError:
    _HAS_NATIVE = False

from .engine import evaluate as _evaluate
from .ps import generate_ps as _generate_ps

# ---------------------------------------------------------------------------
# Write helpers
# ---------------------------------------------------------------------------


def write(diagram: cmd.Diagram) -> str:
    """Serialize a ``Diagram`` tree to a Doodle ``.doo`` format string."""
    return diagram.to_doo()


def write_file(diagram: cmd.Diagram, path: str) -> None:
    """Serialize a ``Diagram`` tree and write it to a file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(write(diagram))
        f.write("\n")


# ---------------------------------------------------------------------------
# Pure-Python rendering path
# ---------------------------------------------------------------------------


def _render_native(
    diagram: cmd.Diagram,
    format: OutputFormat,
    output: str | Path | None,
    *,
    step: int | None = None,
) -> Path:
    """Render using the pure-Python engine + PS writer."""
    header, steps = _evaluate(diagram)
    if step is not None:
        steps = steps[:step]
    ps_content = _generate_ps(header, steps)

    if format is OutputFormat.PS:
        if output is None:
            fd, name = tempfile.mkstemp(suffix=".ps")
            os.close(fd)
            output = Path(name)
        else:
            output = Path(output)
        output.write_text(ps_content, encoding="utf-8")
        return output

    # Write PS to temp, then convert
    fd, ps_name = tempfile.mkstemp(suffix=".ps")
    os.close(fd)
    ps_path = Path(ps_name)
    try:
        ps_path.write_text(ps_content, encoding="utf-8")
        if output is None:
            fd, name = tempfile.mkstemp(suffix=f".{format}")
            os.close(fd)
            output = Path(name)
        else:
            output = Path(output)
        if format in CONVERTERS:
            CONVERTERS[format](ps_path, output)
        else:
            raise ValueError(f"Unsupported output format: {format!r}")
        return output
    finally:
        ps_path.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def render(
    diagram: cmd.Diagram,
    format: OutputFormat | str = OutputFormat.PDF,
    output: str | Path | None = None,
    *,
    step: int | None = None,
    verbose: bool = False,
    native: bool | None = None,
) -> Path:
    """Render a Diagram to a file.

    Parameters
    ----------
    diagram:
        A pyorigami ``Diagram`` object.
    format:
        Output format – ``OutputFormat.PS`` / ``"ps"`` for PostScript,
        ``OutputFormat.PDF`` / ``"pdf"`` for PDF, ``OutputFormat.PNG`` /
        ``"png"`` for PNG, or ``OutputFormat.SVG`` / ``"svg"`` for SVG.
    output:
        Destination file path.  When *None* a temporary file is created
        with the appropriate extension.
    step:
        When *None* (the default) the entire diagram is rendered.
        Otherwise only steps 1 through *step* are included (1-based,
        must be ≥ 1)
    verbose:
        Enable doodle verbose diagnostics on stderr.
    native:
        When *True* use the pure-Python engine instead of the C++
        backend.  When *None* (the default) the C++ backend is used if
        available, otherwise falls back to the pure-Python engine.
        When *False* the C++ backend is explicitly requested; a
        :exc:`RuntimeError` is raised if it is not available.

    Returns
    -------
    Path to the generated file.

    Raises
    ------
    ValueError
        If *step* is less than 1 or *format* is not supported.
    RuntimeError
        If *native* is ``False`` and the C++ backend is not available.
    """
    if step is not None and step < 1:
        raise ValueError(f"step must be >= 1, got {step!r}")

    if isinstance(format, str):
        format = OutputFormat.from_string(format)

    use_native = native if native is not None else not _HAS_NATIVE

    if not use_native and not _HAS_NATIVE:
        raise RuntimeError(
            "The C++ backend (_doodle extension) is not available. "
            "Install it or use native=True to use the pure-Python engine."
        )

    if use_native:
        return _render_native(diagram, format, output, step=step)

    def _to_ps(doo: str, ps: str) -> None:
        if step is not None:
            _render_step_to_ps(doo, ps, step, verbose)
        else:
            _render_to_ps(doo, ps, verbose)

    doo_text = write(diagram)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".doo", delete=False, encoding="utf-8") as tmp:
        tmp.write(doo_text)
        tmp.write("\n")
        doo_path = Path(tmp.name)

    try:
        output = doo_path.with_suffix(f".{format}") if output is None else Path(output)

        if format is OutputFormat.PS:
            _to_ps(str(doo_path), str(output))
        elif format in CONVERTERS:
            fd, ps_name = tempfile.mkstemp(suffix=".ps")
            os.close(fd)
            ps_path = Path(ps_name)
            try:
                _to_ps(str(doo_path), str(ps_path))
                CONVERTERS[format](ps_path, output)
            finally:
                ps_path.unlink(missing_ok=True)
        else:
            raise ValueError(f"Unsupported output format: {format!r}")

        return output
    finally:
        doo_path.unlink(missing_ok=True)
