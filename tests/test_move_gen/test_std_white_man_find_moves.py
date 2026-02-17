from athena.core.move import Move
from athena.damboard.damboard import Damboard
from athena.movegen.base.factories import gen_std_white_move_finder


def test_std_white_man_find_moves():
    board = Damboard()
    movelist: list[Move] = []
    board.setup("W:W29,30:B11,15.")
    find_moves = gen_std_white_move_finder(board)
    find_moves.find_moves(81, movelist)
    assert len(movelist) == 1
    find_moves.find_moves(83, movelist)
    assert len(movelist) == 3
