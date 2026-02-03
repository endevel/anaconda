from enum import Enum

from athena.core.player import Player


class BoardSquare(Enum):
    EMPTY = 0
    WHITE_PIECE = 1
    WHITE_KING = 2
    BLACK_PIECE = 3
    BLACK_KING = 4
    TAKEN = 5
    OUT_OF_BOUNDS = 6

    @property
    def is_white(self) -> bool:
        return (
            True
            if self == BoardSquare.WHITE_PIECE or self == BoardSquare.WHITE_KING
            else False
        )

    @property
    def is_black(self) -> bool:
        return (
            True
            if self == BoardSquare.BLACK_PIECE or self == BoardSquare.BLACK_KING
            else False
        )

    @property
    def is_empty(self) -> bool:
        return self == BoardSquare.EMPTY

    @property
    def is_man(self) -> bool:
        return self == BoardSquare.WHITE_PIECE or self == BoardSquare.BLACK_PIECE

    @property
    def is_king(self) -> bool:
        return self == BoardSquare.WHITE_KING or self == BoardSquare.BLACK_KING

    @property
    def owner(self) -> Player:
        if self.is_white:
            return Player.WHITE
        elif self.is_black:
            return Player.BLACK
        else:
            raise ValueError("Invalid square")
