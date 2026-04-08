/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output, and Bison version.  */
#define YYBISON 30802

/* Bison version string.  */
#define YYBISON_VERSION "3.8.2"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* First part of user prologue.  */
#line 7 "doodle/src/parser.y"


#ifdef WIN32
#pragma warning (disable : 4786)
#endif // WIN32
#include <stdio.h>
#include <string>
#include <time.h>  //- for localtime
#include <sys/types.h> //- for time_t
#include <vector>
#include <map>
#include <malloc.h>
  
#include "diag_header.h"
#include "date.h"
#include "step.h"
#include "vertex.h"
#include "edge.h"
#include "macro.h"
#include "read_instruction.h"
#include "global_def.h"
#include "color.h"

  //- work variables
  int line_num = 1;
  std::string file_name;

  int current_index = 1;
  int current_step = 0;
  bool is_sub_step = false;
  int nbComment = 0;

  //- global data parser fills
  diag_header info;
  std::vector<step> steps;
  bool verbose = false;
  int visible_height = CLIP_HEIGHT; 
  int visible_width = CLIP_WIDTH;
  int scale         = 100;  //- original scale factor is identity (100%)
  std::string center;
  bool clip;
  typedef std::map<std::string,macro> macromap;
  macromap macros;
  static macromap::iterator current_macro;
  
 //- Avoid error messages from yacc
 void yyerror(char *s);
 void yywarning(char* s);
 int  yylex();
 

#line 123 "generated/parser.tab.cpp"

# ifndef YY_CAST
#  ifdef __cplusplus
#   define YY_CAST(Type, Val) static_cast<Type> (Val)
#   define YY_REINTERPRET_CAST(Type, Val) reinterpret_cast<Type> (Val)
#  else
#   define YY_CAST(Type, Val) ((Type) (Val))
#   define YY_REINTERPRET_CAST(Type, Val) ((Type) (Val))
#  endif
# endif
# ifndef YY_NULLPTR
#  if defined __cplusplus
#   if 201103L <= __cplusplus
#    define YY_NULLPTR nullptr
#   else
#    define YY_NULLPTR 0
#   endif
#  else
#   define YY_NULLPTR ((void*)0)
#  endif
# endif

#include "parser.tab.hpp"
/* Symbol kind.  */
enum yysymbol_kind_t
{
  YYSYMBOL_YYEMPTY = -2,
  YYSYMBOL_YYEOF = 0,                      /* "end of file"  */
  YYSYMBOL_YYerror = 1,                    /* error  */
  YYSYMBOL_YYUNDEF = 2,                    /* "invalid token"  */
  YYSYMBOL_HEADER = 3,                     /* HEADER  */
  YYSYMBOL_STEP = 4,                       /* STEP  */
  YYSYMBOL_TURN_VERTICAL = 5,              /* TURN_VERTICAL  */
  YYSYMBOL_TURN_HORIZONTAL = 6,            /* TURN_HORIZONTAL  */
  YYSYMBOL_ROTATE = 7,                     /* ROTATE  */
  YYSYMBOL_DESIGN_DATE = 8,                /* DESIGN_DATE  */
  YYSYMBOL_DIAG_DATE = 9,                  /* DIAG_DATE  */
  YYSYMBOL_DESIGNER = 10,                  /* DESIGNER  */
  YYSYMBOL_DIAGRAMER = 11,                 /* DIAGRAMER  */
  YYSYMBOL_DIAGRAMMER = 12,                /* DIAGRAMMER  */
  YYSYMBOL_TODAY = 13,                     /* TODAY  */
  YYSYMBOL_TITLE = 14,                     /* TITLE  */
  YYSYMBOL__LEFT_MARGIN = 15,              /* _LEFT_MARGIN  */
  YYSYMBOL__RIGHT_MARGIN = 16,             /* _RIGHT_MARGIN  */
  YYSYMBOL__TOP_MARGIN = 17,               /* _TOP_MARGIN  */
  YYSYMBOL__BOTTOM_MARGIN = 18,            /* _BOTTOM_MARGIN  */
  YYSYMBOL__VSPACE = 19,                   /* _VSPACE  */
  YYSYMBOL__HSPACE = 20,                   /* _HSPACE  */
  YYSYMBOL_SQUARE = 21,                    /* SQUARE  */
  YYSYMBOL_DIAMOND = 22,                   /* DIAMOND  */
  YYSYMBOL_MIDDLE = 23,                    /* MIDDLE  */
  YYSYMBOL_FRACT = 24,                     /* FRACT  */
  YYSYMBOL_CAPTION = 25,                   /* CAPTION  */
  YYSYMBOL_VALLEY_FOLD = 26,               /* VALLEY_FOLD  */
  YYSYMBOL_MOUNTAIN_FOLD = 27,             /* MOUNTAIN_FOLD  */
  YYSYMBOL_FOLD = 28,                      /* FOLD  */
  YYSYMBOL_SCALE = 29,                     /* SCALE  */
  YYSYMBOL_POINT_TO_POINT = 30,            /* POINT_TO_POINT  */
  YYSYMBOL_POINT_TO_LINE = 31,             /* POINT_TO_LINE  */
  YYSYMBOL_LINE_TO_LINE = 32,              /* LINE_TO_LINE  */
  YYSYMBOL_SIMPLE_ARROW = 33,              /* SIMPLE_ARROW  */
  YYSYMBOL_RETURN_ARROW = 34,              /* RETURN_ARROW  */
  YYSYMBOL_HIDE = 35,                      /* HIDE  */
  YYSYMBOL_SHOW = 36,                      /* SHOW  */
  YYSYMBOL_BORDER = 37,                    /* BORDER  */
  YYSYMBOL_INTERSECTION = 38,              /* INTERSECTION  */
  YYSYMBOL_SYMMETRY = 39,                  /* SYMMETRY  */
  YYSYMBOL_CUT = 40,                       /* CUT  */
  YYSYMBOL_DEBUG_INST = 41,                /* DEBUG_INST  */
  YYSYMBOL_DEBUG_POINT_INST = 42,          /* DEBUG_POINT_INST  */
  YYSYMBOL_DEBUG_LINE_INST = 43,           /* DEBUG_LINE_INST  */
  YYSYMBOL_XRAY_FOLD = 44,                 /* XRAY_FOLD  */
  YYSYMBOL_VISIBLE_HEIGHT = 45,            /* VISIBLE_HEIGHT  */
  YYSYMBOL_VISIBLE_WIDTH = 46,             /* VISIBLE_WIDTH  */
  YYSYMBOL_VISIBLE_CENTER = 47,            /* VISIBLE_CENTER  */
  YYSYMBOL_COLOR_FRONT = 48,               /* COLOR_FRONT  */
  YYSYMBOL_COLOR_BACK = 49,                /* COLOR_BACK  */
  YYSYMBOL_FILL = 50,                      /* FILL  */
  YYSYMBOL_UNFILL = 51,                    /* UNFILL  */
  YYSYMBOL_V_RECTANGLE = 52,               /* V_RECTANGLE  */
  YYSYMBOL_H_RECTANGLE = 53,               /* H_RECTANGLE  */
  YYSYMBOL_CLIP = 54,                      /* CLIP  */
  YYSYMBOL_UNCLIP = 55,                    /* UNCLIP  */
  YYSYMBOL_PERPENDICULAR = 56,             /* PERPENDICULAR  */
  YYSYMBOL_PARALLEL = 57,                  /* PARALLEL  */
  YYSYMBOL_MOVE = 58,                      /* MOVE  */
  YYSYMBOL_INTER_CUT = 59,                 /* INTER_CUT  */
  YYSYMBOL_SPACE_FOLD = 60,                /* SPACE_FOLD  */
  YYSYMBOL_COMMENT = 61,                   /* COMMENT  */
  YYSYMBOL_EPS = 62,                       /* EPS  */
  YYSYMBOL_RESET = 63,                     /* RESET  */
  YYSYMBOL_SHIFT = 64,                     /* SHIFT  */
  YYSYMBOL_MACRO = 65,                     /* MACRO  */
  YYSYMBOL_MACROTEXT = 66,                 /* MACROTEXT  */
  YYSYMBOL_OPERATOR = 67,                  /* OPERATOR  */
  YYSYMBOL_DARKER = 68,                    /* DARKER  */
  YYSYMBOL_LIGHTER = 69,                   /* LIGHTER  */
  YYSYMBOL_TEXT = 70,                      /* TEXT  */
  YYSYMBOL_UNSHIFT = 71,                   /* UNSHIFT  */
  YYSYMBOL_RABBIT_EAR = 72,                /* RABBIT_EAR  */
  YYSYMBOL_OPEN_ARROW = 73,                /* OPEN_ARROW  */
  YYSYMBOL_PUSH_ARROW = 74,                /* PUSH_ARROW  */
  YYSYMBOL_REPEAT_ARROW = 75,              /* REPEAT_ARROW  */
  YYSYMBOL_LABEL = 76,                     /* LABEL  */
  YYSYMBOL_DEBUG_INFO = 77,                /* DEBUG_INFO  */
  YYSYMBOL_INTEGER = 78,                   /* INTEGER  */
  YYSYMBOL_FLOAT = 79,                     /* FLOAT  */
  YYSYMBOL_SYMBOL = 80,                    /* SYMBOL  */
  YYSYMBOL_STRING = 81,                    /* STRING  */
  YYSYMBOL_82_ = 82,                       /* ';'  */
  YYSYMBOL_83_ = 83,                       /* '{'  */
  YYSYMBOL_84_ = 84,                       /* '}'  */
  YYSYMBOL_85_ = 85,                       /* '('  */
  YYSYMBOL_86_ = 86,                       /* ')'  */
  YYSYMBOL_87_ = 87,                       /* ','  */
  YYSYMBOL_88_ = 88,                       /* '='  */
  YYSYMBOL_89_ = 89,                       /* '['  */
  YYSYMBOL_90_ = 90,                       /* ']'  */
  YYSYMBOL_YYACCEPT = 91,                  /* $accept  */
  YYSYMBOL_diagram = 92,                   /* diagram  */
  YYSYMBOL_definitions = 93,               /* definitions  */
  YYSYMBOL_statement = 94,                 /* statement  */
  YYSYMBOL_pre_statement = 95,             /* pre_statement  */
  YYSYMBOL_header_statement = 96,          /* header_statement  */
  YYSYMBOL_header_data = 97,               /* header_data  */
  YYSYMBOL_design_date = 98,               /* design_date  */
  YYSYMBOL_diag_date = 99,                 /* diag_date  */
  YYSYMBOL_designer = 100,                 /* designer  */
  YYSYMBOL_diagrammer = 101,               /* diagrammer  */
  YYSYMBOL_title = 102,                    /* title  */
  YYSYMBOL_header_visible_height = 103,    /* header_visible_height  */
  YYSYMBOL_header_visible_width = 104,     /* header_visible_width  */
  YYSYMBOL_left_margin = 105,              /* left_margin  */
  YYSYMBOL_right_margin = 106,             /* right_margin  */
  YYSYMBOL_top_margin = 107,               /* top_margin  */
  YYSYMBOL_bottom_margin = 108,            /* bottom_margin  */
  YYSYMBOL_vspace = 109,                   /* vspace  */
  YYSYMBOL_hspace = 110,                   /* hspace  */
  YYSYMBOL_color_front = 111,              /* color_front  */
  YYSYMBOL_color_back = 112,               /* color_back  */
  YYSYMBOL_comment = 113,                  /* comment  */
  YYSYMBOL_inter_step_statement = 114,     /* inter_step_statement  */
  YYSYMBOL_visible_height_inter = 115,     /* visible_height_inter  */
  YYSYMBOL_visible_width_inter = 116,      /* visible_width_inter  */
  YYSYMBOL_scale_inter = 117,              /* scale_inter  */
  YYSYMBOL_visible_center_inter = 118,     /* visible_center_inter  */
  YYSYMBOL_clip_inter = 119,               /* clip_inter  */
  YYSYMBOL_unclip_inter = 120,             /* unclip_inter  */
  YYSYMBOL_macro_def = 121,                /* macro_def  */
  YYSYMBOL_macro_ope = 122,                /* macro_ope  */
  YYSYMBOL_macro_param = 123,              /* macro_param  */
  YYSYMBOL_macro_part = 124,               /* macro_part  */
  YYSYMBOL_rotate_inter = 125,             /* rotate_inter  */
  YYSYMBOL_turn_over_vertical_inter = 126, /* turn_over_vertical_inter  */
  YYSYMBOL_turn_over_horizontal_inter = 127, /* turn_over_horizontal_inter  */
  YYSYMBOL_step_statement = 128,           /* step_statement  */
  YYSYMBOL_begin_step = 129,               /* begin_step  */
  YYSYMBOL_instruction_list = 130,         /* instruction_list  */
  YYSYMBOL_diamond_inst = 131,             /* diamond_inst  */
  YYSYMBOL_square_inst = 132,              /* square_inst  */
  YYSYMBOL_middle_inst = 133,              /* middle_inst  */
  YYSYMBOL_fract_inst = 134,               /* fract_inst  */
  YYSYMBOL_caption_inst = 135,             /* caption_inst  */
  YYSYMBOL_valley_fold_inst = 136,         /* valley_fold_inst  */
  YYSYMBOL_mountain_fold_inst = 137,       /* mountain_fold_inst  */
  YYSYMBOL_border_inst = 138,              /* border_inst  */
  YYSYMBOL_fold_inst = 139,                /* fold_inst  */
  YYSYMBOL_xray_fold_inst = 140,           /* xray_fold_inst  */
  YYSYMBOL_point_to_point_inst = 141,      /* point_to_point_inst  */
  YYSYMBOL_point_to_line_inst = 142,       /* point_to_line_inst  */
  YYSYMBOL_line_to_line_inst = 143,        /* line_to_line_inst  */
  YYSYMBOL_simple_arrow_inst = 144,        /* simple_arrow_inst  */
  YYSYMBOL_return_arrow_inst = 145,        /* return_arrow_inst  */
  YYSYMBOL_hide_inst = 146,                /* hide_inst  */
  YYSYMBOL_show_inst = 147,                /* show_inst  */
  YYSYMBOL_intersection_inst = 148,        /* intersection_inst  */
  YYSYMBOL_symmetry_inst = 149,            /* symmetry_inst  */
  YYSYMBOL_cut_inst = 150,                 /* cut_inst  */
  YYSYMBOL_debug_inst = 151,               /* debug_inst  */
  YYSYMBOL_debug_point_inst = 152,         /* debug_point_inst  */
  YYSYMBOL_debug_line_inst = 153,          /* debug_line_inst  */
  YYSYMBOL_visible_height_inst = 154,      /* visible_height_inst  */
  YYSYMBOL_visible_width_inst = 155,       /* visible_width_inst  */
  YYSYMBOL_visible_center_inst = 156,      /* visible_center_inst  */
  YYSYMBOL_scale_inst = 157,               /* scale_inst  */
  YYSYMBOL_fill_inst = 158,                /* fill_inst  */
  YYSYMBOL_unfill_inst = 159,              /* unfill_inst  */
  YYSYMBOL_debug_info_inst = 160,          /* debug_info_inst  */
  YYSYMBOL_vertical_rectangle_inst = 161,  /* vertical_rectangle_inst  */
  YYSYMBOL_horizontal_rectangle_inst = 162, /* horizontal_rectangle_inst  */
  YYSYMBOL_clip_inst = 163,                /* clip_inst  */
  YYSYMBOL_unclip_inst = 164,              /* unclip_inst  */
  YYSYMBOL_perpendicular_inst = 165,       /* perpendicular_inst  */
  YYSYMBOL_parallel_inst = 166,            /* parallel_inst  */
  YYSYMBOL_move_inst = 167,                /* move_inst  */
  YYSYMBOL_inter_cut_inst = 168,           /* inter_cut_inst  */
  YYSYMBOL_space_fold_inst = 169,          /* space_fold_inst  */
  YYSYMBOL_eps_inst = 170,                 /* eps_inst  */
  YYSYMBOL_reset_inst = 171,               /* reset_inst  */
  YYSYMBOL_shift_inst = 172,               /* shift_inst  */
  YYSYMBOL_unshift_inst = 173,             /* unshift_inst  */
  YYSYMBOL_text_inst = 174,                /* text_inst  */
  YYSYMBOL_duplicate_inst = 175,           /* duplicate_inst  */
  YYSYMBOL_rabbit_ear_inst = 176,          /* rabbit_ear_inst  */
  YYSYMBOL_push_arrow_inst = 177,          /* push_arrow_inst  */
  YYSYMBOL_open_arrow_inst = 178,          /* open_arrow_inst  */
  YYSYMBOL_repeat_arrow_inst = 179,        /* repeat_arrow_inst  */
  YYSYMBOL_label_inst = 180,               /* label_inst  */
  YYSYMBOL_symbol_list = 181,              /* symbol_list  */
  YYSYMBOL_a_date = 182,                   /* a_date  */
  YYSYMBOL_a_color = 183,                  /* a_color  */
  YYSYMBOL_rotate_old_syntax_error = 184,  /* rotate_old_syntax_error  */
  YYSYMBOL_rotate_in_step_error = 185,     /* rotate_in_step_error  */
  YYSYMBOL_turn_over_vertical_error = 186, /* turn_over_vertical_error  */
  YYSYMBOL_turn_over_horizontal_error = 187 /* turn_over_horizontal_error  */
};
typedef enum yysymbol_kind_t yysymbol_kind_t;




#ifdef short
# undef short
#endif

/* On compilers that do not define __PTRDIFF_MAX__ etc., make sure
   <limits.h> and (if available) <stdint.h> are included
   so that the code can choose integer types of a good width.  */

#ifndef __PTRDIFF_MAX__
# include <limits.h> /* INFRINGES ON USER NAME SPACE */
# if defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stdint.h> /* INFRINGES ON USER NAME SPACE */
#  define YY_STDINT_H
# endif
#endif

/* Narrow types that promote to a signed type and that can represent a
   signed or unsigned integer of at least N bits.  In tables they can
   save space and decrease cache pressure.  Promoting to a signed type
   helps avoid bugs in integer arithmetic.  */

#ifdef __INT_LEAST8_MAX__
typedef __INT_LEAST8_TYPE__ yytype_int8;
#elif defined YY_STDINT_H
typedef int_least8_t yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef __INT_LEAST16_MAX__
typedef __INT_LEAST16_TYPE__ yytype_int16;
#elif defined YY_STDINT_H
typedef int_least16_t yytype_int16;
#else
typedef short yytype_int16;
#endif

/* Work around bug in HP-UX 11.23, which defines these macros
   incorrectly for preprocessor constants.  This workaround can likely
   be removed in 2023, as HPE has promised support for HP-UX 11.23
   (aka HP-UX 11i v2) only through the end of 2022; see Table 2 of
   <https://h20195.www2.hpe.com/V2/getpdf.aspx/4AA4-7673ENW.pdf>.  */
#ifdef __hpux
# undef UINT_LEAST8_MAX
# undef UINT_LEAST16_MAX
# define UINT_LEAST8_MAX 255
# define UINT_LEAST16_MAX 65535
#endif

#if defined __UINT_LEAST8_MAX__ && __UINT_LEAST8_MAX__ <= __INT_MAX__
typedef __UINT_LEAST8_TYPE__ yytype_uint8;
#elif (!defined __UINT_LEAST8_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST8_MAX <= INT_MAX)
typedef uint_least8_t yytype_uint8;
#elif !defined __UINT_LEAST8_MAX__ && UCHAR_MAX <= INT_MAX
typedef unsigned char yytype_uint8;
#else
typedef short yytype_uint8;
#endif

#if defined __UINT_LEAST16_MAX__ && __UINT_LEAST16_MAX__ <= __INT_MAX__
typedef __UINT_LEAST16_TYPE__ yytype_uint16;
#elif (!defined __UINT_LEAST16_MAX__ && defined YY_STDINT_H \
       && UINT_LEAST16_MAX <= INT_MAX)
typedef uint_least16_t yytype_uint16;
#elif !defined __UINT_LEAST16_MAX__ && USHRT_MAX <= INT_MAX
typedef unsigned short yytype_uint16;
#else
typedef int yytype_uint16;
#endif

#ifndef YYPTRDIFF_T
# if defined __PTRDIFF_TYPE__ && defined __PTRDIFF_MAX__
#  define YYPTRDIFF_T __PTRDIFF_TYPE__
#  define YYPTRDIFF_MAXIMUM __PTRDIFF_MAX__
# elif defined PTRDIFF_MAX
#  ifndef ptrdiff_t
#   include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  endif
#  define YYPTRDIFF_T ptrdiff_t
#  define YYPTRDIFF_MAXIMUM PTRDIFF_MAX
# else
#  define YYPTRDIFF_T long
#  define YYPTRDIFF_MAXIMUM LONG_MAX
# endif
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif defined __STDC_VERSION__ && 199901 <= __STDC_VERSION__
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned
# endif
#endif

#define YYSIZE_MAXIMUM                                  \
  YY_CAST (YYPTRDIFF_T,                                 \
           (YYPTRDIFF_MAXIMUM < YY_CAST (YYSIZE_T, -1)  \
            ? YYPTRDIFF_MAXIMUM                         \
            : YY_CAST (YYSIZE_T, -1)))

#define YYSIZEOF(X) YY_CAST (YYPTRDIFF_T, sizeof (X))


/* Stored state numbers (used for stacks). */
typedef yytype_int16 yy_state_t;

/* State numbers in computations.  */
typedef int yy_state_fast_t;

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif


#ifndef YY_ATTRIBUTE_PURE
# if defined __GNUC__ && 2 < __GNUC__ + (96 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_PURE __attribute__ ((__pure__))
# else
#  define YY_ATTRIBUTE_PURE
# endif
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# if defined __GNUC__ && 2 < __GNUC__ + (7 <= __GNUC_MINOR__)
#  define YY_ATTRIBUTE_UNUSED __attribute__ ((__unused__))
# else
#  define YY_ATTRIBUTE_UNUSED
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YY_USE(E) ((void) (E))
#else
# define YY_USE(E) /* empty */
#endif

/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
#if defined __GNUC__ && ! defined __ICC && 406 <= __GNUC__ * 100 + __GNUC_MINOR__
# if __GNUC__ * 100 + __GNUC_MINOR__ < 407
#  define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                           \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")
# else
#  define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN                           \
    _Pragma ("GCC diagnostic push")                                     \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")              \
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# endif
# define YY_IGNORE_MAYBE_UNINITIALIZED_END      \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif

#if defined __cplusplus && defined __GNUC__ && ! defined __ICC && 6 <= __GNUC__
# define YY_IGNORE_USELESS_CAST_BEGIN                          \
    _Pragma ("GCC diagnostic push")                            \
    _Pragma ("GCC diagnostic ignored \"-Wuseless-cast\"")
# define YY_IGNORE_USELESS_CAST_END            \
    _Pragma ("GCC diagnostic pop")
#endif
#ifndef YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_BEGIN
# define YY_IGNORE_USELESS_CAST_END
#endif


#define YY_ASSERT(E) ((void) (0 && (E)))

#if !defined yyoverflow

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* !defined yyoverflow */

#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yy_state_t yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (YYSIZEOF (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (YYSIZEOF (yy_state_t) + YYSIZEOF (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYPTRDIFF_T yynewbytes;                                         \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * YYSIZEOF (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / YYSIZEOF (*yyptr);                        \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, YY_CAST (YYSIZE_T, (Count)) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYPTRDIFF_T yyi;                      \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  3
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   1110

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  91
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  97
/* YYNRULES -- Number of rules.  */
#define YYNRULES  265
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  1087

/* YYMAXUTOK -- Last valid token kind.  */
#define YYMAXUTOK   336


/* YYTRANSLATE(TOKEN-NUM) -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, with out-of-bounds checking.  */
#define YYTRANSLATE(YYX)                                \
  (0 <= (YYX) && (YYX) <= YYMAXUTOK                     \
   ? YY_CAST (yysymbol_kind_t, yytranslate[YYX])        \
   : YYSYMBOL_YYUNDEF)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex.  */
static const yytype_int8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
      85,    86,     2,     2,    87,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,    82,
       2,    88,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,    89,     2,    90,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    83,     2,    84,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81
};

#if YYDEBUG
/* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_int16 yyrline[] =
{
       0,   102,   102,   130,   131,   134,   135,   136,   141,   142,
     146,   149,   150,   151,   152,   153,   154,   155,   156,   157,
     158,   159,   160,   161,   162,   163,   164,   165,   168,   174,
     180,   186,   191,   197,   201,   207,   213,   219,   225,   231,
     237,   243,   249,   255,   260,   266,   272,   278,   296,   297,
     298,   299,   300,   301,   302,   303,   304,   305,   306,   307,
     310,   316,   322,   329,   336,   345,   354,   362,   379,   380,
     381,   390,   391,   397,   403,   410,   417,   426,   432,   439,
     452,   457,   463,   464,   465,   466,   467,   468,   469,   470,
     471,   472,   473,   474,   475,   476,   477,   478,   479,   480,
     481,   482,   483,   484,   485,   486,   487,   488,   489,   490,
     491,   492,   493,   494,   495,   496,   497,   498,   499,   500,
     501,   502,   503,   504,   505,   506,   507,   508,   509,   510,
     511,   512,   513,   514,   515,   516,   517,   518,   525,   532,
     539,   546,   553,   560,   565,   570,   575,   580,   585,   592,
     597,   602,   607,   612,   617,   624,   629,   634,   639,   644,
     649,   656,   661,   666,   671,   676,   681,   688,   693,   698,
     703,   708,   713,   720,   730,   740,   752,   758,   766,   771,
     776,   781,   786,   791,   798,   804,   810,   818,   823,   830,
     835,   842,   847,   854,   861,   868,   875,   879,   886,   890,
     895,   902,   908,   914,   921,   927,   934,   939,   945,   954,
     960,   968,   974,   982,   986,   992,   998,  1003,  1010,  1017,
    1022,  1029,  1036,  1043,  1048,  1055,  1061,  1066,  1071,  1076,
    1083,  1087,  1094,  1101,  1108,  1114,  1121,  1127,  1135,  1140,
    1145,  1150,  1155,  1162,  1167,  1174,  1180,  1186,  1192,  1197,
    1203,  1209,  1215,  1222,  1231,  1237,  1245,  1249,  1256,  1262,
    1267,  1272,  1284,  1291,  1297,  1304
};
#endif

/** Accessing symbol of state STATE.  */
#define YY_ACCESSING_SYMBOL(State) YY_CAST (yysymbol_kind_t, yystos[State])

#if YYDEBUG || 0
/* The user-facing name of the symbol whose (internal) number is
   YYSYMBOL.  No bounds checking.  */
static const char *yysymbol_name (yysymbol_kind_t yysymbol) YY_ATTRIBUTE_UNUSED;

/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "\"end of file\"", "error", "\"invalid token\"", "HEADER", "STEP",
  "TURN_VERTICAL", "TURN_HORIZONTAL", "ROTATE", "DESIGN_DATE", "DIAG_DATE",
  "DESIGNER", "DIAGRAMER", "DIAGRAMMER", "TODAY", "TITLE", "_LEFT_MARGIN",
  "_RIGHT_MARGIN", "_TOP_MARGIN", "_BOTTOM_MARGIN", "_VSPACE", "_HSPACE",
  "SQUARE", "DIAMOND", "MIDDLE", "FRACT", "CAPTION", "VALLEY_FOLD",
  "MOUNTAIN_FOLD", "FOLD", "SCALE", "POINT_TO_POINT", "POINT_TO_LINE",
  "LINE_TO_LINE", "SIMPLE_ARROW", "RETURN_ARROW", "HIDE", "SHOW", "BORDER",
  "INTERSECTION", "SYMMETRY", "CUT", "DEBUG_INST", "DEBUG_POINT_INST",
  "DEBUG_LINE_INST", "XRAY_FOLD", "VISIBLE_HEIGHT", "VISIBLE_WIDTH",
  "VISIBLE_CENTER", "COLOR_FRONT", "COLOR_BACK", "FILL", "UNFILL",
  "V_RECTANGLE", "H_RECTANGLE", "CLIP", "UNCLIP", "PERPENDICULAR",
  "PARALLEL", "MOVE", "INTER_CUT", "SPACE_FOLD", "COMMENT", "EPS", "RESET",
  "SHIFT", "MACRO", "MACROTEXT", "OPERATOR", "DARKER", "LIGHTER", "TEXT",
  "UNSHIFT", "RABBIT_EAR", "OPEN_ARROW", "PUSH_ARROW", "REPEAT_ARROW",
  "LABEL", "DEBUG_INFO", "INTEGER", "FLOAT", "SYMBOL", "STRING", "';'",
  "'{'", "'}'", "'('", "')'", "','", "'='", "'['", "']'", "$accept",
  "diagram", "definitions", "statement", "pre_statement",
  "header_statement", "header_data", "design_date", "diag_date",
  "designer", "diagrammer", "title", "header_visible_height",
  "header_visible_width", "left_margin", "right_margin", "top_margin",
  "bottom_margin", "vspace", "hspace", "color_front", "color_back",
  "comment", "inter_step_statement", "visible_height_inter",
  "visible_width_inter", "scale_inter", "visible_center_inter",
  "clip_inter", "unclip_inter", "macro_def", "macro_ope", "macro_param",
  "macro_part", "rotate_inter", "turn_over_vertical_inter",
  "turn_over_horizontal_inter", "step_statement", "begin_step",
  "instruction_list", "diamond_inst", "square_inst", "middle_inst",
  "fract_inst", "caption_inst", "valley_fold_inst", "mountain_fold_inst",
  "border_inst", "fold_inst", "xray_fold_inst", "point_to_point_inst",
  "point_to_line_inst", "line_to_line_inst", "simple_arrow_inst",
  "return_arrow_inst", "hide_inst", "show_inst", "intersection_inst",
  "symmetry_inst", "cut_inst", "debug_inst", "debug_point_inst",
  "debug_line_inst", "visible_height_inst", "visible_width_inst",
  "visible_center_inst", "scale_inst", "fill_inst", "unfill_inst",
  "debug_info_inst", "vertical_rectangle_inst",
  "horizontal_rectangle_inst", "clip_inst", "unclip_inst",
  "perpendicular_inst", "parallel_inst", "move_inst", "inter_cut_inst",
  "space_fold_inst", "eps_inst", "reset_inst", "shift_inst",
  "unshift_inst", "text_inst", "duplicate_inst", "rabbit_ear_inst",
  "push_arrow_inst", "open_arrow_inst", "repeat_arrow_inst", "label_inst",
  "symbol_list", "a_date", "a_color", "rotate_old_syntax_error",
  "rotate_in_step_error", "turn_over_vertical_error",
  "turn_over_horizontal_error", YY_NULLPTR
};

static const char *
yysymbol_name (yysymbol_kind_t yysymbol)
{
  return yytname[yysymbol];
}
#endif

#define YYPACT_NINF (-292)

#define yypact_value_is_default(Yyn) \
  ((Yyn) == YYPACT_NINF)

#define YYTABLE_NINF (-83)

#define yytable_value_is_error(Yyn) \
  0

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
static const yytype_int16 yypact[] =
{
    -292,     2,     0,  -292,   -40,     6,  -292,  -292,  -292,  -292,
    -292,  -292,    35,   150,   172,    90,    23,     3,    45,    93,
     -71,    87,   113,   118,   155,   148,   169,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
     245,  -292,   159,   244,   246,   247,   248,   249,   250,   251,
     252,   253,   254,   255,   256,   257,   258,   259,   260,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,   -51,  -292,
    -292,  -292,  -292,   207,    21,   268,   269,   270,   271,  -292,
    -292,     4,    -9,    -9,   272,   273,   274,   275,   279,   280,
     281,   282,   283,   284,   285,   286,    27,   134,   287,  -292,
     289,     5,  -292,   263,   264,   266,   288,   290,   291,   293,
      89,  -292,   243,   292,   294,   295,   296,   297,   -65,   298,
     299,   300,   301,   302,   303,   304,   305,   278,   306,   307,
     309,   310,  -292,  -292,  -292,  -292,  -292,   311,   315,   316,
     317,   318,   319,  -292,   320,   321,   322,   323,   324,   325,
     326,   327,   328,   329,   330,   331,   332,   333,   334,   335,
     339,   -63,   131,   337,   338,   340,   341,   342,   137,   343,
     344,   143,   348,   346,   347,   349,   351,   350,   352,   149,
     353,   354,   355,   356,   357,   336,  -292,  -292,   363,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,   358,   362,   364,   365,   366,   367,  -292,   368,
     369,   370,   371,   372,   373,   374,   375,   376,   381,   378,
     383,   380,   382,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,   385,   386,   387,   384,   388,   389,   390,   393,   392,
     277,   -19,    24,   394,   391,  -292,  -292,   395,  -292,    32,
     396,   399,   400,   401,   -56,  -292,   395,   402,   403,  -292,
     406,  -292,   405,   397,   398,  -292,   407,   408,  -292,   395,
     404,   409,   410,   411,   413,   170,   412,   414,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,   415,  -292,   416,  -292,  -292,   359,   417,   418,
     420,   421,   422,   423,   425,   426,   427,   432,   120,   434,
     160,   428,   436,   162,   437,   166,   431,   433,   435,   438,
     440,   441,  -292,   442,   168,   443,   444,   445,   446,   447,
     171,   448,   449,   173,   454,   175,   177,   451,   452,   455,
     456,   457,   458,   459,   460,   461,   462,   463,   464,   468,
     471,   419,   450,   474,   472,   473,   475,   476,   477,   479,
     480,   481,    39,   469,   478,   482,   483,   484,   487,   485,
     486,   488,   489,   493,   492,   494,   495,   -56,   -56,   395,
     496,   499,   500,   491,    78,   497,   501,   503,    67,   439,
     504,   498,   505,   157,   506,   158,   507,   508,   502,   511,
     512,   513,    88,   514,   509,   510,   515,   516,  -292,   314,
    -292,   453,   517,  -292,   518,   519,  -292,   179,   181,   183,
    -292,   520,   521,   522,   528,  -292,   529,  -292,   185,   530,
    -292,   531,  -292,   187,  -292,  -292,  -292,   526,   527,   189,
    -292,   532,   533,   535,   536,   534,   537,  -292,   538,   539,
     540,   542,  -292,   543,  -292,   191,   544,  -292,   193,   545,
    -292,  -292,   546,   547,   548,   549,   550,   558,   552,   560,
     561,   562,   556,   541,   563,   564,   567,   568,   569,   -62,
     570,   -55,   571,   -36,   574,   557,   525,   559,   565,   575,
     -26,   566,   572,   576,    -2,  -292,  -292,   577,   580,   581,
     582,   583,   579,   573,   589,   145,   203,   586,   584,   587,
     592,   591,   590,   595,   596,   597,   598,   599,   600,   601,
     588,   593,   602,   603,   604,   605,   -12,  -292,  -292,   606,
     607,  -292,   608,   612,  -292,   609,   617,  -292,   611,   619,
     613,   621,   615,   618,   620,  -292,   616,   625,   622,   624,
    -292,   626,   627,  -292,   628,   629,  -292,  -292,   631,   630,
     632,   634,   635,   636,   637,  -292,   197,  -292,   638,   199,
    -292,   201,   204,   639,   640,   641,   642,   643,   646,   651,
     652,   653,   654,   648,   623,   633,   655,   656,   657,    12,
     658,    13,   659,    14,   660,   661,   594,   649,   662,   666,
      19,   663,   669,   670,    20,   664,   673,   674,   665,   610,
     678,   675,   676,   677,   679,   680,   683,   682,   684,   687,
     685,   690,   688,   691,   689,   694,   650,   693,   695,   686,
     692,   696,   697,   698,   700,   701,   671,   702,   699,   703,
     704,   711,   712,   707,   714,   715,   710,   717,   718,   206,
     713,   719,  -292,  -292,   716,   721,   723,   720,  -292,   722,
     724,   725,   726,   727,   729,   730,   731,  -292,  -292,  -292,
    -292,  -292,   733,  -292,  -292,   734,  -292,   735,  -292,   208,
    -292,   736,   732,   737,   738,   739,   742,   740,   741,   743,
     744,   745,   749,   746,   728,   752,   753,   750,   748,   754,
     755,   751,   757,   756,   758,   762,   760,   765,   759,   767,
     763,   761,   770,   771,   768,   764,   161,   165,   774,   705,
     706,   775,   776,   777,   778,   769,   783,   779,   773,   784,
     780,   781,   785,   787,   786,   788,   790,   789,   792,  -292,
    -292,  -292,   793,   210,  -292,   794,   212,  -292,   797,   214,
    -292,   216,   791,   799,  -292,   800,   218,  -292,  -292,   801,
     220,   796,   798,   802,   803,  -292,   804,   805,  -292,  -292,
    -292,  -292,   222,   806,   807,   813,   808,   815,   810,   224,
     811,   817,   226,   812,   820,   814,   795,   821,    59,   816,
     822,    72,   818,   823,    96,   825,   824,   829,   826,   827,
     828,   121,   830,   831,   122,   832,   833,   836,   837,   839,
     840,   841,   834,   842,   835,   843,   844,   845,   846,   847,
     838,   848,   849,   851,   850,   852,   853,   854,   856,  -292,
     858,   855,   859,  -292,   860,   867,   862,  -292,   863,   870,
    -292,   865,   228,   866,   868,  -292,   869,   872,   871,  -292,
     873,   876,  -292,  -292,  -292,  -292,  -292,  -292,  -292,   874,
    -292,   875,   878,  -292,   881,  -292,  -292,   883,   884,   885,
    -292,   886,   887,   882,   230,   888,   889,   890,   891,   892,
     893,   894,   896,   895,   897,   899,   903,   904,   905,   906,
     898,   907,   908,   909,   910,   879,   901,   911,   912,   913,
     914,   915,   916,   917,   923,   918,  -292,  -292,   928,  -292,
    -292,   929,  -292,  -292,   930,  -292,  -292,   232,   924,  -292,
    -292,   932,  -292,  -292,   933,  -292,   934,   900,   931,   935,
     936,   937,   938,   939,   940,  -292,   941,   942,   943,   944,
     945,   919,   946,   947,   948,   949,   953,   957,   950,   951,
     960,   954,   955,   956,   959,   961,   962,   963,  -292,   964,
     234,   965,   966,   973,  -292,  -292,   968,   969,  -292,   970,
     971,   977,   979,   978,   980,   981,   982,   983,   986,   985,
     987,   984,   988,   989,   990,   972,   991,   992,  -292,  -292,
    -292,  -292,  -292,   236,  -292,  -292,   238,  -292,  -292,  -292,
     993,   996,   994,   995,   920,   997,   998,   999,  1000,  1002,
    -292,  1001,  -292,  1004,  1005,  1008,  -292,  1009,  1010,  1003,
    1007,  -292,  -292,  1011,  1015,  1014,  1012,  -292,  1013,  1016,
    1018,  1017,  1019,  1020,  1021,  1024,  -292
};

/* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
   Performed when YYTABLE does not specify something else to do.  Zero
   means the default is an error.  */
static const yytype_int16 yydefact[] =
{
       3,     0,     0,     1,     0,     0,     9,     4,     5,     8,
      11,    67,    68,     2,     0,     0,     0,    80,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    59,     7,    48,
      49,    50,    51,    52,    53,    54,    55,    56,    57,     6,
       0,    58,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    10,
      12,    13,    14,    15,    16,    17,    18,    19,    20,    21,
      22,    23,    24,    25,    26,    27,   254,    69,     0,    71,
      81,    77,    78,     0,     0,     0,     0,     0,     0,    64,
      65,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    70,
       0,     0,   262,     0,     0,     0,     0,     0,     0,     0,
       0,   257,   258,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   255,    74,    72,    73,    66,     0,     0,     0,
       0,     0,     0,   137,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   136,    79,     0,    83,
      84,    85,    86,    87,    88,    89,    97,    98,   105,    90,
      91,    92,    93,    94,    95,    96,    99,   100,   101,   102,
     103,   104,   106,   107,   108,   109,   110,   111,   112,   113,
     114,   115,   116,   117,   118,   119,   120,   121,   122,   123,
     124,   126,   125,   127,   128,   129,   130,   131,   132,   133,
     134,   135,     0,     0,     0,     0,     0,     0,    34,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    76,    75,    62,    60,    61,    63,   264,
     265,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   195,   196,     0,   198,     0,
       0,     0,     0,     0,     0,   207,     0,     0,     0,   213,
       0,   215,     0,     0,     0,   225,     0,     0,   230,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    28,    29,
      30,    31,    32,    33,    37,    38,    39,    40,    41,    42,
      35,    36,     0,    43,     0,    45,    47,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   259,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   233,     0,
     256,     0,     0,   263,     0,     0,   142,     0,     0,     0,
     204,     0,     0,     0,     0,   188,     0,   190,     0,     0,
     197,     0,   199,     0,   201,   202,   203,     0,     0,     0,
     206,     0,     0,     0,     0,     0,     0,   223,     0,     0,
       0,     0,   231,     0,   240,     0,     0,   248,     0,     0,
     253,   208,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   260,   261,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    44,    46,     0,
       0,   143,     0,     0,   149,     0,     0,   161,     0,     0,
       0,     0,     0,     0,     0,   155,     0,     0,     0,     0,
     167,     0,     0,   205,     0,     0,   214,   219,     0,     0,
       0,     0,     0,     0,     0,   232,     0,   239,     0,     0,
     247,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   187,   189,     0,     0,     0,     0,   200,     0,
       0,     0,     0,     0,     0,     0,     0,   226,   228,   229,
     227,   244,     0,   238,   242,     0,   246,     0,   252,     0,
     140,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   139,
     138,   144,     0,     0,   150,     0,     0,   162,     0,     0,
     178,     0,     0,     0,   156,     0,     0,   194,   168,     0,
       0,     0,     0,     0,     0,   220,     0,     0,   243,   241,
     245,   251,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   146,
       0,     0,     0,   152,     0,     0,     0,   164,     0,     0,
     179,     0,     0,     0,     0,   158,     0,     0,     0,   170,
       0,     0,   209,   210,   211,   212,   222,   224,   250,     0,
     141,     0,     0,   192,     0,   193,   216,     0,     0,     0,
     237,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   148,   147,     0,   154,
     153,     0,   166,   165,     0,   180,   181,     0,     0,   160,
     159,     0,   172,   171,     0,   249,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   235,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   182,     0,
       0,     0,     0,     0,   177,   191,     0,     0,   221,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   145,   151,
     163,   183,   184,     0,   157,   169,     0,   217,   218,   236,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     185,     0,   174,     0,     0,     0,   234,     0,     0,     0,
       0,   186,   175,     0,     0,     0,     0,   173,     0,     0,
       0,     0,     0,     0,     0,     0,   176
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
     360,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,  -292,
    -291,   312,  -101,  -292,  -292,  -292,  -292
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
       0,     1,     2,    13,     7,     8,    14,    60,    61,    62,
      63,    64,    65,    66,    67,    68,    69,    70,    71,    72,
      73,    74,    75,    28,    29,    30,    31,    32,    33,    34,
       9,    12,    16,   111,    36,    37,    38,    39,    40,   120,
     199,   200,   201,   202,   203,   204,   205,   206,   207,   208,
     209,   210,   211,   212,   213,   214,   215,   216,   217,   218,
     219,   220,   221,   222,   223,   224,   225,   226,   227,   228,
     229,   230,   231,   232,   233,   234,   235,   236,   237,   238,
     239,   240,   241,   242,   243,   244,   245,   246,   247,   248,
      78,   123,   373,    41,   249,   250,   251
};

/* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule whose
   number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
     358,   360,     3,     4,   121,   119,   363,    83,   365,   -82,
     -82,   -82,   370,   371,    84,   374,   582,   258,   634,   296,
     635,   259,   297,   585,   372,   -82,   -82,   583,   383,   -82,
     -82,   -82,   -82,   -82,   586,   109,   110,   -82,   -82,   -82,
     -82,   -82,   588,    10,   -82,   -82,   -82,   -82,   -82,   -82,
     -82,   -82,   596,   589,   -82,   -82,   -82,   -82,   -82,   -82,
     636,    76,   -82,   597,   -82,     5,   -82,   -82,   -82,   122,
     357,   143,   144,    11,   -82,   -82,   601,   -82,   -82,   -82,
     -82,   -82,     6,    80,   -82,   145,   -82,   602,   -82,   146,
     690,   693,   696,   -82,   154,   155,   156,   704,   709,   113,
     114,   691,   694,   697,    76,   137,    79,   138,   705,   710,
     157,   158,    76,   359,   159,   160,   161,   162,   163,   471,
      15,   364,   164,   165,   166,   167,   168,    81,   472,   169,
     170,   171,   172,   173,   174,   175,   176,   880,   489,   177,
     178,   179,   180,   181,   182,   499,   500,   183,   881,   184,
     884,   185,   186,   187,    17,    18,    19,    20,   494,   188,
     189,   885,   190,   191,   192,   193,   194,   495,   516,   195,
      76,   196,    85,   197,   888,    82,    77,   517,   198,    21,
      42,    43,    44,    45,    46,   889,    47,    48,    49,    50,
      51,    52,    53,   389,   390,    22,    23,    24,    86,   896,
     900,   391,   392,    87,    25,    26,   415,   110,   393,   394,
     897,   901,   139,   298,   140,     5,   299,    54,    55,   305,
      56,    57,   306,   611,   612,   309,   395,   396,   310,   397,
      89,   318,    27,    58,   319,   505,   508,   506,   509,   811,
      88,   812,   398,   813,    92,   814,   417,   110,   420,   110,
     399,    90,   422,   110,   430,   110,    59,   436,   437,   440,
     110,   442,   443,   444,   445,   528,   529,   530,   531,   532,
     533,   539,   540,   543,   544,   547,   110,   559,   560,   562,
     563,   613,   614,   665,   666,   668,   669,   670,   671,   112,
     672,   673,   755,   756,   774,   775,   837,   838,   840,   841,
     843,   844,   845,   846,   850,   851,   853,   854,   861,   862,
     869,   870,   873,   874,   935,   936,   954,   955,   990,   991,
    1027,  1028,  1053,  1054,  1055,  1056,   487,   488,    91,    93,
     252,    94,    95,    96,    97,    98,    99,   100,   101,   102,
     103,   104,   105,   106,   107,   108,   115,   116,   117,   147,
     148,   118,   149,   125,   126,   127,   128,   129,   130,   131,
     132,   133,   134,   135,   136,   268,   356,     0,   141,   142,
       0,     0,     0,    35,   150,   153,   151,   152,   253,     0,
     254,   255,   256,   257,   260,   261,   262,   263,   264,   265,
     266,   267,   269,   273,   270,   271,   272,   274,   275,   276,
     277,   278,   279,   280,   523,   124,     0,   281,   282,   283,
     284,   285,   286,   287,   288,   289,   290,   291,   292,   293,
     294,   295,   300,   301,   325,   302,   303,   304,   307,   308,
     311,   312,   313,   315,   314,   316,   327,   317,   320,   321,
     322,   323,   324,   326,   328,   404,   329,   330,   331,   332,
     333,   334,   335,   336,   337,   338,   339,   340,   341,   342,
     343,   344,   345,   347,   346,   350,   348,   349,   351,   352,
     353,   354,   355,     0,   361,    76,   366,   367,   368,   380,
     362,   369,   375,   376,   377,   378,   379,   381,   382,   385,
     386,   387,     0,   384,   388,     0,     0,   460,     0,   400,
       0,   401,   402,   403,   405,   406,   407,   413,   408,   409,
     410,   411,   414,   412,   416,   418,   419,   421,   423,   424,
     501,   425,     0,     0,   426,   427,   428,   435,   461,   429,
     431,   432,   433,   434,   441,   438,   439,   446,   447,   524,
     448,   449,   450,   451,   452,   453,   454,   455,   456,   457,
     458,   459,   462,   464,   463,   465,   473,   467,   466,   468,
     469,     0,     0,   470,   475,   474,   477,   478,   480,   493,
     476,   482,   479,   483,   484,   481,   485,   486,   490,   491,
     492,   498,   512,   497,   496,   503,   502,   504,   507,   510,
     511,   513,   514,   515,   518,     0,   522,     0,   519,   520,
       0,   535,   536,   525,   521,   526,   527,   534,   537,   538,
     541,   542,   545,   546,   552,   592,     0,   553,     0,   548,
     549,   550,   551,   558,     0,   554,   555,   556,   557,   576,
       0,   561,   564,   565,   566,   567,   568,   569,   570,   571,
     572,   573,   574,   575,   591,   577,   578,   579,   580,   593,
       0,   581,   584,   587,   590,   594,   598,   595,   600,   603,
     604,   605,   599,   609,   606,   607,   608,   610,   615,   617,
     618,   619,   620,   621,   616,   628,   622,   623,   624,   625,
     626,   627,   629,     0,   700,   633,     0,     0,   715,   630,
     631,   632,   640,   637,   638,   639,   641,   642,   643,   644,
     645,   646,   647,   650,   648,   651,   649,   655,   685,   652,
     653,   658,     0,   654,     0,   656,   657,   659,   686,   660,
     661,   662,   663,   664,   667,   674,   679,   675,   676,   677,
     678,   680,   681,   682,   683,   684,   688,   689,   701,   732,
     687,   699,     0,     0,   702,   692,   695,   698,   703,   707,
     706,   711,   708,   712,   713,   714,   716,   717,   718,   719,
     742,   720,   721,   722,   723,   725,   724,   726,   727,   729,
     728,   730,   731,   733,     0,   734,   735,     0,     0,   736,
     740,   741,   743,   816,   817,   744,   737,   738,   739,   745,
     746,   747,   748,   749,   750,   751,   752,   753,   754,   758,
     757,   760,   759,   761,   764,   765,   762,     0,   763,     0,
     789,     0,   777,   766,   767,   768,     0,   769,   770,   771,
     772,   773,   781,   776,   778,   779,   780,   782,   783,   787,
     784,   785,   786,   788,   790,   791,   794,   792,   793,   797,
     801,   796,   795,   798,   800,   802,   803,   822,   799,   804,
     805,   806,   807,   808,   810,   809,   815,   818,   819,   820,
     821,   823,   825,     0,   826,   829,   824,   830,   832,   827,
     833,   828,   835,   836,   839,   831,   834,   842,   847,   848,
     849,   852,   855,     0,   856,   878,     0,   864,   857,   858,
     859,   860,   863,   865,   866,   867,   868,   872,   871,   875,
     876,   877,   891,   879,   883,   887,   882,   890,   886,   892,
     895,     0,   909,   899,   902,   903,   893,   894,   904,   905,
     898,   906,   907,   908,   910,   911,   913,   917,   915,   916,
     912,     0,   914,   920,   924,   927,   919,   918,     0,   921,
       0,   922,   925,   923,   926,   928,   929,   930,   931,   932,
     933,   934,   940,   937,   938,   939,   943,   941,   946,   942,
     944,   947,   945,   948,   949,   950,   951,   952,   976,   953,
     956,   957,     0,   959,   960,     0,   962,   958,   963,   965,
     961,   966,   964,   967,   968,   971,   996,   969,   970,   972,
     973,   977,   975,     0,     0,     0,   974,  1009,  1061,   979,
     980,   978,   982,   983,   981,   985,   984,   986,   987,   988,
     989,   992,   993,   994,   995,   998,   999,   997,  1001,  1002,
    1003,  1004,     0,  1000,     0,     0,  1010,  1008,     0,     0,
       0,     0,  1005,  1006,  1007,  1014,  1013,  1011,  1012,  1015,
    1016,  1017,  1018,  1021,  1019,  1020,  1022,  1023,  1024,  1025,
    1026,  1029,  1030,  1031,  1032,  1033,  1034,  1036,  1035,  1037,
    1038,  1050,  1039,  1040,  1041,  1042,  1043,  1044,     0,  1045,
    1047,  1048,  1049,  1057,  1046,     0,     0,  1060,  1063,  1062,
    1059,  1051,  1052,  1058,  1066,  1069,  1064,  1067,  1070,  1065,
    1068,  1071,  1072,  1073,  1074,  1076,  1077,  1075,  1081,  1083,
    1079,     0,  1078,     0,  1082,  1080,  1086,  1085,     0,     0,
    1084
};

static const yytype_int16 yycheck[] =
{
     291,   292,     0,     3,    13,     1,   297,    78,   299,     5,
       6,     7,    68,    69,    85,   306,    78,    82,    30,    82,
      32,    86,    85,    78,    80,    21,    22,    89,   319,    25,
      26,    27,    28,    29,    89,    86,    87,    33,    34,    35,
      36,    37,    78,    83,    40,    41,    42,    43,    44,    45,
      46,    47,    78,    89,    50,    51,    52,    53,    54,    55,
      72,    80,    58,    89,    60,    65,    62,    63,    64,    78,
      89,    66,    67,    67,    70,    71,    78,    73,    74,    75,
      76,    77,    82,    80,    80,    80,    82,    89,    84,    84,
      78,    78,    78,    89,     5,     6,     7,    78,    78,    78,
      79,    89,    89,    89,    80,    78,    83,    80,    89,    89,
      21,    22,    80,    89,    25,    26,    27,    28,    29,    80,
      85,    89,    33,    34,    35,    36,    37,    82,    89,    40,
      41,    42,    43,    44,    45,    46,    47,    78,   429,    50,
      51,    52,    53,    54,    55,    78,    79,    58,    89,    60,
      78,    62,    63,    64,     4,     5,     6,     7,    80,    70,
      71,    89,    73,    74,    75,    76,    77,    89,    80,    80,
      80,    82,    85,    84,    78,    82,    86,    89,    89,    29,
       8,     9,    10,    11,    12,    89,    14,    15,    16,    17,
      18,    19,    20,    23,    24,    45,    46,    47,    85,    78,
      78,    31,    32,    85,    54,    55,    86,    87,    38,    39,
      89,    89,    78,    82,    80,    65,    85,    45,    46,    82,
      48,    49,    85,    78,    79,    82,    56,    57,    85,    59,
      82,    82,    82,    61,    85,    78,    78,    80,    80,    78,
      85,    80,    72,    78,    85,    80,    86,    87,    86,    87,
      80,    82,    86,    87,    86,    87,    84,    86,    87,    86,
      87,    86,    87,    86,    87,    86,    87,    86,    87,    86,
      87,    86,    87,    86,    87,    86,    87,    86,    87,    86,
      87,    78,    79,    86,    87,    86,    87,    86,    87,    82,
      86,    87,    86,    87,    86,    87,    86,    87,    86,    87,
      86,    87,    86,    87,    86,    87,    86,    87,    86,    87,
      86,    87,    86,    87,    86,    87,    86,    87,    86,    87,
      86,    87,    86,    87,    86,    87,   427,   428,    83,    85,
      87,    85,    85,    85,    85,    85,    85,    85,    85,    85,
      85,    85,    85,    85,    85,    85,    78,    78,    78,    86,
      86,    80,    86,    81,    81,    81,    81,    78,    78,    78,
      78,    78,    78,    78,    78,    87,    89,    -1,    81,    80,
      -1,    -1,    -1,    13,    86,    82,    86,    86,    86,    -1,
      86,    86,    86,    86,    86,    86,    86,    86,    86,    86,
      86,    86,    86,    82,    87,    86,    86,    82,    82,    82,
      82,    82,    82,    82,    90,    93,    -1,    85,    85,    85,
      85,    85,    85,    85,    85,    85,    85,    85,    85,    85,
      85,    82,    85,    85,    88,    85,    85,    85,    85,    85,
      82,    85,    85,    82,    85,    85,    78,    85,    85,    85,
      85,    85,    85,    80,    82,    86,    82,    82,    82,    82,
      82,    82,    82,    82,    82,    82,    82,    82,    82,    78,
      82,    78,    82,    78,    82,    81,    80,    80,    80,    80,
      80,    78,    80,    -1,    80,    80,    80,    78,    78,    81,
      89,    80,    80,    80,    78,    80,    89,    80,    80,    80,
      80,    80,    -1,    89,    81,    -1,    -1,    78,    -1,    87,
      -1,    87,    87,    87,    87,    87,    86,    80,    87,    87,
      87,    86,    80,    87,    80,    87,    80,    80,    87,    86,
      81,    86,    -1,    -1,    86,    85,    85,    80,    78,    87,
      87,    87,    87,    87,    80,    87,    87,    86,    86,    86,
      85,    85,    85,    85,    85,    85,    85,    85,    85,    85,
      82,    80,    78,    80,    82,    80,    87,    80,    82,    80,
      80,    -1,    -1,    82,    82,    87,    82,    80,    82,    78,
      87,    82,    87,    80,    82,    87,    82,    82,    82,    80,
      80,    78,    80,    82,    87,    87,    82,    82,    82,    82,
      82,    80,    80,    80,    80,    -1,    80,    -1,    89,    89,
      -1,    80,    80,    86,    89,    87,    87,    87,    80,    80,
      80,    80,    86,    86,    80,    90,    -1,    80,    -1,    87,
      87,    86,    86,    80,    -1,    87,    87,    87,    86,    88,
      -1,    87,    87,    87,    87,    87,    87,    87,    80,    87,
      80,    80,    80,    87,    87,    82,    82,    80,    80,    90,
      -1,    82,    82,    82,    80,    90,    90,    82,    82,    82,
      80,    80,    90,    90,    82,    82,    87,    78,    82,    82,
      78,    80,    82,    78,    90,    87,    80,    80,    80,    80,
      80,    80,    89,    -1,    90,    80,    -1,    -1,    78,    87,
      87,    87,    80,    87,    87,    87,    87,    80,    87,    80,
      87,    80,    87,    87,    86,    80,    86,    80,    85,    87,
      86,    80,    -1,    87,    -1,    87,    87,    87,    85,    87,
      86,    86,    86,    86,    86,    86,    80,    87,    87,    87,
      87,    80,    80,    80,    80,    87,    80,    80,    89,    89,
      85,    80,    -1,    -1,    82,    87,    87,    87,    82,    80,
      87,    87,    82,    80,    80,    90,    78,    82,    82,    82,
      89,    82,    82,    80,    82,    78,    82,    82,    78,    78,
      82,    82,    78,    80,    -1,    80,    90,    -1,    -1,    87,
      80,    80,    80,    78,    78,    86,    90,    90,    90,    86,
      86,    80,    80,    86,    80,    80,    86,    80,    80,    80,
      87,    80,    86,    80,    80,    80,    86,    -1,    86,    -1,
      82,    -1,    80,    87,    87,    86,    -1,    87,    87,    86,
      86,    86,    80,    87,    87,    87,    87,    87,    87,    80,
      87,    87,    87,    87,    82,    82,    82,    87,    90,    82,
      80,    90,    87,    87,    82,    80,    87,    78,    90,    82,
      87,    90,    82,    82,    90,    87,    82,    82,    82,    82,
      82,    78,    89,    -1,    80,    80,    87,    80,    80,    89,
      80,    90,    80,    80,    80,    89,    87,    80,    87,    80,
      80,    80,    86,    -1,    86,    90,    -1,    80,    86,    86,
      86,    86,    86,    80,    86,    80,    86,    80,    87,    87,
      80,    87,    78,    82,    82,    82,    90,    82,    90,    80,
      82,    -1,    78,    82,    82,    82,    90,    90,    82,    82,
      90,    82,    82,    82,    82,    90,    82,    89,    82,    82,
      87,    -1,    87,    82,    80,    80,    87,    89,    -1,    89,
      -1,    89,    86,    90,    86,    86,    86,    80,    86,    86,
      80,    86,    80,    87,    86,    86,    80,    86,    80,    86,
      86,    80,    87,    80,    80,    80,    80,    80,    89,    87,
      82,    82,    -1,    82,    82,    -1,    82,    87,    82,    82,
      87,    82,    87,    80,    80,    87,    86,    82,    82,    82,
      82,    90,    82,    -1,    -1,    -1,    87,    78,    78,    87,
      87,    90,    87,    87,    90,    82,    89,    89,    80,    80,
      80,    87,    80,    80,    80,    80,    80,    86,    80,    80,
      80,    80,    -1,    86,    -1,    -1,    80,    82,    -1,    -1,
      -1,    -1,    90,    90,    90,    82,    87,    90,    90,    82,
      90,    90,    82,    87,    90,    90,    87,    86,    86,    86,
      86,    86,    86,    80,    86,    86,    86,    80,    87,    80,
      82,    89,    82,    82,    82,    82,    80,    82,    -1,    82,
      82,    82,    82,    80,    90,    -1,    -1,    82,    80,    82,
      86,    90,    90,    87,    82,    80,    87,    86,    80,    89,
      86,    82,    82,    90,    87,    80,    82,    86,    80,    80,
      87,    -1,    90,    -1,    87,    89,    82,    86,    -1,    -1,
      90
};

/* YYSTOS[STATE-NUM] -- The symbol kind of the accessing symbol of
   state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,    92,    93,     0,     3,    65,    82,    95,    96,   121,
      83,    67,   122,    94,    97,    85,   123,     4,     5,     6,
       7,    29,    45,    46,    47,    54,    55,    82,   114,   115,
     116,   117,   118,   119,   120,   121,   125,   126,   127,   128,
     129,   184,     8,     9,    10,    11,    12,    14,    15,    16,
      17,    18,    19,    20,    45,    46,    48,    49,    61,    84,
      98,    99,   100,   101,   102,   103,   104,   105,   106,   107,
     108,   109,   110,   111,   112,   113,    80,    86,   181,    83,
      80,    82,    82,    78,    85,    85,    85,    85,    85,    82,
      82,    83,    85,    85,    85,    85,    85,    85,    85,    85,
      85,    85,    85,    85,    85,    85,    85,    85,    85,    86,
      87,   124,    82,    78,    79,    78,    78,    78,    80,     1,
     130,    13,    78,   182,   182,    81,    81,    81,    81,    78,
      78,    78,    78,    78,    78,    78,    78,    78,    80,    78,
      80,    81,    80,    66,    67,    80,    84,    86,    86,    86,
      86,    86,    86,    82,     5,     6,     7,    21,    22,    25,
      26,    27,    28,    29,    33,    34,    35,    36,    37,    40,
      41,    42,    43,    44,    45,    46,    47,    50,    51,    52,
      53,    54,    55,    58,    60,    62,    63,    64,    70,    71,
      73,    74,    75,    76,    77,    80,    82,    84,    89,   131,
     132,   133,   134,   135,   136,   137,   138,   139,   140,   141,
     142,   143,   144,   145,   146,   147,   148,   149,   150,   151,
     152,   153,   154,   155,   156,   157,   158,   159,   160,   161,
     162,   163,   164,   165,   166,   167,   168,   169,   170,   171,
     172,   173,   174,   175,   176,   177,   178,   179,   180,   185,
     186,   187,    87,    86,    86,    86,    86,    86,    82,    86,
      86,    86,    86,    86,    86,    86,    86,    86,    87,    86,
      87,    86,    86,    82,    82,    82,    82,    82,    82,    82,
      82,    85,    85,    85,    85,    85,    85,    85,    85,    85,
      85,    85,    85,    85,    85,    82,    82,    85,    82,    85,
      85,    85,    85,    85,    85,    82,    85,    85,    85,    82,
      85,    82,    85,    85,    85,    82,    85,    85,    82,    85,
      85,    85,    85,    85,    85,    88,    80,    78,    82,    82,
      82,    82,    82,    82,    82,    82,    82,    82,    82,    82,
      82,    82,    78,    82,    78,    82,    82,    78,    80,    80,
      81,    80,    80,    80,    78,    80,    89,    89,   181,    89,
     181,    80,    89,   181,    89,   181,    80,    78,    78,    80,
      68,    69,    80,   183,   181,    80,    80,    78,    80,    89,
      81,    80,    80,   181,    89,    80,    80,    80,    81,    23,
      24,    31,    32,    38,    39,    56,    57,    59,    72,    80,
      87,    87,    87,    87,    86,    87,    87,    86,    87,    87,
      87,    86,    87,    80,    80,    86,    80,    86,    87,    80,
      86,    80,    86,    87,    86,    86,    86,    85,    85,    87,
      86,    87,    87,    87,    87,    80,    86,    87,    87,    87,
      86,    80,    86,    87,    86,    87,    86,    86,    85,    85,
      85,    85,    85,    85,    85,    85,    85,    85,    82,    80,
      78,    78,    78,    82,    80,    80,    82,    80,    80,    80,
      82,    80,    89,    87,    87,    82,    87,    82,    80,    87,
      82,    87,    82,    80,    82,    82,    82,   183,   183,   181,
      82,    80,    80,    78,    80,    89,    87,    82,    78,    78,
      79,    81,    82,    87,    82,    78,    80,    82,    78,    80,
      82,    82,    80,    80,    80,    80,    80,    89,    80,    89,
      89,    89,    80,    90,    86,    86,    87,    87,    86,    87,
      86,    87,    86,    87,    87,    80,    80,    80,    80,    86,
      87,    80,    80,    86,    87,    86,    86,    86,    87,    87,
      86,    86,    80,    80,    87,    87,    87,    86,    80,    86,
      87,    87,    86,    87,    87,    87,    87,    87,    87,    87,
      80,    87,    80,    80,    80,    87,    88,    82,    82,    80,
      80,    82,    78,    89,    82,    78,    89,    82,    78,    89,
      80,    87,    90,    90,    90,    82,    78,    89,    90,    90,
      82,    78,    89,    82,    80,    80,    82,    82,    87,    90,
      78,    78,    79,    78,    79,    82,    90,    82,    78,    80,
      82,    78,    80,    80,    80,    80,    80,    80,    87,    89,
      87,    87,    87,    80,    30,    32,    72,    87,    87,    87,
      80,    87,    80,    87,    80,    87,    80,    87,    86,    86,
      87,    80,    87,    86,    87,    80,    87,    87,    80,    87,
      87,    86,    86,    86,    86,    86,    87,    86,    86,    87,
      86,    87,    86,    87,    86,    87,    87,    87,    87,    80,
      80,    80,    80,    80,    87,    85,    85,    85,    80,    80,
      78,    89,    87,    78,    89,    87,    78,    89,    87,    80,
      90,    89,    82,    82,    78,    89,    87,    80,    82,    78,
      89,    87,    80,    80,    90,    78,    78,    82,    82,    82,
      82,    82,    80,    82,    82,    78,    82,    78,    82,    78,
      82,    78,    89,    80,    80,    90,    87,    90,    90,    90,
      80,    80,    89,    80,    86,    86,    86,    80,    80,    86,
      80,    80,    86,    80,    80,    86,    87,    87,    80,    86,
      80,    80,    86,    86,    80,    80,    87,    87,    86,    87,
      87,    86,    86,    86,    86,    87,    87,    80,    87,    87,
      87,    80,    87,    87,    87,    87,    87,    80,    87,    82,
      82,    82,    87,    90,    82,    87,    90,    82,    87,    90,
      82,    80,    80,    87,    82,    87,    90,    82,    82,    87,
      90,    78,    80,    78,    80,    82,    78,    78,    82,    82,
      82,    82,    78,    78,    87,    89,    80,    89,    90,    80,
      80,    89,    80,    80,    87,    80,    80,    86,    87,    80,
      86,    87,    80,    86,    87,    86,    87,    87,    80,    80,
      86,    87,    80,    86,    87,    86,    86,    86,    86,    86,
      86,    86,    87,    86,    80,    80,    86,    80,    86,    86,
      87,    87,    80,    86,    87,    87,    80,    87,    90,    82,
      78,    89,    90,    82,    78,    89,    90,    82,    78,    89,
      82,    78,    80,    90,    90,    82,    78,    89,    90,    82,
      78,    89,    82,    82,    82,    82,    82,    82,    82,    78,
      82,    90,    87,    82,    87,    82,    82,    89,    89,    87,
      82,    89,    89,    90,    80,    86,    86,    80,    86,    86,
      80,    86,    86,    80,    86,    86,    87,    87,    86,    86,
      80,    86,    86,    80,    86,    87,    80,    80,    80,    80,
      80,    80,    80,    87,    86,    87,    82,    82,    87,    82,
      82,    87,    82,    82,    87,    82,    82,    80,    80,    82,
      82,    87,    82,    82,    87,    82,    89,    90,    90,    87,
      87,    90,    87,    87,    89,    82,    89,    80,    80,    80,
      86,    87,    87,    80,    80,    80,    86,    86,    80,    80,
      86,    80,    80,    80,    80,    90,    90,    90,    82,    78,
      80,    90,    90,    87,    82,    82,    90,    90,    82,    90,
      90,    87,    87,    86,    86,    86,    86,    86,    87,    86,
      86,    80,    86,    86,    86,    87,    80,    80,    82,    82,
      82,    82,    82,    80,    82,    82,    90,    82,    82,    82,
      89,    90,    90,    86,    87,    86,    87,    80,    87,    86,
      82,    78,    82,    80,    87,    89,    82,    86,    86,    80,
      80,    82,    82,    90,    87,    86,    80,    82,    90,    87,
      89,    80,    87,    80,    90,    86,    82
};

/* YYR1[RULE-NUM] -- Symbol kind of the left-hand side of rule RULE-NUM.  */
static const yytype_uint8 yyr1[] =
{
       0,    91,    92,    93,    93,    94,    94,    94,    95,    95,
      96,    97,    97,    97,    97,    97,    97,    97,    97,    97,
      97,    97,    97,    97,    97,    97,    97,    97,    98,    99,
     100,   101,   101,   102,   102,   103,   104,   105,   106,   107,
     108,   109,   110,   111,   111,   112,   112,   113,   114,   114,
     114,   114,   114,   114,   114,   114,   114,   114,   114,   114,
     115,   116,   117,   118,   119,   120,   121,   122,   123,   123,
     123,   124,   124,   124,   124,   125,   125,   126,   127,   128,
     129,   129,   130,   130,   130,   130,   130,   130,   130,   130,
     130,   130,   130,   130,   130,   130,   130,   130,   130,   130,
     130,   130,   130,   130,   130,   130,   130,   130,   130,   130,
     130,   130,   130,   130,   130,   130,   130,   130,   130,   130,
     130,   130,   130,   130,   130,   130,   130,   130,   130,   130,
     130,   130,   130,   130,   130,   130,   130,   130,   131,   132,
     133,   134,   135,   136,   136,   136,   136,   136,   136,   137,
     137,   137,   137,   137,   137,   138,   138,   138,   138,   138,
     138,   139,   139,   139,   139,   139,   139,   140,   140,   140,
     140,   140,   140,   141,   142,   142,   143,   143,   144,   144,
     144,   144,   144,   144,   145,   145,   145,   146,   146,   147,
     147,   148,   148,   149,   150,   151,   152,   152,   153,   153,
     153,   154,   155,   156,   157,   158,   159,   159,   160,   161,
     161,   162,   162,   163,   163,   164,   165,   165,   166,   167,
     167,   168,   169,   170,   170,   171,   172,   172,   172,   172,
     173,   173,   174,   175,   176,   176,   176,   176,   177,   177,
     177,   177,   177,   178,   178,   179,   179,   179,   179,   179,
     179,   179,   179,   180,   181,   181,   182,   182,   182,   183,
     183,   183,   184,   185,   186,   187
};

/* YYR2[RULE-NUM] -- Number of symbols on the right-hand side of rule RULE-NUM.  */
static const yytype_int8 yyr2[] =
{
       0,     2,     3,     0,     2,     0,     2,     2,     1,     1,
       4,     0,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     5,     5,
       5,     5,     5,     5,     4,     5,     5,     5,     5,     5,
       5,     5,     5,     5,     9,     5,     9,     5,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       5,     5,     5,     5,     2,     2,     6,     1,     0,     2,
       3,     0,     2,     2,     2,     5,     5,     2,     2,     4,
       1,     2,     0,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    11,    11,
       9,    13,     5,     7,    11,    19,    13,    15,    15,     7,
      11,    19,    13,    15,    15,     7,    11,    19,    13,    15,
      15,     7,    11,    19,    13,    15,    15,     7,    11,    19,
      13,    15,    15,    25,    21,    23,    33,    17,    11,    13,
      15,    15,    17,    19,    19,    21,    23,     9,     5,     9,
       5,    17,    13,    13,    11,     2,     2,     5,     2,     5,
       9,     5,     5,     5,     5,     7,     5,     2,     5,    13,
      13,    13,    13,     2,     7,     2,    13,    19,    19,     7,
      11,    17,    13,     5,    13,     2,     9,     9,     9,     9,
       2,     5,     7,     4,    21,    15,    19,    13,     9,     7,
       5,    11,     9,    11,     9,    11,     9,     7,     5,    15,
      13,    11,     9,     5,     1,     3,     5,     1,     1,     1,
       4,     4,     3,     5,     2,     2
};


enum { YYENOMEM = -2 };

#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab
#define YYNOMEM         goto yyexhaustedlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                    \
  do                                                              \
    if (yychar == YYEMPTY)                                        \
      {                                                           \
        yychar = (Token);                                         \
        yylval = (Value);                                         \
        YYPOPSTACK (yylen);                                       \
        yystate = *yyssp;                                         \
        goto yybackup;                                            \
      }                                                           \
    else                                                          \
      {                                                           \
        yyerror (YY_("syntax error: cannot back up")); \
        YYERROR;                                                  \
      }                                                           \
  while (0)

/* Backward compatibility with an undocumented macro.
   Use YYerror or YYUNDEF. */
#define YYERRCODE YYUNDEF


/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)




# define YY_SYMBOL_PRINT(Title, Kind, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Kind, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*-----------------------------------.
| Print this symbol's value on YYO.  |
`-----------------------------------*/

static void
yy_symbol_value_print (FILE *yyo,
                       yysymbol_kind_t yykind, YYSTYPE const * const yyvaluep)
{
  FILE *yyoutput = yyo;
  YY_USE (yyoutput);
  if (!yyvaluep)
    return;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YY_USE (yykind);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/*---------------------------.
| Print this symbol on YYO.  |
`---------------------------*/

static void
yy_symbol_print (FILE *yyo,
                 yysymbol_kind_t yykind, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyo, "%s %s (",
             yykind < YYNTOKENS ? "token" : "nterm", yysymbol_name (yykind));

  yy_symbol_value_print (yyo, yykind, yyvaluep);
  YYFPRINTF (yyo, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yy_state_t *yybottom, yy_state_t *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yy_state_t *yyssp, YYSTYPE *yyvsp,
                 int yyrule)
{
  int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %d):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       YY_ACCESSING_SYMBOL (+yyssp[yyi + 1 - yynrhs]),
                       &yyvsp[(yyi + 1) - (yynrhs)]);
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args) ((void) 0)
# define YY_SYMBOL_PRINT(Title, Kind, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif






/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg,
            yysymbol_kind_t yykind, YYSTYPE *yyvaluep)
{
  YY_USE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yykind, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YY_USE (yykind);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}


/* Lookahead token kind.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;




/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    yy_state_fast_t yystate = 0;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus = 0;

    /* Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* Their size.  */
    YYPTRDIFF_T yystacksize = YYINITDEPTH;

    /* The state stack: array, bottom, top.  */
    yy_state_t yyssa[YYINITDEPTH];
    yy_state_t *yyss = yyssa;
    yy_state_t *yyssp = yyss;

    /* The semantic value stack: array, bottom, top.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs = yyvsa;
    YYSTYPE *yyvsp = yyvs;

  int yyn;
  /* The return value of yyparse.  */
  int yyresult;
  /* Lookahead symbol kind.  */
  yysymbol_kind_t yytoken = YYSYMBOL_YYEMPTY;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;



#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yychar = YYEMPTY; /* Cause a token to be read.  */

  goto yysetstate;


/*------------------------------------------------------------.
| yynewstate -- push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;


/*--------------------------------------------------------------------.
| yysetstate -- set current state (the top of the stack) to yystate.  |
`--------------------------------------------------------------------*/
yysetstate:
  YYDPRINTF ((stderr, "Entering state %d\n", yystate));
  YY_ASSERT (0 <= yystate && yystate < YYNSTATES);
  YY_IGNORE_USELESS_CAST_BEGIN
  *yyssp = YY_CAST (yy_state_t, yystate);
  YY_IGNORE_USELESS_CAST_END
  YY_STACK_PRINT (yyss, yyssp);

  if (yyss + yystacksize - 1 <= yyssp)
#if !defined yyoverflow && !defined YYSTACK_RELOCATE
    YYNOMEM;
#else
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYPTRDIFF_T yysize = yyssp - yyss + 1;

# if defined yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        yy_state_t *yyss1 = yyss;
        YYSTYPE *yyvs1 = yyvs;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * YYSIZEOF (*yyssp),
                    &yyvs1, yysize * YYSIZEOF (*yyvsp),
                    &yystacksize);
        yyss = yyss1;
        yyvs = yyvs1;
      }
# else /* defined YYSTACK_RELOCATE */
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        YYNOMEM;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yy_state_t *yyss1 = yyss;
        union yyalloc *yyptr =
          YY_CAST (union yyalloc *,
                   YYSTACK_ALLOC (YY_CAST (YYSIZE_T, YYSTACK_BYTES (yystacksize))));
        if (! yyptr)
          YYNOMEM;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YY_IGNORE_USELESS_CAST_BEGIN
      YYDPRINTF ((stderr, "Stack size increased to %ld\n",
                  YY_CAST (long, yystacksize)));
      YY_IGNORE_USELESS_CAST_END

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }
#endif /* !defined yyoverflow && !defined YYSTACK_RELOCATE */


  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;


/*-----------.
| yybackup.  |
`-----------*/
yybackup:
  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either empty, or end-of-input, or a valid lookahead.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token\n"));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = YYEOF;
      yytoken = YYSYMBOL_YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else if (yychar == YYerror)
    {
      /* The scanner already issued an error message, process directly
         to error recovery.  But do not keep the error token as
         lookahead, it is too special and may lead us to an endless
         loop in error recovery. */
      yychar = YYUNDEF;
      yytoken = YYSYMBOL_YYerror;
      goto yyerrlab1;
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);
  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  /* Discard the shifted token.  */
  yychar = YYEMPTY;
  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
  case 2: /* diagram: definitions header_statement statement  */
#line 103 "doodle/src/parser.y"
{
  std::string s;
  //- end of parsing. It's time to resolve references
  //- ref can be found in comments, captions, text associated to vertex
  info.set_comment1(expand_ref(info.get_comment1()));
  info.set_comment2(expand_ref(info.get_comment2()));
  info.set_comment3(expand_ref(info.get_comment3()));
  //- For all steps
  for(unsigned int stepId=0; stepId < steps.size(); stepId++) {
    //- Change all captions
    for(step::it_captions itCap = steps[stepId].ref_captions_begin();
	itCap != steps[stepId].ref_captions_end(); ++itCap) {
      *itCap = expand_ref(*itCap);
    }
    //- For all text vertices
    for(step::it_vertices it = steps[stepId].ref_begin_vertices();
      it != steps[stepId].ref_end_vertices(); ++it) {
      if(it->has_text()) {
	s = expand_ref(it->get_text());
	it->clear_text();
	it->add_text(s);
      }
    }
  }
}
#line 1998 "generated/parser.tab.cpp"
    break;

  case 28: /* design_date: DESIGN_DATE '(' a_date ')' ';'  */
#line 169 "doodle/src/parser.y"
{
  info.set_design_date(*(yyvsp[-2].Date));
}
#line 2006 "generated/parser.tab.cpp"
    break;

  case 29: /* diag_date: DIAG_DATE '(' a_date ')' ';'  */
#line 175 "doodle/src/parser.y"
{
  info.set_diagram_date(*(yyvsp[-2].Date));
}
#line 2014 "generated/parser.tab.cpp"
    break;

  case 30: /* designer: DESIGNER '(' STRING ')' ';'  */
#line 181 "doodle/src/parser.y"
{
  info.set_designer(*(yyvsp[-2].String));
}
#line 2022 "generated/parser.tab.cpp"
    break;

  case 31: /* diagrammer: DIAGRAMER '(' STRING ')' ';'  */
#line 187 "doodle/src/parser.y"
{
  yywarning("Syntax changes: use \\diagrammer instead of");
  info.set_diagrammer(*(yyvsp[-2].String));
}
#line 2031 "generated/parser.tab.cpp"
    break;

  case 32: /* diagrammer: DIAGRAMMER '(' STRING ')' ';'  */
#line 192 "doodle/src/parser.y"
{
  info.set_diagrammer(*(yyvsp[-2].String));
}
#line 2039 "generated/parser.tab.cpp"
    break;

  case 33: /* title: TITLE '(' STRING ')' ';'  */
#line 198 "doodle/src/parser.y"
{
  info.set_title(*(yyvsp[-2].String));
}
#line 2047 "generated/parser.tab.cpp"
    break;

  case 34: /* title: TITLE '(' STRING ';'  */
#line 202 "doodle/src/parser.y"
{
  yyerror("Expecting ')' before ';'");
}
#line 2055 "generated/parser.tab.cpp"
    break;

  case 35: /* header_visible_height: VISIBLE_HEIGHT '(' INTEGER ')' ';'  */
#line 208 "doodle/src/parser.y"
{
  visible_height = (yyvsp[-2].ival);
}
#line 2063 "generated/parser.tab.cpp"
    break;

  case 36: /* header_visible_width: VISIBLE_WIDTH '(' INTEGER ')' ';'  */
#line 214 "doodle/src/parser.y"
{
  visible_width = (yyvsp[-2].ival);
}
#line 2071 "generated/parser.tab.cpp"
    break;

  case 37: /* left_margin: _LEFT_MARGIN '(' INTEGER ')' ';'  */
#line 220 "doodle/src/parser.y"
{
  info.set_left_margin((yyvsp[-2].ival));
}
#line 2079 "generated/parser.tab.cpp"
    break;

  case 38: /* right_margin: _RIGHT_MARGIN '(' INTEGER ')' ';'  */
#line 226 "doodle/src/parser.y"
{
  info.set_right_margin((yyvsp[-2].ival));
}
#line 2087 "generated/parser.tab.cpp"
    break;

  case 39: /* top_margin: _TOP_MARGIN '(' INTEGER ')' ';'  */
#line 232 "doodle/src/parser.y"
{
  info.set_top_margin((yyvsp[-2].ival));
}
#line 2095 "generated/parser.tab.cpp"
    break;

  case 40: /* bottom_margin: _BOTTOM_MARGIN '(' INTEGER ')' ';'  */
#line 238 "doodle/src/parser.y"
{
  info.set_bottom_margin((yyvsp[-2].ival));
}
#line 2103 "generated/parser.tab.cpp"
    break;

  case 41: /* vspace: _VSPACE '(' INTEGER ')' ';'  */
#line 244 "doodle/src/parser.y"
{
  info.set_vspace((yyvsp[-2].ival));
}
#line 2111 "generated/parser.tab.cpp"
    break;

  case 42: /* hspace: _HSPACE '(' INTEGER ')' ';'  */
#line 250 "doodle/src/parser.y"
{
  info.set_hspace((yyvsp[-2].ival));
}
#line 2119 "generated/parser.tab.cpp"
    break;

  case 43: /* color_front: COLOR_FRONT '(' SYMBOL ')' ';'  */
#line 256 "doodle/src/parser.y"
{
  info.set_front_color(*(yyvsp[-2].String));
  delete (yyvsp[-2].String);
}
#line 2128 "generated/parser.tab.cpp"
    break;

  case 44: /* color_front: COLOR_FRONT '(' INTEGER ',' INTEGER ',' INTEGER ')' ';'  */
#line 261 "doodle/src/parser.y"
{
  info.set_front_color((yyvsp[-6].ival), (yyvsp[-4].ival), (yyvsp[-2].ival));
}
#line 2136 "generated/parser.tab.cpp"
    break;

  case 45: /* color_back: COLOR_BACK '(' SYMBOL ')' ';'  */
#line 267 "doodle/src/parser.y"
{
  info.set_back_color(*(yyvsp[-2].String));
  delete (yyvsp[-2].String);

}
#line 2146 "generated/parser.tab.cpp"
    break;

  case 46: /* color_back: COLOR_BACK '(' INTEGER ',' INTEGER ',' INTEGER ')' ';'  */
#line 273 "doodle/src/parser.y"
{
  info.set_back_color((yyvsp[-6].ival), (yyvsp[-4].ival), (yyvsp[-2].ival) );
}
#line 2154 "generated/parser.tab.cpp"
    break;

  case 47: /* comment: COMMENT '(' STRING ')' ';'  */
#line 279 "doodle/src/parser.y"
{
  switch(nbComment) {
  case 0 : info.set_comment1(*(yyvsp[-2].String));
    delete (yyvsp[-2].String); break;
  case 1 : info.set_comment2(*(yyvsp[-2].String));
    delete (yyvsp[-2].String); break;
  case 2 : info.set_comment3(*(yyvsp[-2].String));
    delete (yyvsp[-2].String); break;
  default : yywarning("Only 3 comment lines are allowed.");
  }
  nbComment++;
}
#line 2171 "generated/parser.tab.cpp"
    break;

  case 60: /* visible_height_inter: VISIBLE_HEIGHT '(' INTEGER ')' ';'  */
#line 311 "doodle/src/parser.y"
{
  visible_height = (yyvsp[-2].ival);
}
#line 2179 "generated/parser.tab.cpp"
    break;

  case 61: /* visible_width_inter: VISIBLE_WIDTH '(' INTEGER ')' ';'  */
#line 317 "doodle/src/parser.y"
{
  visible_width = (yyvsp[-2].ival);
}
#line 2187 "generated/parser.tab.cpp"
    break;

  case 62: /* scale_inter: SCALE '(' INTEGER ')' ';'  */
#line 323 "doodle/src/parser.y"
{
  if((yyvsp[-2].ival) < 1) yyerror("Wrong scale factor, it should be greater than 1");
  scale = (yyvsp[-2].ival);
}
#line 2196 "generated/parser.tab.cpp"
    break;

  case 63: /* visible_center_inter: VISIBLE_CENTER '(' SYMBOL ')' ';'  */
#line 330 "doodle/src/parser.y"
{
  read_visible_center_inter(*(yyvsp[-2].String));
  delete (yyvsp[-2].String);
}
#line 2205 "generated/parser.tab.cpp"
    break;

  case 64: /* clip_inter: CLIP ';'  */
#line 337 "doodle/src/parser.y"
{
  if(verbose) {
    std::cout << "Before step #" << current_index << " : clipping state : ON" << std::endl;
  }
  clip = true;
}
#line 2216 "generated/parser.tab.cpp"
    break;

  case 65: /* unclip_inter: UNCLIP ';'  */
#line 346 "doodle/src/parser.y"
{
  if(verbose) {
    std::cout << "Before step #" << current_index << " : clipping state : OFF" << std::endl;
  }
  clip = false;
}
#line 2227 "generated/parser.tab.cpp"
    break;

  case 66: /* macro_def: MACRO macro_ope macro_param '{' macro_part '}'  */
#line 355 "doodle/src/parser.y"
{
  if(verbose) {
    std::cout << "macro : " << current_macro->first << std::endl;
  }
}
#line 2237 "generated/parser.tab.cpp"
    break;

  case 67: /* macro_ope: OPERATOR  */
#line 363 "doodle/src/parser.y"
{
  // *$1 const std::string& nom de la marco
  std::pair<macromap::iterator, bool> p = macros.insert(
	macromap::value_type(*(yyvsp[0].String),macro())
  );
  if (!p.second) {
	yyerror("macro already exists. Could be extended in a next version...");
	current_macro = macros.end();
  }
  else {
	current_macro  = p.first;
  }
  delete (yyvsp[0].String);
}
#line 2256 "generated/parser.tab.cpp"
    break;

  case 70: /* macro_param: '(' symbol_list ')'  */
#line 382 "doodle/src/parser.y"
{
  // *$2 const std::vector<std::string>& vertices
  if (current_macro != macros.end())
	current_macro->second.set(*(yyvsp[-1].List));
  delete (yyvsp[-1].List);
}
#line 2267 "generated/parser.tab.cpp"
    break;

  case 72: /* macro_part: macro_part OPERATOR  */
#line 392 "doodle/src/parser.y"
{
 if (current_macro != macros.end())
	current_macro->second.add(*(yyvsp[0].String));
  delete (yyvsp[0].String);
}
#line 2277 "generated/parser.tab.cpp"
    break;

  case 73: /* macro_part: macro_part SYMBOL  */
#line 398 "doodle/src/parser.y"
{
  if (current_macro != macros.end())
	current_macro->second.addsymb(*(yyvsp[0].String));
  delete (yyvsp[0].String);
}
#line 2287 "generated/parser.tab.cpp"
    break;

  case 74: /* macro_part: macro_part MACROTEXT  */
#line 404 "doodle/src/parser.y"
{
  if (current_macro != macros.end())
	current_macro->second.add((yyvsp[0].ival));
}
#line 2296 "generated/parser.tab.cpp"
    break;

  case 75: /* rotate_inter: ROTATE '(' FLOAT ')' ';'  */
#line 411 "doodle/src/parser.y"
{
  if(current_step != 0) read_rotate((yyvsp[-2].fval));
  else {
    yywarning("operator \\rotate is skipped (forbidden before first step)");
  }
}
#line 2307 "generated/parser.tab.cpp"
    break;

  case 76: /* rotate_inter: ROTATE '(' INTEGER ')' ';'  */
#line 418 "doodle/src/parser.y"
{
  if(current_step != 0) read_rotate((double)(yyvsp[-2].ival));
  else {
    yywarning("operator \\rotate is skipped (forbidden before first step)");
  }
}
#line 2318 "generated/parser.tab.cpp"
    break;

  case 77: /* turn_over_vertical_inter: TURN_VERTICAL ';'  */
#line 427 "doodle/src/parser.y"
{
  read_turn_over(true);
}
#line 2326 "generated/parser.tab.cpp"
    break;

  case 78: /* turn_over_horizontal_inter: TURN_HORIZONTAL ';'  */
#line 433 "doodle/src/parser.y"
{
  read_turn_over(false);  
}
#line 2334 "generated/parser.tab.cpp"
    break;

  case 79: /* step_statement: begin_step '{' instruction_list '}'  */
#line 440 "doodle/src/parser.y"
{
  if(!steps[current_step].get_captions_number()) {
    steps[current_step].add_caption("");
  }
  //- update dx dy according to local scale factor 
  steps[current_step].update_dx_dy(scale);
  current_step++; //- index for steps array
  if(!is_sub_step) current_index++; //- index of current step in diagram
}
#line 2348 "generated/parser.tab.cpp"
    break;

  case 80: /* begin_step: STEP  */
#line 453 "doodle/src/parser.y"
{
  //- adding a new step filled with current symbols and lines from others steps
  read_new_step();
}
#line 2357 "generated/parser.tab.cpp"
    break;

  case 81: /* begin_step: STEP SYMBOL  */
#line 458 "doodle/src/parser.y"
{
  read_new_step();
}
#line 2365 "generated/parser.tab.cpp"
    break;

  case 137: /* instruction_list: error ';'  */
#line 519 "doodle/src/parser.y"
{
  yyerror("wrong instruction (perhaps a ; is missing)");
  YYABORT;
}
#line 2374 "generated/parser.tab.cpp"
    break;

  case 138: /* diamond_inst: DIAMOND '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 526 "doodle/src/parser.y"
{
  read_diamond(*(yyvsp[-8].String),*(yyvsp[-6].String),*(yyvsp[-4].String),*(yyvsp[-2].String));
  delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2383 "generated/parser.tab.cpp"
    break;

  case 139: /* square_inst: SQUARE '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 533 "doodle/src/parser.y"
{
  read_square(*(yyvsp[-8].String),*(yyvsp[-6].String),*(yyvsp[-4].String),*(yyvsp[-2].String)); 
  delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2392 "generated/parser.tab.cpp"
    break;

  case 140: /* middle_inst: SYMBOL '=' MIDDLE '(' SYMBOL ',' SYMBOL ')' ';'  */
#line 540 "doodle/src/parser.y"
{
  read_fraction(*(yyvsp[-8].String), *(yyvsp[-4].String), *(yyvsp[-2].String), 1, 2);
  delete (yyvsp[-8].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2401 "generated/parser.tab.cpp"
    break;

  case 141: /* fract_inst: SYMBOL '=' FRACT '(' SYMBOL ',' SYMBOL ',' INTEGER ',' INTEGER ')' ';'  */
#line 547 "doodle/src/parser.y"
{
  read_fraction(*(yyvsp[-12].String), *(yyvsp[-8].String), *(yyvsp[-6].String), (yyvsp[-4].ival), (yyvsp[-2].ival));
  delete (yyvsp[-12].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String);
}
#line 2410 "generated/parser.tab.cpp"
    break;

  case 142: /* caption_inst: CAPTION '(' STRING ')' ';'  */
#line 554 "doodle/src/parser.y"
{
  read_caption(*(yyvsp[-2].String));
  delete (yyvsp[-2].String);
}
#line 2419 "generated/parser.tab.cpp"
    break;

  case 143: /* valley_fold_inst: VALLEY_FOLD '(' SYMBOL ',' SYMBOL ')' ';'  */
#line 561 "doodle/src/parser.y"
{
  read_fold_percent(*(yyvsp[-4].String), *(yyvsp[-2].String), edgeValley, 0, 0);
  delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2428 "generated/parser.tab.cpp"
    break;

  case 144: /* valley_fold_inst: VALLEY_FOLD '(' SYMBOL ',' SYMBOL ',' INTEGER ',' INTEGER ')' ';'  */
#line 566 "doodle/src/parser.y"
{
  read_fold_percent(*(yyvsp[-8].String), *(yyvsp[-6].String), edgeValley, (yyvsp[-4].ival), (yyvsp[-2].ival));
  delete (yyvsp[-8].String); delete (yyvsp[-6].String);
}
#line 2437 "generated/parser.tab.cpp"
    break;

  case 145: /* valley_fold_inst: VALLEY_FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 571 "doodle/src/parser.y"
{
  read_fold_limit(*(yyvsp[-16].String), *(yyvsp[-14].String), edgeValley, *(yyvsp[-11].String), *(yyvsp[-9].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-16].String); delete (yyvsp[-14].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2446 "generated/parser.tab.cpp"
    break;

  case 146: /* valley_fold_inst: VALLEY_FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 576 "doodle/src/parser.y"
{
  read_fold_limit(*(yyvsp[-10].String), *(yyvsp[-8].String), edgeValley, *(yyvsp[-5].String), *(yyvsp[-3].String), "", "");
  delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2455 "generated/parser.tab.cpp"
    break;

  case 147: /* valley_fold_inst: VALLEY_FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' INTEGER ')' ';'  */
#line 581 "doodle/src/parser.y"
{
  read_fold_both(*(yyvsp[-12].String), *(yyvsp[-10].String), edgeValley, (yyvsp[-2].ival), *(yyvsp[-7].String), *(yyvsp[-5].String), true);
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-7].String); delete (yyvsp[-5].String);
}
#line 2464 "generated/parser.tab.cpp"
    break;

  case 148: /* valley_fold_inst: VALLEY_FOLD '(' SYMBOL ',' SYMBOL ',' INTEGER ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 586 "doodle/src/parser.y"
{
  read_fold_both(*(yyvsp[-12].String), *(yyvsp[-10].String), edgeValley, (yyvsp[-8].ival), *(yyvsp[-5].String), *(yyvsp[-3].String), false);
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2473 "generated/parser.tab.cpp"
    break;

  case 149: /* mountain_fold_inst: MOUNTAIN_FOLD '(' SYMBOL ',' SYMBOL ')' ';'  */
#line 593 "doodle/src/parser.y"
{
  read_fold_percent(*(yyvsp[-4].String), *(yyvsp[-2].String), edgeMountain, 0, 0);
  delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2482 "generated/parser.tab.cpp"
    break;

  case 150: /* mountain_fold_inst: MOUNTAIN_FOLD '(' SYMBOL ',' SYMBOL ',' INTEGER ',' INTEGER ')' ';'  */
#line 598 "doodle/src/parser.y"
{
  read_fold_percent(*(yyvsp[-8].String), *(yyvsp[-6].String), edgeMountain, (yyvsp[-4].ival), (yyvsp[-2].ival));
  delete (yyvsp[-8].String); delete (yyvsp[-6].String);
}
#line 2491 "generated/parser.tab.cpp"
    break;

  case 151: /* mountain_fold_inst: MOUNTAIN_FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 603 "doodle/src/parser.y"
{
  read_fold_limit(*(yyvsp[-16].String), *(yyvsp[-14].String), edgeMountain, *(yyvsp[-11].String), *(yyvsp[-9].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-16].String); delete (yyvsp[-14].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2500 "generated/parser.tab.cpp"
    break;

  case 152: /* mountain_fold_inst: MOUNTAIN_FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 608 "doodle/src/parser.y"
{
  read_fold_limit(*(yyvsp[-10].String), *(yyvsp[-8].String), edgeMountain, *(yyvsp[-5].String), *(yyvsp[-3].String), "", "");
  delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2509 "generated/parser.tab.cpp"
    break;

  case 153: /* mountain_fold_inst: MOUNTAIN_FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' INTEGER ')' ';'  */
#line 613 "doodle/src/parser.y"
{
  read_fold_both(*(yyvsp[-12].String), *(yyvsp[-10].String), edgeMountain, (yyvsp[-2].ival), *(yyvsp[-7].String), *(yyvsp[-5].String), true);
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-7].String); delete (yyvsp[-5].String);
}
#line 2518 "generated/parser.tab.cpp"
    break;

  case 154: /* mountain_fold_inst: MOUNTAIN_FOLD '(' SYMBOL ',' SYMBOL ',' INTEGER ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 618 "doodle/src/parser.y"
{
  read_fold_both(*(yyvsp[-12].String), *(yyvsp[-10].String), edgeMountain, (yyvsp[-8].ival), *(yyvsp[-5].String), *(yyvsp[-3].String), false);
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2527 "generated/parser.tab.cpp"
    break;

  case 155: /* border_inst: BORDER '(' SYMBOL ',' SYMBOL ')' ';'  */
#line 625 "doodle/src/parser.y"
{
  read_fold_percent(*(yyvsp[-4].String), *(yyvsp[-2].String), edgeBorder, 0, 0);
  delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2536 "generated/parser.tab.cpp"
    break;

  case 156: /* border_inst: BORDER '(' SYMBOL ',' SYMBOL ',' INTEGER ',' INTEGER ')' ';'  */
#line 630 "doodle/src/parser.y"
{
  read_fold_percent(*(yyvsp[-8].String), *(yyvsp[-6].String), edgeBorder, (yyvsp[-4].ival), (yyvsp[-2].ival));
  delete (yyvsp[-8].String); delete (yyvsp[-6].String);
}
#line 2545 "generated/parser.tab.cpp"
    break;

  case 157: /* border_inst: BORDER '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 635 "doodle/src/parser.y"
{
  read_fold_limit(*(yyvsp[-16].String), *(yyvsp[-14].String), edgeBorder, *(yyvsp[-11].String), *(yyvsp[-9].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-16].String); delete (yyvsp[-14].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2554 "generated/parser.tab.cpp"
    break;

  case 158: /* border_inst: BORDER '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 640 "doodle/src/parser.y"
{
  read_fold_limit(*(yyvsp[-10].String), *(yyvsp[-8].String), edgeBorder, *(yyvsp[-5].String), *(yyvsp[-3].String), "", "");
  delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2563 "generated/parser.tab.cpp"
    break;

  case 159: /* border_inst: BORDER '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' INTEGER ')' ';'  */
#line 645 "doodle/src/parser.y"
{
  read_fold_both(*(yyvsp[-12].String), *(yyvsp[-10].String), edgeBorder, (yyvsp[-2].ival), *(yyvsp[-7].String), *(yyvsp[-5].String), true);
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-7].String); delete (yyvsp[-5].String);
}
#line 2572 "generated/parser.tab.cpp"
    break;

  case 160: /* border_inst: BORDER '(' SYMBOL ',' SYMBOL ',' INTEGER ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 650 "doodle/src/parser.y"
{
  read_fold_both(*(yyvsp[-12].String), *(yyvsp[-10].String), edgeBorder, (yyvsp[-8].ival), *(yyvsp[-5].String), *(yyvsp[-3].String), false);
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2581 "generated/parser.tab.cpp"
    break;

  case 161: /* fold_inst: FOLD '(' SYMBOL ',' SYMBOL ')' ';'  */
#line 657 "doodle/src/parser.y"
{
  read_fold_percent(*(yyvsp[-4].String), *(yyvsp[-2].String), edgeFold, FOLDSPC, FOLDSPC);
  delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2590 "generated/parser.tab.cpp"
    break;

  case 162: /* fold_inst: FOLD '(' SYMBOL ',' SYMBOL ',' INTEGER ',' INTEGER ')' ';'  */
#line 662 "doodle/src/parser.y"
{
  read_fold_percent(*(yyvsp[-8].String), *(yyvsp[-6].String), edgeFold, (yyvsp[-4].ival), (yyvsp[-2].ival));
  delete (yyvsp[-8].String); delete (yyvsp[-6].String);
}
#line 2599 "generated/parser.tab.cpp"
    break;

  case 163: /* fold_inst: FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 667 "doodle/src/parser.y"
{
  read_fold_limit(*(yyvsp[-16].String), *(yyvsp[-14].String), edgeFold, *(yyvsp[-11].String), *(yyvsp[-9].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-16].String); delete (yyvsp[-14].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2608 "generated/parser.tab.cpp"
    break;

  case 164: /* fold_inst: FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 672 "doodle/src/parser.y"
{
  read_fold_limit(*(yyvsp[-10].String), *(yyvsp[-8].String), edgeFold, *(yyvsp[-5].String), *(yyvsp[-3].String), "", "");
  delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2617 "generated/parser.tab.cpp"
    break;

  case 165: /* fold_inst: FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' INTEGER ')' ';'  */
#line 677 "doodle/src/parser.y"
{
  read_fold_both(*(yyvsp[-12].String), *(yyvsp[-10].String), edgeFold, (yyvsp[-2].ival), *(yyvsp[-7].String), *(yyvsp[-5].String), true);
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-7].String); delete (yyvsp[-5].String);
}
#line 2626 "generated/parser.tab.cpp"
    break;

  case 166: /* fold_inst: FOLD '(' SYMBOL ',' SYMBOL ',' INTEGER ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 682 "doodle/src/parser.y"
{
  read_fold_both(*(yyvsp[-12].String), *(yyvsp[-10].String), edgeFold, (yyvsp[-8].ival), *(yyvsp[-5].String), *(yyvsp[-3].String), false);
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2635 "generated/parser.tab.cpp"
    break;

  case 167: /* xray_fold_inst: XRAY_FOLD '(' SYMBOL ',' SYMBOL ')' ';'  */
#line 689 "doodle/src/parser.y"
{
  read_fold_percent(*(yyvsp[-4].String), *(yyvsp[-2].String), edgeXray, 0, 0);
  delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2644 "generated/parser.tab.cpp"
    break;

  case 168: /* xray_fold_inst: XRAY_FOLD '(' SYMBOL ',' SYMBOL ',' INTEGER ',' INTEGER ')' ';'  */
#line 694 "doodle/src/parser.y"
{
  read_fold_percent(*(yyvsp[-8].String), *(yyvsp[-6].String), edgeXray, (yyvsp[-4].ival), (yyvsp[-2].ival));
  delete (yyvsp[-8].String); delete (yyvsp[-6].String);
}
#line 2653 "generated/parser.tab.cpp"
    break;

  case 169: /* xray_fold_inst: XRAY_FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 699 "doodle/src/parser.y"
{
  read_fold_limit(*(yyvsp[-16].String), *(yyvsp[-14].String), edgeXray, *(yyvsp[-11].String), *(yyvsp[-9].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-16].String); delete (yyvsp[-14].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2662 "generated/parser.tab.cpp"
    break;

  case 170: /* xray_fold_inst: XRAY_FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 704 "doodle/src/parser.y"
{
  read_fold_limit(*(yyvsp[-10].String), *(yyvsp[-8].String), edgeXray, *(yyvsp[-5].String), *(yyvsp[-3].String), "", "");
  delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2671 "generated/parser.tab.cpp"
    break;

  case 171: /* xray_fold_inst: XRAY_FOLD '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' INTEGER ')' ';'  */
#line 709 "doodle/src/parser.y"
{
  read_fold_both(*(yyvsp[-12].String), *(yyvsp[-10].String), edgeXray, (yyvsp[-2].ival), *(yyvsp[-7].String), *(yyvsp[-5].String), true);
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-7].String); delete (yyvsp[-5].String);
}
#line 2680 "generated/parser.tab.cpp"
    break;

  case 172: /* xray_fold_inst: XRAY_FOLD '(' SYMBOL ',' SYMBOL ',' INTEGER ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 714 "doodle/src/parser.y"
{
  read_fold_both(*(yyvsp[-12].String), *(yyvsp[-10].String), edgeXray, (yyvsp[-8].ival), *(yyvsp[-5].String), *(yyvsp[-3].String), false);
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2689 "generated/parser.tab.cpp"
    break;

  case 173: /* point_to_point_inst: '[' SYMBOL ',' SYMBOL ']' '=' POINT_TO_POINT '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 723 "doodle/src/parser.y"
{
  read_point_to_point(*(yyvsp[-23].String), *(yyvsp[-21].String), *(yyvsp[-16].String), *(yyvsp[-14].String), *(yyvsp[-11].String), *(yyvsp[-9].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-23].String); delete (yyvsp[-21].String); delete (yyvsp[-16].String); delete (yyvsp[-14].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String);
  delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2699 "generated/parser.tab.cpp"
    break;

  case 174: /* point_to_line_inst: SYMBOL '=' POINT_TO_LINE '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 733 "doodle/src/parser.y"
{
  read_point_to_line(*(yyvsp[-20].String), std::string("first"), *(yyvsp[-16].String), *(yyvsp[-14].String), *(yyvsp[-11].String), *(yyvsp[-9].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-20].String); delete (yyvsp[-16].String); delete (yyvsp[-14].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String);
  delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2709 "generated/parser.tab.cpp"
    break;

  case 175: /* point_to_line_inst: SYMBOL '=' POINT_TO_LINE '(' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ')' ';'  */
#line 744 "doodle/src/parser.y"
{
  read_point_to_line(*(yyvsp[-22].String), *(yyvsp[-2].String), *(yyvsp[-18].String), *(yyvsp[-16].String), *(yyvsp[-13].String), *(yyvsp[-11].String), *(yyvsp[-7].String), *(yyvsp[-5].String));
  delete (yyvsp[-22].String); delete (yyvsp[-18].String); delete (yyvsp[-16].String); delete (yyvsp[-13].String); delete (yyvsp[-11].String);
  delete (yyvsp[-7].String); delete (yyvsp[-5].String); delete (yyvsp[-2].String);
}
#line 2719 "generated/parser.tab.cpp"
    break;

  case 176: /* line_to_line_inst: '[' SYMBOL ',' SYMBOL ']' '=' LINE_TO_LINE '(' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 754 "doodle/src/parser.y"
{
  read_line_to_line(*(yyvsp[-31].String), *(yyvsp[-29].String), *(yyvsp[-23].String), *(yyvsp[-21].String), *(yyvsp[-17].String), *(yyvsp[-15].String), *(yyvsp[-11].String), *(yyvsp[-9].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-31].String); delete (yyvsp[-29].String); delete (yyvsp[-23].String); delete (yyvsp[-21].String); delete (yyvsp[-17].String); delete (yyvsp[-15].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2728 "generated/parser.tab.cpp"
    break;

  case 177: /* line_to_line_inst: SYMBOL '=' LINE_TO_LINE '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 760 "doodle/src/parser.y"
{
  read_line_to_line(*(yyvsp[-16].String),*(yyvsp[-12].String), *(yyvsp[-10].String), *(yyvsp[-8].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-16].String); delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2737 "generated/parser.tab.cpp"
    break;

  case 178: /* simple_arrow_inst: SIMPLE_ARROW '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 767 "doodle/src/parser.y"
{ //- simple_arrow( B, C, none, valley) between two vertices (right)
  read_simple_arrow(*(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), *(yyvsp[-2].String), std::string("right"), 60);//- 60 is SIMPLE_ARROW_ANGLE
  delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String); 
}
#line 2746 "generated/parser.tab.cpp"
    break;

  case 179: /* simple_arrow_inst: SIMPLE_ARROW '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 772 "doodle/src/parser.y"
{ //- simple_arrow( B, C, none, valley, left) between two vertices
  read_simple_arrow(*(yyvsp[-10].String), *(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), *(yyvsp[-2].String), 60);//- 60 is SIMPLE_ARROW_ANGLE
  delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2755 "generated/parser.tab.cpp"
    break;

  case 180: /* simple_arrow_inst: SIMPLE_ARROW '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ',' INTEGER ')' ';'  */
#line 777 "doodle/src/parser.y"
{ //- simple_arrow( B, C, none, valley, left, angle) between two vertices
  read_simple_arrow(*(yyvsp[-12].String), *(yyvsp[-10].String), *(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), (yyvsp[-2].ival));
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String);
}
#line 2764 "generated/parser.tab.cpp"
    break;

  case 181: /* simple_arrow_inst: SIMPLE_ARROW '(' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 782 "doodle/src/parser.y"
{ //- simple_arrow( B, [C, AB2], none, valley) a vertex across a edge (right)
  read_simple_arrow(*(yyvsp[-12].String), *(yyvsp[-9].String), *(yyvsp[-7].String), *(yyvsp[-4].String), *(yyvsp[-2].String),  std::string("right"), 60); //- 60 is SIMPLE_ARROW_ANGLE
  delete (yyvsp[-12].String); delete (yyvsp[-9].String); delete (yyvsp[-7].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2773 "generated/parser.tab.cpp"
    break;

  case 182: /* simple_arrow_inst: SIMPLE_ARROW '(' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 787 "doodle/src/parser.y"
{ //- simple_arrow( B, [C, AB2], none, valley, left) a vertex across a edge
  read_simple_arrow(*(yyvsp[-14].String), *(yyvsp[-11].String), *(yyvsp[-9].String), *(yyvsp[-6].String), *(yyvsp[-4].String), *(yyvsp[-2].String), 60); //- 60 is SIMPLE_ARROW_ANGLE
  delete (yyvsp[-14].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2782 "generated/parser.tab.cpp"
    break;

  case 183: /* simple_arrow_inst: SIMPLE_ARROW '(' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ',' SYMBOL ',' SYMBOL ',' INTEGER ')' ';'  */
#line 792 "doodle/src/parser.y"
{ //- simple_arrow( B, [C, AB2], none, valley, left, angle) a vertex across a edge
  read_simple_arrow(*(yyvsp[-16].String), *(yyvsp[-13].String), *(yyvsp[-11].String), *(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), (yyvsp[-2].ival));
  delete (yyvsp[-16].String); delete (yyvsp[-13].String); delete (yyvsp[-11].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String);
}
#line 2791 "generated/parser.tab.cpp"
    break;

  case 184: /* return_arrow_inst: RETURN_ARROW '(' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 800 "doodle/src/parser.y"
{
  read_return_arrow(*(yyvsp[-15].String), *(yyvsp[-13].String), *(yyvsp[-9].String), *(yyvsp[-7].String), *(yyvsp[-4].String), *(yyvsp[-2].String), std::string("right"), 50); //- 50 is RETURN_ARROW_RATIO
  delete (yyvsp[-15].String); delete (yyvsp[-13].String); delete (yyvsp[-9].String); delete (yyvsp[-7].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2800 "generated/parser.tab.cpp"
    break;

  case 185: /* return_arrow_inst: RETURN_ARROW '(' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 806 "doodle/src/parser.y"
{
  read_return_arrow(*(yyvsp[-17].String), *(yyvsp[-15].String), *(yyvsp[-11].String), *(yyvsp[-9].String), *(yyvsp[-6].String), *(yyvsp[-4].String), *(yyvsp[-2].String), 50); //- 50 is RETURN_ARROW_RATIO
  delete (yyvsp[-17].String); delete (yyvsp[-15].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2809 "generated/parser.tab.cpp"
    break;

  case 186: /* return_arrow_inst: RETURN_ARROW '(' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ',' SYMBOL ',' SYMBOL ',' INTEGER ')' ';'  */
#line 812 "doodle/src/parser.y"
{
  read_return_arrow(*(yyvsp[-19].String), *(yyvsp[-17].String), *(yyvsp[-13].String), *(yyvsp[-11].String), *(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), (yyvsp[-2].ival));
  delete (yyvsp[-19].String); delete (yyvsp[-17].String); delete (yyvsp[-13].String); delete (yyvsp[-11].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String);
}
#line 2818 "generated/parser.tab.cpp"
    break;

  case 187: /* hide_inst: HIDE '(' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 819 "doodle/src/parser.y"
{
  read_hide_show(*(yyvsp[-5].String), *(yyvsp[-3].String), false);
  delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2827 "generated/parser.tab.cpp"
    break;

  case 188: /* hide_inst: HIDE '(' symbol_list ')' ';'  */
#line 824 "doodle/src/parser.y"
{
  read_hide_show(*(yyvsp[-2].List), false);
  delete (yyvsp[-2].List);
}
#line 2836 "generated/parser.tab.cpp"
    break;

  case 189: /* show_inst: SHOW '(' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 831 "doodle/src/parser.y"
{
  read_hide_show(*(yyvsp[-5].String), *(yyvsp[-3].String), true);
  delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2845 "generated/parser.tab.cpp"
    break;

  case 190: /* show_inst: SHOW '(' symbol_list ')' ';'  */
#line 836 "doodle/src/parser.y"
{
  read_hide_show(*(yyvsp[-2].List), true);
  delete (yyvsp[-2].List);
}
#line 2854 "generated/parser.tab.cpp"
    break;

  case 191: /* intersection_inst: SYMBOL '=' INTERSECTION '(' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 843 "doodle/src/parser.y"
{
  read_intersection(*(yyvsp[-16].String), *(yyvsp[-11].String), *(yyvsp[-9].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-16].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2863 "generated/parser.tab.cpp"
    break;

  case 192: /* intersection_inst: SYMBOL '=' INTERSECTION '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 848 "doodle/src/parser.y"
{
  read_intersection(*(yyvsp[-12].String), *(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), *(yyvsp[-2].String));
  delete (yyvsp[-12].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 2872 "generated/parser.tab.cpp"
    break;

  case 193: /* symmetry_inst: SYMBOL '=' SYMMETRY '(' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 855 "doodle/src/parser.y"
{
  read_symmetry(*(yyvsp[-12].String),*(yyvsp[-8].String),*(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-12].String); delete (yyvsp[-8].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2881 "generated/parser.tab.cpp"
    break;

  case 194: /* cut_inst: CUT '(' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ')' ';'  */
#line 862 "doodle/src/parser.y"
{
  read_cut(*(yyvsp[-7].String), *(yyvsp[-5].String),*(yyvsp[-2].String));
  delete (yyvsp[-7].String); delete (yyvsp[-5].String); delete (yyvsp[-2].String);
}
#line 2890 "generated/parser.tab.cpp"
    break;

  case 195: /* debug_inst: DEBUG_INST ';'  */
#line 869 "doodle/src/parser.y"
{
  read_debug_point();
  read_debug_line();
}
#line 2899 "generated/parser.tab.cpp"
    break;

  case 196: /* debug_point_inst: DEBUG_POINT_INST ';'  */
#line 876 "doodle/src/parser.y"
{
  read_debug_point();
}
#line 2907 "generated/parser.tab.cpp"
    break;

  case 197: /* debug_point_inst: DEBUG_POINT_INST '(' symbol_list ')' ';'  */
#line 880 "doodle/src/parser.y"
{
  read_debug_point(*(yyvsp[-2].List));
  delete (yyvsp[-2].List);
}
#line 2916 "generated/parser.tab.cpp"
    break;

  case 198: /* debug_line_inst: DEBUG_LINE_INST ';'  */
#line 887 "doodle/src/parser.y"
{
  read_debug_line();  
}
#line 2924 "generated/parser.tab.cpp"
    break;

  case 199: /* debug_line_inst: DEBUG_LINE_INST '(' symbol_list ')' ';'  */
#line 891 "doodle/src/parser.y"
{
  read_debug_line(*(yyvsp[-2].List));
  delete (yyvsp[-2].List);
}
#line 2933 "generated/parser.tab.cpp"
    break;

  case 200: /* debug_line_inst: DEBUG_LINE_INST '(' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 896 "doodle/src/parser.y"
{
  read_debug_line(*(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 2942 "generated/parser.tab.cpp"
    break;

  case 201: /* visible_height_inst: VISIBLE_HEIGHT '(' INTEGER ')' ';'  */
#line 903 "doodle/src/parser.y"
{
  read_visible_height((yyvsp[-2].ival));
}
#line 2950 "generated/parser.tab.cpp"
    break;

  case 202: /* visible_width_inst: VISIBLE_WIDTH '(' INTEGER ')' ';'  */
#line 909 "doodle/src/parser.y"
{
  read_visible_width((yyvsp[-2].ival));
}
#line 2958 "generated/parser.tab.cpp"
    break;

  case 203: /* visible_center_inst: VISIBLE_CENTER '(' SYMBOL ')' ';'  */
#line 915 "doodle/src/parser.y"
{
  read_visible_center(*(yyvsp[-2].String));
  delete (yyvsp[-2].String);
}
#line 2967 "generated/parser.tab.cpp"
    break;

  case 204: /* scale_inst: SCALE '(' INTEGER ')' ';'  */
#line 922 "doodle/src/parser.y"
{
  read_scale((yyvsp[-2].ival));
}
#line 2975 "generated/parser.tab.cpp"
    break;

  case 205: /* fill_inst: FILL '(' a_color ',' symbol_list ')' ';'  */
#line 928 "doodle/src/parser.y"
{
  read_fill(*(yyvsp[-4].Color), *(yyvsp[-2].List));
  delete (yyvsp[-4].Color); delete (yyvsp[-2].List);
}
#line 2984 "generated/parser.tab.cpp"
    break;

  case 206: /* unfill_inst: UNFILL '(' symbol_list ')' ';'  */
#line 935 "doodle/src/parser.y"
{
  read_unfill(*(yyvsp[-2].List));
  delete (yyvsp[-2].List);
}
#line 2993 "generated/parser.tab.cpp"
    break;

  case 207: /* unfill_inst: UNFILL ';'  */
#line 940 "doodle/src/parser.y"
{
  read_unfill_all();
}
#line 3001 "generated/parser.tab.cpp"
    break;

  case 208: /* debug_info_inst: DEBUG_INFO '(' STRING ')' ';'  */
#line 946 "doodle/src/parser.y"
{
#ifdef DEBUG
  steps[current_step].gdb_info(*(yyvsp[-2].String));
#endif /* ! DEBUG */
  delete (yyvsp[-2].String);
}
#line 3012 "generated/parser.tab.cpp"
    break;

  case 209: /* vertical_rectangle_inst: V_RECTANGLE '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ',' INTEGER ')' ';'  */
#line 956 "doodle/src/parser.y"
{
  read_vertical_rectangle(*(yyvsp[-10].String), *(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), (yyvsp[-2].ival));
  delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String);
}
#line 3021 "generated/parser.tab.cpp"
    break;

  case 210: /* vertical_rectangle_inst: V_RECTANGLE '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 962 "doodle/src/parser.y"
{
  read_vertical_rectangle(*(yyvsp[-10].String), *(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), *(yyvsp[-2].String));
  delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 3030 "generated/parser.tab.cpp"
    break;

  case 211: /* horizontal_rectangle_inst: H_RECTANGLE '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ',' INTEGER ')' ';'  */
#line 970 "doodle/src/parser.y"
{
  read_horizontal_rectangle(*(yyvsp[-10].String), *(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), (yyvsp[-2].ival));
  delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String);
}
#line 3039 "generated/parser.tab.cpp"
    break;

  case 212: /* horizontal_rectangle_inst: H_RECTANGLE '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 976 "doodle/src/parser.y"
{
  read_horizontal_rectangle(*(yyvsp[-10].String), *(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), *(yyvsp[-2].String));
  delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 3048 "generated/parser.tab.cpp"
    break;

  case 213: /* clip_inst: CLIP ';'  */
#line 983 "doodle/src/parser.y"
{
  read_clip(true);
}
#line 3056 "generated/parser.tab.cpp"
    break;

  case 214: /* clip_inst: CLIP '(' INTEGER ',' INTEGER ')' ';'  */
#line 987 "doodle/src/parser.y"
{
  read_clip(true, (yyvsp[-4].ival), (yyvsp[-2].ival));
}
#line 3064 "generated/parser.tab.cpp"
    break;

  case 215: /* unclip_inst: UNCLIP ';'  */
#line 993 "doodle/src/parser.y"
{
  read_clip(false);
}
#line 3072 "generated/parser.tab.cpp"
    break;

  case 216: /* perpendicular_inst: SYMBOL '=' PERPENDICULAR '(' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ')' ';'  */
#line 999 "doodle/src/parser.y"
{
  read_perpendicular(*(yyvsp[-12].String), *(yyvsp[-7].String), *(yyvsp[-5].String), *(yyvsp[-2].String));
  delete (yyvsp[-12].String); delete (yyvsp[-7].String); delete (yyvsp[-5].String); delete (yyvsp[-2].String);
}
#line 3081 "generated/parser.tab.cpp"
    break;

  case 217: /* perpendicular_inst: SYMBOL '=' PERPENDICULAR '(' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 1004 "doodle/src/parser.y"
{
  read_perpendicular(*(yyvsp[-18].String), *(yyvsp[-13].String), *(yyvsp[-11].String), *(yyvsp[-8].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-18].String); delete (yyvsp[-13].String); delete (yyvsp[-11].String); delete (yyvsp[-8].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 3090 "generated/parser.tab.cpp"
    break;

  case 218: /* parallel_inst: SYMBOL '=' PARALLEL '(' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 1011 "doodle/src/parser.y"
{
  read_parallel(*(yyvsp[-18].String), *(yyvsp[-13].String), *(yyvsp[-11].String), *(yyvsp[-8].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-18].String); delete (yyvsp[-13].String); delete (yyvsp[-11].String); delete (yyvsp[-8].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 3099 "generated/parser.tab.cpp"
    break;

  case 219: /* move_inst: MOVE '(' SYMBOL ',' SYMBOL ')' ';'  */
#line 1018 "doodle/src/parser.y"
{
  read_move(*(yyvsp[-4].String), *(yyvsp[-2].String));
  delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 3108 "generated/parser.tab.cpp"
    break;

  case 220: /* move_inst: MOVE '(' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 1023 "doodle/src/parser.y"
{
  read_move(*(yyvsp[-8].String), *(yyvsp[-5].String), *(yyvsp[-3].String));
  delete (yyvsp[-8].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 3117 "generated/parser.tab.cpp"
    break;

  case 221: /* inter_cut_inst: SYMBOL '=' INTER_CUT '(' '[' SYMBOL ',' SYMBOL ']' ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 1030 "doodle/src/parser.y"
{
  read_inter_cut(*(yyvsp[-16].String), *(yyvsp[-11].String),*(yyvsp[-9].String),*(yyvsp[-5].String),*(yyvsp[-3].String));
  delete (yyvsp[-16].String); delete (yyvsp[-11].String); delete (yyvsp[-9].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 3126 "generated/parser.tab.cpp"
    break;

  case 222: /* space_fold_inst: SPACE_FOLD '(' '[' SYMBOL ',' SYMBOL ']' ',' INTEGER ',' INTEGER ')' ';'  */
#line 1037 "doodle/src/parser.y"
{
  read_space_fold(*(yyvsp[-9].String), *(yyvsp[-7].String), (yyvsp[-4].ival), (yyvsp[-2].ival));
  delete (yyvsp[-9].String); delete (yyvsp[-7].String);
}
#line 3135 "generated/parser.tab.cpp"
    break;

  case 223: /* eps_inst: EPS '(' STRING ')' ';'  */
#line 1044 "doodle/src/parser.y"
{
  read_eps(*(yyvsp[-2].String), 210, 480, 380, 655);
  delete (yyvsp[-2].String);
}
#line 3144 "generated/parser.tab.cpp"
    break;

  case 224: /* eps_inst: EPS '(' STRING ',' INTEGER ',' INTEGER ',' INTEGER ',' INTEGER ')' ';'  */
#line 1049 "doodle/src/parser.y"
{
  read_eps(*(yyvsp[-10].String), (yyvsp[-8].ival), (yyvsp[-6].ival), (yyvsp[-4].ival), (yyvsp[-2].ival));
  delete (yyvsp[-10].String);
}
#line 3153 "generated/parser.tab.cpp"
    break;

  case 225: /* reset_inst: RESET ';'  */
#line 1056 "doodle/src/parser.y"
{
  read_reset();
}
#line 3161 "generated/parser.tab.cpp"
    break;

  case 226: /* shift_inst: SHIFT '(' SYMBOL ',' INTEGER ',' INTEGER ')' ';'  */
#line 1062 "doodle/src/parser.y"
{
  read_shift(*(yyvsp[-6].String), (yyvsp[-4].ival),(yyvsp[-2].ival));
  delete (yyvsp[-6].String);
}
#line 3170 "generated/parser.tab.cpp"
    break;

  case 227: /* shift_inst: SHIFT '(' SYMBOL ',' FLOAT ',' FLOAT ')' ';'  */
#line 1067 "doodle/src/parser.y"
{
  read_shift(*(yyvsp[-6].String), (yyvsp[-4].fval),(yyvsp[-2].fval));
  delete (yyvsp[-6].String);
}
#line 3179 "generated/parser.tab.cpp"
    break;

  case 228: /* shift_inst: SHIFT '(' SYMBOL ',' INTEGER ',' FLOAT ')' ';'  */
#line 1072 "doodle/src/parser.y"
{
  read_shift(*(yyvsp[-6].String), (yyvsp[-4].ival),(yyvsp[-2].fval));
  delete (yyvsp[-6].String);
}
#line 3188 "generated/parser.tab.cpp"
    break;

  case 229: /* shift_inst: SHIFT '(' SYMBOL ',' FLOAT ',' INTEGER ')' ';'  */
#line 1077 "doodle/src/parser.y"
{
  read_shift(*(yyvsp[-6].String), (yyvsp[-4].fval),(yyvsp[-2].ival));
  delete (yyvsp[-6].String);
}
#line 3197 "generated/parser.tab.cpp"
    break;

  case 230: /* unshift_inst: UNSHIFT ';'  */
#line 1084 "doodle/src/parser.y"
{
  read_unshift_all();
}
#line 3205 "generated/parser.tab.cpp"
    break;

  case 231: /* unshift_inst: UNSHIFT '(' symbol_list ')' ';'  */
#line 1088 "doodle/src/parser.y"
{
  read_unshift(*(yyvsp[-2].List));
  delete (yyvsp[-2].List);
}
#line 3214 "generated/parser.tab.cpp"
    break;

  case 232: /* text_inst: TEXT '(' SYMBOL ',' STRING ')' ';'  */
#line 1095 "doodle/src/parser.y"
{
  read_text(*(yyvsp[-4].String), *(yyvsp[-2].String));
  delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 3223 "generated/parser.tab.cpp"
    break;

  case 233: /* duplicate_inst: SYMBOL '=' SYMBOL ';'  */
#line 1102 "doodle/src/parser.y"
{
  read_duplicate(*(yyvsp[-3].String), *(yyvsp[-1].String));
  delete (yyvsp[-3].String); delete (yyvsp[-1].String);
}
#line 3232 "generated/parser.tab.cpp"
    break;

  case 234: /* rabbit_ear_inst: '[' SYMBOL ',' SYMBOL ']' '=' RABBIT_EAR '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 1109 "doodle/src/parser.y"
{
  //- [VERTEX, CENTER] = \rabbit_ear(MOVING_VERTEX, VERTEX_DEST, V3, EDGE);
  read_rabbit_ear(*(yyvsp[-19].String), *(yyvsp[-17].String), *(yyvsp[-12].String), *(yyvsp[-10].String), *(yyvsp[-8].String), *(yyvsp[-5].String), *(yyvsp[-3].String), false);
  delete (yyvsp[-19].String); delete (yyvsp[-17].String); delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 3242 "generated/parser.tab.cpp"
    break;

  case 235: /* rabbit_ear_inst: '[' SYMBOL ',' SYMBOL ']' '=' RABBIT_EAR '(' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 1115 "doodle/src/parser.y"
{
  //- [VERTEX, CENTER] = \rabbit_ear(MOVING_VERTEX, VERTEX_DEST, V3);
  read_rabbit_ear(*(yyvsp[-13].String), *(yyvsp[-11].String), *(yyvsp[-6].String), *(yyvsp[-4].String), *(yyvsp[-2].String), *(yyvsp[-6].String), *(yyvsp[-4].String), false);
  delete (yyvsp[-13].String); delete (yyvsp[-11].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);

}
#line 3253 "generated/parser.tab.cpp"
    break;

  case 236: /* rabbit_ear_inst: SYMBOL '=' RABBIT_EAR '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ',' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 1122 "doodle/src/parser.y"
{
  //- VERTEX = \rabbit_ear(MOVING_VERTEX, VERTEX_DEST, V3, CENTER, EDGE);
  read_rabbit_ear(*(yyvsp[-18].String), *(yyvsp[-8].String), *(yyvsp[-14].String), *(yyvsp[-12].String), *(yyvsp[-10].String), *(yyvsp[-5].String), *(yyvsp[-3].String), true);
  delete (yyvsp[-18].String); delete (yyvsp[-8].String); delete (yyvsp[-14].String); delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 3263 "generated/parser.tab.cpp"
    break;

  case 237: /* rabbit_ear_inst: SYMBOL '=' RABBIT_EAR '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 1128 "doodle/src/parser.y"
{
  //- VERTEX = \rabbit_ear(MOVING_VERTEX, VERTEX_DEST, V3, CENTER);
  read_rabbit_ear(*(yyvsp[-12].String), *(yyvsp[-2].String), *(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), *(yyvsp[-8].String), *(yyvsp[-6].String), true);
  delete (yyvsp[-12].String); delete (yyvsp[-2].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String);
}
#line 3273 "generated/parser.tab.cpp"
    break;

  case 238: /* push_arrow_inst: PUSH_ARROW '(' SYMBOL ',' INTEGER ',' INTEGER ')' ';'  */
#line 1136 "doodle/src/parser.y"
{
  read_push_arrow(*(yyvsp[-6].String), (yyvsp[-4].ival), (yyvsp[-2].ival));
  delete (yyvsp[-6].String);
}
#line 3282 "generated/parser.tab.cpp"
    break;

  case 239: /* push_arrow_inst: PUSH_ARROW '(' SYMBOL ',' INTEGER ')' ';'  */
#line 1141 "doodle/src/parser.y"
{
  read_push_arrow(*(yyvsp[-4].String), (yyvsp[-2].ival), 0);
  delete (yyvsp[-4].String);
}
#line 3291 "generated/parser.tab.cpp"
    break;

  case 240: /* push_arrow_inst: PUSH_ARROW '(' SYMBOL ')' ';'  */
#line 1146 "doodle/src/parser.y"
{
  read_push_arrow(*(yyvsp[-2].String));
  delete (yyvsp[-2].String);
}
#line 3300 "generated/parser.tab.cpp"
    break;

  case 241: /* push_arrow_inst: PUSH_ARROW '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' INTEGER ')' ';'  */
#line 1151 "doodle/src/parser.y"
{
  read_push_arrow(*(yyvsp[-8].String), *(yyvsp[-6].String), *(yyvsp[-4].String), (yyvsp[-2].ival));
  delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String);
}
#line 3309 "generated/parser.tab.cpp"
    break;

  case 242: /* push_arrow_inst: PUSH_ARROW '(' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 1156 "doodle/src/parser.y"
{
  read_push_arrow(*(yyvsp[-6].String), *(yyvsp[-4].String), *(yyvsp[-2].String), 0);
  delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);
}
#line 3318 "generated/parser.tab.cpp"
    break;

  case 243: /* open_arrow_inst: OPEN_ARROW '(' '[' SYMBOL ',' SYMBOL ']' ',' SYMBOL ')' ';'  */
#line 1163 "doodle/src/parser.y"
{
  read_open_arrow(*(yyvsp[-7].String), *(yyvsp[-5].String), *(yyvsp[-2].String));
  delete (yyvsp[-7].String); delete (yyvsp[-5].String); delete (yyvsp[-2].String);
}
#line 3327 "generated/parser.tab.cpp"
    break;

  case 244: /* open_arrow_inst: OPEN_ARROW '(' '[' SYMBOL ',' SYMBOL ']' ')' ';'  */
#line 1168 "doodle/src/parser.y"
{
  read_open_arrow(*(yyvsp[-5].String), *(yyvsp[-3].String), std::string("right"));
  delete (yyvsp[-5].String); delete (yyvsp[-3].String);
}
#line 3336 "generated/parser.tab.cpp"
    break;

  case 245: /* repeat_arrow_inst: REPEAT_ARROW '(' SYMBOL ',' INTEGER ',' INTEGER ',' INTEGER ')' ';'  */
#line 1175 "doodle/src/parser.y"
{
  if((yyvsp[-6].ival) < 1) yyerror("Repeat number shouldn't be negative or null.");
  read_repeat_arrow(*(yyvsp[-8].String), (unsigned int) (yyvsp[-6].ival), std::string(), std::string(), (yyvsp[-4].ival), (yyvsp[-2].ival));
  delete (yyvsp[-8].String);
}
#line 3346 "generated/parser.tab.cpp"
    break;

  case 246: /* repeat_arrow_inst: REPEAT_ARROW '(' SYMBOL ',' INTEGER ',' INTEGER ')' ';'  */
#line 1181 "doodle/src/parser.y"
{
  if((yyvsp[-4].ival) < 1) yyerror("Repeat number shouldn't be negative or null.");
  read_repeat_arrow(*(yyvsp[-6].String), (unsigned int) (yyvsp[-4].ival), std::string(), std::string(), (yyvsp[-2].ival), 0);
  delete (yyvsp[-6].String);
}
#line 3356 "generated/parser.tab.cpp"
    break;

  case 247: /* repeat_arrow_inst: REPEAT_ARROW '(' SYMBOL ',' INTEGER ')' ';'  */
#line 1187 "doodle/src/parser.y"
{
  if((yyvsp[-2].ival) < 1) yyerror("Repeat number shouldn't be negative or null.");
  read_repeat_arrow(*(yyvsp[-4].String), (unsigned int) (yyvsp[-2].ival), std::string(), std::string());
  delete (yyvsp[-4].String);
}
#line 3366 "generated/parser.tab.cpp"
    break;

  case 248: /* repeat_arrow_inst: REPEAT_ARROW '(' SYMBOL ')' ';'  */
#line 1193 "doodle/src/parser.y"
{
  read_repeat_arrow(*(yyvsp[-2].String), (unsigned int) 1, std::string(), std::string());
  delete (yyvsp[-2].String);
}
#line 3375 "generated/parser.tab.cpp"
    break;

  case 249: /* repeat_arrow_inst: REPEAT_ARROW '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' INTEGER ',' INTEGER ',' INTEGER ')' ';'  */
#line 1198 "doodle/src/parser.y"
{
  if((yyvsp[-6].ival) < 1) yyerror("Repeat number shouldn't be negative or null.");
  read_repeat_arrow(*(yyvsp[-12].String), (unsigned int) (yyvsp[-6].ival), *(yyvsp[-10].String), *(yyvsp[-8].String), (yyvsp[-4].ival), (yyvsp[-2].ival));
  delete (yyvsp[-12].String); delete (yyvsp[-10].String); delete (yyvsp[-8].String);  
}
#line 3385 "generated/parser.tab.cpp"
    break;

  case 250: /* repeat_arrow_inst: REPEAT_ARROW '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' INTEGER ',' INTEGER ')' ';'  */
#line 1204 "doodle/src/parser.y"
{
  if((yyvsp[-4].ival) < 1) yyerror("Repeat number shouldn't be negative or null.");
  read_repeat_arrow(*(yyvsp[-10].String), (unsigned int) (yyvsp[-4].ival), *(yyvsp[-8].String), *(yyvsp[-6].String), (yyvsp[-2].ival), 0);
  delete (yyvsp[-10].String); delete (yyvsp[-8].String); delete (yyvsp[-6].String);  
}
#line 3395 "generated/parser.tab.cpp"
    break;

  case 251: /* repeat_arrow_inst: REPEAT_ARROW '(' SYMBOL ',' SYMBOL ',' SYMBOL ',' INTEGER ')' ';'  */
#line 1210 "doodle/src/parser.y"
{
  if((yyvsp[-2].ival) < 1) yyerror("Repeat number shouldn't be negative or null.");
  read_repeat_arrow(*(yyvsp[-8].String), (unsigned int) (yyvsp[-2].ival), *(yyvsp[-6].String), *(yyvsp[-4].String));
  delete (yyvsp[-8].String); delete (yyvsp[-6].String); delete (yyvsp[-4].String);  
}
#line 3405 "generated/parser.tab.cpp"
    break;

  case 252: /* repeat_arrow_inst: REPEAT_ARROW '(' SYMBOL ',' SYMBOL ',' SYMBOL ')' ';'  */
#line 1216 "doodle/src/parser.y"
{
  read_repeat_arrow(*(yyvsp[-6].String), 1, *(yyvsp[-4].String), *(yyvsp[-2].String));
  delete (yyvsp[-6].String); delete (yyvsp[-4].String); delete (yyvsp[-2].String);  
}
#line 3414 "generated/parser.tab.cpp"
    break;

  case 253: /* label_inst: LABEL '(' SYMBOL ')' ';'  */
#line 1223 "doodle/src/parser.y"
{
  read_label(*(yyvsp[-2].String));
  delete (yyvsp[-2].String);
}
#line 3423 "generated/parser.tab.cpp"
    break;

  case 254: /* symbol_list: SYMBOL  */
#line 1232 "doodle/src/parser.y"
{
  (yyval.List) = new std::vector<std::string>;
  (yyval.List)->push_back(*(yyvsp[0].String));
  delete (yyvsp[0].String);
}
#line 3433 "generated/parser.tab.cpp"
    break;

  case 255: /* symbol_list: symbol_list ',' SYMBOL  */
#line 1238 "doodle/src/parser.y"
  {
    (yyval.List) = (yyvsp[-2].List);
    (yyval.List)->push_back(*(yyvsp[0].String));
    delete (yyvsp[0].String);
}
#line 3443 "generated/parser.tab.cpp"
    break;

  case 256: /* a_date: INTEGER ',' INTEGER ',' INTEGER  */
#line 1246 "doodle/src/parser.y"
{ /* Ex. 03, 29, 2000 */
  (yyval.Date) = new date((yyvsp[-2].ival), (yyvsp[-4].ival), (yyvsp[0].ival));
}
#line 3451 "generated/parser.tab.cpp"
    break;

  case 257: /* a_date: TODAY  */
#line 1250 "doodle/src/parser.y"
{
  time_t c = time(NULL);
  struct tm * t = localtime(&c);
  
  (yyval.Date) = new date(t->tm_mday, t->tm_mon+1, t->tm_year+1900);
}
#line 3462 "generated/parser.tab.cpp"
    break;

  case 258: /* a_date: INTEGER  */
#line 1257 "doodle/src/parser.y"
{
  (yyval.Date) = new date(0 ,0 , (yyvsp[0].ival));
}
#line 3470 "generated/parser.tab.cpp"
    break;

  case 259: /* a_color: SYMBOL  */
#line 1263 "doodle/src/parser.y"
{
  (yyval.Color) = read_color(*(yyvsp[0].String));
  delete (yyvsp[0].String);
}
#line 3479 "generated/parser.tab.cpp"
    break;

  case 260: /* a_color: DARKER '(' a_color ')'  */
#line 1268 "doodle/src/parser.y"
{
  (yyval.Color) = new color(*(yyvsp[-1].Color), 0.9);
  delete (yyvsp[-1].Color);
}
#line 3488 "generated/parser.tab.cpp"
    break;

  case 261: /* a_color: LIGHTER '(' a_color ')'  */
#line 1273 "doodle/src/parser.y"
{
  (yyval.Color) = new color(*(yyvsp[-1].Color), 1.1);
  delete (yyvsp[-1].Color);
}
#line 3497 "generated/parser.tab.cpp"
    break;

  case 262: /* rotate_old_syntax_error: ROTATE INTEGER ';'  */
#line 1285 "doodle/src/parser.y"
{
  char msg[100];

  sprintf(msg, "Syntax has changed\n\\rotate syntax has changed. Use now \\rotate(%d); instead of.", (yyvsp[-1].ival));
  yywarning(msg);
}
#line 3508 "generated/parser.tab.cpp"
    break;

  case 263: /* rotate_in_step_error: ROTATE '(' INTEGER ')' ';'  */
#line 1292 "doodle/src/parser.y"
{
  yywarning("Syntax has changed\n\\rotate can no longer be found inside a step block");
}
#line 3516 "generated/parser.tab.cpp"
    break;

  case 264: /* turn_over_vertical_error: TURN_VERTICAL ';'  */
#line 1298 "doodle/src/parser.y"
{
  yywarning("Syntax has changed\n\\turn_over_vertical can no longer be found inside a step block");
  read_turn_over(true);
}
#line 3525 "generated/parser.tab.cpp"
    break;

  case 265: /* turn_over_horizontal_error: TURN_HORIZONTAL ';'  */
#line 1305 "doodle/src/parser.y"
{
  yywarning("Syntax has changed\n\\turn_over_horizontal can no longer be found inside a step block");
  read_turn_over(false);
}
#line 3534 "generated/parser.tab.cpp"
    break;


#line 3538 "generated/parser.tab.cpp"

      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", YY_CAST (yysymbol_kind_t, yyr1[yyn]), &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */
  {
    const int yylhs = yyr1[yyn] - YYNTOKENS;
    const int yyi = yypgoto[yylhs] + *yyssp;
    yystate = (0 <= yyi && yyi <= YYLAST && yycheck[yyi] == *yyssp
               ? yytable[yyi]
               : yydefgoto[yylhs]);
  }

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYSYMBOL_YYEMPTY : YYTRANSLATE (yychar);
  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
      yyerror (YY_("syntax error"));
    }

  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:
  /* Pacify compilers when the user code never invokes YYERROR and the
     label yyerrorlab therefore never appears in user code.  */
  if (0)
    YYERROR;
  ++yynerrs;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  /* Pop stack until we find a state that shifts the error token.  */
  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYSYMBOL_YYerror;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYSYMBOL_YYerror)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  YY_ACCESSING_SYMBOL (yystate), yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", YY_ACCESSING_SYMBOL (yyn), yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturnlab;


/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturnlab;


/*-----------------------------------------------------------.
| yyexhaustedlab -- YYNOMEM (memory exhaustion) comes here.  |
`-----------------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  goto yyreturnlab;


/*----------------------------------------------------------.
| yyreturnlab -- parsing is finished, clean up and return.  |
`----------------------------------------------------------*/
yyreturnlab:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  YY_ACCESSING_SYMBOL (+*yyssp), yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif

  return yyresult;
}

#line 1312 "doodle/src/parser.y"

/*--------------------------------------------------------------------*/
/* Maintenant c'est du C 					      */

/**
 ** Traitement des erreurs lors du parsing
 **/
void yyerror(char* s)
{
#ifdef WIN32
  // Message d'erreur style visual
  fprintf(stderr, "%s(%d): error %s\n", file_name.c_str(), line_num, s);
#else // WIN32
  // Message d'erreur style unix
  fprintf(stderr, "%s:%d: error %s\n", file_name.c_str(), line_num, s);
#endif // WIN32
  /* exit(2); */
}

void yywarning(char* s)
{
#ifdef WIN32
  // Message d'erreur style visual
  fprintf(stderr, "%s(%d): warning %s\n", file_name.c_str(), line_num, s);
#else // WIN32
  // Message d'erreur style unix
  fprintf(stderr, "%s:%d: warning %s\n", file_name.c_str(), line_num, s);
#endif // WIN32
}
