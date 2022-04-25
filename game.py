from enum import IntEnum


class Move(IntEnum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Game:
    def __init__(self, board=None) -> None:
        if not board:
            self.board = [
                [2, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
        else:
            self.board = board

    def move(direction: Move) -> None:
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass


if __name__ == "__main__":
    pass