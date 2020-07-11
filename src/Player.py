import random

from Errors import WrongChessError, ChessOverlapError
from Utilities import Utilities

default_chesses = [
    (4, -8),
    (4, -7),
    (4, -6),
    (4, -5),
    (3, -7),
    (3, -6),
    (3, -5),
    (2, -6),
    (2, -5),
    (1, -5)
]

default_destination = [Utilities.reflect(chess) for chess in default_chesses]


class Player:

    def __init__(self, color, board):
        self.color = color
        self.board = board
        self.chesses = [Utilities.rotateToGlobal(self.color, chess) for chess in default_chesses]
        self.populateBoard()
        self.destination_area = [Utilities.rotateToGlobal(self.color, corner) for corner in default_destination]
        self.win = False

    def populateBoard(self):
        for chess in self.chesses:
            self.board.set(chess, self.color.value)

    def isWinning(self):
        for chess in self.chesses:
            if not chess in self.destination_area:
                return
        self.win = True

    # decide a move for player, in the form of [(orig_x,orig_y),(dest_x,dest_y)]
    def decide(self):

        while True:
            orig = random.choice(self.chesses)
            possible_dests = self.board.treeSearch(orig)
            if possible_dests:
                break
        if not self.board.checkColor(orig, self.color):
            raise WrongChessError
        dest = random.choice(possible_dests)
        if not self.board.checkEmpty(dest):
            raise ChessOverlapError
        return [orig, dest]

    def inspectChess(self, coord):
        pass

    def updateBoard(self, move):
        orig, dest = move
        self.board.set(orig, 0)
        self.board.set(dest, self.color.value)

    def updateChesses(self, move):
        orig, dest = move
        self.chesses = [dest if x == orig else x for x in self.chesses]

    def makeMove(self):
        move = self.decide()
        self.updateChesses(move)
        self.updateBoard(move)
        self.isWinning()
            # move = [(2, -5), (1, -2)]
            # self.updateChesses(move)
            # self.updateBoard(move)
            # self.isWinning()
            # print(self.board.treeSearch((1, -5)))
