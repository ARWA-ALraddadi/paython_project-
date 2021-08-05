#----------------------------------------------------------------------
#  Luck of the Irish
#
#  As another example of code reuse, in this exercise you will develop
#  a Turtle graphics function to draw a shamrock (a three-leaf clover)
#  and use it to populate an Irish field.
#

# Import the turtle graphics functions
from turtle import *

# Set up the "grassy field"
field_size = 600 # pixels
setup(field_size, field_size)
bgcolor("dark green")
title("Luck of the Irish")

# Adjust the drawing speed, if necessary
speed('normal')

#----------
# Step 1
#
# Define a function that draws a single shamrock.  It should have
# two parameters, the x and y coordinates at which to draw the
# image.  The shamrock should consist of three circular leaves and
# a stem.  Choose an appropriate colour, distinct from the background.

def shamrock(x_coord, y_coord):
    leaf_size = 20 # pixels
    color("light green")
    penup()
    # Draw stem
    goto(x_coord, y_coord)
    setheading(255)
    width(4)
    pendown()
    forward(20)
    # Draw leaves
    penup()
    goto(x_coord - 3, y_coord + 15)
    dot(leaf_size)
    goto(x_coord - 10, y_coord)
    dot(leaf_size)
    goto(x_coord + 5, y_coord + 6)
    dot(leaf_size)
    

#----------
# Step 2
#
# Write a main program to display 50 (or so) shamrocks randomly
# positioned on the field.  Use the field size defined above
# to limit the placement of shamrocks so that they don't go
# off the screen.

from random import randint

max_coord = field_size // 2 # how far we can go from the origin
shamrock_numbers = range(50) # a list of numbers, one per shamrock
for shamrock_num in shamrock_numbers: # call our function 50 times
    shamrock(randint(-max_coord, max_coord), \
             randint(-max_coord, max_coord))

# Exit gracefully
hideturtle()
done()
