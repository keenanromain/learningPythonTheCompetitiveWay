"""
You are given a two-digit integer n. Return the sum of its digits.
Example
For n = 29, the output should be
addTwoDigits(n) = 11.
Input/Output
    [time limit] 4000ms (py3)
    [input] integer n
    A positive two-digit integer.
    Guaranteed constraints:
    10 ≤ n ≤ 99.
    [output] integer
    The sum of the first and second digits of the input number.
"""

def addTwoDigits(n):
    return(n//10+n%10)

"""
Reasoning ~
Given that n will be a two digit number between 10 and 99 inclusive, we can effectively
slice n in half through dividing by 10. The quotient will be the
digit in the tens place and the remainder will be the digit in the ones place.
Adding both the quotient and remainder will give us the answer to this problem.
"""
