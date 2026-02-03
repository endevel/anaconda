from enum import Enum


class Team(Enum):
    WHITE = 0
    BLACK = 1

    @property
    def opponent(self):
        return Team(1 - self.value)
