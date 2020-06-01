"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""

def solution(s):
    # if string is odd, make it even
    if len(s) & 1:
        s += '_'

    ret_arr = []
    i = 1
    # hop over the string two characters at a time, adding each two chars to array
    while i < len(s):
        sub_str = s[i-1] + s[i]
        ret_arr.append(sub_str)
        i += 2
    return ret_arr
