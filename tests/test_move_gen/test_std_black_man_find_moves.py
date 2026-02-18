from athena.core.move import Move
from athena.damboard.damboard import Damboard
from athena.movegen.base.factories import (
    gen_std_black_move_finder,
    gen_std_white_move_finder,
)


def test_std_black_man_find_moves_01():
    board = Damboard()
    movelist: list[Move] = []
    board.setup("B:W29,30:B11,15.")
    find_moves = gen_std_black_move_finder(board)
    find_moves.find_moves(36, movelist)
    assert len(movelist) == 1
    find_moves.find_moves(45, movelist)
    assert len(movelist) == 3


def test_std_black_man_find_moves_02():
    board = Damboard()
    movelist: list[Move] = []
    board.setup("B:W29,30:B2,3.")
    find_moves = gen_std_black_move_finder(board)
    find_moves.find_moves(14, movelist)
    assert len(movelist) == 2
    find_moves.find_moves(16, movelist)
    assert len(movelist) == 4
