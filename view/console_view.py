"""
Console rendering view.
"""

from model.game import Game


class ConsoleView:
    """
    Responsible for rendering the game state to console.
    """

    @staticmethod
    def render(game: Game) -> None:
        display = [row[:] for row in game.field]

        if game.current:
            for r, c, sym in game.current.cells():
                if 0 <= r < game.height and 0 <= c < game.width:
                    display[r][c] = sym

        for row in display:
            print("  | " + " ".join(row) + " |")