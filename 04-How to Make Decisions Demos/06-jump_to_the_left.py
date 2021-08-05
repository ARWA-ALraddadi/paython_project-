#-------------------------------------------------------------------
#
# "It's just a jump to the left"
#
# As a visual demonstration of a program that uses a Boolean-valued
# function to make a decision, this program simulates the
# behaviour of a turtle that walks in straight lines, but avoids
# going off the screen by turning to the left if it is near
# an edge.
#
# This version of the program uses a very simple algorithm.  If the
# turtle recognises that it is near an edge of the screen it veers
# to the left until it is no longer near any edge.  Since it only
# ever turns left, this particular turtle often wastes energy going
# in circles, when it could have more efficiently avoided the edge
# by turning right.  It can also get trapped in corners for several
# iterations.
#


# Import the necessary pre-defined functions
from turtle import *
from random import randint


#-------------------------------------------------------------------
# This Boolean-valued function returns True if the turtle is near
# any of the drawing window's four edges 
#
border = 75 # how close we must get to be considered "near" the edge
max_x_coord = (window_width() // 2) - border # how far we can go left or right
max_y_coord = (window_height() // 2) - border # how far we can go up or down

def near_edge():
    x_distance_from_home = abs(xcor())
    y_distance_from_home = abs(ycor())
    return x_distance_from_home > max_x_coord or \
           y_distance_from_home > max_y_coord

#-------------------------------------------------------------------
# Define some fixed values to control the simulation
#
step_size = 10 # how far the turtle moves in each step, in pixels
turn_angle = 20 # how far to turn to avoid the edge, in degrees

#-------------------------------------------------------------------
# Set up the drawing window and other overall parameters
#
title("Stay in the window, little turtle")
shape("turtle")
turtlesize(2, 2)
color("dark green")
bgcolor("light green")
width(2)
speed("fast")

#-------------------------------------------------------------------
# Start by pointing the turtle in a random direction
#
setheading(randint(0, 359))

#-------------------------------------------------------------------
# In each step check to see if we're near an edge and,
# if so, turn to the left
#
for step in range(2000): # how many steps to take
    if near_edge(): # turn only if we're near the edge
        left(turn_angle)
    forward(step_size) # always move forward

#-------------------------------------------------------------------
# Release the drawing window when finished
#
done()
