"""
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
Example
For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.integer inputArray
    Guaranteed constraints:
    3 ≤ inputArray.length ≤ 10,
    -15 ≤ inputArray[i] ≤ 15.
    [output] integer
    The maximal absolute difference.
"""

def arrayMaximalAdjacentDifference(a):
    return max([max(a[i], a[i+1]) - min(a[i], a[i+1]) for i in range(len(a)-1)])