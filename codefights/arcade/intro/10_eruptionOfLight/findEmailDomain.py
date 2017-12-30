"""
An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").
The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.
Given a valid email address, find its domain part.
Example
    For address = "prettyandsimple@example.com", the output should be
    findEmailDomain(address) = "example.com";
    For address = "<>[]:,;@\"!#$%&*+-/=?^_{}| ~.a\"@example.org", the output should be
    findEmailDomain(address) = "example.org".
Input/Output
    [execution time limit] 4 seconds (py3)
    [input] string address
    Guaranteed constraints:
    10 ≤ address.length ≤ 50.
    [output] string
"""

def findEmailDomain(address):
    return address[address.rfind('@')+1:]