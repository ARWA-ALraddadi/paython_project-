######################################################################
##
##  Demonstration - Checking input values
##
##  In practice it would be too distracting to worry about everything
##  that could go wrong while trying to get a program to work.
##  Instead we should get the basic functionality correct first, and
##  then introduce additional checks for invalid conditions to make
##  the solution more robust.
##
##  This demonstration of defensive programming shows how checking
##  of input values can be added after getting the basic algorithm
##  to work first.  It also shows how we can write unit tests that
##  expect an exception to the thrown.
##


#---------------------------------------------------------------------
#
# Step 0 - Requirements specification
#
# Given a list of integers, return its median, i.e., the middle
# value in the list if it is arranged in order of magnitude.  If the
# length of the list is even the median is the average of the middle
# two numbers.
#
"""
Acceptance tests provided as part of the original requirements
specification

A typical example of an odd-length list:
>>> median_0([5, 9, 1, 0, 8, 7, 4]) # Test 1
5

A typical example of an even-length list (which also shows that
integer arithmetic is used for calculating the average):
>>> median_0([8, 3, 2, 9, 6, 1]) # Test 2
4

The shortest possible odd-length list:
>>> median_0([6]) # Test 3
6

A very short even-length list:
>>> median_0([6, 4]) # Test 4
5

A typical example involving positive and negative numbers:
>>> median_0([4, -3, 8, 0, -1]) # Test 5
0

Additional acceptance tests added for invalid inputs

A non-list argument:
>>> median_1(67) # Test 6
Traceback (most recent call last):
AssertionError: Wrong type of argument given to 'median'

A list containing a non-integer value:
>>> median_1([4, 5, 'a', 6, 3]) # Test 7
Traceback (most recent call last):
AssertionError: Non-integer value given to 'median'

An empty list, which has no median:
>>> median_1([]) # Test 8
Traceback (most recent call last):
AssertionError: Given list has no median value
"""


#---------------------------------------------------------------------
#
# Step 1 - First version of the function
#
# The following version of the required program passes all the
# tests above with valid inputs.  However, it's behaviour when given
# invalid input is unclear.  (Try it with Tests 6 to 8).
#

# Return the median of a list of integers
def median_0(numbers):

    # Utility function: Return True iff given number is odd
    def is_odd(num):
        return num % 2 != 0

    # Utility function: Return average of two integers
    def average(num1, num2):
        return (num1 + num2) // 2 

    # Sort the given numbers into ascending order
    sorted_numbers = sorted(numbers)

    # Return their median
    how_many = len(sorted_numbers)
    midpoint = how_many // 2
    if is_odd(how_many):
        return sorted_numbers[midpoint]
    else: # Even-length list
        return average(sorted_numbers[midpoint - 1],
                       sorted_numbers[midpoint])


#---------------------------------------------------------------------
#
# Step 2 - Second version of the function
#
# Before completing the function we should ask ourselves what things
# the specification above left unstated.
#
# Firstly, it assumed that the function is actually
# given a list of natural numbers when called.  As defensive
# programmers we should assert that this is indeed true.
#
# More subtly, the requirements specification failed to specify
# what should be done in the extreme case where the median function
# is given an empty list.  In this situation there is no median
# value to return.  Returning some default value, such as zero, would
# be misleading because this is a possible median value for a
# non-empty list.  The best solution in this case, therefore, is
# to alert the calling program to the problem by raising an
# exception.
#
# Below is a second version of the function with assertions added
# to check that the input is correct and to generate exceptions
# with helpful error messages if it is not. Note the additional unit
# tests above which show how the function is expected to respond to
# invalid inputs.
#


# Return the median of a list of integers
def median_1(numbers):

    # Utility function: Return True iff given number is odd
    def is_odd(num):
        return num % 2 != 0

    # Utility function: Return average of two integers
    def average(num1, num2):
        return (num1 + num2) / 2 

    # Confirm that the argument is a non-empty list of integers
    assert isinstance(numbers, list), "Wrong type of argument given to 'median'"
    for item in numbers:
        assert isinstance(item, int), "Non-integer value given to 'median'"
    assert numbers != [], "Given list has no median value"

    # Sort the given numbers into ascending order
    sorted_numbers = sorted(numbers)

    # Return their median
    how_many = len(sorted_numbers)
    midpoint = how_many // 2
    if is_odd(how_many):
        return sorted_numbers[midpoint]
    else: # Even-length list
        return average(sorted_numbers[midpoint - 1],
                       sorted_numbers[midpoint])


#---------------------------------------------------------------------
#
# A function to run the unit tests
#
def test():
    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
    print(testmod(verbose = False,
                  optionflags = REPORT_ONLY_FIRST_FAILURE))
