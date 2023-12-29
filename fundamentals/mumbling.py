# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


# my solution: 

def accum(s):
    
    #create an empty list
    letters = []
    
    #make the string lower case
    split = s.lower()
    
    #want to start a loop for each character that duplicates the char based on the index number plus 1
    #start by looping over each index
    for indx in range(len(split)):
        chars = ''
        
        #duplicating each letter found at the index to total the index + 1, i.e. index 0 would have 1 letter
        for nums in range(indx + 1):
            #checking to see if the char is not the first, if so then it's lower case           
            if not nums == 0:
                chars += split[indx]
            #if the char is the first, capitilize it
            else:
                chars += split[indx].upper()
            
        letters.append(chars)
    
    return '-'.join(letters)


# other solutions that are much shorter found on the solutions page: 

#1
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

#2
def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))