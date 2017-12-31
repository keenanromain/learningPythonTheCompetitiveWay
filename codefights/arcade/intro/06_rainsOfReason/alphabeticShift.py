"""
Given a string, replace each its character by the next one in the English alphabet (z would be replaced by a).
Example
For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string inputString
    Non-empty string consisting of lowercase English characters.
    Guaranteed constraints:
    1 ≤ inputString.length ≤ 10.
    [output] string
    The result string after replacing all of its characters.
"""

def alphabeticShift(s):
    return "".join('a' if c == 'z' else chr(ord(c)+1) for c in s)