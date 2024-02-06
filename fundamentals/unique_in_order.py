# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]


# my solution:

def unique_in_order(sequence):
    
    unique = []
    
    for char in sequence:
        
        if len(unique) < 1:             
            unique.append(char)
        
        if unique[-1] != char:
            unique.append(char)
        
    return unique

# clever solutions found on the code wars solutions page: 

#1
def unique_in_order(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            res.append(item)
    return res

#2
def unique_in_order(iterable):
	r = []
	for x in iterable:
		x in r[-1:] or r.append(x)
	return r

