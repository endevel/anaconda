from athena.core.board_square import BoardSquare
from athena.core.player import Player


def test_owner():
    wm = BoardSquare.WHITE_PIECE
    bm = BoardSquare.BLACK_PIECE
    assert wm.owner == Player.WHITE
    assert bm.owner == Player.BLACK
    assert wm.is_opponent(Player.BLACK)
    assert bm.is_opponent(Player.WHITE)


def test_invalid_owner():
    assert BoardSquare.EMPTY.owner == Player.UNDEFINED
    assert BoardSquare.OUT_OF_BOUNDS.owner == Player.UNDEFINED
    assert BoardSquare.TAKEN.owner == Player.UNDEFINED
