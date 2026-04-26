from athena.core.player import Player
from athena.damboard.damboard import Damboard
from athena.movegen.movegen import MoveGen


def test_captures_white_man_01():
    board = Damboard()
    board.setup("W:W25,29:B22,4.")
    movegen = MoveGen(Player.WHITE, board.size)
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 1
    