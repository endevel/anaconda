from athena.core.player import Player


def test_player_opponent():
    assert Player.WHITE.opponent == Player.BLACK
    assert Player.BLACK.opponent == Player.WHITE
