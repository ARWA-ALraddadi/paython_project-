#--------------------------------------------------------------------
#
# Fun With Flags
#
# In the lecture demonstration program "stars and stripes" we saw
# how function definitions allowed us to reuse code that drew a
# star and a rectangle (stripe) multiple times to create a copy of
# the United States flag.
#
# As a further example of the way functions allow us to reuse code,
# in this exercise we will import the flag_elements module into
# this program and create a different flag.  In the PDF document
# accompanying this file you will find several flags which can be
# constructed easily using the "star" and "stripe" functions already
# defined.  Choose one of these and try to draw it.
#

# First we import the two functions we need (make sure a copy of file
# flag_elements.py is in the same folder as this one)
from flag_elements import star, stripe

# Import the turtle graphics functions
from turtle import *

# Here we draw the Panamanian flag as an illustration.
#
# Comment: Since this is such a small example, we've hardwired all
# the numeric constants below.  For non-trivial programs, however,
# such "magic numbers" (i.e., unexplained numeric values) are best
# avoided.  Named, fixed values should be defined instead.

# Set up the drawing environment
setup(600, 400)
bgcolor("white")
title("Panama")
penup()

# Draw the two rectangles
goto(0, 200)
stripe(300, 200, "red")
goto(-300, 0)
stripe(300, 200, "blue")

# Draw the two stars
goto(-150, 140)
star(80, "blue")
goto(150, -60)
star(80, "red")

# Exit gracefully
hideturtle()
done()
