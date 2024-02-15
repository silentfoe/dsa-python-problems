# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.

# I
# If it is the case we will return k, if not return -1.

# Note: n and p will always be strictly positive integers.

# Examples:
# n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

# n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

# n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

# n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# my first solution: 

def dig_pow(n, p):
    
    sep_num = [int(num) for num in str(n)]
    
    total_value = []
    
    for indx,num in enumerate(sep_num):
        total_value.append(num ** (indx + p))
    
    if (sum(total_value) / n) == (sum(total_value) // n):
        return sum(total_value) / n
    
    return -1

# my second reworked solution: 

def dig_pow(n, p):
    
    sep_num = [int(num) for num in str(n)]
    
    total_value = sum([num ** (indx + p) for indx,num in enumerate(sep_num)])
    
    if total_value / n == total_value // n:
        return total_value / n

    return -1

# really cool solutions I found on the solutions page: 

#1
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

#2
def dig_pow(n, p):
    s = sum(int(d)**(p+i) for i,d in enumerate(str(n)))
    return s/n if s%n == 0 else -1