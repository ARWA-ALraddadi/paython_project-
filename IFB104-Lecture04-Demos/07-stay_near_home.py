#-------------------------------------------------------------------
#
# Don't stray too far, little turtle
#
# As a visual demonstration of a program that uses Boolean-valued
# functions, this program draws a dotted line on the screen which
# is never allowed to get too far away from the origin.  We use
# both the pre-defined Turtle predicate "is_down" and define
# our own predicate "too_far_from_home".
#
# The complete program appears below, but in the demonstration
# we'll develop it incrementally via the following steps:
#
# 1. Set up and shut down the drawing window
# 2. Make the cursor look like a turtle
# 3. Move the turtle forward a fixed number of times
# 4. Make the turtle change colour when it gets
#    frightened by being too far from home
# 5. Make the turtle turn around when too far from home
# 6. Give the turtle a more realistic action by adding
#    a random wobble to its walk
# 7. Cause the turtle to leave a dotted trail by
#    toggling the state of the pen at each step
# 8. Improve the readability of our code by defining
#    a predicate (Boolean-valued function) to test if
#    the turtle is too far from home
#


# Import the necessary pre-defined functions
from turtle import *
from random import randint


#-------------------------------------------------------------------
# This Boolean-valued function returns True if the turtle is a long
# way from home, i.e., from coordinate (0, 0)
#
max_distance = 200 # how far away we are allowed to stray, in pixels

def too_far_from_home():
    return distance(0, 0) >= max_distance

#-------------------------------------------------------------------
# Define some fixed values to control the simulation
#
step_size = 10 # how far the turtle moves in each step, in pixels
turn_angle = 20 # how far to turn, in degrees

#-------------------------------------------------------------------
# Set up the drawing window and other overall parameters
#
title("Don't wander too far from home, little turtle")
bgcolor("light gray")
width(2)
speed('fastest') # adjust the drawing speed, if necessary

#-------------------------------------------------------------------
# Put a mark on the origin so we can clearly see how far the turtle
# has strayed
#
shape('square')
stamp()

#-------------------------------------------------------------------
# Start by pointing the turtle in a random direction
#
shape('turtle')
color('dark green')
setheading(randint(0, 359))

#-------------------------------------------------------------------
# Draw each of the line segments
#
for segment in range(2000): # how many segments to draw
    # Turn the turtle back towards home, if necessary,
    # otherwise add a random wobble, and make the
    # turtle's colour reflect its mood
    if too_far_from_home():
        color('red')
        left(turn_angle)
    else:
        color('dark green')
        left(randint(-turn_angle, turn_angle))
    # Draw the current line segment
    forward(step_size)
    # Toggle the state of the pen
    if isdown():
        penup()
    else:
        pendown()

#-------------------------------------------------------------------
# Release the drawing window when finished
#
done()
