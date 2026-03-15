from athena.core.player import Player
from athena.damboard.damboard import Damboard
from athena.movegen.movegen import MoveGen


def test_black_man_movegen_01():
    board = Damboard()
    board.setup("B:W29,30:B11,15.")
    movegen = MoveGen(Player.BLACK)
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 3

def test_black_man_movegen_02():
    board = Damboard()
    board.setup("B:W9,13,14:B1,5.")
    movegen = MoveGen(Player.BLACK)
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 1    

def test_black_man_movegen_03():
    board = Damboard()
    board.setup("B:W9,13,14:B24,28.")
    movegen = MoveGen(Player.BLACK)
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 2    
    