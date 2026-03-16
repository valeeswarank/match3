
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
## Assumptions and Notes

1. **Operating System**
   - The game has been developed and tested using the **Windows operating system**.
   - It is assumed that users will run the game on a **Windows machine**.

2. **Cross-Platform Compatibility**
   - The game has **not yet been tested on macOS or Linux environments**.
   - Additional testing is required to ensure the game runs correctly on:
     - **macOS**
     - **Linux**

3. **Application Architecture**
   - The application has been designed using the **MVC (Model–View–Controller) architectural pattern**.
   - This structure separates the game logic, user interface, and control flow, making the application easier to maintain, extend, and test.

4. **Future Enhancements**
   - Based on the provided instructions and current implementation, the game represents a **basic functional version**.
   - Further **enhancements, improvements, and testing** may be required for future versions to improve:
     - Stability
     - Cross-platform compatibility
     - Additional game features
     - Performance and robustness

5. **Running the Game**
   - To execute the game, please follow the instructions provided in the **“How to Run the Game?”** section.

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
