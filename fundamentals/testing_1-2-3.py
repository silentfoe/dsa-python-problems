# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

# my solution: 

def number(lines):
    numbered_lines = []
    count = 1
    
    for letter in lines:
        numbered_lines.append(f'{count}: {letter}')
        count += 1
    
    return numbered_lines

# some cool solutions from the solutions page: 

#1
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]

#2
def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]

#3
def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]

#4
def number(lines):
    return ["{0}: {1}".format(i + 1, lines[i]) for i in xrange(len(lines))]
