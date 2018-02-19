"""
Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the first half of the digits
is equal to the sum of the second half.
Given a ticket number n, determine if it's lucky or not.
Example
    For n = 1230, the output should be
    isLucky(n) = true;
    For n = 239017, the output should be
    isLucky(n) = false.
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] integer n
    A ticket number represented as a positive integer with an even number of digits.
    Guaranteed constraints:
    10 ≤ n < 106.
    [output] boolean
    true if n is a lucky ticket number, false otherwise.
"""

def isLucky(n):
    s = str(n)
    first, second = s[0:int(len(s)/2)], s[int(len(s)/2):len(s)]
    left, right = 0, 0
    for c in first:
        left += int(c)
    for c in second:
        right += int(c)
    return left == right

    """
    Reasoning~
    Turning the input into a string made it easier to split the number in half. We can then
    grab each half do by dividing the length of the string by two and either iterating up
    to that point to get the first half or iterating immediately past it to get the second
    half. Next we can sum up the values in each half then compare the results with a boolean
    expression in our return statement.
    
    """