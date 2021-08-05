#---------------------------------------------------------
#
# Vowel counter
#
# Define an iterative function with one parameter, a string,
# which returns the number of vowels the string contains
# (including duplicates).
#
# Recall that the vowels in english are a, e, i, o and u.
#

#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> vowel_count('abc') # Test 1
1

>>> vowel_count('My very elegant mother just sat upon nine porcupines') # Test 2
16

>>> vowel_count('The quick brown fox jumps over the lazy dog') # Test 3
11

>>> vowel_count('aeiou') # Test 4
5

>>> vowel_count('') # Test 5
0

>>> vowel_count('xyzzy') # Test 6
0

>>> vowel_count('abc') == 1 # Test 7 (confirm value is returned, not printed)
True

"""


#---------------------------------------------------------
#
# Suggested solution strategy:
#
# 1. Initialise a new integer variable to keep count
# 2. For every character in the given string:
#    a. If the character is a vowel:
#         i. Increment the counter 
# 3. Return the counter
#


# Given a string, return the number of vowels it contains
def vowel_count(text):

    # Initialise counter
    count = 0

    # Count the number of vowels
    for character in text:
        if character in 'aeiou':
            count = count + 1
        # otherwise, do nothing 

    # Return the result
    return count


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
