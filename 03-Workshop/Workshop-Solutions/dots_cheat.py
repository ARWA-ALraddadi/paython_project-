#----------------------------------------------------------------
#
# Cheating at Join-the-Dots
#
# We have seen how functions are typically "called" from within
# the main program (or even from within other functions).  In
# embedded or interactive software, however, functions may be
# called by certain "events" occurring.  In this game we will
# create a function which is called when you click the mouse
# in a Turtle drawing window.
#
# Objective: Recall that in children's join-the-dots puzzles the
# aim is to connect numbered dots by a line.  Here we will create
# a join-the-dots puzzle that we can't lose because the dots are
# placed wherever we move the cursor!
#
# Approach: You are to define a function that will be called
# when a mouse click occurs. This function should move the
# turtle to the location of the click, drawing a line as it
# goes, and draw a dot in the new position.  To do this
# you will need to call Turtle's "onscreenclick" function in
# the main program to "bind" mouse clicks to your dot drawing
# function.  NB: The parameter to "onscreenclick" is the
# name of the function to be called.  The function itself must
# have two parameters, denoting the x and y coordinates at
# which the click occurred.
#
# Extra challenge: As an extension you can also get the
# function to put a number beside each dot, just like a real
# join-the-dots puzzle.  Hint: To make the number advance
# in each step you will need to use a global variable to keep
# track of how many dots have been drawn.  NB: To assign to a
# global variable from within a function you need to declare
# it as "global" inside the function, otherwise
# the Python interpreter will think it's a new local variable.
# See the global_variable demonstration from the lecture for
# an example.
#
# You will need the following turtle graphics functions.
# Look them up in the Python Library Reference manual to see
# what they do and what arguments they need.
#
# * color, goto, dot, etc - for moving and drawing, as usual
# * write - for adding text in the "extra challenge" step
# * onscreenclick - for defining the function to call
#   when the mouse is clicked
#

# Import the turtle graphics functions
from turtle import *

#-----
# Introduce a global variable here to keep track of the dot
# number between function calls for the "extra challenge".
dot_number = 1

#-----
# Define a function that will be called whenever the mouse is
# clicked in the drawing window.  It moves the turtle to the
# given location (drawing as we go), draws a dot, writes
# the dot's number and increments the number of
# dots drawn.
#
def add_dot(x_coord, y_coord):
    global dot_number # Access the global variable, not a local one
    goto(x_coord, y_coord)
    dot(10)
    write("  " + str(dot_number), font=("Arial", 15, "normal"))
    dot_number = dot_number + 1 # This function has a side effect!

#-----
# The main program which binds mouse events to the function
# above.
#
title("World's Easiest Join-the-Dots Puzzle")
onscreenclick(add_dot) # Bind the start_move function to mouse clicks
hideturtle() # Hide the cursor (looks better!)
add_dot(0, 0) # Draw the first dot
done() # Allow the drawing window to be closed gracefully

