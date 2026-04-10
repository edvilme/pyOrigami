"""Test: parse a .doo file → round-trip to .doo, render to .svg, .png, .pdf.

Exercises the full pipeline: parse_file → Diagram → write/render.
Converters that need external tools (Ghostscript, PyMuPDF) are skipped
when those tools are unavailable.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from pyorigami import OutputFormat
from pyorigami.render import write_file, render
from pyorigami.parsing import parse_file

EXAMPLES_DIR = Path(__file__).resolve().parent.parent / "examples"
DOO_FILE = EXAMPLES_DIR / "simple_boat.doo"

_has_gs = bool(shutil.which("gs") or shutil.which("gswin64c") or shutil.which("gswin32c"))

try:
    import pymupdf  # noqa: F401

    _has_pymupdf = True
except ImportError:
    _has_pymupdf = False


@pytest.fixture
def diagram():
    """Parse the sample .doo file into a Diagram tree."""
    return parse_file(DOO_FILE)


# ── .doo round-trip ──────────────────────────────────────────────────────


def test_parse_and_write_doo(diagram, tmp_path):
    """Parsing a .doo file and serializing back produces valid .doo text."""
    out = tmp_path / "output.doo"
    write_file(diagram, str(out))

    text = out.read_text(encoding="utf-8")
    assert "\\diagram_header" in text
    assert "\\step" in text
    assert "\\valley_fold" in text
    assert len(text) > 100

    # The output can itself be re-parsed without error.
    reparsed = parse_file(out)
    assert len(reparsed.header.body) == len(diagram.header.body)
    assert len(reparsed.body) == len(diagram.body)


# ── PostScript ───────────────────────────────────────────────────────────


def test_render_ps(diagram, tmp_path):
    """Rendering to PostScript produces a non-empty .ps file."""
    out = tmp_path / "output.ps"
    result = render(diagram, format=OutputFormat.PS, output=out, native=True)

    assert result.exists()
    content = result.read_text(encoding="utf-8")
    assert content.startswith("%!")  # PS header


# ── PDF (requires Ghostscript) ───────────────────────────────────────────


@pytest.mark.skipif(not _has_gs, reason="Ghostscript not found")
def test_render_pdf(diagram, tmp_path):
    """Rendering to PDF produces a non-empty file with a PDF header."""
    out = tmp_path / "output.pdf"
    result = render(diagram, format=OutputFormat.PDF, output=out, native=True)

    assert result.exists()
    assert result.stat().st_size > 0
    header = result.read_bytes()[:5]
    assert header == b"%PDF-"


# ── PNG (requires Ghostscript) ───────────────────────────────────────────


@pytest.mark.skipif(not _has_gs, reason="Ghostscript not found")
def test_render_png(diagram, tmp_path):
    """Rendering to PNG produces a non-empty file with a PNG signature."""
    out = tmp_path / "output.png"
    result = render(diagram, format=OutputFormat.PNG, output=out, native=True)

    assert result.exists()
    assert result.stat().st_size > 0
    header = result.read_bytes()[:8]
    assert header == b"\x89PNG\r\n\x1a\n"


# ── SVG (requires Ghostscript + PyMuPDF) ─────────────────────────────────


@pytest.mark.skipif(not _has_gs, reason="Ghostscript not found")
@pytest.mark.skipif(not _has_pymupdf, reason="PyMuPDF not installed")
def test_render_svg(diagram, tmp_path):
    """Rendering to SVG produces a non-empty file containing <svg."""
    out = tmp_path / "output.svg"
    result = render(diagram, format=OutputFormat.SVG, output=out, native=True)

    assert result.exists()
    content = result.read_text(encoding="utf-8")
    assert "<svg" in content
