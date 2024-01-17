# Task:
# Given a list of integers, determine whether the sum of its elements is odd or even.

# Give your answer as a string matching "odd" or "even".

# If the input array is empty consider it as: [0] (array with a zero).

# Examples:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"

# my solution: 

def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return 'even'
    
    return 'odd'


# two other cool solutions I found on the solutions page: 

#1
def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'

#2
def oddOrEven(arr):
    return ('even', 'odd')[sum(arr) % 2]