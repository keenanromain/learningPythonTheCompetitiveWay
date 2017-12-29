"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.
Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.
Find the minimal length of the jump enough to avoid all the obstacles.
Example
For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.
Check out the image in this directory for a better understanding
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.integer inputArray
    Non-empty array of positive integers.
    Guaranteed constraints:
    2 ≤ inputArray.length ≤ 10,
    1 ≤ inputArray[i] ≤ 40.
    [output] integer
    The desired length.
"""

def avoidObstacles(inputArray):
    for i in range(1, max(inputArray)):
        j = 0
        while j <= max(inputArray):
            j += i
            if j in inputArray:
                break
        if j > max(inputArray):
            return i
    return max(inputArray) + 1