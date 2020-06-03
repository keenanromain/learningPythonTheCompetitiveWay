"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""

def unique_in_order(iterable):
    # account for empty string edge case
    if not iterable:
        return []

    # using the previous char in the string, decide whether the next one is a copy
    returning_lst = [iterable[0]]
    for x in iterable:
        if x != returning_lst[-1]:
            returning_lst.append(x)

    return returning_lst
