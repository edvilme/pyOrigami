"""High-level Python API for rendering Doodle diagrams.

The C++ renderer always produces PostScript first.  Non-PS formats are
produced by a converter registered in ``_CONVERTERS``.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from collections.abc import Callable
from functools import partial
from pathlib import Path

from . import commands as cmd
from .types import OutputFormat
from .writer import write
from ._doodle import render_to_ps as _render_to_ps
from ._doodle import render_step_to_ps as _render_step_to_ps

# ---------------------------------------------------------------------------
# Converter registry
# ---------------------------------------------------------------------------

_CONVERTERS: dict[OutputFormat, Callable[[Path, Path], None]] = {}


def _find_gs() -> str:
    gs = shutil.which("gs") or shutil.which("gswin64c") or shutil.which("gswin32c")
    if gs is None:
        raise RuntimeError(
            "Ghostscript ('gs') is required for PS conversion but "
            "was not found on this system.  Install it with your package "
            "manager (e.g. 'apt install ghostscript' or 'brew install "
            "ghostscript')."
        )
    return gs


def _gs_convert(device: str, extra_args: list[str], ps_path: Path, out_path: Path) -> None:
    """Convert a PostScript file using a Ghostscript device."""
    gs = _find_gs()
    result = subprocess.run(
        [
            gs,
            "-dNOPAUSE",
            "-dBATCH",
            "-dSAFER",
            f"-sDEVICE={device}",
            *extra_args,
            f"-sOutputFile={out_path}",
            str(ps_path),
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Ghostscript PS→{device} conversion failed " f"(exit {result.returncode}):\n{result.stderr}"
        )


def _ps_to_svg(ps_path: Path, out_path: Path) -> None:
    """Convert a PostScript file to SVG via an intermediate PDF.

    Uses Ghostscript for PS→PDF, then PyMuPDF (``pymupdf``) for PDF→SVG.
    """
    import pymupdf  # lazy import to avoid hard dependency at module level

    fd, pdf_name = tempfile.mkstemp(suffix=".pdf")
    os.close(fd)
    pdf_path = Path(pdf_name)
    try:
        _CONVERTERS[OutputFormat.PDF](ps_path, pdf_path)
        doc = pymupdf.open(pdf_path)
        try:
            page = doc[0]
            out_path.write_text(page.get_svg_image(), encoding="utf-8")
        finally:
            doc.close()
    finally:
        pdf_path.unlink(missing_ok=True)


_CONVERTERS[OutputFormat.PNG] = partial(_gs_convert, "png16m", ["-r150"])
_CONVERTERS[OutputFormat.PDF] = partial(_gs_convert, "pdfwrite", ["-dCompatibilityLevel=1.4"])
_CONVERTERS[OutputFormat.SVG] = _ps_to_svg


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def render(
    diagram: cmd.Diagram,
    format: OutputFormat | str = OutputFormat.PDF,
    output: str | Path | None = None,
    *,
    step: int | None = None,
    single_step: int | None = None,
    verbose: bool = False,
) -> Path:
    """Render a Diagram to a file.

    Parameters
    ----------
    diagram:
        A pydoodle ``Diagram`` object.
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

    Returns
    -------
    Path to the generated file.

    Raises
    ------
    ValueError
        If *step* is less than 1 or *format* is not supported.
    """
    if step is not None and step < 1:
        raise ValueError(f"step must be >= 1, got {step!r}")

    if isinstance(format, str):
        format = OutputFormat.from_string(format)

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
        elif format in _CONVERTERS:
            fd, ps_name = tempfile.mkstemp(suffix=".ps")
            os.close(fd)
            ps_path = Path(ps_name)
            try:
                _to_ps(str(doo_path), str(ps_path))
                _CONVERTERS[format](ps_path, output)
            finally:
                ps_path.unlink(missing_ok=True)
        else:
            raise ValueError(f"Unsupported output format: {format!r}")

        return output
    finally:
        doo_path.unlink(missing_ok=True)
