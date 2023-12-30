# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more: http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

# my solution: 

def DNA_strand(dna):
    
    new_str = ''
    
    for letter in dna:
        if letter == 'A':
            new_str += 'T'
        elif letter == 'T':
            new_str += 'A'
        elif letter == 'G':
            new_str += 'C'
        elif letter == 'C':
            new_str += 'G'
        else:
            new_str += letter
    
    return new_str
    
#better solution I found on the solutions page: 

def DNA_strand(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([reference[x] for x in dna])