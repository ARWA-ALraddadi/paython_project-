#--------------------------------------------------------------------#
#
# Scribbly turtles
#
# As a simple example showing that we can create two independent
# Turtle objects, each with their own distinct state, here
# we create two cursors (turtles) that draw squiggly lines on the
# canvas separately.
#
# To develop this program from the beginning you can
#
# 1) Develop code to draw a single squiggly line using the
#    anonymous "default" turtle,
#
# 2) Modify the code to use a named Turtle object, and
#
# 3) Copy the code to create another named Turtle object.
#

from turtle import *
from random import randint

# Set up the drawing canvas and hide the default turtle
setup()
title('Two scribbly turtles')
hideturtle() # Hide the default turtle since we don't use it

# Create the two Turtle objects
red_turtle = Turtle()
blue_turtle = Turtle()

# Define the characteristics of the red turtle
red_turtle.color('red')
red_turtle.turtlesize(2)
red_turtle.width(4)
red_turtle.pendown()
red_turtle.speed('fast')

# Define the characteristics of the blue turtle
blue_turtle.color('blue')
blue_turtle.turtlesize(3)
blue_turtle.width(6)
blue_turtle.pendown()
blue_turtle.speed('fast')

# Make the two turtles appear to draw at the same
# time by interleaving their actions
for steps in range(200):
    # Move the red turtle
    red_turtle.left(randint(-90, 90))
    red_turtle.forward(15)
    # Move the blue turtle
    blue_turtle.left(randint(-45, 45))
    blue_turtle.forward(5)

# Exit
done()
