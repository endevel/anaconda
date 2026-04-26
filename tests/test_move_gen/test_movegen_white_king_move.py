from athena.core.player import Player
from athena.damboard.damboard import Damboard
from athena.movegen.movegen import MoveGen


def test_move_gen_white_king_move_01():
    board = Damboard()
    movegen = MoveGen(Player.WHITE, board.size)
    board.setup("W:WK29,K30:B1,2,3,4.")
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 13


def test_move_gen_white_king_move_02():
    board = Damboard()
    movegen = MoveGen(Player.WHITE, board.size)
    board.setup("W:WK29,K30,K31,K32:B1,2,3,4.")
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 27
