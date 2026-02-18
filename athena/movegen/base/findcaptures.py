from athena.core.player import Player
from athena.damboard.damboard import Damboard
from athena.movegen.base.basemove import BaseMove


class FindCaptures:
    def __init__(
        self,
        board: Damboard,
        player: Player,
        moves: tuple[BaseMove, ...],
        promo_squares: set[int],
    ):
        self.board: Damboard = board
        self.player: Player = player
        self.moves: tuple[BaseMove, ...] = moves
        self.promo_squares: set[int] = promo_squares
