# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""


# my solution: 

def order(sentence):
    
    broken_list = sentence.split(' ')
    
    numbered_words = {}
    
    for word in broken_list:  
        
        for char in word:
            
            if char.isdigit():
                
                numbered_words[int(char) - 1] = word
        
    ordered_words = dict(sorted(numbered_words.items()))
    
    return ' '.join(list(ordered_words.values()))

# asked chatGPT for code and this is what it came up with:

def order(sentence):
    # Split the sentence into words
    broken_list = sentence.split(' ')
    
    # Initialize a list with placeholders to ensure the list has the correct size
    ordered_list = [None] * len(broken_list)
    
    for word in broken_list:
        for char in word:
            if char.isdigit():
                # Place the word at its correct position (subtracting 1 for zero-based indexing)
                index = int(char) - 1
                ordered_list[index] = word
                break  # Assuming only one digit per word, we can break after finding it
    
    # Filter out any None values and join the words into a sentence
    ordered_sentence = ' '.join(word for word in ordered_list if word is not None)
    
    return ordered_sentence

# clever solutions from the solutions page:

#1
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))


#2
def order(sentence):
    if not sentence:
        return ""
    result = []    #the list that will eventually become our setence
      
    split_up = sentence.split() #the original sentence turned into a list
  
    for i in range(1,10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    #adds them in numerical order since it cycles through i first
  
    return " ".join(result)

#3
def order(sentence):
  return " ".join(sorted(sentence.split(), key=min))