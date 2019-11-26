################################################################
##
##  As a demonstration of a function which applies defensive
##  programming in different ways, consider a predicate
##  which is intended to return True if a given natural
##  number (i.e., a non-negative integer) is a square of
##  another natural number.
##
##  From this description the function could be "misused" in
##  three ways:
##
##  1) It could be given a negative number.
##  2) It could be given a floating point number.
##  3) It could be given a value which is not a number at
##     all.
##
##  By adding some "defensive" code we can make a naive
##  implementation more robust by responding appropriately
##  to each of these cases:
##
##  1) A negative number can never be a square of another
##     number, so we can always return False in this case.
##     Here we choose to do so "silently", not drawing
##     attention to the unexpected value at all, since the
##     answer returned is still "correct" mathematically.
##  2) A positive floating point number could be a square of
##     a natural number so, even though we're not required
##     to handle floating point numbers we can still do so,
##     but choose to generate a "warning" message in this
##     case.
##  3) If the function is given a non-numerical value it
##     is reasonable to assume that something is seriously
##     wrong with the calling code, so in this case we
##     generate an "error" message and return the special
##     value None.



#---------------------------------------------------------


# Return True if the given natural number is the square of
# some other natural number
def is_square(natural_number):

    from math import sqrt

    # Three "defensive" checks follow

##    # Check that the parameter is a number
##    if not (isinstance(natural_number, int) or isinstance(natural_number, float)):
##        print('ERROR - parameter must be numeric, given:', repr(natural_number))
##        return None
##
##    # Check that the parameter is positive
##    if natural_number < 0:
##        return False
##
##    # Check that the parameter is a natural number
##    if isinstance(natural_number, float):
##        print('Warning - expected natural, given float:', natural_number)

    # Return True if the number's square root is a whole number
    return sqrt(natural_number) % 1 == 0



#---------------------------------------------------------


# Some tests
#
# The first of these tests is a "valid" one, but the remaining
# three all provide unexpected inputs.  Uncommenting the
# "defensive" checks above will cause the function to respond
# appropriately.  (It will crash until the defensive code is
# uncommented.  Why?)

print(is_square(36)) # expected input
print()
print(is_square(-1)) # unexpected input, but handled silently
print()
print(is_square(225.0)) # unexpected input, handled with warning
print()
print(is_square('August')) # unexpected input, handled as an error


