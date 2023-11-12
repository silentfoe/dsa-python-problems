# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# my solution: 

def solution(string):
    # using slice to reverse the string [start : end : interval] not putting anything for start and end to run through whole string. Using -1 so that the slice starts from the end of the string and hits each character in the string. 
    return string[::-1]