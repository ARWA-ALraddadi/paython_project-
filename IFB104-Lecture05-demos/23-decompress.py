##--------------------------------------------------------------------
##
##  Demonstration - Decompressor
##
##  This demonstration shows elegant recursive solution to a
##  complex-looking repetitive problem.
##


#---------------------------------------------------------------------
#
# Problem statement
#
# Consider a list of items which has been compressed using
# the following scheme: whenever a particular item appears more than
# twice consecutively it is replaced with two values, the number of
# repetitions followed by the item itself.  For example, the list
#
#   ['a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd']
#
# would be compressed as
#
#   ['a', 4, 'b', 3, 'c', 'd', 'd'].
#
# We are required to write a function to decompress such lists.  It
# may be assumed that none of the items in the original list was a
# number.
#
"""
Extreme case - empty list:
>>> decompress([])
[]

Extreme case - no decompression required:
>>> decompress(['a', 'b', 'c', 'd', 'e'])
['a', 'b', 'c', 'd', 'e']

A normal case:
>>> decompress([3, 'a', 'b', 5, 'c', 'd', 3, 'e'])
['a', 'a', 'a', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'e', 'e', 'e']

Another normal case:
>>> decompress([3, 'a', 3, 'b', 3, 'c'])
['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']

And a short, but normal example:
>>> decompress([10, 'x'])
['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']

"""

#---------------------------------------------------------------------
#
# The recursive solution
#

# Return the result of decompressing a compressed list
#
def decompress(items):

    if items == []:
        # Base case - Nothing to process
        return []
    elif not isinstance(items[0], int):
        # Recursive case - First item is not a number so keep it
        # and continue processing
        return [items[0]] + decompress(items[1:])
    else:
        # Recursive case - First item is a number so duplicate the
        # second item that many times and process the remainder
        return (items[0] * [items[1]]) + decompress(items[2:])


#---------------------------------------------------------------------
#
# Run the tests
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
