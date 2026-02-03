from athena.core.board_size import BoardSize


def test_board_size_height():
    assert BoardSize.STANDARD.height == 8
    assert BoardSize.BIG.height == 10
    assert BoardSize.LARGE.height == 12


def test_board_size_width():
    assert BoardSize.STANDARD.width == 8
    assert BoardSize.BIG.width == 10
    assert BoardSize.LARGE.width == 12


def test_board_size_start_position():
    assert (
        BoardSize.STANDARD.start_position
        == "B:W21,22,23,24,25,26,27,28,29,30,31,32:B1,2,3,4,5,6,7,8,9,10,11,12."
    )
    assert (
        BoardSize.BIG.start_position
        == "B:W31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50:B1,2,3,4,6,7,9,10,11,12,13,14,15,16,17,18,19,20."
    )
    assert (
        BoardSize.LARGE.start_position
        == "B:W45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72:B1,2,3,4,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30."
    )