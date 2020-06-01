"""
Write a function that will take in any array and reverse it.

Sounds simple doesn't it?

NOTES:

    Array should be reversed in place! (no need to return it)
    Usual builtins have been deactivated. Don't count on them.
    You'll have to do it fast enough, so think about performances


"""

def reverse(seq):
    i, j = 0, len(seq)-1
    while i <= len(seq)//2 <= j:
        tmp = seq[i]
        seq[i] = seq[j]
        seq[j] = tmp
        i += 1
        j -= 1
    return seq
