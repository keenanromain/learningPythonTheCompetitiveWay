"""
Given two strings, find the number of common characters between them.
Example
For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.
Strings have 3 common characters - 2 "a"s and 1 "c".
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string s1
    A string consisting of lowercase latin letters a-z.
    Guaranteed constraints:
    1 ≤ s1.length ≤ 15.
    [input] string s2
    A string consisting of lowercase latin letters a-z.
    Guaranteed constraints:
    1 ≤ s2.length ≤ 15.
    [output] integer
"""

def commonCharacterCount(s1, s2):
    count = 0
    for c1 in s1:
        for c2 in s2:
            if c1 == c2:
                s2 = s2.replace(c2, "", 1)
                count += 1
                break
    return count

    """
    Reasoning~
    Iterate over each character of each string through nested loops. If there ever is a match
    between the character of the outer and inner loop, we know we can increment the count
    variable. Next, to ensure we prohibit double counting we replace the character from
    the matched string with empty space.
    """