# Your task is to write a function which returns the sum of following series upto nth term(parameter).

# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# Rules:
# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return 0.00

# You will only be given Natural Numbers as arguments.

# Examples:(Input --> Output)
# 1 --> 1 --> "1.00"
# 2 --> 1 + 1/4 --> "1.25"
# 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"

# my solution: 

def series_sum(n):
    
    total = 0
    
    for i in range(0,n):
        if i == 0:
            total += 1.00
        elif i == 1:
            total += 1/4
        else:
            total += 1/(4 + ((i - 1) * 3))
    
    return f"{total:.2f}"

# clever solution found on the solutions page: 

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))