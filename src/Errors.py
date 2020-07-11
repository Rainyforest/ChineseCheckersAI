class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class WrongChessError(Error):

    def __init__(self):
        self.message = "Error, not moving a chess belongs to the player."


class ChessOverlapError(Error):

    def __init__(self):
        self.message = "Error, chess is placed at an occupied grid."


class GridOutOfBoundError(Error):

    def __init__(self):
        self.message = "Error, trying to set grid out of bound."
