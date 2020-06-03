"""
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
Example:

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
Note

consecutive strings : follow one after another without an interruption
"""

early_exit = lambda a,b: a <= 0 or a > len(b)

def longest_consec(strarr, k):
    biggest = ''
    if not early_exit(k,strarr):
        biggest += ''.join(x for x in strarr[:k])
        for i in range(1,len(strarr)-k+1):
            current = ''.join(x for x in strarr[i:i+k])
            if len(current) > len(biggest):
                biggest = current
    return biggest
