from athena.core.move import Move
from athena.damboard.damboard import Damboard
from athena.movegen.base.factories import gen_std_white_move_finder


def test_std_white_man_find_moves_01():
    board = Damboard()
    movelist: list[Move] = []
    board.setup("W:W29,30:B11,15.")
    find_moves = gen_std_white_move_finder(board)
    find_moves.find_moves(81, movelist)
    assert len(movelist) == 1
    find_moves.find_moves(83, movelist)
    assert len(movelist) == 3


def test_std_white_man_find_moves_02():
    board = Damboard()
    movelist: list[Move] = []
    board.setup("W:W24,28:B11,15.")  # у шашки 28 нет ходов, у шашки 24 есть 2 хода
    find_moves = gen_std_white_move_finder(board)
    find_moves.find_moves(78, movelist)
    assert len(movelist) == 0
    find_moves.find_moves(67, movelist)
    assert len(movelist) == 2
