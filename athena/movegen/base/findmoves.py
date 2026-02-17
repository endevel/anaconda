from athena.core.move import Move
from athena.core.player import Player
from athena.damboard.damboard import Damboard
from athena.movegen.base.basemove import BaseMove


class FindMoves:
    def __init__(
        self,
        board: Damboard,
        player: Player,
        moves: tuple[BaseMove],
        promo_squares: set[int],
    ):
        self.board = board
        self.player = player
        self.moves = moves
        self.promo_squares = promo_squares

    def find_moves(self, square: int, movelist: list[Move]):
        if self.board[square].is_empty or self.board[square].owner != self.player:
            return
        for mv in self.moves:
            for ndx in range(mv.length):
                if self.board[square + ndx * mv.direction].is_empty:
                    piece_before = self.board[square]
                    piece_after = self.board[square + ndx * mv.direction]
                    if square + ndx * mv.direction in self.promo_squares:
                        piece_after = piece_after.promote()
                    move = Move(
                        from_square=square,
                        to_square=square + ndx * mv.direction,
                        piece_before=piece_before,
                        piece_after=piece_after,
                        kill_pieces=list(),
                    )
                    movelist.append(move)
