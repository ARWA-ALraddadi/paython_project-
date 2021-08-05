######################################################################
##
##  Demonstration - Locate vowels
##
##  The following function contains two coding errors.  Although it
##  sometimes produces the right answer, it doesn't always do so.
##  The aim of this demonstration is to use IDLE's debugger (and/or
##  calls to the PRINT function) to help pinpoint the errors.  (The
##  corrected code is given in the comment at the end of this file.)
##


#---------------------------------------------------------------------
#
# The requirement:
#
# Given some text, define a function that returns the
# positions (indices) of all vowels.
#


#---------------------------------------------------------------------
#
# A faulty implementation:
#
# The following attempted solution to the above requirement contains
# (at least) two coding errors.  Can you identify them using the
# debugger?
#

# Return the positions of the vowels in a string
def locate_vowels(text):

    locations = []
    location = 0

    while location < len(text) - 1:
        location = location + 1
        current = text[location]
        if current in 'aeiou':
            locations = locations + [location]
            
    return locations


# The following tests all return the correct answers...
print('Test 1:', locate_vowels('My very earnest man just showed us nine planets'))
print('Test 2:', locate_vowels('Rats live on no evil star'))
print('Test 3:', locate_vowels('Supercalifragilisticexpialidocious'))
print('Test 4:', locate_vowels('Strch prst skrz krk')) # Czech for 'Stick a finger in the throat'

# But this one doesn't!
print('Test 5:', locate_vowels("Aaron's Outlandish Owl"))







































##---------------------------------------------------------------------
##
##    The two bugs in the program are:
##
##        1) The WHILE loop is incorrectly coded so that it never examines
##           the first item (at position zero).
##
##        2) The condition in the IF statement does not allow for
##           capitalised vowels.
##
##    A corrected version of the function is as follows:
##
##    # Return the positions of the vowels in a string
##    def locate_vowels(text):
##
##        locations = []
##        location = 0
##
##        while location < len(text):
##            current = text[location]
##            if current in 'aeiouAEIOU':
##                locations = locations + [location]
##            location = location + 1
##                
##        return locations

