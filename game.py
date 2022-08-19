from enum import IntEnum


class Direction(IntEnum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Game:
    def __init__(self, board=None, generation=1) -> None:
        if not board:  # use default board
            self.board = [
                [2, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
        else:
            # assume that input is in my format
            # TODO convert 1D (length 16) board into 2D board (4x4)
            self.board = board

        self.generation = generation

    def move(direction: Direction) -> None:
        pass

    def generate(self) -> None:
        # generate {self.generation} number of values (for now, just the value 2) into random empty (value 0) spaces
        pass

    def __str__(self) -> str:
        # str is "informal" representation
        pass

    def __repr__(self) -> str:
        # repr is "formal" representation
        pass


if __name__ == "__main__":
    # TODO generate random board
    pass