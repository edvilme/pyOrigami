# pyOrigami

A Python library for writing `.doo` files used to create origami diagrams. These files follow the DOODLE (Description Of Origami by Drawing Little Elements) format, a markup language for describing origami folding sequences step by step.

## About

pyOrigami lets you programmatically generate `.doo` diagram files that describe origami models — including folds, arrows, captions, and visual styling — which can then be rendered into folding instructions.

## Credits

The `.doo` file format originates from the [DOODLE](https://doodle.sourceforge.net/) project, a tool for creating origami diagrams.

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
