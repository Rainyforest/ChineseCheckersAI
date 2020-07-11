import numpy as np

from Direction import Direction
from Errors import GridOutOfBoundError
from Utilities import Utilities


class Board:
    def __init__(self):
        self.grid = self.init_board()

    def __getitem__(self, key):
        x, y = key
        if x < 0 or y < 0 or x > 16 or y > 16:
            return -1
        return self.grid[key]

    def __setitem__(self, key, value):
        x, y = key
        if x < 0 or y < 0 or x > 16 or y > 16:
            raise GridOutOfBoundError
        self.grid[key] = value

    @staticmethod
    def init_board():
        board = np.zeros(shape=(17, 17))
        for x, y in np.ndindex(board.shape):
            coord = Utilities.boardArrayToCoord((x, y))
            if not Utilities.inBoard(coord):
                board[x, y] = -1
        return board

    def get(self, coord):
        return self[Utilities.coordToBoardArray(coord)]

    def set(self, coord, val):
        self[Utilities.coordToBoardArray(coord)] = val

    def empty(self, coord):
        self.set(coord, 0)

    def checkColor(self, coord, color):
        return self.get(coord) == color.value

    def checkEmpty(self, coord):
        return self.get(coord) == 0

    def checkInBoard(self, coord):
        return self.get(coord) != -1

    def hop(self, coord, direction):
        pos = coord
        count = 0
        while True:
            next_pos = Utilities.oneStep(pos, direction)
            if self.checkEmpty(next_pos):
                count += 1
                pos = next_pos
            else:
                break
        if not self.checkInBoard(next_pos):
            return None
        else:
            pos = next_pos
            count += 1
            for i in range(count):
                next_pos = Utilities.oneStep(pos, direction)
                if self.checkEmpty(next_pos):
                    pos = next_pos
                else:
                    return None
            return pos

    # def multiHop(self, coord, dir_list):
    #     temp = self.get(coord)
    #     self.empty(coord)
    #     pos = coord
    #     for direction in dir_list:
    #         next_pos = self.hop(pos, direction)
    #         if not next_pos:
    #             return None
    #         pos = next_pos
    #     self.set(coord, temp)
    #     return pos

    def treeSearch(self, coord):
        # first add all valid rolls to the results
        rolls = []
        for d in Direction:
            roll_result = self.roll(coord, d)
            if roll_result:
                rolls.append(roll_result)
        # perform BFS tree search for multiHop
        visited = []
        frontier = [coord]
        while frontier:
            curr = frontier.pop(0)
            visited.append(curr)
            for direction in Direction:
                hop_result = self.hop(curr, direction)
                if hop_result and (hop_result not in visited):
                    frontier.append(hop_result)
        hops = visited
        hops.remove(coord)
        return rolls + hops

    def roll(self, coord, direction):
        result = Utilities.oneStep(coord, direction)
        if self.checkEmpty(result):  # self.checkInBoard(coord) and
            return result
        return None
