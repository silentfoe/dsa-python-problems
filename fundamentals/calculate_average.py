# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

# my solution:

def find_average(numbers):
    
    if numbers:
        return sum(numbers) / len(numbers)
    
    return 0

# other cool solution I found on the code wars solution page: 

def find_average(array):
    return sum(array) / len(array) if array else 0