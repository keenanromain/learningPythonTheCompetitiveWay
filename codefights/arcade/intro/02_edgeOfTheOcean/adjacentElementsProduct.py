"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
Example
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.
7 and 3 produce the largest product.
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] array.integer inputArray
    An array of integers containing at least two elements.
    Guaranteed constraints:
    2 ≤ inputArray.length ≤ 10,
    -1000 ≤ inputArray[i] ≤ 1000.
    [output] integer
    The largest product of adjacent elements.
"""

def adjacentElementsProduct(inputArray):
    return max([inputArray[i] * inputArray[i-1] for i in range(1,len(inputArray))])

"""
Reasoning~
We can iterate over the input array and multiply each current value against it's predecessor,
storing each result in a separate array. Once the looping is complete, the max method
can be used to extract the biggest product found in the new array.
"""