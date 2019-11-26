#-------------------------------------------------------------------
#
# Turtle controller, with text input widget
#
# One reason for having conditional statements in your program
# is to respond appropriately to external inputs.  As an illustration
# of this, below is a program that lets the user control the
# turtle via text commands.  The turtle decides what to do based
# on both the user's inputs and its own state.  Three different
# kinds of conditional statement are illustrated, "one-armed",
# two-way and multi-way.
#
# This version uses Turtle's "text input" widget, rather than
# interacting with the user via the shell window.
#


# Import the necessary pre-defined functions
from turtle import *

#-------------------------------------------------------------------
# Define some fixed values to control the simulation
#
step_size = 60 # how far the turtle moves in each step, in pixels
max_coord = 250 # how big to make the window

#-------------------------------------------------------------------
# Set up the drawing window
#
title('Turtle controller')
setup(max_coord * 2, max_coord * 2)
bgcolor('light gray')

#-------------------------------------------------------------------
# Set up the turtle
#
shape('turtle')
color('dark green')
turtlesize(2, 2)
penup()

#-------------------------------------------------------------------
# This predicate tells us if the turtle is off the screen (actually
# if the turtle's centrepoint is off screen)
#
def off_screen():
    x_distance_from_home = abs(xcor())
    y_distance_from_home = abs(ycor())
    return x_distance_from_home > max_coord or \
           y_distance_from_home > max_coord

#-------------------------------------------------------------------
# Read and obey each of the user's instructions
#
for step in range(15): # how many steps we'll do in the simulation
    # Decide which prompt to use
    if not off_screen():
        prompt = 'What is your wish, Oh Great Master? '
    else:
        prompt = 'Help me! How do I get back home? '
    # Get the user's command, using a text input widget (which
    # will return None if the user cancels data entry)
    command = textinput('Turtle query', prompt)
    if command == None:
        command = 'cancelled'
    else:
        command = command.lower()
    # Take the appropriate action
    if 'left' in command:
        left(90)
    elif 'right' in command:
        right(90)
    elif 'forward' in command or 'move' in command:
        forward(step_size)
    else: # spin around to indicate confusion
        for turn in range(8):
            left(90)

#-------------------------------------------------------------------
# Release the drawing window when finished
#
done()
