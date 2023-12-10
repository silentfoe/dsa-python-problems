# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

# my solution: 

def invert(lst):
    return [nums * -1 for nums in lst]

# other solutions I found on the code wars solutions page:

#1
def invert(lst):
    return [-x for x in lst]


#2
def invert(lst):
    return list(map(lambda x: -x, lst));
