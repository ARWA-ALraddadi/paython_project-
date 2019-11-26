######################################################################
##
##  Demonstration - Adding machine
##
##  The following example shows how an exception handler can be
##  used to recover gracefully from input errors
##


#---------------------------------------------------------------------
#
# Requirement:
#
# The aim is to define an easy-to-use adding machine that lets the
# user enter numbers with a subtotal displayed after each
#


#---------------------------------------------------------------------
#
# Comment:
#
# Notice that the requirement above says nothing about how to respond
# if the user enters anything other than a number, nor does it say
# how to terminate the program
#


#---------------------------------------------------------------------
#
# A fragile implementation:
#
# The following function implements the requirement but is easily
# "crashed" and cannot be terminated elegantly
#

# Read numbers from the user and display a running total
def fragile_adding_machine():

    # Initialise the running total
    total = 0

    # Read and add numbers until a keyboard interrupt occurs
    while True:
        total = total + eval(input('Subtotal: ' + str(total) + '\n'))


#---------------------------------------------------------------------
#
# A robust implementation:
#
# The following function implements the requirement and additionally
# handles non-numerical input and allows the program to be terminated
# by entering Control-C
#

# Read numbers from the user and display a running total
def robust_adding_machine():

    # Initialise the running total
    total = 0

    # Read and add numbers until a keyboard interrupt occurs
    while True:
        try:
            total = total + eval(input('Subtotal: ' + str(total) + '\n'))
        except KeyboardInterrupt:
            print('Quit')
            break
        except Exception:
            print('Invalid input - ignored')
