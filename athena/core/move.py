from dataclasses import dataclass, field

from athena.core.board_square import BoardSquare
from athena.damboard.damboard import Damboard


@dataclass(frozen=True)
class Piece:
    value: BoardSquare
    index: int = 0


@dataclass
class Move:
    from_square: int
    to_square: int
    piece_before: BoardSquare
    piece_after: BoardSquare
    kill_pieces: list[Piece] = field(default_factory=list)


def copy_move(move: Move) -> Move:
    return Move(
        from_square=move.from_square,
        to_square=move.to_square,
        piece_before=move.piece_before,
        piece_after=move.piece_after,
        kill_pieces=move.kill_pieces.copy(),
    )


def do_move(board: Damboard, move: Move):
    board[move.from_square] = BoardSquare.EMPTY
    board[move.to_square] = move.piece_after
    for piece in move.kill_pieces:
        board[piece.index] = BoardSquare.EMPTY


def undo_move(board: Damboard, move: Move):
    board[move.from_square] = move.piece_before
    board[move.to_square] = BoardSquare.EMPTY
    for piece in move.kill_pieces:
        board[piece.index] = piece.value


def move_to_str(move: Move, movelist: list[Move], board: Damboard) -> str:
    return " "
