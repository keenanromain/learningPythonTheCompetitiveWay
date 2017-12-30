"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that
each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.
This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.
Example
For the first example below, the output should be true. For the other grid, the output should be false:
each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.array.integer grid
    A matrix representing 9 × 9 grid already filled with numbers from 1 to 9.
    [output] boolean
    true if the given grid represents a correct solution to Sudoku, false otherwise.
"""

def sudoku(grid):
    row = [[False]*9 for _ in range(9)]
    col = [[False]*9 for _ in range(9)]
    box = [[False]*9 for _ in range(9)]
    for x in range(9):
        for y in range(9):
            n = grid[x][y]-1
            z = 3*(x//3)+(y//3)
            if row[x][n] or col[y][n] or box[z][n]:
                return False
            row[x][n] = col[y][n] = box[z][n] = True
    return True