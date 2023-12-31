# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"

# my solution: 

def are_you_playing_banjo(name):
    
    if name.lower()[0] == 'r':
        return f"{name} plays banjo"
    
    return f"{name} does not play banjo"