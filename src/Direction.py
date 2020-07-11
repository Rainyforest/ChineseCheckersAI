from enum import Enum, unique


@unique
class Direction(Enum):
    RIGHT = (1, 0)
    UP_RIGHT = (0, 1)
    UP_LEFT = (-1, 1)
    LEFT = (-1, 0)
    DOWN_LEFT = (0, -1)
    DOWN_RIGHT = (1, -1)
