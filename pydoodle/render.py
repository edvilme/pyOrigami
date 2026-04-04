"""High-level Python API for rendering Doodle diagrams to PostScript."""

from __future__ import annotations

import tempfile
from pathlib import Path

from . import commands as cmd
from .writer import write
from ._doodle import render_to_ps as _render_to_ps
from ._doodle import render_step_to_ps as _render_step_to_ps


def render(
    diagram: cmd.Diagram,
    output: str | Path | None = None,
    *,
    verbose: bool = False,
) -> Path:
    """Render a Diagram object to PostScript.

    Parameters
    ----------
    diagram:
        A pydoodle Diagram object.
    output:
        Path for the .ps file. If None a temporary file is used.
    verbose:
        Enable doodle verbose diagnostics on stderr.

    Returns
    -------
    Path to the generated PostScript file.
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
            output = doo_path.with_suffix(".ps")
        else:
            output = Path(output)

        _render_to_ps(str(doo_path), str(output), verbose)
        return output
    finally:
        doo_path.unlink(missing_ok=True)


def render_file(
    doo_path: str | Path,
    output: str | Path | None = None,
    *,
    verbose: bool = False,
) -> Path:
    """Render an existing .doo file to PostScript.

    Parameters
    ----------
    doo_path:
        Path to a .doo input file.
    output:
        Path for the .ps file. Defaults to the input name with .ps.
    verbose:
        Enable doodle verbose diagnostics on stderr.

    Returns
    -------
    Path to the generated PostScript file.
    """
    doo_path = Path(doo_path)
    if not doo_path.is_file():
        raise FileNotFoundError(f"Input file not found: {doo_path}")

    if output is None:
        output = doo_path.with_suffix(".ps")
    else:
        output = Path(output)

    _render_to_ps(str(doo_path), str(output), verbose)
    return output


def render_up_to_step(
    diagram: cmd.Diagram,
    step: int,
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
        A pydoodle Diagram object.
    step:
        Render only up to and including this step number (1-based).
        Must be >= 1.
    output:
        Path for the .ps file. If None a temporary file is used.
    verbose:
        Enable doodle verbose diagnostics on stderr.

    Returns
    -------
    Path to the generated PostScript file.

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
            output = doo_path.with_suffix(".ps")
        else:
            output = Path(output)

        _render_step_to_ps(str(doo_path), str(output), step, verbose)
        return output
    finally:
        doo_path.unlink(missing_ok=True)
