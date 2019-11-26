##-------------------------------------------------------------------
##
##  Demonstration - A simple repetitive function
##
##  The following program calculates the sum of the
##  integers in an inclusive-exclusive range in four different
##  ways:
##  1. Using Python's built-in sum, range and list functions.
##  2. Using fixed iteration
##  3. Using condition-controlled iteration
##  4. Using recursion
##
##  So that you can see the way variables and parameters are
##  updated we have added some print statements to the iterative
##  and recursive versions, but they do not contribute to the
##  calculation


#---------------------------------------------------------------------
#
# The built-in version:
#
# To return the sum of the numbers in the range a, inclusive, to b,
# exclusive, return the sum of the numbers in that range expressed
# as a list

# Given two numbers a and b, return the sum of the integers
# in the range a, inclusive, to b, exclusive
#
def sum_range_1(a, b):
    return sum(list(range(a, b)))


#---------------------------------------------------------------------
#
# Using fixed iteration:
#
# To return the sum of the numbers in the range a, inclusive, to b,
# exclusive:
# 1. Set the total so far to 0
# 2. For each value from a, inclusive, to b, exclusive:
#    a. Add the value to the total
# 3. Return the total
#

# Given two numbers a and b, return the sum of the integers
# in the range a, inclusive, to b, exclusive
#
def sum_range_2(a, b):
    total = 0
    for value in range(a, b):
        print('Fixed iteration:', value, total)
        total = total + value
    return total


#---------------------------------------------------------------------
#
# Using conditional iteration:
#
# To return the sum of the numbers in the range a, inclusive, to b,
# exclusive:
# 1. Set the total so far to 0
# 2. While a is less than b:
#    a. Add a to the total
#    b. Increment a
# 3. Return the total
#

# Given two numbers a and b, return the sum of the integers
# in the range a, inclusive, to b, exclusive
#
def sum_range_3(a, b):
    total = 0
    while a < b:
        print('Conditional iteration:', a, b, total)
        total = total + a
        a = a + 1
    return total


#---------------------------------------------------------------------
#
# The recursive algorithm:
#
# To return the sum of the numbers in the range a, inclusive, to b,
# exclusive:
# 1. Return 0 if a equals or exceeds b (base case)
# 2. Return a plus the sum of the numbers in the range
#    (a+1) to b otherwise (recursive case)
#

# Given two numbers a and b, return the sum of the integers
# in the range a, inclusive, to b, exclusive
#
def sum_range_4(a, b):
    if a >= b:
        print('Base case:', a, b)
        return 0
    else:
        print('Recursive case:', a, b)
        return a + sum_range_4(a + 1, b)
    

#---------------------------------------------------------------------
#
# Some tests, showing that all four functions produce the same result:
#

print('Using built-in functions:')
print(sum_range_1(4, 8))
print()
print('Using fixed iteration:')
print(sum_range_2(4, 8))
print()
print('Using conditional iteration:')
print(sum_range_3(4, 8))
print()
print('Using recursion:')
print(sum_range_4(4, 8))
