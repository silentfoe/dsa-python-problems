# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# my solution: 

def reverse_words(text):

    words_list = text.split(' ')
    
    return ' '.join([words[::-1] for words in words_list])


# other clever solution I found on the code wars solutions page: 

def reverse_words(str):
  return " ".join(map(lambda word: word[::-1], str.split(' ')))