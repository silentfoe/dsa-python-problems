# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.


# my solution: 

def get_count(sentence):
    vowels = ['a','e','i','o','u']
    count = 0
    
    for vow in sentence: 
        if vow in vowels:
            count += 1
        
    return count

# other solution that was clever found on code wars solutions page: 

def getCount(s):
    return sum(c in 'aeiou' for c in s)