from enum import Enum


class Player(Enum):
    white = 0
    black = 1
    undefined = -1


class PieceRank(Enum):
    man = 0
    king = 1
    undefined = -1


class BoardSize(Enum):
    standard = 0
    big = 1
    large = 2
    rect = 3


class BoardSquareStatus(Enum):
    empty = 0
    white_man = 1
    white_king = 2
    black_man = 3
    black_king = 4
    taken = 5
    border = 6
    illegal = 7

    @property
    def player(self):
        if self == BoardSquareStatus.white_man:
            return Player.white
        elif self == BoardSquareStatus.white_king:
            return Player.white
        elif self == BoardSquareStatus.black_man:
            return Player.black
        elif self == BoardSquareStatus.black_king:
            return Player.black
        else:
            return Player.undefined

    @property
    def piece_rank(self):
        if self == BoardSquareStatus.white_man:
            return PieceRank.man
        elif self == BoardSquareStatus.white_king:
            return PieceRank.king
        elif self == BoardSquareStatus.black_man:
            return PieceRank.man
        elif self == BoardSquareStatus.black_king:
            return PieceRank.king
        else:
            return PieceRank.undefined
