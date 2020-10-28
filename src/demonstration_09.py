"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
import math

def is_even(input_string):
    return input_string % 2 == 0

def get_middle(input_string):
    
    if is_even(len(input_string)):
        # we would want to slice to get multiple characters
        midpoint = math.floor(len(input_string) / 2)
        return input_string[midpoint-1 : midpoint+1]
        
    
    else:
        midpoint = math.floor(len(input_string) / 2)
        return input_string[midpoint]


print(get_middle("testing"))