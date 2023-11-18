# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1(squared) + 2(squared) + 2(squared) = 9

# my solution: 

def square_sum(numbers):
    
    total = 0
    
    for num in numbers:
        total += num ** 2
        
    return total


# cool solution found on code wars solution page for this problem:

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)