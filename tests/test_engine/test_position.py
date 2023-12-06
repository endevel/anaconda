from anaconda.engine.damboard import Position


def test_create():
    pos = Position()
    assert pos is not None
    
    