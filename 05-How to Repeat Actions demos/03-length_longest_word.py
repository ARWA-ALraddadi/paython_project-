#---------------------------------------------------------
#
# Length of the longest word
#
# As a demonstration of a program that iterates over the
# values in a list, here we present a function with one
# parameter, some text, that calculates and returns
# the length of the longest word in that text.  For
# simplicity we assume the only punctuation marks in the
# text are commas and full stops.


#---------------------------------------------------------
#
# Some test cases
#
""" 
Normal case - similar sized words
>>> length_longest_word('One, two, three, four and five.') # Test 1
5

Normal case - all words the same length
>>> length_longest_word('Yo, Ho, Ho') # Test 2
2

Normal case - words of widely differing lengths
>>> length_longest_word('An honorificabilitudinitatibus of \
antidisestablishmentarianism.') # Test 3
28

Normal case
>>> length_longest_word('Space, the final frontier.  These are the \
voyages of the Starship Enterprise.') # Test 4
10

Boundary case - empty string
>>> length_longest_word('') # Test 5
0
"""


#---------------------------------------------------------
#
# A solution using a for-each loop
#

# A function that determines the length of the longest
# word in some given text
#
def length_longest_word(text):

    # Remove punctation characters
    text = text.replace(',', '')
    text = text.replace('.', '')

    # Split the text into separate words
    words = text.split()

    # Initialise a variable to keep track of the longest word's length
    longest_length = 0

    # For each word, see if it's the longest so far
    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)

    # Return the result
    return longest_length
                         

#---------------------------------------------------------------------
#
# Run the tests, automatically
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))

