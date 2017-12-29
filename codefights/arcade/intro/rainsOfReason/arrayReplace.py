"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
Example
For inputArray = [1, 2, 1], elemToReplace = 1 and substitutionElem = 3, the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.integer inputArray
    Guaranteed constraints:
    2 ≤ inputArray.length ≤ 10,
    0 ≤ inputArray[i] ≤ 10.
    [input] integer elemToReplace
    Guaranteed constraints:
    0 ≤ elemToReplace ≤ 10.
    [input] integer substitutionElem
    Guaranteed constraints:
    0 ≤ substitutionElem ≤ 10.
    [output] array.integer
"""

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i,elem in enumerate(inputArray):
        if elemToReplace == elem:
            inputArray[i] = substitutionElem
    return inputArray