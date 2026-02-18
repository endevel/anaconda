from athena.core.move import Move
from athena.core.player import Player
from athena.damboard.damboard import Damboard


class TryCapture:
    def __init__(
        self,
        player: Player,
    ):
        self.player = player

    def __call__(
        self,
        board: Damboard,
        square: int,
        move: Move,
        direction: int,
        length: int,
    ) -> bool:
        if board[square].is_empty or board[square].owner != self.player:
            return False
        for ndx in range(length):
            if board[square + (ndx + 1) * direction].is_opponent(self.player):
                if board[square + (ndx + 2) * direction].is_empty:
                    move.from_square = square
                    move.to_square = square + (ndx + 2) * direction
                    return True
                else:
                    return False
            else:
                if not board[square + (ndx + 2) * direction].is_empty:
                    return False    
        return False
