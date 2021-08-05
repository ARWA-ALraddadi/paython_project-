# Three non-overlapping circles
#
# As a simple exercise in using the Turtle package you are
# required to draw three circles on the screen.  Each circle
# must be of a different size and colour.  Most importantly,
# the circles must not touch or overlap at any point, nor
# can one circle appear inside another.
#
# NB: We want unfilled circles, so you can't use Turtle's
# "dot" function for this purpose.  Also, you must ensure that
# lines are not drawn between or connecting the circles.
#
# The basic strategy for drawing each circle is to lift
# up the pen, move to a suitable location on the screen,
# choose a colour, put the pen down and walk in a circle.
# Having done this once you can copy your code (with minor
# changes) three times.
#
# Observation: Turtle's "circle" function does NOT draw a
# circle centred at the current location.  Instead it causes
# the turtle to walk in a circle, ending up back where
# it started.


# A SOLUTION
#
# 1. Import the turtle library
from turtle import *

# 2. Create the drawing canvas and give it a name
setup()
title('Three non-overlapping circles')

# 3. Make the lines thick enough to see easily
width(5) # pixels

# 4. Set the pen colour to red
color('red')

# 5. Draw the first circle with a radius of 20 pixels, at the origin
circle(20)

# 6. Lift the pen, relocate it, then set the pen down at new location
#    a. lift the pen up
penup()

#    b. relocate the pen
forward(100) # Our initial heading is east by default

#    c. set the pen down
pendown()

# 7. Set the pen colour to blue
color('blue')

# 8. Draw another circle of a different radius
circle(35)

# 9. Lift the pen, relocate it, then set the pen down at new location
#    a. lift the pen up
penup()

#    b. relocate the pen
setheading(135) # Face northwest
forward(250)

#    c. set the pen down
pendown()

# 10. Set the pen colour to blue
color('green')

# 11. Draw another circle of a different radius
circle(80)

# 12. Hide the cursor
hideturtle()

# 13. Release the drawing window
done()
