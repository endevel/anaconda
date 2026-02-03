from enum import Enum


class Player(Enum):
    WHITE = 0
    BLACK = 1

    @property
    def opponent(self):
        return Player(1 - self.value)
