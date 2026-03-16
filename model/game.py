from .brick import Brick, EMPTY

# Constants
VALID_SYMBOLS: set[str] = {"~", "^", "*", "@"}
VALID_COMMANDS: list[str] = ["L", "R", "D"]


class Game:
    """Main game logic for Match-3 falling bricks."""

    def __init__(self, width: int, height: int, bricks: list[str]) -> None:
        """
        Initialize the game with field dimensions and brick definitions.

        Args:
            width (int): Width of the game field.
            height (int): Height of the game field.
            bricks (list[str]): List of brick definitions.
        """
        self.width: int = width
        self.height: int = height
        self.initial_bricks: list[str] = bricks[:]
        self.reset()

    def reset(self) -> None:
        """
        Reset the game to its initial state.
        """
        self.field: list[list[str]] = [[EMPTY for _ in range(self.width)] for _ in range(self.height)]
        self.bricks: list[str] = self.initial_bricks[:]
        self.current: Brick | None = None
        self.game_over: bool = False
        self.spawn()

    def valid(self, coords: list[tuple[int, int, str]]) -> bool:
        """
        Check whether a set of brick coordinates is valid.
        """
        for r, c, _ in coords:
            if r < 0 or r >= self.height:
                return False
            if c < 0 or c >= self.width:
                return False
            if self.field[r][c] != EMPTY:
                return False
        return True

    def spawn(self) -> None:
        """
        Spawn the next brick from the queue.
        """
        if not self.bricks:
            self.game_over = True
            return

        definition = self.bricks.pop(0)
        brick = Brick(definition, self.width)

        if self.valid(brick.cells()):
            self.current = brick
        else:
            self.game_over = True

    def place(self) -> None:
        """
        Place the current brick permanently onto the field.
        """
        for r, c, sym in self.current.cells():
            self.field[r][c] = sym

        self.remove_matches()
        self.spawn()

    def find_matches(self) -> set[tuple[int, int]]:
        """
        Find all horizontal and vertical matches of three identical symbols.
        """
        to_remove: set[tuple[int, int]] = set()

        for r in range(self.height):
            for c in range(self.width - 2):
                a, b, d = self.field[r][c], self.field[r][c + 1], self.field[r][c + 2]
                if a != EMPTY and a == b == d:
                    to_remove.update([(r, c), (r, c + 1), (r, c + 2)])

        for c in range(self.width):
            for r in range(self.height - 2):
                a, b, d = self.field[r][c], self.field[r + 1][c], self.field[r + 2][c]
                if a != EMPTY and a == b == d:
                    to_remove.update([(r, c), (r + 1, c), (r + 2, c)])

        return to_remove

    def remove_matches(self) -> None:
        """
        Remove all matched cells from the field.
        """
        to_remove = self.find_matches()
        for r, c in to_remove:
            self.field[r][c] = EMPTY

    def step(self, commands: list[str]) -> None:
        """
        Execute one game step.
        """
        if not self.current:
            return

        for cmd in commands[:2]:

            if cmd == "L":
                coords = self.current.cells(self.current.row, self.current.col - 1)
                if self.valid(coords):
                    self.current.col -= 1

            elif cmd == "R":
                coords = self.current.cells(self.current.row, self.current.col + 1)
                if self.valid(coords):
                    self.current.col += 1

            elif cmd == "D":
                while True:
                    coords = self.current.cells(self.current.row + 1, self.current.col)
                    if self.valid(coords):
                        self.current.row += 1
                    else:
                        break

        coords = self.current.cells(self.current.row + 1, self.current.col)

        if self.valid(coords):
            self.current.row += 1
        else:
            self.place()
                
            
