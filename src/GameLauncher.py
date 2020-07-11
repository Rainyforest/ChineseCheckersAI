import time

import numpy as np
import pygame

from PlayerColor import PlayerColor
from Game import Game
from Utilities import Utilities


class GameLauncher:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center = (int(width / 2), int(height / 2))

    def run(self):
        checker_game = Game()
        # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("../pics/doge_icon.jpg")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Chinese Checkers")

        # create a surface on screen that has the size of 800 x 600
        screen = pygame.display.set_mode((self.width, self.height))
        screen.fill([0, 0, 0])  # fill screen with black

        self.render(checker_game, screen)
        pygame.display.update()

        # define a variable to control the main loop
        running = True

        step = False
        # main loop
        while running:

            if step:
                time.sleep(0.5)
                checker_game.step()
                # step = False
            screen.fill([0, 0, 0])  # fill screen with black
            self.render(checker_game, screen)
            pygame.display.update()
            if checker_game.decided:
                step = False  # freeze the game

            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if event.button == 1:  # Left mouse button.
                        # Check if the rect collides with the mouse pos.
                        coord = self.getClickCoord(pos)
                        player = checker_game.board.get(coord)
                        print(PlayerColor(player).name)

    def getClickCoord(self, pos):
        pos = Utilities.coordAdd([-self.center[0], -self.center[1]], pos)
        orig_pos = pos[0], -pos[1]
        return Utilities.screenPosToCoord(orig_pos)

    def render(self, checker_game, screen):
        board = checker_game.board.grid
        for x, y in np.ndindex(board.shape):
            if board[x, y] in [1, 2, 3, 4, 5, 6]:
                color = PlayerColor(board[x, y]).RGB()
            elif board[x, y] == 0:
                color = (50, 50, 50)
            else:
                color = (0, 0, 0)
            self.render_dot(Utilities.coordToScreenPos(Utilities.boardArrayToCoord((x, y))), color, 15, screen)

    def render_dot(self, pos, color, radius, screen):
        pos = Utilities.coordAdd(self.center, [pos[0], -pos[1]])
        pygame.draw.circle(screen, list(color),
                           pos, radius,
                           0)  # draw red circle
    #
    # def render_ngon(self, pos, color, n, radius, screen):
    #     pi = 3.1415
    #     n, r = n, radius
    #     x, y = Utilities.coordAdd(self.center, list(pos))
    #     pygame.draw.polygon(screen, color, [
    #         (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
    #         for i in range(n)
    #     ])


# define a main function
def main():
    gl = GameLauncher(800, 600)
    gl.run()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
