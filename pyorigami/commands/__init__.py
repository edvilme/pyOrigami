"""User-facing command dataclasses for the DOODLE diagram language.

Each dataclass maps to a DOODLE operator and can serialize itself back
to ``.doo`` text via :meth:`to_doo`.  Based on the grammar defined in
``doodle/src/parser.y`` from the `DOODLE <https://doodle.sourceforge.net/>`_
project by Olivier Bettens.
"""

from .structure import Assign, AssignPair, Diagram, DiagramHeader, DooComment, Step
from .header import (
    BottomMargin,
    ColorBack,
    ColorFront,
    Comment,
    DesignDate,
    Designer,
    DiagramDate,
    Diagrammer,
    HorizontalSpace,
    LeftMargin,
    RightMargin,
    Title,
    TopMargin,
    VerticalSpace,
)
from .paper import Diamond, HorizontalRectangle, Square, VerticalRectangle
from .geometry import (
    Fraction,
    InterCut,
    Intersection,
    LineToLine,
    Middle,
    Parallel,
    Perpendicular,
    PointToLine,
    PointToPoint,
    RabbitEar,
    Symmetry,
)
from .transforms import Move, Shift, Unshift
from .folds import Border, Cut, Fold, MountainFold, ValleyFold, XrayFold
from .arrows import OpenArrow, PushArrow, RepeatArrow, ReturnArrow, SimpleArrow
from .display import (
    Caption,
    Darker,
    Fill,
    Hide,
    Label,
    Lighter,
    Ref,
    Show,
    SpaceFold,
    Text,
    Unfill,
)
from .layout import (
    Clip,
    Rotate,
    Scale,
    TurnOverHorizontal,
    TurnOverVertical,
    Unclip,
    VisibleAreaCenter,
    VisibleAreaHeight,
    VisibleAreaWidth,
)
from .misc import Debug, DebugLine, DebugPoint, Include, Reset
