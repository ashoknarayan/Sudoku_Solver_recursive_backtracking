# Global variable to store the Sudoku grid
sudoku_grid = []

def sudoku_input():
    """
    Function to take input for a Sudoku puzzle.
    The input should be 9 lines of 9 digits (0-9), where 0 represents an empty cell.
    """
    global sudoku_grid
    print("Enter the Sudoku grid row by row (9 rows, each with 9 digits). Use '0' to represent empty squares:")
    sudoku_grid = []
    for i in range(9):
        while True:
            row = input(f"Row {i + 1}: ")
            if len(row) == 9 and all(ch.isdigit() and 0 <= int(ch) <= 9 for ch in row):
                sudoku_grid.append([int(ch) for ch in row])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0-9).")

def solve_sudoku(grid):
    """
    Recursive backtracking function to solve the Sudoku puzzle.
    Returns True if a solution is found, otherwise False.
    """
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                # Try all possible numbers (1-9) in the empty cell
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Backtrack
                return False  # No valid number found, trigger backtracking
    return True  # Puzzle solved

def is_valid_move(grid, row, col, num):
    """
    Check if placing 'num' in grid[row][col] is valid.
    """
    # Check the row
    if num in grid[row]:
        return False
    # Check the column
    if num in [grid[i][col] for i in range(9)]:
        return False
    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True

def main():
    """
    Main function to solve the Sudoku puzzle.
    """
    global sudoku_grid
    sudoku_input()
    print("\nInput Sudoku Grid:")
    for row in sudoku_grid:
        print(" ".join(map(str, row)))
    
    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Grid:")
        for row in sudoku_grid:
            print(" ".join(map(str, row)))
    else:
        print("\nNo solution exists for the given Sudoku grid.")

if __name__ == "__main__":
    main()
