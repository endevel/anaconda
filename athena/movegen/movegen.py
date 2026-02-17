from athena.core.move import Move


class MoveGen:
    def __init__(self, board, player):
        self.board = board
        self.player = player

    def __call__(self, movelist: list[Move]):
        pass
