from athena.core.team import Team


def test_team_opponent():
    assert Team.WHITE.opponent == Team.BLACK
    assert Team.BLACK.opponent == Team.WHITE
