"""
Correct variable names consist only of Latin letters, digits and underscores and they can't start with a digit.
Check if the given string is a correct variable name.
Example
    For name = "var_1__Int", the output should be
    variableName(name) = true;
    For name = "qq-q", the output should be
    variableName(name) = false;
    For name = "2w2", the output should be
    variableName(name) = false.
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string name
    Guaranteed constraints:
    1 ≤ name.length ≤ 10.
    [output] boolean
    true if name is a correct variable name, false otherwise.
"""

def variableName(name):
    for i in list(name):
        if i == '_' or i.isalnum():
            continue
        return False
    return not name[0].isnumeric()