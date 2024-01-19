# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

# my solution: 

def grow(arr):
    
    num = 1
    
    for nums in arr:
        num = num * nums
    
    return num