"""High-level Python API for rendering Doodle diagrams to PDF.

The C++ renderer produces PostScript which is then converted to PDF using
Ghostscript (``gs``).  The original ``.ps`` file is removed after
conversion unless *keep_ps* is set to ``True``.
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

from . import commands as cmd
from .writer import write
from ._doodle import render_to_ps as _render_to_ps
from ._doodle import render_step_to_ps as _render_step_to_ps


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


def _render_and_convert(render_fn, output: Path, keep_ps: bool) -> Path:
    """Run a C++ PS render function and convert the result to PDF.

    *render_fn* is called with the path to the intermediate ``.ps`` file.
    The PS file is converted to *output* (PDF) via Ghostscript.
    """
    # Use a unique temp path for the intermediate PS to avoid collisions
    # when the caller-supplied output already has a .ps extension.
    with tempfile.NamedTemporaryFile(
        suffix=".ps", delete=False, dir=output.parent
    ) as tmp:
        ps_path = Path(tmp.name)

    try:
        render_fn(str(ps_path))
        _ps_to_pdf(ps_path, output)
    finally:
        if keep_ps:
            target = output.with_suffix(".ps")
            if ps_path != target:
                ps_path.rename(target)
        else:
            ps_path.unlink(missing_ok=True)


def render(
    diagram: cmd.Diagram,
    output: str | Path | None = None,
    *,
    keep_ps: bool = False,
    verbose: bool = False,
) -> Path:
    """Render a Diagram object to PDF.

    Parameters
    ----------
    diagram:
        A pydoodle Diagram object.
    output:
        Path for the ``.pdf`` file.  If *None* a temporary file is used.
    keep_ps:
        When *True* the intermediate PostScript file is kept alongside
        the PDF.
    verbose:
        Enable doodle verbose diagnostics on stderr.

    Returns
    -------
    Path to the generated PDF file.
    """
    doo_text = write(diagram)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".doo", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(doo_text)
        tmp.write("\n")
        doo_path = Path(tmp.name)

    try:
        if output is None:
            output = doo_path.with_suffix(".pdf")
        else:
            output = Path(output)

        _render_and_convert(
            lambda ps: _render_to_ps(str(doo_path), ps, verbose),
            output,
            keep_ps,
        )
        return output
    finally:
        doo_path.unlink(missing_ok=True)


def render_file(
    doo_path: str | Path,
    output: str | Path | None = None,
    *,
    keep_ps: bool = False,
    verbose: bool = False,
) -> Path:
    """Render an existing .doo file to PDF.

    Parameters
    ----------
    doo_path:
        Path to a ``.doo`` input file.
    output:
        Path for the ``.pdf`` file.  Defaults to the input name with
        ``.pdf`` extension.
    keep_ps:
        When *True* the intermediate PostScript file is kept alongside
        the PDF.
    verbose:
        Enable doodle verbose diagnostics on stderr.

    Returns
    -------
    Path to the generated PDF file.
    """
    doo_path = Path(doo_path)
    if not doo_path.is_file():
        raise FileNotFoundError(f"Input file not found: {doo_path}")

    if output is None:
        output = doo_path.with_suffix(".pdf")
    else:
        output = Path(output)

    _render_and_convert(
        lambda ps: _render_to_ps(str(doo_path), ps, verbose),
        output,
        keep_ps,
    )
    return output


def render_file_up_to_step(
    doo_path: str | Path,
    step: int,
    output: str | Path | None = None,
    *,
    keep_ps: bool = False,
    verbose: bool = False,
) -> Path:
    """Render an existing .doo file up to and including a specific step.

    This is the most direct path to the C++ renderer — the .doo file is
    parsed natively, the internal step list is truncated to *step* entries,
    and ``ps_output`` renders the result which is then converted to PDF.

    Parameters
    ----------
    doo_path:
        Path to a ``.doo`` input file.
    step:
        Render only up to and including this step number (1-based).
        Must be >= 1.
    output:
        Path for the ``.pdf`` file.  Defaults to the input name with
        ``.pdf`` extension.
    keep_ps:
        When *True* the intermediate PostScript file is kept alongside
        the PDF.
    verbose:
        Enable doodle verbose diagnostics on stderr.

    Returns
    -------
    Path to the generated PDF file.

    Raises
    ------
    ValueError
        If *step* is less than 1.
    FileNotFoundError
        If *doo_path* does not exist.
    """
    if step < 1:
        raise ValueError(f"step must be >= 1, got {step!r}")

    doo_path = Path(doo_path)
    if not doo_path.is_file():
        raise FileNotFoundError(f"Input file not found: {doo_path}")

    if output is None:
        output = doo_path.with_suffix(".pdf")
    else:
        output = Path(output)

    _render_and_convert(
        lambda ps: _render_step_to_ps(str(doo_path), ps, step, verbose),
        output,
        keep_ps,
    )
    return output


def render_up_to_step(
    diagram: cmd.Diagram,
    step: int,
    output: str | Path | None = None,
    *,
    keep_ps: bool = False,
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
        A pydoodle Diagram object.
    step:
        Render only up to and including this step number (1-based).
        Must be >= 1.
    output:
        Path for the ``.pdf`` file.  If *None* a temporary file is used.
    keep_ps:
        When *True* the intermediate PostScript file is kept alongside
        the PDF.
    verbose:
        Enable doodle verbose diagnostics on stderr.

    Returns
    -------
    Path to the generated PDF file.

    Raises
    ------
    ValueError
        If *step* is less than 1.
    """
    if step < 1:
        raise ValueError(f"step must be >= 1, got {step!r}")

    doo_text = write(diagram)

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".doo", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(doo_text)
        tmp.write("\n")
        doo_path = Path(tmp.name)

    try:
        if output is None:
            output = doo_path.with_suffix(".pdf")
        else:
            output = Path(output)

        _render_and_convert(
            lambda ps: _render_step_to_ps(str(doo_path), ps, step, verbose),
            output,
            keep_ps,
        )
        return output
    finally:
        doo_path.unlink(missing_ok=True)
