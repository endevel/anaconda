from athena.core.player import Player
from athena.damboard.damboard import Damboard
from athena.movegen.movegen import MoveGen


def test_move_gen_black_king_move_01():
    board = Damboard()
    movegen = MoveGen(Player.BLACK, board.size)
    board.setup("B:W29,30:BK1,K2,3,4.")
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 17
