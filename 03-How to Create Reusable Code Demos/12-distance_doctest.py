#---------------------------------------------------------------------
#
#  Demonstration - Automatically testing programs
#
#  This file illustrates the way we can use Python's "doctest"
#  module to automatically run several tests of our functions.
#
#  We assume we've been asked to write a function called "distance"
#  which returns the distance between two given cartesian coordinates.
#  Recall that the distance between two points is the square root of
#  the difference between the x coordinates squared plus the
#  difference between the y coordinates squared.


#---------------------------------------------------------------------
#
# The acceptance tests
#
# The following docstring contains the various tests that we want
# applied to the function.  Note that they're written in exactly
# the same way they would appear if you ran each test manually in
# the shell window.
#
"""
Test 1 - No distance at all
>>> distance([1, 1], [1, 1])
0.0

Test 2 - Typical case
>>> distance([4, 5], [1, 1])
5.0

Test 3 - The same example switched around
>>> distance([1, 1], [4, 5])
5.0

Test 4 - A vertical distance
>>> distance([-3, -3], [-3, 7])
10.0

Test 5 - A horizontal distance
>>> distance([4, -2], [-3, -2])
7.0
"""


#---------------------------------------------------------------------
#
# The function under development
#
# The version of the function shown here contains two distinct errors
# and fails most of the tests.  How to fix the code is explained
# at the end of this file.
#
# Return the distance between two given coordinates expressed
# as x-y pairs
#
def distance(coord_a, coord_b):
    from math import sqrt
    x_diffs_squared = coord_a[0] - coord_b[0] ** 2
    y_diffs_squared = coord_a[1] - coord_b[0] ** 2
    return sqrt(x_diffs_squared + y_diffs_squared)


#---------------------------------------------------------------------
#
# A main program to run the tests
#
# When this module is run, the following main program performs
# the unit tests using the docstring above - see Section 25.2 of
# the "Python Library Reference" for further detail.  To avoid
# being overwhelmed with output, we've requested a non-verbose
# result and that only the first failure is described, if any.
# Normally "testmod" prints nothing if all the tests succeed, which
# is a bit anticlimactic, so we've printed the value it returns, to
# allow us to see the outcome in all cases.
#
if __name__ == "__main__":
    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
    print(testmod(verbose = False,
                  optionflags = REPORT_ONLY_FIRST_FAILURE))








































#---------------------------------------------------------------------
#
# Solution
#
# There are two problems with the way the "differences squared" of the
# x and y values are calculated:
#
# 1) The programmer has forgotten the precedence rules for arithmetic
#    operators and has written the equivalent of "x1 - (x2 ** 2)"
#    instead of "(x1 - x2) ** 2".  This error causes Test 2 to fail,
#    as well as some later ones.
#
# 2) The programmer has made a cut-and-paste error when calculating
#    the differences of the y coordinates squared and has written
#    "coord_b[0]" instead of "coord_b[1]".  Even after the first
#    problem above is fixed, this causes Test 3 to fail.
#
# The corrected code, which allows all tests to pass, is:
#
#    x_diffs_squared = (coord_a[0] - coord_b[0]) ** 2
#    y_diffs_squared = (coord_a[1] - coord_b[1]) ** 2



