"""PostScript format converters (PDF, PNG, SVG).

Wraps Ghostscript for PS → PDF / PNG conversion and PyMuPDF for
PDF → SVG.  Used by :mod:`pyorigami.render` to produce final output.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from collections.abc import Callable
from enum import Enum
from functools import partial
from pathlib import Path


class OutputFormat(Enum):
    """Output format for rendered diagrams.

    * ``PS``  — PostScript (native C++ output).
    * ``PDF`` — PDF (converted from PostScript via Ghostscript).
    * ``PNG`` — PNG (converted from PostScript via Ghostscript).
    * ``SVG`` — SVG (converted from PostScript via Ghostscript to PDF,
      then from PDF via PyMuPDF).
    """

    PS = "ps"
    PDF = "pdf"
    PNG = "png"
    SVG = "svg"

    def __str__(self) -> str:
        return self.value

    @staticmethod
    def from_string(value: str) -> OutputFormat:
        """Convert a string to an :class:`OutputFormat` member (case-insensitive).

        Raises
        ------
        ValueError
            If *value* does not match any known format.
        """
        try:
            return OutputFormat(value.lower())
        except ValueError:
            valid = ", ".join(repr(f.value) for f in OutputFormat)
            raise ValueError(f"Unsupported format {value!r}; expected one of {valid}") from None


CONVERTERS: dict[OutputFormat, Callable[[Path, Path], None]] = {}


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
        CONVERTERS[OutputFormat.PDF](ps_path, pdf_path)
        doc = pymupdf.open(pdf_path)
        try:
            page = doc[0]
            out_path.write_text(page.get_svg_image(), encoding="utf-8")
        finally:
            doc.close()
    finally:
        pdf_path.unlink(missing_ok=True)


CONVERTERS[OutputFormat.PNG] = partial(_gs_convert, "png16m", ["-r150"])
CONVERTERS[OutputFormat.PDF] = partial(_gs_convert, "pdfwrite", ["-dCompatibilityLevel=1.4"])
CONVERTERS[OutputFormat.SVG] = _ps_to_svg
