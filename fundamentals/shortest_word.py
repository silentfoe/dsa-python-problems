# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

# my solution: 

import math

def find_short(s):
    return min(map(lambda word: len(word), s.split()))



# other solution I found useful on the code wars solutions page: 

def find_short(s):
    return min(len(x) for x in s.split())