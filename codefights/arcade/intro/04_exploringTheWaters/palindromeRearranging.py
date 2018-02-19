"""
Given a string, find out if its characters can be rearranged to form a palindrome.
Example
For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.
We can rearrange "aabb" to make "abba", which is a palindrome.
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string inputString
    A string consisting of lowercase English letters.
    Guaranteed constraints:
    1 ≤ inputString.length ≤ 50.
    [output] boolean
    true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
"""

def palindromeRearranging(inputString):
    d = {}
    for c in inputString:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    odd = 0
    for i in d:
        if d[i] & 1:
            odd += 1
    return odd < 2

    """
    Reasoning~
    We can use a dictionary to store the unique elements of the input string and increment
    the number of repeated characters stored inside. Next, we can go through each element in
    the dictionary and if ever the numerical value for each string key is odd we can increment
    a counter. The purpose behind this is that when evaluating a palindrome, there should
    only ever be at most one odd character that does not have a pair. This would be the 
    character in the middle if the total length of the string wasn't even. So by having this
    counter, we can see if there are ever more than one unqique elements (meaning no pair) and
    if there is more than one, we can infer that there is no palindrome to be rearranged.
    """