# interview question from a certain company...
from random import randint


# str direction to int di, dj (like dx, dy, but accounting for matrix indexing direction)
direction: dict[str, tuple[int, int]] = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}


class Game:
    NEW_TILES_PER_TURN = 1
    NEW_TILE_VALUE = 2  # TODO make new tile value variable

    def __init__(self, board=None) -> None:
        if not board:  # use default board
            self.board = [
                [2, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
        else:
            # assume that input is in my format
            # TODO error check board and convert if necessary
            self.board = board


    def move(direction: str) -> None:
        """
        Given a str direction, updates the game state.
        """
        # TODO
        pass

    
    def generate(self) -> None:
        """
        Generates self.NEW_TILES_PER_TURN values into random empty slots
        """
        zeros = sum(1 for c in r for r in self.board if c == 0)

        location = randint(zeros)

        # TODO generate more than one random value
        # TODO is there a better way to do this?
        # for _ in range(self.NEW_TILES_PER_TURN):

        for r in len(self.board):
            for c in len(self.board[0]):
                if location == 0:
                    self.board[r][c] = self.NEW_TILE_VALUE
                    return
                location -= 1


    def __str__(self) -> str:
        """str is "informal" representation, whatever that means"""
        # TODO 
        return f""


    def __repr__(self) -> str:
        """repr is "formal" representation, whatever that means"""
        # TODO 
        return f""


    
    def play(self):
        """
        display game state to stdout, get move from stdin, update game state, repeat
        """
        # TODO 
        print("Use 'quit' to quit. Valid commands are 'up', 'down', 'left', and 'right'.")
        while command := input() != "quit":
            print("zzz")



if __name__ == "__main__":
    g = Game()

    g.play()