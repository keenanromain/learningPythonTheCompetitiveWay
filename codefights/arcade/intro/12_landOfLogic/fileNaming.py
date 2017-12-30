"""
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.
Return an array of names that will be given to the files.
Example
For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.string names
    Guaranteed constraints:
    5 ≤ names.length ≤ 15,
    1 ≤ names[i].length ≤ 15.
    [output] array.string
"""

def fileNaming(names):
    arr = []
    for i in names:
        if i not in arr:
            arr.append(i)
            continue
        j = 1
        while i + "(" + str(j) + ")" in arr:
            j += 1
        arr.append(i + "(" + str(j) + ")")
    return arr