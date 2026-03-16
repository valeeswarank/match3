"""
Game controller responsible for input/output orchestration.
"""

from model.game import Game, VALID_COMMANDS, VALID_SYMBOLS
from view.console_view import ConsoleView


class GameController:
    """
    Handles gameplay loop and user input.
    """

    def start(self) -> None:

        print("> Please enter field size (width and height) and up to 5 bricks set:")
        print("> Example: 5 8 H^^* V*@^")

        data = input("> ").split()

        if len(data) < 3:
            print("> Invalid input!")
            return

        width = int(data[0])
        height = int(data[1])
        bricks = data[2:7]

        for brick in bricks:
            if brick[0].upper() not in ["H", "V"] or len(brick) != 4:
                print(f"> Invalid brick: {brick}")
                return

            if any(s not in VALID_SYMBOLS for s in brick[1:]):
                print(f"> Invalid symbol in brick: {brick}")
                return

        game = Game(width, height, bricks)

        while True:

            while not game.game_over:

                ConsoleView.render(game)

                cmd_line = input("> Enter up to 2 commands (L,R,D): ").upper()

                commands = [c for c in cmd_line if c in VALID_COMMANDS]

                game.step(commands)

            ConsoleView.render(game)

            print("> Game Over.")

            choice = input("> Enter S to start over or Q to quit: ").upper()

            if choice == "S":
                game.reset()
            else:
                print("> Thank you for playing Match-3!")
                break