from dataclasses import dataclass


@dataclass(frozen=True)
class BaseMove:
    direction: int
    length: int
