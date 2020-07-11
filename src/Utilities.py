import math
from matplotlib import path

from PlayerColor import PlayerColor
from Direction import Direction


class Utilities:
    @staticmethod
    def coordToScreenPos(coord):
        scale = 30
        x, y = coord[0], coord[1]
        return round((x + 0.5 * y) * scale), round((y * math.sqrt(3) / 2) * scale)

    @staticmethod
    def screenPosToCoord(pos):
        scale = 30
        px, py = pos
        return round((px - py / math.sqrt(3)) / scale),round(py / (scale * math.sqrt(3) / 2))

    @staticmethod
    def rotateCounterClockWise(coord):
        # after some high school math: we finally got the rotation equation!!!
        # that is to rotate a coord counterClockWise 60 degree
        # (x0, y0) -> (-y0, x0 + y0)
        x, y = coord[0], coord[1]
        return -y, x + y

    @staticmethod
    def rotateClockWise(coord):
        # (x0, y0) -> (x0 + y0, -x0)
        x, y = coord[0], coord[1]
        return x + y, -x

    @staticmethod
    def reflect(coord):
        x, y = coord[0], coord[1]
        return -x, -y

    @staticmethod
    def inPolygon(polygon, coord):
        polygon_path = path.Path(polygon)
        return polygon_path.contains_points([coord])[0]

    @staticmethod
    def inBoard(coord):
        polygon = [(4, 0),
                   (4, 4),
                   (0, 4),
                   (-4, 8),
                   (-4, -4),
                   (-8, 4),
                   (-4, 0),
                   (-4, -4),
                   (0, -4),
                   (4, -8),
                   (4, -4),
                   (8, -4)
                   ]
        black_list = [(-5, 0), (-5, -1), (-6, 1)]

        return Utilities.inPolygon(polygon, coord) and (coord not in black_list)

    @staticmethod
    def oneStep(coord, direction):
        return Utilities.coordAdd(coord, direction.value)

    @staticmethod
    def coordAdd(coord1, coord2):
        return tuple(sum(x) for x in zip(coord1, coord2))

    @staticmethod
    def rotateToFirstPerson(color, coord):
        if color == PlayerColor.RED:
            return coord
        if color == PlayerColor.GREEN:
            return Utilities.rotateClockWise(coord)
        if color == PlayerColor.PURPLE:
            return Utilities.rotateClockWise(Utilities.rotateClockWise(coord))
        if color == PlayerColor.YELLOW:
            return Utilities.reflect()
        if color == PlayerColor.BLUE:
            return Utilities.rotateCounterClockWise(Utilities.rotateCounterClockWise(coord))
        if color == PlayerColor.WHITE:
            return Utilities.rotateCounterClockWise(coord)

    @staticmethod
    def rotateToGlobal(color, coord):
        if color == PlayerColor.RED:
            return coord
        if color == PlayerColor.GREEN:
            return Utilities.rotateCounterClockWise(coord)
        if color == PlayerColor.PURPLE:
            return Utilities.rotateCounterClockWise(Utilities.rotateCounterClockWise(coord))
        if color == PlayerColor.YELLOW:
            return Utilities.reflect(coord)
        if color == PlayerColor.BLUE:
            return Utilities.rotateClockWise(Utilities.rotateClockWise(coord))
        if color == PlayerColor.WHITE:
            return Utilities.rotateClockWise(coord)

    @staticmethod
    def coordToBoardArray(coord):
        x, y = coord
        return x + 8, y + 8

    @staticmethod
    def boardArrayToCoord(idx):
        x, y = idx
        return x - 8, y - 8

# if __name__ == '__main__':
#     print(Utilities.oneStep((1, 1), Direction.UP_RIGHT.value))
