"""
One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins counting the length of your ride, in minutes. Off you go to explore the neighborhood.
When you finally decide to head back, you realize there's a chance the bridges on your route home are up, leaving you stranded! Unfortunately, you don't have your watch on you and don't know what time it is. All you know thanks to the bike's timer is that n minutes have passed since 00:00.
Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.
Example
    For n = 240, the output should be
    lateRide(n) = 4.
    Since 240 minutes have passed, the current time is 04:00. The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.
    For n = 808, the output should be
    lateRide(n) = 14.
    808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.
Input/Output
    [time limit] 4000ms (py3)
    [input] integer n
    The duration of your ride, in minutes. It is guaranteed that you've been riding for less than a day (24 hours)
    Guaranteed constraints:
    0 ≤ n < 60 · 24.
    [output] integer
    The sum of the digits the digital timer would show.
"""
def lateRide(n):
    h = n // 60
    m = n % 60
    return h//10 + h%10 + m//10 + m%10
"""
Reasoning ~
This problem is very similar to addTwoDigits, but with an additional layer of
abstraction. Because n is the total number of minutes passed rather than the
total number of hours passed, we can divide n by 60 to get the hours. Whatever is
left is the remaining minutes of n. Now that we have the total number of
hours passed and the number of minutes passed since the last full hour, we
can break up these values into the appropriate format using the logic from
addTwoDigits: divide the value by 10 to split it which gets each digit in the 
appropriate spot. Then add all the digits together.
"""