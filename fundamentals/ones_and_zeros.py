# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

# Examples:

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
# However, the arrays can have varying lengths, not just limited to 4.

# my solution: 

def binary_array_to_number(arr):
    
    binary = {0:1, 1:2, 2:4, 3:8, 4:16, 5:32, 6:64, 7:128, 8:256}
    
    num = 0
    
    reversed_arr = arr[::-1]
    
    for indx,val in enumerate(reversed_arr):
        if val == 1:
            num += binary[indx]
    
    return num


# a couple of clever solutions to this problem that are shorted than mine: 

#1
def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)

#2
def binary_array_to_number(arr):
    s = 0
    for digit in arr:
        s = s * 2 + digit

    return s