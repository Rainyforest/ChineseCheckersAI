from enum import unique, Enum


@unique
class PlayerColor(Enum):
    RED = 1
    GREEN = 2
    PURPLE = 3
    YELLOW = 4
    BLUE = 5
    WHITE = 6

    def RGB(self):
        if self == PlayerColor.RED:
            return 255, 51, 0
        if self == PlayerColor.GREEN:
            return 0, 204, 102
        if self == PlayerColor.PURPLE:
            return 204, 51, 255
        if self == PlayerColor.YELLOW:
            return 255, 255, 26
        if self == PlayerColor.BLUE:
            return 102, 153, 255
        if self == PlayerColor.WHITE:
            return 242, 242, 242
