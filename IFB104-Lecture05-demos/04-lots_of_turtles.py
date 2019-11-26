#--------------------------------------------------------------------#
#
# Lots of turtles
#
# This demo simply use loops to draw lots of turtles on the screen.
# Each turtle varies in either size and/or colour depending on
# how you structure the loops. Experiment with the code to produce
# different effects.
#

from turtle import *
from random import choice

# Set up the drawing canvas and cursor
setup()
title('Lots of turtles')
penup()
shape('turtle')

# Define a list of colours we can iterate over
colours = ['red', 'green', 'blue', 'grey', 'orange', 'purple']

# Define a list of sizes we can iterate over
sizes = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

# Now draw turtles with differing sizes and colours
for size in sizes:
    for colour in colours:
        # Change the turtle's size and colour
        turtlesize(size)
        color(colour)
        # Move to a new location so that the different
        # turtles aren't all on top of one another
        left(20)
        forward(30)
        # Impress the cursor's image on the canvas
        stamp()

# Exit
done()
