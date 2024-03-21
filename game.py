"""
2048 Game

interview question from a certain company
"""

from random import randint

from typing import Optional


class Game:
    """The Game!"""

    # NEW_TILES_PER_TURN = 1
    NEW_TILE_VALUE = 1

    BOARD_SIZE = 4  #TODO variable board shape and size

    def __init__(self, board: Optional[list[list[int]]] = None) -> None:
        if board:  # assume that input is in my format
            # TODO error check board and convert if necessary
            self.board = board
        else:
            # use default board
            self.board = [
                [0 for _ in range(Game.BOARD_SIZE)] for _ in range(Game.BOARD_SIZE)
            ]

            self.generate()

        print("Controls: (includes vim keybindings!)")
        for k, v in Game.CONTROLS.items():
            print(f"{k}\t: {', '.join(val for val in v)}")
        print()
        self.display_board()

    # str direction to int di, dj (like dx, dy, but accounting for matrix indexing direction)
    DIRECTIONS = {
        "up": ("c", True),
        "down": ("c", False),
        "left": ("r", True),
        "right": ("r", False),
    }

    @staticmethod
    def get_iteration_params(command: str) -> Optional[tuple[str, bool]]:
        """Convert the command"""
        for k, v in Game.CONTROLS.items():
            if command in v:
                return Game.DIRECTIONS[k]

        print("Invalid command. Try again.")
        return None

    @staticmethod
    def resolve_row_col(row_or_col: str, i, j) -> tuple[int, int]:
        """Sometimes we want to iterate rows first. Other times we want to iterate columns first."""
        return i if row_or_col == "r" else j, j if row_or_col == "r" else i

    def move(self, command: str) -> None:
        """
        Given a command, updates the game state.
        """
        iteration = self.get_iteration_params(command)

        if iteration is None:
            return

        row_or_col, direc = iteration

        a, b, c = (
            (0 if direc else Game.BOARD_SIZE - 1),
            (Game.BOARD_SIZE if direc else -1),
            (1 if direc else -1),
        )

        for i in range(Game.BOARD_SIZE):
            stack = []
            for j in range(a, b, c):
                x, y = self.resolve_row_col(row_or_col, i, j)

                cur = self.board[x][y]
                if cur == 0:
                    continue
                while stack and stack[-1] == cur:
                    stack.pop()
                    cur *= 2

                stack.append(cur)

            stack = stack + [0] * (Game.BOARD_SIZE - len(stack))

            for j, val in zip(range(a, b, c), stack):
                x, y = self.resolve_row_col(row_or_col, i, j)

                self.board[x][y] = val

        self.generate()

    def generate(self) -> None:
        """
        Generates a value into a random empty slot
        """
        zeros = sum(1 for row in self.board for cell in row if cell == 0)

        location = randint(0, zeros)

        for row_ind in range(Game.BOARD_SIZE):
            for col_ind in range(Game.BOARD_SIZE):
                if self.board[row_ind][col_ind] != 0:
                    continue

                if location == 0:
                    self.board[row_ind][col_ind] = self.NEW_TILE_VALUE
                    return
                location -= 1

    def __str__(self) -> str:
        """str is "informal" representation, whatever that means"""
        return "\n".join([" ".join([str(n) for n in row]) for row in self.board])

    def display_board(self) -> None:
        """Prints the board output with a starting newline for padding"""
        print()
        print(self)

    CONTROLS = {
        "quit": {"quit", "q"},
        "up": {"up", "k"},
        "down": {"down", "j"},
        "left": {"left", "h"},
        "right": {"right", "l"},
    }

    def play(self):
        """
        display game state to stdout, get move from stdin, update game state, repeat
        """
        while (command := input("Move: ")) not in Game.CONTROLS["quit"]:
            self.move(command)

            self.display_board()


if __name__ == "__main__":
    g = Game()

    g.play()
