# Global variable to store the Sudoku grid
from collections import defaultdict


sudoku_grid = []

def sudoku_input():
    """
    Function to take input for a Sudoku puzzle row by row.
    Each row should contain exactly 9 digits (0-9), where 0 represents an empty cell.
    """
    global sudoku_grid
    print("Enter the Sudoku grid row by row (use '0' for empty squares):")
    sudoku_grid = []
    for i in range(9):
        while True:
            row_input = input(f"Row {i + 1}: ").strip()
            if len(row_input) == 9 and all(ch.isdigit() and 0 <= int(ch) <= 9 for ch in row_input):
                sudoku_grid.append([int(ch) for ch in row_input])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0-9) for the row.")                

def solve_sudoku(grid):
    """
    Highly optimized Sudoku solver using backtracking with constraint propagation and bitwise operations.
    Returns True if a solution is found, otherwise False.
    """

    # Precompute bitmasks for rows, columns, and subgrids
    row_masks = [0] * 9
    col_masks = [0] * 9
    subgrid_masks = [0] * 9

    # Initialize masks based on the initial grid
    for r in range(9):
        for c in range(9):
            num = grid[r][c]
            if num != 0:
                bit = 1 << num
                row_masks[r] |= bit
                col_masks[c] |= bit
                subgrid_masks[(r // 3) * 3 + (c // 3)] |= bit

    # Find the next empty cell
    def find_empty_cell(grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    return row, col
        return None

    # Recursive backtracking
    def backtrack(grid):
        empty_cell = find_empty_cell(grid)
        if not empty_cell:
            return True  # Solved

        row, col = empty_cell
        subgrid_index = (row // 3) * 3 + (col // 3)
        available = ~(row_masks[row] | col_masks[col] | subgrid_masks[subgrid_index]) & 0x3FE

        while available:
            bit = available & -available  # Extract the lowest set bit
            num = bit.bit_length() - 1

            # Place the number
            grid[row][col] = num
            row_masks[row] |= bit
            col_masks[col] |= bit
            subgrid_masks[subgrid_index] |= bit

            if backtrack(grid):
                return True

            # Backtrack
            grid[row][col] = 0
            row_masks[row] &= ~bit
            col_masks[col] &= ~bit
            subgrid_masks[subgrid_index] &= ~bit

            available &= available - 1  # Remove the lowest set bit

        return False

    # Start solving
    return backtrack(grid)

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
