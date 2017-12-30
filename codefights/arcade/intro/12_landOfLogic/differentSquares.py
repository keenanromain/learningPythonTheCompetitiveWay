"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.
Example
For
matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.
Here are all 6 different 2 × 2 squares:
    1 2
    2 2

    2 1
    2 2

    2 2
    2 2

    2 2
    1 2

    2 2
    2 3

    2 3
    2 1
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.array.integer matrix
    Guaranteed constraints:
    1 ≤ matrix.length ≤ 100,
    1 ≤ matrix[i].length ≤ 100,
    0 ≤ matrix[i][j] ≤ 9.
    [output] integer
    The number of different 2 × 2 squares in matrix.
"""

def differentSquares(matrix):
    arr = []
    for x in range(1,len(matrix)):
        for y in range(1,len(matrix[0])):
            arr.append((matrix[x][y],
                        matrix[x][y-1],
                        matrix[x-1][y],
                        matrix[x-1][y-1]))
    return len(set(arr))