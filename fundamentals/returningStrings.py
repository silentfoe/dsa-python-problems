# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

# [Make sure you type the exact thing I wrote or the program may not execute properly]

# my solution: 

def greet(name):
    return "Hello, " + name + " how are you doing today?"

# three other cool solutions found on the code wars solutions page: 

def greet(name):
    return f'Hello, {name} how are you doing today?'

def greet(name):
    return "Hello, {} how are you doing today?".format(name)

def greet(name):
    return "Hello, %s how are you doing today?" % name