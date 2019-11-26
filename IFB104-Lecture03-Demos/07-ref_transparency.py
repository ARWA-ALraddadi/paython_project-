#---------------------------------------------------------------------
#
# Demonstration - Referential transparency
#
# The small examples in this file illustrate the meaning of
# "referentially transparent" function definitions.  A
# function that is referentially transparent always does this
# same thing when given the same arguments.  In general, it is
# easier to understand programs that use only referentially-
# transparent functions.
#
# Functions that are NOT referentially transparent usually
# return random values or, as in the example below, use a
# global variable to "remember" their previous state.
#

#---------------------------------------------------------------------
#
# The following function is referentially transparent because it
# always gives the same answer when given the same argument:
#

# Returns the given number less five
def take_5(minuend):
    subtrahend = 5 # constant to be subtracted
    return minuend - subtrahend
    
# Some tests:
print(take_5(10))
print(take_5(10))
print(take_5(10))
print(take_5(10))
print(take_5(10))

print()

#---------------------------------------------------------------------
#
# The following function is NOT referentially transparent because it
# gives different answers when given the same argument:
#

subtrahend = 5 # global variable to remember how much to subtract

# Returns the given number less five or more
def take_at_least_5(minuend):
    global subtrahend # allow assignment to global variable
    subtrahend = subtrahend + 1 # increment amount to be subtracted
    return minuend - subtrahend
    
# Some tests:
print(take_at_least_5(10))
print(take_at_least_5(10))
print(take_at_least_5(10))
print(take_at_least_5(10))
print(take_at_least_5(10))
