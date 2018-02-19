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

"""
Reasoning~
We first can set the top and bottom row of asteriks by finding the length of the input
matrix's first row and adding the result to two. This width, n, when multiplied by the
asterik tells Python to create the asterik n many times. Next, we can then create a new array
from the contents of the input array and modify each element to have an asterik in front of
and behind it each time. Lastly, we place this new array in the middle of the top and bottom
row of asteriks and return the result.
"""