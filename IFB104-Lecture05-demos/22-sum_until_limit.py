##--------------------------------------------------------------------
##
##  Demonstration - Recursive function with two base cases
##
##  This example illustrates a recursively-defined function that
##  has two base cases because there are two possible
##  ways in which it can stop.
##


#---------------------------------------------------------------------
#
# The problem:
#
# Define a function which, given a numerical limit, and a list of
# numbers, returns the sum of the numbers up to, but not exceeding
# the limit.  For instance, if the limit was the maximum carrying
# capacity of a truck, and the list contained the weights of packages
# arriving on a conveyor belt, we could use this function to
# determine how heavily laden the truck will be when filled
# up to, but not exceeding, its capacity.
#


#---------------------------------------------------------------------
#
# The algorithm:
#
# Given a limit and a list of values, select one of
# the following alternatives:
#
# 1. If the list of numbers is empty there are no values to sum,
#    so return zero (base case); or
#
# 2. If the first value in the list exceeds the limit then
#    there are no acceptable values to sum, so return zero
#    (base case); or
#
# 3. If the first number in the list is less than or equal to the
#    limit then return the sum of the first number plus the
#    sum of the numbers from the remainder of the list until
#    the limit less the first value in the list (recursive case).
#


#---------------------------------------------------------------------
#
# The implementation:
#

# Returns the sum of the numbers in the given list up to but
# not exceeding the given limit
#
def sum_until(limit, numbers):

    if numbers == []:
        # Base case - No numbers to process
        return 0
    elif numbers[0] > limit:
        # Base case - Can't add another number without
        # exceeding the limit
        return 0
    else: 
        # Recursive case - Result is the first number added to
        # the sum remaining within a reduced limit
        return numbers[0] + sum_until(limit - numbers[0], numbers[1:])


#---------------------------------------------------------------------
#
# Some tests:
#

# A normal case - the sum of the first three items fits within the
# limit:
print('Test 1:', sum_until(10, [4, 2, 3, 5, 1]))

# Another normal case - the first five items fit within the limit:
print('Test 2:', sum_until(20, [1, 2, 9, 5, 1, 6, 3, 2, 7]))

# An extreme case - the first item exceeds the limit:
print('Test 3:', sum_until(15, [20, 25, 17]))

# An extreme case - the sum of all items is less than the limit:
print('Test 4:', sum_until(50, [25, 10, 2, 3, 5]))


