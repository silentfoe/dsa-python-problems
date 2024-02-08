# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]

# my solution: 

def reverse_seq(n):
    return [x for x in range(n,0,-1)]

# different way to solve using range found on solutions page: 

def reverseseq(n):
    return list(range(n, 0, -1))