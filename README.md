# Games
These are Mini-Games built in python
## 1. Sudoku:
### Sudoku Solver in Python
This project solves a standard 9x9 Sudoku puzzle using backtracking.

#### Files
- `sudoku_solver.py` : Contains all functions for solving the puzzle

#### How it Works
- `puzzle(a)`  
  Prints the Sudoku grid row by row.

- `solve(grid, row, col, num)`  
  Checks if placing `num` at position `(row, col)` is valid:
  - Number not already in the same row
  - Number not already in the same column
  - Number not already in the same 3x3 subgrid

- `Suduko(grid, row, col)`  
  Uses recursion and backtracking to:
  - Skip already filled cells
  - Try all numbers 1 to 9 in empty cells
  - Backtrack if no number fits

#### Input Format
- The input is a 9x9 grid with zeros representing empty cells:
```python
grid = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]
```
#### Output
- If the puzzle is solvable, the filled grid is printed.
- If not, the message Solution does not exist :( is shown.

## 2. Snake Game:
   ### Snake Game using Python Turtle
This is a simple snake game built using Python's `turtle` graphics module. The snake moves automatically and can be controlled using arrow keys. Food appears at random positions, and the snake grows each time it eats.

#### Features
- Classic snake game mechanics
- Arrow key controls: Up, Down, Left, Right
- Snake wraps around screen edges
- Food appears at random locations
- Auto-restart on self-collision

#### How It Works
- `move_snake()`: Updates snake movement and handles wrapping and growth
- `food_collision()`: Checks if the snake eats the food
- `reset()`: Resets the game on collision
- `get_random_food_position()`: Spawns food randomly within screen bounds

#### Requirements
- Python (preferably 3.x)
- No external libraries required (uses built-in `turtle` and `random`)

#### Controls
- Arrow keys (↑ ↓ ← →) to change direction

#### P.S
- Game runs in a Turtle graphics window
- Food and snake are drawn using turtle shapes

---
Here I intended to add AI implementation in future.
