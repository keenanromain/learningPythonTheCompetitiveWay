"""
Given an integer n, return the largest number that contains exactly n digits.
Example
For n = 2, the output should be
largestNumber(n) = 99.
Input/Output
   [time limit] 4000ms (py3)
   [input] integer n
   Guaranteed constraints:
   1 ≤ n ≤ 7.
   [output] integer
   The largest integer of length n.
"""
def largestNumber(n):
    return int(n*"9")
"""
Reasoning ~
Because n indicates the number of digits to be produced in our result,
we can take advantage of Python's simplicity by multiplying n 
against string "9" then converting the result to an integer through
the built-in type int().
"""