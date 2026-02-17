from enum import Enum


class BoardSize(Enum):  # noqa: F821
    """
    Enum representing different board sizes for the game.

    Attributes:
        STANDARD: Standard 8x8 board size.
        BIG: Larger 10x10 board size.
        LARGE: Largest 12x12 board size.
    """

    STANDARD = 0
    BIG = 1
    LARGE = 2

    @property
    def height(self):
        """Return the height of the board."""
        return (
            8
            if self == BoardSize.STANDARD
            else 10 if self == BoardSize.BIG else 12 if self == BoardSize.LARGE else 0
        )

    @property
    def width(self):
        """Return the width of the board."""
        return (
            8
            if self == BoardSize.STANDARD
            else 10 if self == BoardSize.BIG else 12 if self == BoardSize.LARGE else 0
        )

    @property
    def start_position(self) -> str:
        """Return the starting position notation for the board."""
        if self == BoardSize.STANDARD:
            return "B:W21,22,23,24,25,26,27,28,29,30,31,32:B1,2,3,4,5,6,7,8,9,10,11,12."
        elif self == BoardSize.BIG:
            return "B:W31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50:B1,2,3,4,6,7,9,10,11,12,13,14,15,16,17,18,19,20."
        elif self == BoardSize.LARGE:
            return "B:W45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72:B1,2,3,4,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30."
        else:
            raise ValueError("Invalid Invalid board size")
