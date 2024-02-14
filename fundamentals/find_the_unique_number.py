# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# my solution: 

def find_uniq(arr):
    
    lowest = min(arr)
    highest = max(arr)
    
    slice = arr[:10]
    
    if slice.count(lowest) > 1:
        return highest
    
    return lowest


# a few solutions I thought were interesting from the solutions page: 

#1
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

#2
def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e

#3
def find_uniq(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]
