from athena.core.board_size import BoardSize
from athena.core.board_square import BoardSquare
from athena.damboard.damboard import Damboard


def test_create_default():
    board = Damboard()
    assert board is not None


def test_create_standard():
    board = Damboard(size=BoardSize.standard)
    assert board is not None
    assert board[12] == BoardSquare.black_piece
    assert board[14] == BoardSquare.black_piece
    assert board[16] == BoardSquare.black_piece
    assert board[18] == BoardSquare.black_piece
    assert board[21] == BoardSquare.black_piece
    assert board[23] == BoardSquare.black_piece
    assert board[25] == BoardSquare.black_piece
    assert board[27] == BoardSquare.black_piece
    assert board[32] == BoardSquare.black_piece
    assert board[34] == BoardSquare.black_piece
    assert board[36] == BoardSquare.black_piece
    assert board[38] == BoardSquare.black_piece

    assert board[41].is_empty
    assert board[43].is_empty
    assert board[45].is_empty
    assert board[47].is_empty
    assert board[52].is_empty
    assert board[54].is_empty
    assert board[56].is_empty
    assert board[58].is_empty

    assert board[61] == BoardSquare.white_piece
    assert board[63] == BoardSquare.white_piece
    assert board[65] == BoardSquare.white_piece
    assert board[67] == BoardSquare.white_piece
    assert board[72] == BoardSquare.white_piece
    assert board[74] == BoardSquare.white_piece
    assert board[76] == BoardSquare.white_piece
    assert board[78] == BoardSquare.white_piece
    assert board[81] == BoardSquare.white_piece
    assert board[83] == BoardSquare.white_piece
    assert board[85] == BoardSquare.white_piece
    assert board[87] == BoardSquare.white_piece


def test_standard_promo_squares():
    board = Damboard(size=BoardSize.standard)
    assert board.top_promo_squares == {12, 14, 16, 18}
    assert board.bottom_promo_squares == {81, 83, 85, 87}


def test_big_promo_squares():
    board = Damboard(size=BoardSize.big)
    assert board.top_promo_squares == {14, 16, 18, 20, 22}
    assert board.bottom_promo_squares == {121, 123, 125, 127, 129}
