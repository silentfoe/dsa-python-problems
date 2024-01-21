# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

# my solution: 

def fake_bin(x):
    
    str = ''
    
    for chars in x:
        if int(chars) > 4:
            str += '1'
        else:
            str += '0'
    
    return str

# clever solution found on the code wars solutions page: 

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)