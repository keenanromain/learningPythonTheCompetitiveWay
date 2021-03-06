"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
Examples

to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
"""

import re

def to_camel_case(text):
    if not text:
        return text
    regex = re.sub('[^0-9a-zA-Z]+', '', text.title())[1:]
    return text[:1].upper() + regex if text[0].isupper() else text[:1] + regex

