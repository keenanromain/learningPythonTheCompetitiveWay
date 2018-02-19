"""
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.
You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.
Example
For a = [50, 60, 60, 45, 70], the output should be
alternatingSums(a) = [180, 105].
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.integer a
    Guaranteed constraints:
    1 ≤ a.length ≤ 10,
    45 ≤ a[i] ≤ 100.
    [output] array.integer
"""

def alternatingSums(a):
    ret = [0,0]
    for i in range(len(a)):
        ret[i&1] += a[i]
    return ret

"""
Reasoning~
We can create a list to be returned, ret, of size two with zero initialized in each
position. Next, we can run over the length of the array and sum the contents of each
element against the even or odd position in ret. We're using a bit-wise operation to
signify which element to use in list ret, but 'ret[i%2]' would have worked as well.
"""