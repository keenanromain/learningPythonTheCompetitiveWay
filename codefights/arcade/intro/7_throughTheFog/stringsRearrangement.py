"""
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the rearrangement the strings at consecutive positions would differ by exactly one character.
Example
    For inputArray = ["aba", "bbb", "bab"], the output should be
    stringsRearrangement(inputArray) = false;
    All rearrangements don't satisfy the description condition.
    For inputArray = ["ab", "bb", "aa"], the output should be
    stringsRearrangement(inputArray) = true.
    Strings can be rearranged in the following way: "aa", "ab", "bb".
    Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.string inputArray
    A non-empty array of strings of lowercase letters.
    Guaranteed constraints:
    2 ≤ inputArray.length ≤ 10,
    1 ≤ inputArray[i].length ≤ 15.
    [output] boolean
"""

import itertools

def differByOne(a, b):
    differBy = 0
    for i, j in zip(a, b):
        if i != j:
            differBy +=1
    return differBy == 1 and len(a) == len(b)

def stringsRearrangement(inputArray):
    perms = [x for x in itertools.permutations(inputArray)]
    for perm in perms:
        possible = True
        i = 1
        while i < len(perm):
            if (not differByOne(perm[i],perm[i-1])):
                possible = False
                break
            i += 1
        if possible:
            return True
    return False