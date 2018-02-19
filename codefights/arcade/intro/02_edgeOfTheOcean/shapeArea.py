"""
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the
n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3-
and 4-interesting polygons in the picture in this directory.
Example
    For n = 2, the output should be
    shapeArea(n) = 5;
    For n = 3, the output should be
    shapeArea(n) = 13.
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] integer n
    Guaranteed constraints:
    1 ≤ n < 104.
    [output] integer
    The area of the n-interesting polygon.
"""

def shapeArea(n):
    return n**2 + (n-1)**2

"""
Reasoning~
The example above and the rate of change in the polygons in area.png give us valuable data; namely
that the resulting output of our desired function seems to be the sum of two algebraic squares.
The input value, n, results in one side of the addition with n minus one being the other.
"""