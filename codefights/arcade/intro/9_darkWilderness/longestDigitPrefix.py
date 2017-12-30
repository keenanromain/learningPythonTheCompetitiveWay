"""
Given a string, output its longest prefix which contains only digits.
Example
For inputString="123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string inputString
    Guaranteed constraints:
    3 ≤ inputString.length ≤ 35.
    [output] string
"""

def longestDigitsPrefix(inputString):
    s = ""
    for c in inputString:
        if ord(c) < 48 or ord(c) > 57:
            break
        s += c
    return s