# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Example:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

# my first solution: 

def to_jaden_case(string):
    words = string.lower().split(' ')
    
    cap_words = []
    
    for word in words: 
        cap_words.append(word[0].upper() + word[1:])
        
    return ' '.join(cap_words) or ''

# second solution to solve using lamba function with map

def to_jaden_case(string):
    
    words = string.lower().split(' ')
    
    if words:
        return ' '.join(map(lambda word: word[0].upper() + word[1:], words)) 
    
    return ''

# third solution, removing the words variable 
def to_jaden_case(string):
    
    if string:
        
        return ' '.join(map(lambda word: word[0].upper() + word[1:], string.lower().split(' ')))
    
    return ''


# a couple of other cool solutions and methods I didn't know about in python: 

#1
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

#2 
import string
def to_jaden_case(strr):
    strr = string.capwords(strr)
    return strr

    