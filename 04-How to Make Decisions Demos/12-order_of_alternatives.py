#----------------------------------------------------------------
#
# Demonstration - Evaluation order of conditional alternatives
#
# This demonstration illustrates the significance of the order in
# which alternatives appear in a conditional statement
#

# Imagine that you are required to write a function which returns
# a string based on the current temperature (in degrees Celsius)
# as follows:
#
#    Temperature range                    Response
#
#    30 or more                           'Hot'
#    20 (inclusive) to 30 (exclusive)     'Warm'
#    10 (inclusive) to 20 (exclusive)     'Cool'
#    below 10                             'Cold'
#
# The following program is wrong.  Can you see why?  What test(s)
# would reveal the problem?  How can it be fixed?  (A correct
# version appears far below.)


# Returns a string summarising the current temperature
def temp_summary(degrees_Celsius):
    if degrees_Celsius >= 20:
        return 'Warm'
    elif degrees_Celsius >= 10:
        return 'Cool'
    elif degrees_Celsius >= 30:
        return 'Hot'
    else:
        return 'Cold'

# Let's try some tests:

print(temp_summary(25)) # does this call produce the right result?
print(temp_summary(15)) # how about this?
print(temp_summary(35)) # and this?




































# Solution: The program was wrong because the programmer did
# not consider the order in which alternatives are
# evaluated - a corrected version of the program appears
# below
#
# (But this is not the only way to fix this program - can you
# think of a way of doing so without reordering the alternatives?)


# Returns a string summarising the current temperature
def temp_summary_2(degrees_Celsius):
    if degrees_Celsius >= 30:
        return 'Hot'
    elif degrees_Celsius >= 20:
        return 'Warm'
    elif degrees_Celsius >= 10:
        return 'Cool'
    else:
        return 'Cold'

# Let's try the tests again (uncomment the following code):

##print()
##print(temp_summary_2(25))
##print(temp_summary_2(15))
##print(temp_summary_2(35))
