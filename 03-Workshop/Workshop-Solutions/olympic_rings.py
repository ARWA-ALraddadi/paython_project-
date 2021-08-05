#-------------------------------------------------------------------------
#
#  Olympic Rings
#
#  In this folder you will find a file "olympic_rings.pdf" which shows
#  the flag used for the Olympics since 1920.  Notice that this flag
#  consists of five rings that differ only in their position and colour.
#  If we want to draw it using Turtle graphics it would therefore be
#  a good idea to define a function that draws one ring and reuse it
#  five times.
#
#  Complete the code below to produce a program that draws a reasonable
#  facsimile of the Olympic flag.  (NB: In the real flag the rings are
#  interlocked.  Don't try to reproduce this tricky feature, just draw
#  rings that overlap.)
#


#-------------------------------------------------------------------------
#  Step 1: Function definition
#
#  Define a function called "ring" that takes three parameters, an
#  x-coordinate, a y-coordinate and a colour.  When called this function
#  should draw an "olympic ring" of the given colour centred on the
#  given coordinates.  (Note that Turtle graphic's "circle" function
#  draws a circle starting from the cursor's current position, not
#  centred on the cursor's position.)  Since all the circles are the
#  same size you can define the radius and thickness of the circle
#  within the function

def olympic_ring(x_coord, y_coord, colour):
    ring_radius, ring_width = 110, 20 # pixels
    penup()
    goto(x_coord + ring_radius, y_coord) # easternmost point
    setheading(90) # face north
    width(ring_width)
    color(colour)
    pendown()
    circle(ring_radius) # walk in a circle to create the ring
    

#-------------------------------------------------------------------------
#  Step 2: Calling the function
#
#  Now write code to call the function five times, each time with
#  different coordinates and colours, to create the flag.  To get
#  you started we have provided some of the Turtle framework.

#  Import the Turtle functions
from turtle import *

#  Create the drawing window
setup(1000, 650)
title('"... and it\'s gold, Gold, GOLD for Australia!"')

# Draw the five rings
olympic_ring(-250, 60, "blue")
olympic_ring(0, 60, "black")
olympic_ring(250, 60, "red")
olympic_ring(-125, -60, "yellow")
olympic_ring(125, -60, "green")

#  Shut down the drawing window
hideturtle()
done()
