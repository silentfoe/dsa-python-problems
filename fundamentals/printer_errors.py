# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

# The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

# You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

# The string has a length greater or equal to one and contains only letters from ato z.

# Examples:
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"

# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"

# my solution: 

def printer_error(s):
    count = 0
    
    for char in s:
        if ord(char) < 97 or ord(char) > 109:
            count += 1
              
    return f'{count}/{len(s)}'

# four cool solutions I found on the code wars solutions page: 

#1
from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

#2
def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

#3
def printer_error(s):
    errors = 0
    count = len(s)
    for i in s:
        if i > "m":
            errors += 1
    return str(errors) + "/" + str(count)

#4
def printer_error(s):
    return '{}/{}'.format(sum(color > 'm' for color in s), len(s))