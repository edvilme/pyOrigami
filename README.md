# pyOrigami

A Python library for writing `.doo` files used to create origami diagrams. These files follow the DOODLE (Description Of Origami by Drawing Little Elements) format, a markup language for describing origami folding sequences step by step.

## About

pyOrigami lets you programmatically generate `.doo` diagram files that describe origami models — including folds, arrows, captions, and visual styling — which can then be rendered into folding instructions.

## Project structure

```
pyorigami/           # Python package (types, commands, render)
ext/                 # C++ pybind11 bindings & generated parser
doodle/              # Upstream C++ source (git submodule)
examples/            # Sample .doo files and scripts
```

## Credits

The `.doo` file format originates from the [DOODLE](https://doodle.sourceforge.net/) project, a tool for creating origami diagrams.

## Building locally

### Prerequisites

- Python 3.9+
- A C++ compiler (MSVC on Windows, gcc/clang on Linux/macOS)
- [pybind11](https://pybind11.readthedocs.io/) (installed automatically by the build)
- [Ghostscript](https://ghostscript.com/) (required for PDF, PNG, and SVG output)

### Clone (with submodules)

```bash
git clone --recurse-submodules https://github.com/<owner>/pyOrigami.git
cd pyOrigami
```

If you already cloned without `--recurse-submodules`:

```bash
git submodule update --init --recursive
```

### Install in development mode

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install --no-build-isolation -e .
```

To enable SVG output, install with the optional `svg` extra:

```bash
pip install --no-build-isolation -e ".[svg]"
```

`--no-build-isolation` lets setuptools use the pybind11 already installed in your
environment. Drop it if you prefer a fully isolated build (pip will fetch build
dependencies automatically).

### Quick test

```python
from pyorigami import (
    Diagram, DiagramHeader, Step,
    Designer, Title, Diagrammer, DiagramDate,
    Square, ValleyFold, Middle, Assign,
    write, render,
)

boat = Diagram(
    header=DiagramHeader(body=[
        Designer("Traditional"),
        Title("Simple boat"),
    ]),
    body=[
        Step(body=[
            Square("a", "b", "c", "d"),
            Assign("m", Middle("a", "d")),
            Assign("n", Middle("b", "c")),
            ValleyFold("m", "n"),
        ]),
    ],
)

# Serialize to .doo text
print(write(boat))

# Render to PDF (requires Ghostscript)
render(boat, "pdf", "boat.pdf")
```

See [examples/verify_boat.py](examples/verify_boat.py) for a more complete example.

## Output formats

| Format | Extension | Requirements |
|--------|-----------|-------------------------------------------|
| PS     | `.ps`     | None (native C++ output)                  |
| PDF    | `.pdf`    | Ghostscript                               |
| PNG    | `.png`    | Ghostscript                               |
| SVG    | `.svg`    | Ghostscript + `pip install ".[svg]"` (PS → PDF → SVG) |

## Examples

See the [examples/](examples/) directory for sample `.doo` files.

## Regenerating parser files

The `ext/generated/` directory contains pre-generated parser files built from
`doodle/src/parser.l` (lexer) and `doodle/src/parser.y` (grammar). These only
need regenerating if the grammar changes. You need `flex` and `bison` installed.

**Windows** (with [WinFlexBison](https://github.com/lexxmark/winflexbison)):

```powershell
win_flex -o"ext/generated/lex.yy.cpp" doodle/src/parser.l
win_bison -t -v -b parser -d -o "ext/generated/parser.tab.cpp" doodle/src/parser.y
```

**Linux / macOS**:

```bash
flex -o ext/generated/lex.yy.cpp doodle/src/parser.l
bison -t -v -b parser -d -o ext/generated/parser.tab.cpp doodle/src/parser.y
```

The `.cpp` extension is required because MSVC compiles `.c` files as C, but the
doodle headers use C++ features. Using `.cpp` ensures all compilers treat
them as C++.
