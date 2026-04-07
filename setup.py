"""Build the Doodle C++ sources into a pybind11 extension module."""

import platform
import os
from pathlib import Path

from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

DOODLE_SRC = os.path.join("doodle", "src")
GENERATED = "generated"

CPP_SOURCES = [
    "vertex.cpp",
    "edge.cpp",
    "vect.cpp",
    "step.cpp",
    "date.cpp",
    "diag_header.cpp",
    "read_instruction.cpp",
    "ps_output.cpp",
    "arrow.cpp",
    "color.cpp",
    "face.cpp",
    "push_arrow.cpp",
    "open_arrow.cpp",
    "repeat_arrow.cpp",
    "ps_prologue.cpp",
]

extra_compile_args = []
define_macros = []

# Suppress harmless warnings from legacy doodle C++ code and generated parser files.
if platform.system() == "Windows":
    define_macros.append(("WIN32", "1"))
    extra_compile_args += ["/wd4244", "/wd4267", "/wd4996"]
else:
    extra_compile_args += ["-Wno-register", "-Wno-unused-function", "-Wno-sign-compare"]

ext_modules = [
    Pybind11Extension(
        "pydoodle._doodle",
        sources=(
            [os.path.join(DOODLE_SRC, f) for f in CPP_SOURCES]
            + [
                os.path.join(GENERATED, "lex.yy.cpp"),  # Generated lexer
                os.path.join(GENERATED, "parser.tab.cpp"),  # Generated parser
                os.path.join("pydoodle", "_bindings.cpp"),  # pybind11 bindings
            ]
        ),
        include_dirs=[DOODLE_SRC, GENERATED],
        define_macros=define_macros,
        extra_compile_args=extra_compile_args,
        language="c++",
    ),
]

setup(ext_modules=ext_modules)
