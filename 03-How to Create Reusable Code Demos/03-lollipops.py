#-----------------------------------------------------------
#
# Demonstration - Lollipops
#
# This demonstration program illustrates code re-use with
# functions and parameter passing.  The functions in
# this case have side-effects, rather than returning
# values.  They draw pictures on a turtle canvas and print
# text to the shell window.
#

# Import the necessary functions from the Turtle module
from turtle import *


#-----------------------------------------------------------
# Draw a stick.  This function has no parameters so
# when it is called it always does the same thing.  It draws
# a stick vertically from the current position.
#
def draw_stick():
    # Set up the drawing pen's properties
    width(3)
    color('brown')
    pendown()
    # Point the pen north and draw
    setheading(90)
    forward(40)
    # Lift up the pen when finished
    penup()


#-----------------------------------------------------------
# Draw a lollipop.  This function has two parameters so
# when it is called it can vary its behaviour.  It draws
# a coloured circle immediately above the current position.
#
def draw_lollipop(radius, colour):
    # Set up the drawing pen's properties
    width(4)
    color(colour) # <--- use the colour provided by the caller
    pendown()
    # Point east and walk in a circle
    setheading(0)
    circle(radius) # <--- use the radius provided by the caller
    # Lift up the pen when finished
    penup()

    
#-----------------------------------------------------------
# This is the "main program" that calls the functions we've
# defined above.  In this case we use them to draw three
# different "lollipops".

# Create the drawing window
setup()
title("Lollipops")
penup()

# Go to where we'll draw the first lollipop
goto (-100, -50)
# Call the two functions to draw the lollipop
draw_stick()
draw_lollipop(50, 'purple')

# Go to where we'll draw the second lollipop
goto(0, -50)
# Call the two functions to draw the lollipop
draw_stick()
draw_lollipop(35, 'orange')

# Go to where we'll draw the third lollipop
goto(100, -50)
# Call the two functions to draw the lollipop
draw_stick()
draw_lollipop(60, 'red')

# Exit gracefully
hideturtle()
done()
