#---------------------------------------------------------------------
# Demonstration - Squiggly lines
#
# This demonstration shows how you can easily create
# some interesting graphics by combining Turtle
# actions with random numbers and simple repetition.
#
# Starting with a program that just draws a crooked
# line we will add features until it produces an
# abstract work of art.

# Import all the functions in the turtle module
from turtle import *

# Import two functions from the random number module
from random import randint, choice

# Some fixed values
screen_size = 600 # pixels
num_steps = 50
step_size = 10 # pixels

# Set up the screen, its title and background colour
setup(screen_size, screen_size)
title("Squiggly Lines")
bgcolor("gray")

# Set the pen's width and the drawing speed
pensize(4) # pixels
speed('slowest')

#-----------------------------------------------------------
# Below are multiple versions of the code we will develop
# in the lecture demonstration, indented and commented out

##  # Version 0: Draw a crooked line whose shape is fixed
##  forward(60) # draw the first bit
##  left(45) # turn left
##  forward(30) # draw the second bit
##  right(70) # turn right
##  forward(100)
##  left(115)

##  # Version 1: Draw the same crooked line four times
##  line_numbers = [1, 2, 3, 4]
##  for line_num in line_numbers:
##      forward(60) # draw the first bit
##      left(45) # turn left
##      forward(30) # draw the second bit
##      right(70) # turn right
##      forward(100)
##      left(115)

##  # Version 2: Draw a straight line in many identical steps
##  for step_num in range(num_steps): # do the code below multiple times
##    forward(step_size) # draw a straight line

##  # Version 3: Draw a wobbly line in many steps
##  for step_num in range(num_steps):
##    left(randint(-30, 30)) # turn left or right a random amount
##    forward(step_size)

##  # Version 4: Draw a wobbly line in different colours
##  pallette = ['red', 'green', 'blue', 'yellow'] # choose from these colours
##  for step_num in range(num_steps):
##    color(choice(pallette)) # choose a random pen colour
##    left(randint(-30, 30)) 
##    forward(step_size)

##  # Version 5: Draw lots of wobbly lines
##  speed('fastest') # draw fast because there are lots of lines
##  pallette = ['red', 'green', 'blue', 'yellow'] # choose from these colours
##  for line_num in range(50): # do this many wobbly lines
##    penup()
##    home() # return to the screen's centre (without drawing)
##    setheading(randint(0, 359)) # point in a random direction
##    pendown()
##    for step_num in range(num_steps): # do this many steps per line
##        color(choice(pallette))
##        left(randint(-30, 30)) 
##        forward(step_size)

# Some other variants to try:
#   Randomly change the line width
#   Randomly change the line segment length
#   Turn at 90 degree angles only

#-----------------------------------------------------------

# Exit gracefully
hideturtle() # make the cursor (turtle) invisible
done() # release the drawing window
