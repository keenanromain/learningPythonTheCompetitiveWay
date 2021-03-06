"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
Example
    For year = 1905, the output should be
    centuryFromYear(year) = 20;
    For year = 1700, the output should be
    centuryFromYear(year) = 17.
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] integer year
    A positive integer, designating the year.
    Guaranteed constraints:
    1 ≤ year ≤ 2005.
    [output] integer
    The number of the century the year is in.
"""

def centuryFromYear(year):
  return math.ceil(year/100)

"""
Reasoning~
We can round up the floating point remainders to determine the century when a given year
is divided by 100. Using the examples in thr prompt, there is no floating point remainder when
year 1700 is divided by 100. Such a year would not be affected by the built-in ceiling method.
However, 1905 when divided by 100 equals 19.05 which then would need to be round up due to the remainder.
"""