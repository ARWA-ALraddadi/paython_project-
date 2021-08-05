#---------------------------------------------------------------------
#
# Demonstration - Global variable
#
# The small example in this file illustrates the use of a global
# variable to allow a function to remember a value between its
# invocations
#

#---------------------------------------------------------------------
#
# The goal is to define a function that returns the number of times
# it has been called.  This means that the function will return a
# different result each time it's called!
#

number_of_calls = 0 # initialise a natural number counter as a
                    # global variable to remember how many calls
                    # have been made

# Returns the number of times this function has been called
def how_many_calls():
    global number_of_calls # allow assignment to global variable
    number_of_calls = number_of_calls + 1 # count this call
    return number_of_calls
    
# Some tests:
print(how_many_calls())
print(how_many_calls())
print(how_many_calls())
print(how_many_calls())
print(how_many_calls())
