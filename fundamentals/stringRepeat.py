# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

# my solution: 

def repeat_str(repeat, string):
    str = ''
    
    for char in range(repeat):
        str += string
    
    return str

# good to know solution I found on the code wars solution page: 

def repeat_str(repeat, string):
    return repeat * string