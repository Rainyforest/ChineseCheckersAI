import time

from Board import Board
from Player import Player
from PlayerColor import PlayerColor
import numpy as np

from Utilities import Utilities


class Game:
    def __init__(self):
        # board is represented as a 17*17 2d array storing many
        self.board = Board()
        self.players = self.init_players()
        self.turns = 0
        self.decided = False

    def init_players(self):
        colors = list(PlayerColor)
        players = []
        for color in colors:
            players.append(Player(color, self.board))

        return players

    def step(self):
        for player in self.players:
            if not player.win:
                player.makeMove()
                # if player.color == PlayerColor.RED: print(player.chesses)
                if player.win:
                    self.updateDecided()

    def updateDecided(self):
        self.decided = not (False in [player.win for player in self.players])
