# Volume of a cylinder
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, denoting the measurements of a cylindrical
# tank:

radius = 4 # metres
height = 10 # metres

# Also assume that we have imported the existential constant "pi"
# from the "math" library module:

from math import pi

# Write an expression, or expressions, to calculate the volume
# of the tank.  Print the result in a message to the screen.


# A SOLUTION
#
# 1. Calculate the area of the end of the cylinder
#    (The area of a circle of radius r is pi times r squared)
area = pi * (radius ** 2) # metres squared

# 2. Multiply the cylinder's area by its height
volume = area * height # metres cubed

# 3. Print the volume in a message to the screen
print("The cylinder's volume is", round(volume, 2), "metres cubed") # about 502


# Quick quiz: Why is "volume" a floating point number instead of
# an integer?
