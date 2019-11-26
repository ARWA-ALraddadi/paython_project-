############################################################################
#
# Gold star
#
# As a simple example of using repetition to draw a shape, this program
# draws a five-pointed star, but instead of copying the code to draw
# each point five times, it repeats the code for drawing one point.
#

# Import all the turtle functions
from turtle import *

# Create the drawing canvas
setup()
title('Gold star')
bgcolor('black')

# Set up the pen
color('gold')
width(10)
pendown()

# Do the same two drawing steps five times
for points in range(5):
    forward(200)
    right(144)

color('gold')
dot(250,0)
# Tidy up the canvas
hideturtle()
done()

