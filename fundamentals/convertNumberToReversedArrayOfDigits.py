# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

# my solution: 

def digitize(n):
    lst = []
    strNums = list(str(n))[::-1]
    
    for nums in strNums:
        lst.append(int(nums))
        
    
    return lst


# another solution I came up with using map function: 

def digitize(n):
    
    def nums(i):
        return int(i)
    
    return list(map(nums,list(str(n))[::-1]))



# three better solutions I found on the code wars solution page: 

#1
def digitize(n):
    return [int(x) for x in str(n)[::-1]]


#2

def digitize(n):
    return map(int, str(n)[::-1])

#3

def digitize(n):
    return [int(x) for x in reversed(str(n))]
