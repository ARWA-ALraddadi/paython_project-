#---------------------------------------------------------
#
# Counting non-space characters
#
# As a simple example of recursion, here we define a
# functon to count the number of non-space characters
# in a given string.
#


#---------------------------------------------------------
#
# Some tests
#
""" 
Normal case - no spaces
>>> count_non_spaces('NoSpacesHere') # Test 1
12

Normal case - some spaces
>>> count_non_spaces('Some spaces here!') # Test 2
15

Normal case - leading/trailing spaces
>>> count_non_spaces('  some... spaces... here  ') # Test 3
20

Boundary case - only spaces
>>> count_non_spaces('         ') # Test 4
0

Boundary case - empty string
>>> count_non_spaces('') # Test 5
0
"""


#---------------------------------------------------------
#
# A solution
#

# A recursive function to count the number of non-space
# characters in a given string
#
def count_non_spaces(phrase):

    # Base case - No characters in the string
    if phrase == '':
        # Return zero because there are no characters at all
        return 0
    
    # Recursive case - First character is a space
    elif phrase[0] == ' ': 
        # Return the number of non-space chars in the
        # rest of the string
        return count_non_spaces(phrase[1:])

    # Recursive case - First character is not a space
    else: 
        # Return one (for this character) plus the number
        # of non-space chars in the rest of the string
        return 1 + count_non_spaces(phrase[1:])


#-----------------------------------------------------------
#
# Run the tests
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
