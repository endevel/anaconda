from athena.core.player import Player
from athena.damboard.damboard import Damboard
from athena.movegen.base.basemove import BaseMove
from athena.movegen.base.findmoves import FindMoves


def gen_std_white_move_finder(board: Damboard) -> FindMoves:
    move_right: BaseMove = BaseMove(direction=-board.width - 1, length=1)
    move_left: BaseMove = BaseMove(direction=-board.width - 3, length=1)
    return FindMoves(
        board, Player.WHITE, tuple([move_right, move_left]), board.top_promo_squares
    )


def gen_std_white_king_move_finder(board: Damboard) -> FindMoves:
    move_right: BaseMove = BaseMove(
        direction=-board.width - 1, length=board.max_move_length
    )
    move_left: BaseMove = BaseMove(
        direction=-board.width - 3, length=board.max_move_length
    )
    move_right_back: BaseMove = BaseMove(
        direction=board.width + 1, length=board.max_move_length
    )
    move_left_back: BaseMove = BaseMove(
        direction=board.width + 3, length=board.max_move_length
    )
    return FindMoves(
        board,
        Player.WHITE,
        tuple([move_right, move_left, move_right_back, move_left_back]),
        board.top_promo_squares,
    )


def gen_std_black_move_finder(board: Damboard) -> FindMoves:
    move_right: BaseMove = BaseMove(direction=board.width + 1, length=1)
    move_left: BaseMove = BaseMove(direction=board.width + 3, length=1)
    return FindMoves(
        board, Player.BLACK, tuple([move_right, move_left]), board.bottom_promo_squares
    )


def gen_std_black_king_move_finder(board: Damboard) -> FindMoves:
    move_right: BaseMove = BaseMove(
        direction=board.width + 1, length=board.max_move_length
    )
    move_left: BaseMove = BaseMove(
        direction=board.width + 3, length=board.max_move_length
    )
    move_right_back: BaseMove = BaseMove(
        direction=-board.width - 1, length=board.max_move_length
    )
    move_left_back: BaseMove = BaseMove(
        direction=-board.width - 3, length=board.max_move_length
    )
    return FindMoves(
        board,
        Player.BLACK,
        tuple([move_right, move_left, move_right_back, move_left_back]),
        board.bottom_promo_squares,
    )
