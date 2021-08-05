######################################################################
##
##  Demonstration - Separate signed numbers
##
##  Assertions are typically used to check input values at the
##  beginning of a function, but they can also be used later in
##  a function to confirm that the calculation is producing the
##  right results.
##
##  This example shows how embedded assertions can help signal
##  problems not only in a function's inputs but also in its
##  calculation.
##


#---------------------------------------------------------------------
#
# The requirement:
#
# Given a list of integers, define a function that returns the
# negative, zero and positive numbers in separate lists.
#


#---------------------------------------------------------------------
#
# A faulty implementation:
#
# The following attempted solution to the above requirement contains
# (at least) two coding errors, but is this obvious from looking at
# at the test results?
#

# Return the negative, zero and positive numbers from a given list
# separately
def separate_signs_0(numbers):

    negatives = []
    zeros = []
    positives = []

    for index in range(1, len(numbers)):
        if numbers[index] < 0:
            negatives += [numbers[index]]
        elif numbers[index] > 0:
            positives += [numbers[index]]
        else:
            zeros = [numbers[index]]

    result = [negatives, zeros, positives]
    return result


# A couple of tests:

print(separate_signs_0([5, -1, 0, 1, 3, 2, -5, -8, -3, 4, 7, 8, 9,
                        6, -6, 0, -2]))
print()
print(separate_signs_0([101, -99, 23, 89, -90, 88, 345, 222, 8, 44,
                        12, -56, 99, -86, 451, -55, -10, 21, 909]))


#---------------------------------------------------------------------
#
# An implementation augmented with assertions:
#
# The following version of the program has assertions added to
# document some assumptions about both the input and output
# values
#

# Return the negative, zero and positive numbers from a given list
# separately
def separate_signs_1(numbers):

    # Confirm that the input is a list of integers
    assert isinstance(numbers, list), "Non-list given to 'separate_signs_1'"
    for item in numbers:
        assert isinstance(item, int), "Non-integer given to 'separate_signs_1'"

    negatives = []
    zeros = []
    positives = []

    for index in range(1, len(numbers)):
        if numbers[index] < 0:
            negatives += [numbers[index]]
        elif numbers[index] > 0:
            positives += [numbers[index]]
        else:
            zeros = [numbers[index]]

    # Confirm that the numbers are correctly separated
    for num in negatives:
        assert num < 0, "Non-negative in negative list in 'separate_signs_1'"
    for num in zeros:
        assert num == 0, "Non-zero in zero list in 'separate_signs_1'"
    for num in positives:
        assert num > 0, "Non-positive in positive list in 'separate_signs_1'"
    
    result = [negatives, zeros, positives]

    # Confirm that all of the given numbers appear in the result
    assert sorted(numbers) == sorted(negatives + zeros + positives), \
           "Outputs differ from inputs in 'separate_signs_1'"

    return result


# A few tests:

print(separate_signs_1('-9, 3, 0, 5, 12'))
print()
print(separate_signs_1([-2, -1, 'Zero', 1, 2]))
print()
print(separate_signs_1([5, -1, 0, 1, 3, 2, -5, -8, -3, 4, 7, 8, 9,
                        6, -6, 0, -2]))
print()
print(separate_signs_1([101, -99, 23, 89, -90, 88, 345, 222, 8, 44,
                        12, -56, 99, -86, 451, -55, -10, 21, 909]))


#---------------------------------------------------------------------
#
# Challenge:
#
# Fix function separate_signs_1 so that it works correctly (and no
# longer raises assertions)
#
# The solution appears (far) below...
#









































#---------------------------------------------------------------------
#
# Solution:
#
# The (known) errors in "separate_signs_1" are:
#
# 1) Counter "index" should be initialised as zero, not one.  This
#    error causes it to skip the first number.
#
# 2) The assignment to "zeros" should be of the form "+=", not "=".
#    This error means that no more than one "0" is ever put into
#    the list.  The fact that this one character makes such a
#    difference also illustrates why concise coding tricks are
#    best avoided.  Make your code clear rather than short.
#
