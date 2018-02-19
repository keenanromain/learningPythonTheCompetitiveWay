"""
Given an array of strings, return another array containing all of its longest strings.
Example
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.string inputArray
    A non-empty array.
    Guaranteed constraints:
    1 ≤ inputArray.length ≤ 10,
    1 ≤ inputArray[i].length ≤ 10.
    [output] array.string
    Array of the longest strings, stored in the same order as in the inputArray.
"""

def allLongestStrings(inputArray):
    biggest = max([len(string) for string in inputArray])
    return [string for string in inputArray if len(string) == biggest]

"""
Reasoning~
We want to extract the largest length of a string in the input array so we can do that by
iterating over it, storing each length, then pulling the biggest number out of the resulting
array. Next, we can then compare what strings match this length and return them in a new array
by running over the inputArray once more with the maximum length in our hands.
"""