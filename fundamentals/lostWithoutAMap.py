# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

# my solution: 

def maps(a):
    return [num * 2 for num in a]

# another cool solution I found on the code wars solution page

def maps(a):
    return map(lambda x:2*x, a)