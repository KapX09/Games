# Initial Setup
robot_position = (0, 0)  # Starting at the top-left corner
robot_direction = 'right'  # The robot starts facing right
grid = [
    ['👀', '.', '.', '.', '⭐'],
    ['.', '.', '.', '⭐', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['⭐', '.', '.', '.', '.']
]

stars_collected = 0
moves_count = 0

# Functions
def move():
    global robot_position
    x, y = robot_position

    if robot_direction == 'right':
        y += 1
    elif robot_direction == 'left':
        y -= 1
    elif robot_direction == 'up':
        x -= 1
    elif robot_direction == 'down':
        x += 1

    # Boundary check: Ensure the robot doesn't move out of the grid
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        robot_position = (x, y)
        check_star(robot_position)
    else:
        print("Move not possible, you are at the edge of the grid.")

def turn_left():
    global robot_direction
    if robot_direction == 'right':
        robot_direction = 'up'
    elif robot_direction == 'up':
        robot_direction = 'left'
    elif robot_direction == 'left':
        robot_direction = 'down'
    elif robot_direction == 'down':
        robot_direction = 'right'

def turn_right():
    global robot_direction
    if robot_direction == 'right':
        robot_direction = 'down'
    elif robot_direction == 'down':
        robot_direction = 'left'
    elif robot_direction == 'left':
        robot_direction = 'up'
    elif robot_direction == 'up':
        robot_direction = 'right'

def check_star(position):
    global stars_collected
    x, y = position
    if grid[x][y] == '⭐':
        stars_collected += 1
        grid[x][y] = '.'  # Remove the star after collecting it

def print_grid():
    global robot_position
    grid_copy = [row[:] for row in grid]
    x, y = robot_position
    grid_copy[x][y] = '🦾'
    for row in grid_copy:
        print(" ".join(row))

# Gameplay loop
while stars_collected < 3:  # You need to collect 3 stars to win
    # Player input
    command = input("Enter command (move/left/right): ").strip()
    if command == 'move':
        move()
        moves_count += 1
    elif command == 'left':
        turn_left()
        moves_count += 1
    elif command == 'right':
        turn_right()
        moves_count += 1
    else:
        print("Invalid move (enter 'move', 'right', 'left')")

    print(f"Stars collected: {stars_collected}")
    print_grid()
    if stars_collected == 3:
        print("You collected all the stars! You win!")
        break

print(f"\nGame Over! You completed the game in {moves_count} moves.")
