#---------------------------------------------------------
#
# Is it a palindrome?
#
# A palindrome is a sentence that reads the same backwards
# and forwards (ignoring capitalisation, punctuation and
# spaces).  See the test cases below for examples.
#
# Define a function with one parameter, a non-empty string,
# which returns True or False depending on whether or not
# that string is a palindrome.
#
# NB: To complete this exercise you must first complete
# the "Get Alphabetics" exercise, because we will import
# your solution to that exercise into this one.
#


# TESTCASES-----------------------------------------------
""" 
>>> is_palindrome('Hannah') # Test 1 (normal case)
True

>>> is_palindrome('Annie') # Test 2 (normal case)
False

>>> is_palindrome('amanaplanacanalpanama') # Test 3 (normal case)
True

>>> is_palindrome('A man, a plan, a canal, Panama!') # Test 4 (normal case)
True

>>> is_palindrome("Madam! In Eden, I'm Adam!") # Test 5 (normal case)
True

>>> is_palindrome("May a moody baby doom a yam?") # Test 6 (normal case)
True

>>> is_palindrome("A Toyota's a Toyota!") # Test 7 (normal case)
True

>>> is_palindrome("Was it a car or a cat I saw?") # Test 8 (normal case)
True

>>> is_palindrome('Frustrated palindrome') # Test 9 (normal case)
False

>>> is_palindrome('a') # Test 10 (boundary case)
True

"""

#---------------------------------------------------------
#

# Import your function for extracting the alphabetic
# characters from a string
from get_alphabetics import *


# Given a non-empty string, a function to determine if it is a palindrome
# (something that reads the same backward or forward)
#
def is_palindrome(phrase):

    # Prepare the string for examination
    only_alpha = get_alphas(phrase)

    # Look at each corresponding pair of characters
    # up until halfway through the string:
    halfway = len(only_alpha) // 2
    for index in range(halfway):

        # Check that characters from each end match
        if only_alpha[index] != only_alpha[-(index + 1)]:

            # Non-match found
            return False

    # Inspected all pairs and found that they matched:
    return True


# Comment: Another solution strategy would be to split the string
# in half, reverse the second half, and see if it equals the
# first half.


#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))

