// pybind11 bindings for the Doodle origami diagram renderer.
//
// Exposes the core parse+render pipeline to Python so that
// .doo files can be converted to PostScript without a separate binary.

#include <pybind11/pybind11.h>
#include <cstdio>
#include <string>
#include <vector>
#include <stdexcept>

#include "diag_header.h"
#include "step.h"
#include "ps_output.h"

namespace py = pybind11;

// Parser interface (defined in bison/flex generated code, compiled as C++)
int yyparse();
void yyrestart(FILE *);
extern FILE *yyin;

// Global state populated by the parser (defined in parser.y)
extern int          line_num;
extern std::string  file_name;
extern int          current_index;
extern int          current_step;
extern bool         is_sub_step;
extern int          nbComment;
extern diag_header  info;
extern std::vector<step> steps;
extern bool         verbose;
extern int          visible_height;
extern int          visible_width;
extern int          scale;
extern std::string  center;
extern bool         clip;

static void reset_parser_state() {
    line_num       = 1;
    file_name.clear();
    current_index  = 1;
    current_step   = 0;
    is_sub_step    = false;
    nbComment      = 0;
    info           = diag_header();
    steps.clear();
    verbose        = false;
    visible_height = 65;   // CLIP_HEIGHT
    visible_width  = 65;   // CLIP_WIDTH
    scale          = 100;
    center.clear();
    clip           = false;
}

static void render_to_ps(const std::string &input_path,
                          const std::string &output_path,
                          bool verbose_mode) {
    reset_parser_state();
    verbose   = verbose_mode;
    file_name = input_path;

    FILE *f = fopen(input_path.c_str(), "r");
    if (!f)
        throw std::runtime_error("Cannot open input file: " + input_path);

    yyin = f;
    yyrestart(f);

    int rc = yyparse();
    fclose(f);

    if (rc != 0)
        throw std::runtime_error("Parse error in: " + input_path);

    ps_output(output_path.c_str());
}

static void render_step_to_ps(const std::string &input_path,
                               const std::string &output_path,
                               int max_step,
                               bool verbose_mode) {
    if (max_step < 1)
        throw std::invalid_argument("max_step must be >= 1");

    reset_parser_state();
    verbose   = verbose_mode;
    file_name = input_path;

    FILE *f = fopen(input_path.c_str(), "r");
    if (!f)
        throw std::runtime_error("Cannot open input file: " + input_path);

    yyin = f;
    yyrestart(f);

    int rc = yyparse();
    fclose(f);

    if (rc != 0)
        throw std::runtime_error("Parse error in: " + input_path);

    // Truncate the parsed steps to the requested limit.
    if (steps.size() > static_cast<size_t>(max_step))
        steps.resize(static_cast<size_t>(max_step));

    ps_output(output_path.c_str());
}

PYBIND11_MODULE(_doodle, m) {
    m.doc() = "Native bindings to the Doodle origami diagram renderer";

    m.def("render_to_ps", &render_to_ps,
          py::arg("input_path"),
          py::arg("output_path"),
          py::arg("verbose") = false,
          "Parse a .doo file and render it to PostScript.");

    m.def("render_step_to_ps", &render_step_to_ps,
          py::arg("input_path"),
          py::arg("output_path"),
          py::arg("max_step"),
          py::arg("verbose") = false,
          "Parse a .doo file and render only the first max_step steps to PostScript.");
}
