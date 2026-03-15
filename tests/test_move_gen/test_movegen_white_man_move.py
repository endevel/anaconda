from athena.core.player import Player
from athena.damboard.damboard import Damboard
from athena.movegen.movegen import MoveGen


def test_white_man_movegen_01():
    board = Damboard()
    board.setup("W:W29,30:B11,15.")
    movegen = MoveGen(Player.WHITE)
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 3

def test_white_man_movegen_02():
    board = Damboard()
    board.setup("W:W25,26:B11,15.")
    movegen = MoveGen(Player.WHITE)
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 4

def test_white_man_movegen_03():
    board = Damboard()
    board.setup("W:W5,9:B11,15.")
    movegen = MoveGen(Player.WHITE)
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 2
    