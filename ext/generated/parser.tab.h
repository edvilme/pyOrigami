/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

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

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_GENERATED_PARSER_TAB_HPP_INCLUDED
# define YY_YY_GENERATED_PARSER_TAB_HPP_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 1
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    HEADER = 258,                  /* HEADER  */
    STEP = 259,                    /* STEP  */
    TURN_VERTICAL = 260,           /* TURN_VERTICAL  */
    TURN_HORIZONTAL = 261,         /* TURN_HORIZONTAL  */
    ROTATE = 262,                  /* ROTATE  */
    DESIGN_DATE = 263,             /* DESIGN_DATE  */
    DIAG_DATE = 264,               /* DIAG_DATE  */
    DESIGNER = 265,                /* DESIGNER  */
    DIAGRAMER = 266,               /* DIAGRAMER  */
    DIAGRAMMER = 267,              /* DIAGRAMMER  */
    TODAY = 268,                   /* TODAY  */
    TITLE = 269,                   /* TITLE  */
    _LEFT_MARGIN = 270,            /* _LEFT_MARGIN  */
    _RIGHT_MARGIN = 271,           /* _RIGHT_MARGIN  */
    _TOP_MARGIN = 272,             /* _TOP_MARGIN  */
    _BOTTOM_MARGIN = 273,          /* _BOTTOM_MARGIN  */
    _VSPACE = 274,                 /* _VSPACE  */
    _HSPACE = 275,                 /* _HSPACE  */
    SQUARE = 276,                  /* SQUARE  */
    DIAMOND = 277,                 /* DIAMOND  */
    MIDDLE = 278,                  /* MIDDLE  */
    FRACT = 279,                   /* FRACT  */
    CAPTION = 280,                 /* CAPTION  */
    VALLEY_FOLD = 281,             /* VALLEY_FOLD  */
    MOUNTAIN_FOLD = 282,           /* MOUNTAIN_FOLD  */
    FOLD = 283,                    /* FOLD  */
    SCALE = 284,                   /* SCALE  */
    POINT_TO_POINT = 285,          /* POINT_TO_POINT  */
    POINT_TO_LINE = 286,           /* POINT_TO_LINE  */
    LINE_TO_LINE = 287,            /* LINE_TO_LINE  */
    SIMPLE_ARROW = 288,            /* SIMPLE_ARROW  */
    RETURN_ARROW = 289,            /* RETURN_ARROW  */
    HIDE = 290,                    /* HIDE  */
    SHOW = 291,                    /* SHOW  */
    BORDER = 292,                  /* BORDER  */
    INTERSECTION = 293,            /* INTERSECTION  */
    SYMMETRY = 294,                /* SYMMETRY  */
    CUT = 295,                     /* CUT  */
    DEBUG_INST = 296,              /* DEBUG_INST  */
    DEBUG_POINT_INST = 297,        /* DEBUG_POINT_INST  */
    DEBUG_LINE_INST = 298,         /* DEBUG_LINE_INST  */
    XRAY_FOLD = 299,               /* XRAY_FOLD  */
    VISIBLE_HEIGHT = 300,          /* VISIBLE_HEIGHT  */
    VISIBLE_WIDTH = 301,           /* VISIBLE_WIDTH  */
    VISIBLE_CENTER = 302,          /* VISIBLE_CENTER  */
    COLOR_FRONT = 303,             /* COLOR_FRONT  */
    COLOR_BACK = 304,              /* COLOR_BACK  */
    FILL = 305,                    /* FILL  */
    UNFILL = 306,                  /* UNFILL  */
    V_RECTANGLE = 307,             /* V_RECTANGLE  */
    H_RECTANGLE = 308,             /* H_RECTANGLE  */
    CLIP = 309,                    /* CLIP  */
    UNCLIP = 310,                  /* UNCLIP  */
    PERPENDICULAR = 311,           /* PERPENDICULAR  */
    PARALLEL = 312,                /* PARALLEL  */
    MOVE = 313,                    /* MOVE  */
    INTER_CUT = 314,               /* INTER_CUT  */
    SPACE_FOLD = 315,              /* SPACE_FOLD  */
    COMMENT = 316,                 /* COMMENT  */
    EPS = 317,                     /* EPS  */
    RESET = 318,                   /* RESET  */
    SHIFT = 319,                   /* SHIFT  */
    MACRO = 320,                   /* MACRO  */
    MACROTEXT = 321,               /* MACROTEXT  */
    OPERATOR = 322,                /* OPERATOR  */
    DARKER = 323,                  /* DARKER  */
    LIGHTER = 324,                 /* LIGHTER  */
    TEXT = 325,                    /* TEXT  */
    UNSHIFT = 326,                 /* UNSHIFT  */
    RABBIT_EAR = 327,              /* RABBIT_EAR  */
    OPEN_ARROW = 328,              /* OPEN_ARROW  */
    PUSH_ARROW = 329,              /* PUSH_ARROW  */
    REPEAT_ARROW = 330,            /* REPEAT_ARROW  */
    LABEL = 331,                   /* LABEL  */
    DEBUG_INFO = 332,              /* DEBUG_INFO  */
    INTEGER = 333,                 /* INTEGER  */
    FLOAT = 334,                   /* FLOAT  */
    SYMBOL = 335,                  /* SYMBOL  */
    STRING = 336                   /* STRING  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 59 "doodle/src/parser.y"

  int                      ival;
  double                   fval;
  std::string              *String;  /* any string (or symbol) */
  date                     *Date;
  diag_header              *Info;
  std::vector<std::string> *List;
  color                    *Color;

#line 155 "generated/parser.tab.hpp"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_GENERATED_PARSER_TAB_HPP_INCLUDED  */
