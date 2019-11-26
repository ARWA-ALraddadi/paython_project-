#-----------------------------------------------------
#
# A small demonstration of debugging a function
#
# Here we have a function which is coded incorrectly.
# The challenge is to use IDLE's debugger to identify
# precisely where the errors occur.
#


#-----------------------------------------------------
# Goal: We want to write a function that takes a list
# of numbers and returns the separation between the
# largest and smallest numbers in the list.  To solve
# this problem we write the following function and
# a simple test case to try it out.  Unfortunately,
# if you try to run this program it doesn't work.  The
# goal of this demonstration, therefore, is to use
# IDLE's debugger to "single step" through the code
# to try and work out exactly what's going wrong.
# (Try it yourself. The solution at the bottom of this
# file.)

# The function we're debugging (uncommented to make
# it harder to understand) ...
def separation(numbers):
    how_many = len(numbers)
    numbers_in_order = sorted(numbers)
    largest = numbers_in_order[how_many]
    smallest = numbers_in_order[1]
    return largest - smallest

# A main program that tests the function defined above ...
test_list = [8, 7, 3, 2, 4]
print(separation(test_list)) # should print 6











































# Solution: There are two distinct errors in the
# draft function, both "off by one" errors with
# the list indices.  The programmer has forgotten
# that we index list values starting from zero,
# not one.  The correct code is:
#
#     largest = numbers_in_order[how_many - 1]
#     smallest = numbers_in_order[0]
#
# By using the debugger to single-step through the
# code and examine the values of all variables,
# you should be able to isolate exactly where the
# error occurs and, hopefully, deduce why.
