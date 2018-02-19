"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
Example
    For sequence = [1, 3, 2, 1], the output should be
    almostIncreasingSequence(sequence) = false;
    There is no one element in this array that can be removed in order to get a strictly increasing sequence.
    For sequence = [1, 3, 2], the output should be
    almostIncreasingSequence(sequence) = true.
    You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
Input/Output
    [execution time limit] 0.5 seconds (c)
    [input] array.integer sequence
    Guaranteed constraints:
    2 ≤ sequence.length ≤ 105,
    -105 ≤ sequence[i] ≤ 105.
    [output] boolean
    Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.
"""

def almostIncreasingSequence(sequence):
    err1 = err2 = False
    for i in range(len(sequence)-1):
        if sequence[i+1] - sequence[i] <= 0:
            err1 = not err1
            if err1 == False: return False
    for i in range(len(sequence)-2):
        if sequence[i+2] - sequence[i] <= 0:
            err2 = not err2
            if err2 == False: return False
    return True

"""
Given the constraints for our program, we can run through the sequence twice checking the differences
between indexes off by one position in the sequence and indexes off by two positions. For each loop,
we are to have at most one discrepancy in the increasing order of elements which is why we have two
error flags that are flipped whenever such a discrepancy is found. If the flags are ever flipped back
to false it means that the discrepancy was triggered more than once which is grounds for returning
False. Othewise, if we complete both loops without returning out early we know that we found an
almost increasing sequence so we can return true. 
"""