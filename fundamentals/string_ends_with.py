# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

# my solution: 

def solution(text, ending):
    
    return text[-len(ending)::] == ending


# other solution found on the code wars solutions page:

def solution(string, ending):
    return string.endswith(ending)