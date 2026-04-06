"""High-level Python API for rendering Doodle diagrams.

The C++ renderer always produces PostScript first.  When the caller
requests ``OutputFormat.PDF`` output a private helper converts the
intermediate ``.ps`` file via Ghostscript.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from . import commands as cmd
from .types import OutputFormat
from .writer import write
from ._doodle import render_to_ps as _render_to_ps
from ._doodle import render_step_to_ps as _render_step_to_ps


# ---------------------------------------------------------------------------
# Private helper – PS → PDF conversion
# ---------------------------------------------------------------------------

def _ps_to_pdf(ps_path: Path, pdf_path: Path) -> None:
    """Convert a PostScript file to PDF using Ghostscript.

    Raises
    ------
    RuntimeError
        If Ghostscript (``gs``) is not found on the system or if the
        conversion fails.
    """
    gs = shutil.which("gs")
    if gs is None:
        raise RuntimeError(
            "Ghostscript ('gs') is required for PS to PDF conversion but "
            "was not found on this system.  Install it with your package "
            "manager (e.g. 'apt install ghostscript' or 'brew install "
            "ghostscript')."
        )

    result = subprocess.run(
        [
            gs,
            "-dNOPAUSE",
            "-dBATCH",
            "-dSAFER",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-sOutputFile={pdf_path}",
            str(ps_path),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Ghostscript PS→PDF conversion failed (exit {result.returncode}):\n"
            f"{result.stderr}"
        )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def render_diagram(
    diagram: cmd.Diagram,
    format: OutputFormat = OutputFormat.PDF,
    output: str | Path | None = None,
    *,
    verbose: bool = False,
) -> Path:
    """Render a full Diagram.

    Parameters
    ----------
    diagram:
        A pydoodle ``Diagram`` object.
    format:
        Output format – ``OutputFormat.PS`` for PostScript or
        ``OutputFormat.PDF`` for PDF.
    output:
        Destination file path.  When *None* a temporary file is created
        with the appropriate extension.
    verbose:
        Enable doodle verbose diagnostics on stderr.

    Returns
    -------
    Path to the generated file.
    """
    fmt = format
    if not isinstance(fmt, OutputFormat):
        raise TypeError(
            f"format must be an OutputFormat enum member, got {type(format).__name__}"
        )

    doo_text = write(diagram)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".doo", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(doo_text)
        tmp.write("\n")
        doo_path = Path(tmp.name)

    try:
        if output is None:
            output = doo_path.with_suffix(f".{fmt}")
        else:
            output = Path(output)

        if fmt is OutputFormat.PS:
            _render_to_ps(str(doo_path), str(output), verbose)
        else:
            fd, ps_name = tempfile.mkstemp(suffix=".ps")
            os.close(fd)
            ps_path = Path(ps_name)
            try:
                _render_to_ps(str(doo_path), str(ps_path), verbose)
                _ps_to_pdf(ps_path, output)
            finally:
                ps_path.unlink(missing_ok=True)

        return output
    finally:
        doo_path.unlink(missing_ok=True)


def render_step(
    diagram: cmd.Diagram,
    step: int,
    format: OutputFormat = OutputFormat.PDF,
    output: str | Path | None = None,
    *,
    verbose: bool = False,
) -> Path:
    """Render a Diagram up to and including a specific step.

    Only the diagram steps numbered 1 through *step* are rendered.
    Inter-step directives (e.g. ``\\scale``, ``\\rotate``,
    ``\\turn_over_vertical``) are fully processed by the native parser so
    the geometry and layout remain correct.

    Parameters
    ----------
    diagram:
        A pydoodle ``Diagram`` object.
    step:
        Render only up to and including this step number (1-based).
        Must be ≥ 1.
    format:
        Output format – ``OutputFormat.PS`` for PostScript or
        ``OutputFormat.PDF`` for PDF.
    output:
        Destination file path.  When *None* a temporary file is created
        with the appropriate extension.
    verbose:
        Enable doodle verbose diagnostics on stderr.

    Returns
    -------
    Path to the generated file.

    Raises
    ------
    ValueError
        If *step* is less than 1.
    """
    if step < 1:
        raise ValueError(f"step must be >= 1, got {step!r}")

    fmt = format
    if not isinstance(fmt, OutputFormat):
        raise TypeError(
            f"format must be an OutputFormat enum member, got {type(format).__name__}"
        )

    doo_text = write(diagram)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".doo", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(doo_text)
        tmp.write("\n")
        doo_path = Path(tmp.name)

    try:
        if output is None:
            output = doo_path.with_suffix(f".{fmt}")
        else:
            output = Path(output)

        if fmt is OutputFormat.PS:
            _render_step_to_ps(str(doo_path), str(output), step, verbose)
        else:
            fd, ps_name = tempfile.mkstemp(suffix=".ps")
            os.close(fd)
            ps_path = Path(ps_name)
            try:
                _render_step_to_ps(str(doo_path), str(ps_path), step, verbose)
                _ps_to_pdf(ps_path, output)
            finally:
                ps_path.unlink(missing_ok=True)

        return output
    finally:
        doo_path.unlink(missing_ok=True)
