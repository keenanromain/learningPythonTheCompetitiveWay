"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
Examples

"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
"""
def duplicate_encode(word):
    # map for letters and their occurence count in the all lower-cased input
    letter_map = {}
    word = word.lower()

    # place each letter into the map and track their occurences
    for x in word:
        if x not in letter_map:
            letter_map[x] = 1
        else:
            letter_map[x] += 1

    # use the map to decide which paranthesis to use
    return_str = ""
    for x in word:
        if letter_map[x] == 1:
            return_str += "("
        else:
            return_str += ")"
    return return_str


