from enum import Enum


class Player(Enum):
    """Enumeration representing a player in the game.

    Each player has a color (WHITE or BLACK) and can determine their opponent.
    """

    WHITE = 0
    BLACK = 1

    @property
    def opponent(self):
        """Get the opponent player.

        Returns:
            Player: The opponent player (WHITE if current is BLACK, BLACK if current is WHITE).
        """
        return Player(1 - self.value)
