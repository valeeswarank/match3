"""
Match-3 Falling Bricks Game - Beginner Version
==============================================

This game implements a falling bricks Match-3 game. Bricks are made of 3 blocks,
can be horizontal or vertical, and can be moved left, right, or dropped down.
The goal is to place all bricks and remove horizontal or vertical lines of
3+ matching symbols.
"""

EMPTY: str = "."


class Brick:
    """Represents a 3-block brick (horizontal or vertical)."""

    def __init__(self, definition: str, field_width: int) -> None:
        """
        Initialize a brick using its definition and the game field width.

        Args:
            definition (str): Brick definition string such as "H^^*" or "V*@^".
                The first character indicates orientation ('H' or 'V'), followed
                by three symbols.
            field_width (int): Width of the game field used to calculate the
                starting column position.
        """
        self.orientation: str = definition[0].upper()
        self.symbols: str = definition[1:]

        if self.orientation == "H":
            self.row: int = 0
            self.col: int = (field_width - 3) // 2
        else:
            self.row: int = 0
            self.col: int = (field_width - 1) // 2

    def cells(self, row: int | None = None, col: int | None = None) -> list[tuple[int, int, str]]:
        """
        Return the list of grid cells occupied by the brick.

        Args:
            row (int | None): Optional row position to test. Defaults to the
                brick's current row.
            col (int | None): Optional column position to test. Defaults to the
                brick's current column.

        Returns:
            list[tuple[int, int, str]]: A list of tuples containing
                (row, column, symbol) representing each block of the brick.
        """
        if row is None:
            row = self.row
        if col is None:
            col = self.col

        if self.orientation == "H":
            return [(row, col + i, self.symbols[i]) for i in range(3)]
        else:
            return [(row + i, col, self.symbols[i]) for i in range(3)]