######################################################################
##
##  Demonstration - Operator overloading
##
##  This demonstration shows how a robust overloaded function can be
##  created through explicit consideration of its argument's type.
##


#---------------------------------------------------------------------
#
# The requirement:
#
# Python's '+' operator can be used to add numbers and concatenate
# sequence types.  However, it does not allow sequence and number
# objects to be concatenated.  Define a function called "glue" that
# accepts a list of strings and integers and returns a single string
# comprising the given strings and numbers concatenated together.
#


#---------------------------------------------------------------------
#
# An algorithm:
#
# To return the given strings and numbers "glued" together:
# a. Convert all the numbers to their string representation
# b. Concatenate all the strings and converted numbers
#


#---------------------------------------------------------------------
#
# A more cautious algorithm:
#
# 1. To return the given strings and numbers "glued" together:
#    a. Convert all the numbers to their string representation
#    b. Concatenate all the strings and converted numbers
#
# 2. However, if the supplied argument is not a list, or if there
#    are items in the list that are not integers or strings, raise
#    an exception 
#


#---------------------------------------------------------------------
#
# An implementation:
#

# Return a string constructed from a list of strings and integers
def glue(items):

    # Confirm that the argument is correctly typed
    assert isinstance(items, list), "Non-list argument provided to 'glue'"
    for item in items:
        assert isinstance(item, int) or isinstance(item, str), \
               "Item provided to 'glue' is neither integer nor string"

    # Construct the result by appending each item in the list,
    # converting it to a string first
    result = ''
    for item in items:
        result = result + str(item)
    return result

    

#---------------------------------------------------------------------
#
# Some tests (using American popular culture and slang references
# from the last century):
#

print(glue(['NCC-', 1000 + 700 + 1, ': U.S.S. Enterprise']))
print(glue([20 + 3, ' Skiddoo! Oh you kid!']))
print(glue(["He's a bum! ", 8 * 10 + 6, ' him.']))
print(glue([1 + 1 + 1, ' on a match - unlucky for some!']))

# And two tests which each produce an exception:

print(glue('One Two Three'))
print(glue(['a', ['x'], 'b']))
