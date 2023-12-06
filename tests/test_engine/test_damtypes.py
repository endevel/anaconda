from anaconda.engine.damtypes import BoardSquareStatus, PieceRank, Player


def test_player_create():
    player = Player.white
    assert player is not None
    
def test_board_square_status_white_man():
    wm = BoardSquareStatus.white_man    
    assert wm.player == Player.white
    assert wm.piece_rank == PieceRank.man

def test_board_square_status_white_king():
    wm = BoardSquareStatus.white_king    
    assert wm.player == Player.white
    assert wm.piece_rank == PieceRank.king
    
def test_board_square_status_black_man():
    wm = BoardSquareStatus.black_man    
    assert wm.player == Player.black
    assert wm.piece_rank == PieceRank.man

def test_board_square_status_black_king():
    wm = BoardSquareStatus.black_king    
    assert wm.player == Player.black
    assert wm.piece_rank == PieceRank.king

    