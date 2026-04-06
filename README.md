# pyOrigami

A Python library for writing `.doo` files used to create origami diagrams. These files follow the DOODLE (Description Of Origami by Drawing Little Elements) format, a markup language for describing origami folding sequences step by step.

## About

pyOrigami lets you programmatically generate `.doo` diagram files that describe origami models — including folds, arrows, captions, and visual styling — which can then be rendered into folding instructions.

## Credits

The `.doo` file format originates from the [DOODLE](https://doodle.sourceforge.net/) project, a tool for creating origami diagrams.

## Building locally

### Prerequisites

- Python 3.9+
- A C++ compiler (MSVC on Windows, gcc/clang on Linux/macOS)
- [pybind11](https://pybind11.readthedocs.io/) (installed automatically by the build)

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

`--no-build-isolation` lets setuptools use the pybind11 already installed in your
environment. Drop it if you prefer a fully isolated build (pip will fetch build
dependencies automatically).

### Quick test

```python
from pydoodle import render_diagram_to_pdf, Diagram, DiagramHeader, Step, Square, Designer, Title, Caption

diagram = Diagram(
    header=DiagramHeader(body=[Designer("Traditional"), Title("Simple boat")]),
    body=[Step(body=[Square("a", "b", "c", "d"), Caption("Start with a square")])],
)
pdf_path = render_diagram_to_pdf(diagram)
print(f"Generated {pdf_path}")
```

Or from the command line:

```bash
python -c "
from pydoodle import render_diagram_to_pdf, Diagram, DiagramHeader, Step, Square, Designer, Title, Caption
d = Diagram(header=DiagramHeader(body=[Designer('X'), Title('T')]), body=[Step(body=[Square('a','b','c','d')])])
print(render_diagram_to_pdf(d))
"
```

This should produce a ``.pdf`` file.

## Examples

See the [examples/](examples/) directory for sample `.doo` files.

## Regenerating parser files

The `generated/` directory contains pre-generated parser files built from
`doodle/src/parser.l` (lexer) and `doodle/src/parser.y` (grammar). These only
need regenerating if the grammar changes. You need `flex` and `bison` installed.

**Windows** (with [WinFlexBison](https://github.com/lexxmark/winflexbison)):

```powershell
win_flex -o"generated/lex.yy.cpp" doodle/src/parser.l
win_bison -t -v -b parser -d -o "generated/parser.tab.cpp" doodle/src/parser.y
```

**Linux / macOS**:

```bash
flex -o generated/lex.yy.cpp doodle/src/parser.l
bison -t -v -b parser -d -o generated/parser.tab.cpp doodle/src/parser.y
```

The `.cpp` extension is required because MSVC compiles `.c` files as C, but the
doodle headers use C++ features. Using `.cpp` ensures all compilers treat
them as C++.
