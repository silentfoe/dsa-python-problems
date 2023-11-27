# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

# Examples(Operator, value1, value2) --> output
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

# my solution: 

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '*':
        return value1 * value2
    if operator == '/':
        return value1 / value2
    

# cool solution I found on the code wars solution page but this solution is dangerous potentially: 
# Note: The use of eval() can be potentially unsafe if the input is not controlled or validated properly, as it allows the execution of arbitrary code. It's important to be cautious when using eval() and ensure that the input values are trusted or properly sanitized to prevent code injection or unintended consequences."

def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))