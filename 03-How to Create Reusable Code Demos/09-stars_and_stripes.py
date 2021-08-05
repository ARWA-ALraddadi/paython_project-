#---------------------------------------------------------------------
#
# Stars and stripes - Demo of functions and modules
#
# To demonstrate how functions can be used to structure code
# and avoid duplication, this program draws the United States
# flag.  The U.S. flag has many duplicated elements -
# the repeated stripes and stars - and would be very
# tedious to draw if we had to do each part separately.
#
# Instead we import a function to draw a single stripe and
# another function to draw a single star, and repeatedly
# "call" these functions to create multiple stars and stripes.


# Import the graphics functions required
from turtle import *

# Import the functions that draw the stars and stripes
from flag_elements import star, stripe


#---------------------------------------------------------------------
# Define some global constants that determine the flag's
# proportions

flag_width = 850
flag_height = 500
stripe_height = 38.45
union_height = 270
union_width = 380
star_size = 32
y_offset = 10 # distance of the star field from the top-left corner
x_offset = 40
x_sep = 60 # separation of the individual stars
y_sep = 52


#---------------------------------------------------------------------
# The "main program" that draws the flag by calling the
# imported functions

# Set up the drawing window
#
setup(flag_width, flag_height)
setworldcoordinates(0, 0, flag_width, flag_height) # make (0, 0) bottom-left
title("This is not a political statement")
bgcolor("white")
penup()

# Draw the seven red stripes
#
goto(0, stripe_height) # top-left of bottom stripe
setheading(90) # point north
for stripe_num in range(7): # draw seven stripes
  stripe(flag_width, stripe_height, "red")
  forward(stripe_height * 2) # go up to next red stripe's position

# Draw the blue "union" in the top left
#
goto(0, flag_height) # top left-hand corner of the flag
stripe(union_width, union_height, "blue")

# Draw the stars (to save time, only 30 of them, in a 6 X 5
# matrix, as the US flag appeared in 1848)
#
goto(0 + x_offset, flag_height - y_offset) # near top left-hand corner of the flag
for row_num in range(5): # draw five rows of stars 
  for column_num in range(6): # draw six stars in each row
      star(star_size, "white")
      setheading(0) # point east
      forward(x_sep)
  goto(0 + x_offset, ycor()) # go back to left-hand edge
  setheading(270) # point south
  forward(y_sep) # move down to next row of stars

# Exit gracefully
hideturtle()
done()
