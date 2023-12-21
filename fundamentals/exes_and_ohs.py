# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# my first solution: 

def xo(s):
    
    x = 0
    o = 0
    
    for char in s.lower():
        if char == 'x':
            x += 1
        if char == 'o':
            o += 1
    
    return x == o

# my second solution trying to shorten code down: 

def xo(s):
    
    return s.lower().count('x') == s.lower().count('o')