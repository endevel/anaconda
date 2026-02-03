from enum import Enum

from athena.core.player import Player


class BoardSquare(Enum):
    empty = 0
    white_piece = 1
    white_king = 2
    black_piece = 3
    black_king = 4
    taken = 5
    out_of_bounds = 6

    @property
    def is_white(self) -> bool:
        return (
            True
            if self == BoardSquare.white_piece or self == BoardSquare.white_king
            else False
        )

    @property
    def is_black(self) -> bool:
        return (
            True
            if self == BoardSquare.black_piece or self == BoardSquare.black_king
            else False
        )

    @property
    def is_empty(self) -> bool:
        return self == BoardSquare.empty

    @property
    def is_man(self) -> bool:
        return self == BoardSquare.white_piece or self == BoardSquare.black_piece

    @property
    def is_king(self) -> bool:
        return self == BoardSquare.white_king or self == BoardSquare.black_king

    @property
    def owner(self) -> Player:
        if self.is_white:
            return Player.white
        elif self.is_black:
            return Player.black
        else:
            raise ValueError("Invalid square")
