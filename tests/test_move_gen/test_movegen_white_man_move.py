from athena.core.board_square import BoardSquare
from athena.core.player import Player
from athena.damboard.damboard import Damboard
from athena.movegen.movegen import MoveGen


def test_move_gen_white_man_move_01():
    board = Damboard()
    movegen = MoveGen(Player.WHITE, board.size)
    board.setup("W:W31:B4.")
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 2
    assert movegen.move_list[0].from_square == 85
    assert movegen.move_list[1].from_square == 85
    assert movegen.move_list[0].piece_before == BoardSquare.WHITE_PIECE
    assert movegen.move_list[1].piece_before == BoardSquare.WHITE_PIECE
    assert movegen.move_list[0].piece_after == BoardSquare.WHITE_PIECE
    assert movegen.move_list[1].piece_after == BoardSquare.WHITE_PIECE


def test_move_gen_white_man_move_02():
    board = Damboard()
    movegen = MoveGen(Player.WHITE, board.size)
    board.setup("W:W26,30,31:B13,17,22.")
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 3


def test_move_gen_white_man_move_03():
    board = Damboard()
    movegen = MoveGen(Player.WHITE, board.size)
    board.setup("W:W29,30,31,32:B1,2,3,4.")
    movegen.generate_all_moves(board)
    assert len(movegen.move_list) == 7
