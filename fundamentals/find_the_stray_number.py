# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

# my solution: 

def stray(arr):

    for num in arr:
        if arr.count(num) == 1:
            return num
        
# clever solution found on the solutions page: 

def stray(arr):
    for x in set(arr):
        if arr.count(x) == 1: return x