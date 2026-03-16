import unittest
from model.game import Game
from model.brick import EMPTY

class TestMatch3Scenario(unittest.TestCase):
    """
    End-to-End scenario test based on the 8-step sequence.
    Tests movement constraints, command slicing, gravity, and match clearing.
    """

    def setUp(self) -> None:
        # Setup as per Step 1: 5x8 field with two specific bricks
        self.bricks = ["H^^*", "V*@^"]
        self.game = Game(5, 8, self.bricks)
        #  | . ^ ^ * . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |        

    def test_eight_step_scenario(self) -> None:
        # --- Step 1 & 2 ---
        # User enters 'LL'. First 'L' moves it to col 0. Second 'L' is invalid.
        # Auto-drop moves it to row 1.
        self.game.step(["L", "L"])
        self.assertEqual(self.game.current.col, 0, "Brick should stop at left boundary (Col 0)")
        self.assertEqual(self.game.current.row, 1, "Brick should be at row 1 after first frame")
        #  | . . . . . |
        #  | ^ ^ * . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |

        # --- Step 3 ---
        # User enters 'R'. Moved to col 1, auto-dropped to row 2.
        self.game.step(["R"])
        self.assertEqual(self.game.current.col, 1)
        self.assertEqual(self.game.current.row, 2)
        #  | . . . . . |
        #  | . . . . . |
        #  | . ^ ^ * . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        
        # --- Step 4 ---
        # User enters 'DR'. 'D' hits floor (Row 7). 'R' moves to col 2.
        # Auto-drop fails (at floor), brick 1 placed, brick 2 spawned.
        self.game.step(["D", "R"])
        
        # Verify Brick 1 is placed at the bottom (Row 7, Cols 2, 3, 4)
        self.assertEqual(self.game.field[7][2], "^")
        self.assertEqual(self.game.field[7][3], "^")
        self.assertEqual(self.game.field[7][4], "*")
        #  | . . * . . |
        #  | . . @ . . |
        #  | . . ^ . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . ^ ^ * |        
        
        # Verify Brick 2 is now active
        self.assertEqual(self.game.current.symbols, "*@^")
        self.assertEqual(self.game.current.orientation, "V")

        # --- Step 5 ---
        # User enters 'LLR'. Program only takes first 2: ['L', 'L'].
        # Center for V-brick in 5-wide is col 2. First 'L' -> Col 1.
        # Second 'L' -> Col 0. Auto-drop -> Row 1.
        self.game.step(["L", "L", "R"]) 
        self.assertEqual(self.game.current.col, 0)
        self.assertEqual(self.game.current.row, 1)
        #  | . . . . . |
        #  | * . . . . |
        #  | @ . . . . |
        #  | ^ . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . ^ ^ * |        

        # --- Step 6 ---
        # Blank command. Auto-drop -> Row 2.
        self.game.step([])
        self.assertEqual(self.game.current.row, 2)
        #  | . . . . . |
        #  | . . . . . |
        #  | * . . . . |
        #  | @ . . . . |
        #  | ^ . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . ^ ^ * |        

        # --- Step 7 ---
        # User enters 'R'. Move to col 1, auto-drop -> Row 3.
        self.game.step(["R"])
        self.assertEqual(self.game.current.col, 1)
        self.assertEqual(self.game.current.row, 3)
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . * . . . |
        #  | . @ . . . |
        #  | . ^ . . . |
        #  | . . . . . |
        #  | . . ^ ^ * |        

        # --- Step 8 ---
        # User enters 'DR'. 'D' drops V-brick to floor. 
        # Bottom cell of V-brick land at (7, 1). 'R' is blocked by Brick 1.
        # Brick 2 becomes stationary.
        self.game.step(["D", "R"])

        # MATCH CLEARING CHECK
        # Brick 2 bottom is '^' at (7, 1). 
        # Brick 1 had '^' at (7, 2) and (7, 3).
        # This forms a 3-match of '^' at (7, 1), (7, 2), (7, 3).
        self.assertEqual(self.game.field[7][1], EMPTY, "Match at (7, 1) should be cleared")
        self.assertEqual(self.game.field[7][2], EMPTY, "Match at (7, 2) should be cleared")
        self.assertEqual(self.game.field[7][3], EMPTY, "Match at (7, 3) should be cleared")
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . . . . . |
        #  | . * . . . |
        #  | . @ . . . |
        #  | . ^ . . * |        
        
        # The '*' at (7, 4) was not part of the match, so it stays.
        self.assertEqual(self.game.field[7][4], "*")

        # Verify Game Over (No more bricks)
        self.assertTrue(self.game.game_over)

if __name__ == "__main__":
    unittest.main()