# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# my solution: 

def solution(s):
    
    sentence = ''
    
    for indx in range(len(s)):
        if s[indx] == s[indx].upper():
            sentence += f' {s[indx]}'
        else:
            sentence += s[indx]
    
    return sentence

# a couple of clever solutions I found on the solutions page: 

#1
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)


#2
def solution(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr
