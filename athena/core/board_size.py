from enum import Enum


class BoardSize(Enum):  # noqa: F821
    standard = 0
    big = 1
    large = 2

    @property
    def height(self):
        return (
            8
            if self == BoardSize.standard
            else 10 if self == BoardSize.big else 12 if self == BoardSize.large else 0
        )

    @property
    def width(self):
        return (
            8
            if self == BoardSize.standard
            else 10 if self == BoardSize.big else 12 if self == BoardSize.large else 0
        )

    @property
    def start_position(self) -> str:
        if self == BoardSize.standard:
            return "B:W21,22,23,24,25,26,27,28,29,30,31,32:B1,2,3,4,5,6,7,8,9,10,11,12."
        elif self == BoardSize.big:
            return "B:W31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50:B1,2,3,4,6,7,9,10,11,12,13,14,15,16,17,18,19,20."
        elif self == BoardSize.large:
            return "B:W45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72:B1,2,3,4,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30."
        else:
            raise ValueError("Invalid Invalid board size")
