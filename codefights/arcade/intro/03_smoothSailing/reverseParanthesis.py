"""
You have a string s that consists of English letters, punctuation marks, whitespace
characters, and brackets. It is guaranteed that the parentheses in s form a regular
bracket sequence. Your task is to reverse the strings contained in each pair of
matching parentheses, starting from the innermost pair. The results string should not
contain any parentheses.
Example
For string s = "a(bc)de", the output should be
reverseParentheses(s) = "acbde".
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string s
    A string consisting of English letters, punctuation marks, whitespace characters and brackets. It is guaranteed that parentheses form a regular bracket sequence.
    Constraints:
    5 ≤ s.length ≤ 55.
    [output] string
"""

def reverseParentheses(s):
    left = s.rfind('(')
    while left != -1:
        right = s.find(')', left)
        s = s[:left] + s[right-1:left:-1] + s[right+1:]
        left = s.rfind('(')
    return s

    """
    Reasoning~
    We first need to find the left-most '(' from the right side because it belongs to the
    inner-most set of paranthesis. From there, we can find it's corresponding ')' by
    searching from the left variable inside our loop. Once we found both, we can perform
    the trickiest bit of this problem. We reset our string variable to be the result of three
    sub-strings; the string up until the left-most '(', the string after the corresponding
    ')', and everything in between those two in reverse. Once this new string is created,
    we need to update the left variable to be the next '(' from the right if it exists.
    """