#-----------------------------------------------------------------
#
#   Coloured Circles - Demonstration of an iterative behaviour
#
#   This graphical demonstration is an example of "indefinite"
#   iteration.  It does the same action - with minor
#   variations - repeatedly until some condition becomes true.
#
#   In this case the program draws a series of circles, each
#   of a slight different size and colour.  The program stops
#   when the circles become too big, but precisely how many
#   circles get drawn depends on updates to certain variables.
#
#   By changing the constants used to update the variables in
#   the WHILE loop, different effects can be produced.
#

# Import the necessary drawing functions
from turtle import *


#-----------------------------------------------------------------

# Set up the drawing window and other overall parameters
title("Coloured Circles")
bgcolor("light grey")
speed("fastest")
colormode(255) # Enable RGB colours from 0 to 255
hideturtle()

# Initialise the circle's colour
red, green, blue = 150, 100, 200
fillcolor(red, green, blue)

# Initialise the circle's size
radius = 10

# Initialise the angle by which we move between circles
angle = 180

# Go to the easternmost point
penup()
goto(radius, 0)

# Draw bigger and bigger circles until their
# radius exceeds a certain size
while radius < 100:
    
    # Draw a filled-in circle
    setheading(90) # face north
    begin_fill()
    pendown()
    circle(radius)
    penup()
    end_fill()
    
    # Move aside a little to create some
    # separation between the circles
    setheading(angle) # face west
    forward(radius // 3)

    # Change the angle by which we move to
    # produce a swirling effect
    angle = angle + 10
    
    # Increase the next circle's size
    radius = radius + 2
    
    # Adjust the next circle's colour, being
    # careful not to go out of the range 0 to 255
    blue = max(blue - 3, 0) # less blue
    red = min(red + 2, 255) # more red
    fillcolor(red, green, blue)
    
# Release the drawing window when finished
done()
