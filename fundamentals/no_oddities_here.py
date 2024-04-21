# Write a small function that returns the values of an array that are not odd.

# All values in the array will be integers. Return the good values in the order they are given.


# my solution: 

def no_odds(values):
    
    even_nums = []
    
    for num in values:
        if num % 2 == 0:
            even_nums.append(num)
    
    return even_nums


# clever solution found on the code wars solutions page: 

def no_odds(values):
    return [i for i in values if i % 2 == 0]