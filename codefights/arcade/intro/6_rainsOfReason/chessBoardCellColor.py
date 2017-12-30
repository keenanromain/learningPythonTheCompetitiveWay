"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

    For cell1 = "A1" and cell2 = "C3", the output should be
    chessBoardCellColor(cell1, cell2) = true.
    See example1.png for visualization
    For cell1 = "A1" and cell2 = "H3", the output should be
    chessBoardCellColor(cell1, cell2) = false.
    See example2.png for visualization
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string cell1
    [input] string cell2
    [output] boolean
    true if both cells have the same color, false otherwise.
"""

def chessBoardCellColor(c1, c2):
    return (ord(c1[0])+ord(c1[1]))&1 == (ord(c2[0])+ord(c2[1]))&1