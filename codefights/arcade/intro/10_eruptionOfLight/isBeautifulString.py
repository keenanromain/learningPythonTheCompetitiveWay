"""
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.
Given a string, check whether it is beautiful.
Example
    For inputString = "bbbaacdafe", the output should be
    isBeautifulString(inputString) = true;
    For inputString = "aabbb", the output should be
    isBeautifulString(inputString) = false;
    For inputString = "bbc", the output should be
    isBeautifulString(inputString) = false.
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string inputString
    A string of lowercase letters.
    Guaranteed constraints:
    3 ≤ inputString.length ≤ 50.
    [output] boolean
"""

def isBeautifulString(s):
    arr = [s.count(chr(x)) for x in range(ord('a'),ord('z')+1)]
    for i in range(1,len(arr)):
        if arr[i-1] < arr[i]:
            return False
    return True