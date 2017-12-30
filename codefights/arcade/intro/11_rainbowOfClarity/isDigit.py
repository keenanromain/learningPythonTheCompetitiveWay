"""
Determine if the given character is a digit or not.
Example
    For symbol = '0', the output should be
    isDigit(symbol) = true;
    For symbol = '-', the output should be
    isDigit(symbol) = false.
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] char symbol
    A character which is either a digit or not.
    [output] boolean
    true if symbol is a digit, false otherwise.
"""

def isDigit(symbol):
    return symbol.isdigit()