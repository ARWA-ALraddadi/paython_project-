##--------------------------------------------------------------------
##
##  Demonstration of indefinite iteration
##
##  This example illustrates a problem involving repetition where
##  it's difficult to know in advance how many iterations will be
##  needed.
##


#---------------------------------------------------------------------
#
# Requirements specification
#
# Given a list of numbers, return its "balance point", i.e., the
# index at which the sum of the numbers to the left equals the sum
# of the numbers to the right (as closely as possible).
#
# More precisely, we define the "balance point" of a list of numbers
# as the smallest index such that the sum of the numbers to the left
# of the index, exclusive, equals or exceeds the sum of the numbers
# to the right of the index, inclusive.
#
# Note 1: If we wanted to think of the physical analogue to this
# situation, i.e., balancing a beam with weights on it, we would
# also need to consider the distance of each weight from the
# balance point, but we ignore this complication here.
#
# Note 2: It's best to think of the index in this kind of situation
# as pointing *between* the list's items, e.g.,
#
#    +---+---+---+---+---+
#    | 7 | 4 | 8 | 1 | 1 |
#    +---+---+---+---+---+
#    0   1   2   3   4   5
#            ^
#            |
#            balance point in this example is 2
#


'''
Some tests

>>> balance_point([3, 1, 3])
2

>>> balance_point([5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5])
5

>>> balance_point([7, 4, 8, 1, 1])
2

>>> balance_point([1, 2, 3, 4, 5, 6])
5

>>> balance_point([6, 5, 4, 3, 2, 1])
2

>>> balance_point([1, 1, 1, 1, 1, 1, 3])
5

>>> balance_point([3, 1, 1, 1, 1, 1, 1])
3

>>> balance_point([3, 3, 3, 0, 0, 0, 0, 0])
2

>>> balance_point([0, 0, 0, 1])
4

>>> balance_point([0, 0, 0, 0])
0

>>> balance_point([])
0
'''


#---------------------------------------------------------------------
#
# A solution using a "while" loop
#
# Return the "balance point" for a list of numbers, i.e., the
# smallest index such that the sum of the numbers to left (exclusive)
# equals or exceeds the sum of the numbers to the right (inclusive)
#
def balance_point(numbers):
    position = 0
    left_sum = 0 # sum of numbers left of the position
    right_sum = sum(numbers) # sum of numbers right of position
    while left_sum < right_sum:
        left_sum = left_sum + numbers.pop(0) # add next number to left
        right_sum = sum(numbers) # recalculate right
        position = position + 1
    return position


#---------------------------------------------------------------------
#
# Observation: We could also have solved this particular
# problem using a "for" loop and a "break" statement because
# there is a known upper bound for the number of iterations,
# expressible in terms of the given list's length
#


#---------------------------------------------------------------------
#
# Run the tests
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
