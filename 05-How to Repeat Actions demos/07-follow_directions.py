#--------------------------------------------------------------------#
#
# Follow directions
#
# As an example of performing different actions for each value in a
# list, here we follow the instructions encoded in a list to draw
# a simple image.
# 
# The list contains two kinds of commands only:
#
#  * ['Left', N] - turn left by 90 degrees N times
#  * ['Forward', N] - move forward 20 pixels N times
#
# By combining these two commands many times in a list we can move
# the turtle around to draw simple shapes.
#

# Import the standard Turtle functions
from turtle import *

# Import the data set to be followed
from directions_data import instructions

# Set up the canvas and drawing characteristics
setup()
width(4)
pendown()
title('Follow instructions')
speed('normal')

# Read and follow each instruction
for command, number in instructions:
    # Decide what to do and do it the specified number of times
    if command == 'Left':
        for iteration in range(number):
            left(90)
    else: # must be 'Forward'
        for iteration in range(number):
            forward(20)

# Shut down
hideturtle()
done()
