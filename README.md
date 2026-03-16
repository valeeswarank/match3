
# Match-3 Game
Match-3 game is a falling bricks game. In this game, you will control “bricks" made up of three blocks, each marked with a special symbol. Bricks can be horizontal or vertical, and you can move or drop them using simple commands. The goal is to place all bricks and clear as many matches as possible.

## Project Structure

```
match3/
│
├── model/
│   ├── __init__.py
│   ├── brick.py
│   └── game.py
│
├── view/
│   ├── __init__.py
│   └── console_view.py
│
├── controller/
│   ├── __init__.py
│   └── game_controller.py
│
├── tests/
│   └── test_game.py
│
└── main.py```
```
## How to Run the Game?
1. Open your Command Prompt (cmd) or terminal.
2. Navigate to the project directory using the following command: 
```
cd <path-to-project>
```

3. Run the game using the command:
```
python main.py
```

4. The program will display the following prompt:
```
> Please enter field size (width and height) and up to 5 bricks set:
```

5. Enter the field size and brick definitions. For example:
```
5 8 H^^* V*@^
```
* 5 → Field width
* 8 → Field height
* H^^*, V*@^ → Brick definitions
6. Press Enter to start the game.
7. Follow the prompts to enter commands and enjoy playing the game.
