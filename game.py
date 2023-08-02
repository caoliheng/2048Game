"""
2048 Game

interview question from a certain company
"""

from random import randint

from typing import Optional


class Game:
    """The Game!"""
    NEW_TILES_PER_TURN = 1
    NEW_TILE_VALUE = 1  # TODO make new tile value variable

    # str direction to int di, dj (like dx, dy, but accounting for matrix indexing direction)
    DIRECTIONS: dict[str, tuple[int, int]] = {
    "up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

    # TODO variable board size
    BOARD_SIZE = 4, 4

    def __init__(self, board: Optional[list[list[int]]]=None) -> None:
        if not board:  # use default board
            self.board = [[0 for _ in range(Game.BOARD_SIZE[0])] for _ in range(Game.BOARD_SIZE[1])]

            self.board[0][0] = Game.NEW_TILE_VALUE
        else:
            # assume that input is in my format
            # TODO error check board and convert if necessary
            self.board = board

    def move(self, direction: str) -> None:
        """
        Given a str direction, updates the game state.
        """
        # TODO

    def generate(self) -> None:
        """
        Generates Game.NEW_TILES_PER_TURN values into random empty slots
        """
        zeros = sum(1 for row in self.board for cell in self.board if cell == 0)

        location = randint(0, zeros)

        # TODO generate more than one random value
        # TODO is there a better way to do this?
        # for _ in range(self.NEW_TILES_PER_TURN):

        for row_ind in range(Game.BOARD_SIZE[0]):
            for col_ind in range(Game.BOARD_SIZE[1]):
                if location == 0:
                    self.board[row_ind][col_ind] = self.NEW_TILE_VALUE
                    return
                location -= 1

    def __str__(self) -> str:
        """str is "informal" representation, whatever that means"""
        # TODO
        return ""

    def __repr__(self) -> str:
        """repr is "formal" representation, whatever that means"""
        # TODO
        return ""

    def play(self):
        """
        display game state to stdout, get move from stdin, update game state, repeat
        """
        # TODO
        print("Use 'quit' to quit. Valid commands are 'up', 'down', 'left', and 'right'.")
        while command := input() != "quit":
            print(f"{command} zzz")

            match command:
                case "up":
                    print("up")
                case _:
                    print("anything but up")


if __name__ == "__main__":
    g = Game()

    g.play()
