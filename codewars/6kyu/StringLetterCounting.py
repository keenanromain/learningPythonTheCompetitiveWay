"""
Take an input string and return a string that is made up of the number of occurances of each english letter in the input, followed by that letter. The string shouldn't contain zeros; leave them out.

An empty string, or one with no letters, should return an empty string.

Notes:

    the input will always be valid;
    treat letters as case-insensitive

Examples

"This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
""                          ==>  ""
"555"                       ==>  ""
"""
import re

def string_letter_count(s):
    s = re.sub('[^a-z]', '', s.lower())
    m = {}
    sort_key = lambda x: x[0]
    for i in range(len(s)):
        current_value = s[i]
        if current_value in m:
            m[current_value] += 1
        else:
            m[current_value] = 1
    return ''.join('{}{}'.format(x[1],x[0]) for x in sorted(m.items(),key=sort_key))
