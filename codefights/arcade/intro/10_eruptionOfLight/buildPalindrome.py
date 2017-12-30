"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.
Example
For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string st
    A string consisting of lowercase latin letters.
    Guaranteed constraints:
    3 ≤ st.length ≤ 10.
    [output] string
"""

def buildPalindrome(st):
    end = ""
    i = 0
    while i < len(st):
        if st[i] == st[len(st)-1] and st[i:] == st[i:][::-1]:
            break
        end = st[i] + end
        i += 1
    return st + end