"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""

def move_zeros(array):
    ok = lambda x: (type(x) is not int and type(x) is not float) or x != 0
    ret = [x for x in array if ok(x)]
    return ret + [0 for x in range(len(array)-len(ret))]
