"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.
Example
For
matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be
minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]       
Check out the image below for better understanding:
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.array.boolean matrix
    A non-empty rectangular matrix consisting of boolean values - true if the corresponding cell contains a mine, false otherwise.
    Guaranteed constraints:
    2 ≤ matrix.length ≤ 5,
    2 ≤ matrix[0].length ≤ 5.
    [output] array.array.integer
    Rectangular matrix of the same size as matrix each cell of which contains an integer equal to the number of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.
"""

def minesweeper(matrix):
    width = len(matrix)-1
    length = len(matrix[0])-1
    ret = [[0] * (length+1) for i in range(width+1)]
    for row in range(width+1):
        for col in range(length+1):
            if col != 0 and matrix[row][col-1] == True:
                ret[row][col] += 1
            if col != length and matrix[row][col+1] == True:
                ret[row][col] += 1
            if row != 0 and matrix[row-1][col] == True:
                ret[row][col] += 1
            if row != width and matrix[row+1][col] == True:
                ret[row][col] += 1
            if row != 0 and col!= 0 and matrix[row-1][col-1] == True:
                ret[row][col] += 1
            if row != width and col != length and matrix[row+1][col+1] == True:
                ret[row][col] += 1
            if row != width and col != 0 and matrix[row+1][col-1] == True:
                ret[row][col] += 1
            if row != 0 and col != length and matrix[row-1][col+1] == True:
                ret[row][col] += 1
    return ret