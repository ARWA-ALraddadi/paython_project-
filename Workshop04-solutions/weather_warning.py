#---------------------------------------------------------
#
# Weather Warning
#
# Define a function which accepts one argument, a number
# representing a temperature in Celsius.
# The function should return warnings about extreme
# temperatures.
#
# Warnings should be issued for temperatures as follows:
#   above 40          = 'Extreme heat caution!'
#   between 30 and 40 = 'Warm weather'
#   between 10 and 20 = 'Cool weather'
#   below 10          = 'Extreme cold caution!'
#
# The tests below tell us how your function is expected to
# behave when called.  After you've written your function,
# confirm that it works correctly by (a) running this module
# so that your function is defined and then (b) copying
# each of the function calls in the set of tests into the
# shell to see if the right answer is returned.  Obviously
# if you don't get the expected answers then you'll need
# to modify your code until you do.
# 
# Finally, the main program of this file runs the tests
# automatically.  The code is commented out, but if you
# want to run all the tests automatically, just uncomment
# the code and run this file.  Of course, you should pass
# all the tests in order to complete this exercise.
#


#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> weather_warning(31) # Test 1. Normal case
'Warm weather'

>>> weather_warning(27) # Test 2. Normal case - no warning issued
''

>>> weather_warning(38) # Test 3. Normal case
'Warm weather'

>>> weather_warning(0) # Test 4. Normal case
'Extreme cold caution!'

>>> weather_warning(100) # Test 5. Normal case
'Extreme heat caution!'

>>> weather_warning(10) # Test 6. Normal case
'Cool weather'

>>> weather_warning(-34) # Test 7. Normal case - negative number
'Extreme cold caution!'

>>> weather_warning(9) # Test 8. Boundary case
'Extreme cold caution!'

>>> weather_warning(24) # Test 9. Normal case - no warning issued
''

"""


#---------------------------------------------------------
# A function to issue warnings about the weather
# given a temperature in Celsius, as per the tests
# above.
def weather_warning(temperature):

    # First check if the temperature is more than 40 degrees.
    if temperature > 40:
        # If so, print the heat warning.
        return 'Extreme heat caution!'

    # Now check if the temp is 30 degrees or more.
    # NB: there is no need to check if the temp is less than or equal to 40
    # as the preceding IF condition has taken care of that.
    elif temperature >= 30:
        return 'Warm weather'

    # Next, check if the temp is greater than 20.
    # Again, there is no need to recheck that it is less than 40, and 30 as
    # execution would not have got to here if either of the conditions in the
    # preceding IF blocks were met.
    elif temperature > 20:
        # According to the specs, we should return and empty string
        # if the temp is between 21 and 29.
        return ''

    # Check if the temp is greater than or equal to 10.
    elif temperature >= 10:
        return 'Cool weather'

    # If all the above conditions fail, it must be extremely cold!
    else: # temp must be < 10
        return 'Extreme cold caution!'
        

#---------------------------------------------------------
# This main program executes all the tests above when this
# file is run.  Uncomment the code below if you want to
# run the tests automatically.

from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))

