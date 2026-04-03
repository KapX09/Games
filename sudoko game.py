M = 9

def print_grid(grid):
    """Print the Sudoku grid nicely"""
    for i in range(M):
        for j in range(M):
            print(grid[i][j], end=" ")
        print()


def is_safe(grid, row, col, num):
    """Check if it's safe to place num at grid[row][col]"""
    
    # Check row
    for x in range(9):
        if grid[row][x] == num:
            return False
    
    # Check column
    for x in range(9):
        if grid[x][col] == num:
            return False
    
    # Check 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    
    return True


def solve_sudoku(grid, row=0, col=0):
    """Main Sudoku solver using backtracking"""
    
    # Base case: we reached the end of the grid
    if row == M - 1 and col == M:
        return True
    
    # Move to next row if we finished current row
    if col == M:
        row += 1
        col = 0
    
    # If cell is already filled, move to next cell
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)
    
    # Try placing numbers 1 to 9
    for num in range(1, M + 1):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            
            if solve_sudoku(grid, row, col + 1):
                return True
                
            # Backtrack
            grid[row][col] = 0
    
    return False


# Your given puzzle (0 means empty)
grid = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]
]

print("Original Sudoku:")
print_grid(grid)
print("\nSolving...\n")

if solve_sudoku(grid):
    print("Solution found:")
    print_grid(grid)
else:
    print("No solution exists :(")
