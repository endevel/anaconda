from athena.damboard.damboard import Damboard


def test_foreach_board():
    board = Damboard()
    ndx = 0
    for square in board:
        ndx += 1
    assert ndx == 32
