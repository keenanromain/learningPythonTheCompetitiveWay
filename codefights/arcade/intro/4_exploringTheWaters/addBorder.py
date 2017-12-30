"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
Example
For
picture = ["abc",
           "ded"]
the output should be
addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.string picture
    A non-empty array of non-empty equal-length strings.
    Guaranteed constraints:
    1 ≤ picture.length ≤ 5,
    1 ≤ picture[i].length ≤ 5.
    [output] array.string
    The same matrix of characters, framed with a border of asterisks of width 1.
"""

def addBorder(picture):
    line = "*" * (len(picture[0]) + 2)
    return [line]+["*" + pic + "*" for pic in picture]+[line]