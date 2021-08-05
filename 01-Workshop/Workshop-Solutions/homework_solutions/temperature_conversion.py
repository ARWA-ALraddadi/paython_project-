# Temperature conversion
#
# THE PROBLEM
#
# Assume the following value has already been entered into the
# Python interpreter, denoting a temperature in degrees Fahrenheit:

fahrenheit = 98.6 # degrees

# Write a Python expression to calculate the temperature in Celsius
# and print the result in a message to the screen.
#
# HINT: Given a temperature F in degrees Fahrenheit the equivalent
# temperature C in degrees Celsius is (F - 32) * (5 / 9).


# A SOLUTION
#
# 1. Deduct 32 from the fahrenheit value
# 2. Multiply:
#    a. the result of Step 1 above by
#    b. 5 divided by 9
celsius = (fahrenheit - 32) * (5 / 9)

# 3. Print the result (37 degrees Celsius) in a message to screen
print(fahrenheit, 'degrees Fahrenheit is equivalent to', celsius, \
      'degrees Celsius.')


