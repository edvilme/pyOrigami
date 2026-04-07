"""Verify DSL ergonomics by modelling simple_boat.doo steps 1-3."""

from pydoodle import *  # noqa: F403

my_color = (60, 85, 60)

boat = Diagram(
    header=DiagramHeader(
        body=[
            Designer("Traditional"),
            Title("Simple boat"),
            Diagrammer("Xavier Fouchet"),
            DiagramDate(2001),
            Comment("Level : beginner"),
            Comment("Paper : A4"),
            ColorFront(my_color),
            ColorBack((90, 70, 90)),
        ]
    ),
    body=[
        # Step 1
        Step(
            body=[
                VerticalRectangle("a", "b", "c", "d", PaperFormat.A),
                Assign("ad", Middle("a", "d")),
                Assign("bc", Middle("b", "c")),
                ValleyFold("ad", "bc"),
                SimpleArrow("a", "d", ArrowHead.NONE, ArrowHead.VALLEY, ArrowSide.LEFT),
                Caption("Fold horizontally in half"),
                Fill(Side.BACK, ["a", "b", "c", "d"]),
            ]
        ),
        # Step 2
        Step(
            body=[
                Cut(Edge("a", "d"), "ad"),
                Cut(Edge("b", "c"), "bc"),
                Move("a", "d"),
                Move("b", "c"),
                Hide(Edge("bc", "c")),
                Border("ad", "bc"),
                Shift("d", -2, 2),
                Border("d", "c", 0, Edge("a", "ad")),
                Unfill(["a", "b", "c", "d"]),
                Assign("o", Middle("ad", "bc")),
                Assign("ab", Middle("a", "b")),
                ValleyFold("o", "ab"),
                SimpleArrow("a", "b", ArrowHead.VALLEY, ArrowHead.UNFOLD, ArrowSide.RIGHT),
                Assign("center", Middle("ad", "b")),
                VisibleAreaCenter("center"),
                Caption("Fold and unfold in half again"),
                Fill(Side.BACK, ["d", "c", "bc", "ad"]),
                Fill(Side.FRONT, ["a", "b", "bc", "ad"]),
            ]
        ),
        # Step 3
        Step(
            body=[
                Assign("aad", PointToLine("ad", "o", Edge("o", "ab"), Edge("a", "ad"))),
                ValleyFold("aad", "o"),
                SimpleArrow(
                    "ad",
                    Edge("aad", "o"),
                    ArrowHead.NONE,
                    ArrowHead.VALLEY,
                    ArrowSide.RIGHT,
                ),
                Assign(
                    "bbc",
                    PointToLine("bc", "o", Edge("o", "ab"), Edge("b", "bc"), Which.SECOND),
                ),
                ValleyFold("bbc", "o"),
                SimpleArrow(
                    "bc",
                    Edge("bbc", "o"),
                    ArrowHead.NONE,
                    ArrowHead.VALLEY,
                    ArrowSide.LEFT,
                ),
                Cut(Edge("ad", "bc"), "o"),
                Caption("Fold upper corners along middle line"),
            ]
        ),
        Scale(150),
    ],
)

if __name__ == "__main__":
    print(write(boat))
    render(boat, OutputFormat.SVG, "simple_boat.svg")
