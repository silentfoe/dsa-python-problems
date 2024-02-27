# Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

# my solution: 

def no_boring_zeros(n):
    
    while len(str(n)) > 1 and str(n)[-1] == '0':
        n = int(str(n)[:-1])
    
    return n


# a few clever solutions found on the solutions page: 

#1
def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0

#2
def no_boring_zeros(n):
    if n==0:
        return n
    while n%10==0:
        n=n/10
    return n

#3
def no_boring_zeros(n):
    return int(str(n).strip("0")) if n else n

#4
def no_boring_zeros(n):
    return int(str(n).strip('0') or 0)