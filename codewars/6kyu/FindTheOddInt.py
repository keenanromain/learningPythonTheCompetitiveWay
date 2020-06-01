"""
Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

"""
def find_it(seq):
    arr = []
    for x in seq:
        if x not in arr:
            arr.append(x)
        else:
            arr.remove(x)
    return arr[0]
