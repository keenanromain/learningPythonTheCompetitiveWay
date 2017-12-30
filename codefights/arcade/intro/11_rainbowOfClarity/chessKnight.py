"""
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.
The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically
and one square horizontally away from it. The complete move therefore looks like the letter L.
Check out the images in the directory to see all valid moves for a knight piece that is placed on one of the central squares.
Example
    For cell = "a1", the output should be
    chessKnight(cell) = 2.
    For cell = "c2", the output should be
    chessKnight(cell) = 6.
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string cell
    String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.
    [output] integer
"""

def chessKnight(cell):
    x,y = ord(cell[0]) - 97, int(cell[1]) - 1
    n = 0
    for i in range(-2,3):
        for j in range(-2,3):
            if abs(i) + abs(j) == 3:
                if x+i in range(0,8) and y+j in range(0,8):
                    n += 1
    return n