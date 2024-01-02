# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
# Your function should only return a number, not the explanation about how you get that number.

# my solution: 

def get_sum(a,b):
    
    if a == b:
        return a
    
    answer = 0
    
    for num in range(min([a,b]), max([a,b]) + 1):
        answer += num
    
    return answer

# better answer found on the solutions page: 

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

# using math to solve for the problem, found on the solutions page: 

def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2