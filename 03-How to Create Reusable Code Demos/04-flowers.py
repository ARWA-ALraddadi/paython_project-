#-----------------------------------------------------------
#
# Demonstration - Flowers
#
# This demonstration program draws a pretty flower, but its
# real purpose is to illustrate some different ways in which
# we can pass parameters to a function.  The functions in
# this case have side-effects.  They draw pictures on a
# turtle canvas and print text to the shell window.
#

# Import the necessary functions from the Turtle module
from turtle import *

#-----------------------------------------------------------
# Draw a flower's stem.  This function has no parameters (and
# does not use random numbers or access global variables) so
# when it is called it always does the same thing.
#
def stem():
    print('Drawing stem...')
    stem_length = 300 # pixels (this variable is local to this function)
    penup()
    goto(0, - stem_length // 2) # start halfway down the screen
    setheading(90) # point north
    color('dark green')
    width(5)
    pendown()
    forward(stem_length) # draw the stem 

#-----------------------------------------------------------
# Draw the pretty flower as a set of petals and some pollen.
# This function has three named parameters, two of which have
# default values.  We assume the pen is down when this function
# is called.
#
def flower(num_petals, petal_colour = 'red', petal_radius = 50):
    angle_to_turn = 360 // num_petals # degrees (another local variable)
    # Draw each of the petals
    for petal_num in range(num_petals):
        print('Drawing petal...')
        color(petal_colour)
        begin_fill()
        circle(petal_radius)
        end_fill()
        right(angle_to_turn)
    # Finish by drawing the pollen (in a size proportional
    # to that of the petals)
    print('Drawing pollen...')
    color('yellow')
    dot(petal_radius)
        
#-----------------------------------------------------------
# This is the main program that calls the functions we've
# defined above.  For the purposes of illustration we've
# included several possible calls to function "flower".
# Try each of them by uncommenting the function call.

# Create the drawing window
setup()
title("Flowers")

# Draw the flower stem
stem()

# Draw the flower, using one of several different types
# of function call
flower(5)
# flower(6, petal_radius = 80)
# flower(4, petal_colour = 'blue')
# flower(7, 'orange', 90)

# Exit gracefully
hideturtle()
done()
