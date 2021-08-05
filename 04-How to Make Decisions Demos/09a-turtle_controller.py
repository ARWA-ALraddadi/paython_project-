#-------------------------------------------------------------------
#
# Turtle controller
#
# One reason for having conditional statements in your program
# is to respond appropriately to external inputs.  As an illustration
# of this, below is a program that lets the user control the
# turtle via text commands.  The turtle decides what to do based
# on both the user's inputs and its own state.  Three different
# kinds of conditional statement are illustrated, "one-armed",
# two-way and multi-way.
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
    print()
    # Optionally alert the user to a problem
    if off_screen():
        print("Help me! I've fallen off the edge of the world!")
    # Decide which prompt to use
    if not off_screen():
        prompt = 'What is your wish, Oh Great Master? '
    else:
        prompt = 'How do I get back home? '
    # Get the user's command and convert to lower case
    command = input(prompt).lower()
    # Take the appropriate action
    if 'left' in command:
        left(90)
        print('Okay')
    elif 'right' in command:
        right(90)
        print('Done')
    elif 'forward' in command or 'move' in command:
        forward(step_size)
        print('All right')
    else:
        print("I'm sorry, I don't understand that")

#-------------------------------------------------------------------
# Print the turtle's final message
#
print()
print("That's enough!  I'm tired.")

#-------------------------------------------------------------------
# Release the drawing window when finished
#
done()
