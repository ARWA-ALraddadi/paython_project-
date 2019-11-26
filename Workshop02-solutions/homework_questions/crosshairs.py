# Crosshairs - Draw a "gunsight" crosshair image
#
# As practice in drawing an image using Turtle graphics, draw the
# familiar image of a gunsight's crosshairs, consisting of a
# cross formed from two lines, plus a circle.  To make it interesting,
# we will aim the crosshairs at an evil alien monster intent on
# destroying the Earth!
#
# The monster will appear in the background image when you run this
# file.  We haven't told you the Turtle coordinates at which the
# monster appears, so you will need to use some trial-and-error to
# find its centre.
#
# Comment: The image of the alien has deliberately been placed
# off-centre.  Therefore you will need to draw the crosshairs
# at this location instead of the default origin in the middle of
# the screen.  Although you could do so using absolute coordinates,
# you are encouraged to move the turtle to the monster's position
# and then draw the crosshairs relative to this point.  This will
# make your program easier to maintain if, for instance, we wanted
# to use it with another picture of a monster in a different
# location.
#
# NB: Ensure that the GIF file with the monster's image is in
# the same folder (directory) as this Python program.


# A SOLUTION
#
# 0. Some predefined preliminaries

from turtle import * # import turtle graphics
setup(600, 600) # set the window size to match the image
bgpic("monster.gif") # add the image of the monster
title("Beware of the monster!") # add a title to the window
width(3) # ensure the crosshairs will be easily visible


# Define some fixed values for use in the code below
circle_radius = 60 # pixels
line_length = 150 # pixels (for each of the two lines)
monster_x, monster_y = -130, -100 # coords of monster's centre


# 1. Move the turtle to the monster's centre (without drawing)
penup()
goto(monster_x, monster_y)


# 2. Draw a vertical line centred on the current position (and
#    return to the starting point)
setheading(90) # face north
forward(line_length / 2) # go to start of line
left(180) # turn around
pendown()
forward(line_length) # draw the line
penup()
goto(monster_x, monster_y) # go back to where we were


# 3. Draw a horizontal line centred on the current position (and
#    return to the starting point)
setheading(0) # face east
forward(line_length / 2) # go to start of line
left(180) # turn around
pendown()
forward(line_length) # draw the line
penup()
goto(monster_x, monster_y) # go back to where we were


# 4. Draw  the crosshair's circle centred on the current position
setheading(90) # face north
forward(circle_radius) # go to the northernmost edge of the circle
left(90) # face east
pendown()
circle(circle_radius) # walk in a circle to draw the line


# 5. Exit the program by hiding the turtle and releasing the
#    drawing window
hideturtle()
done()
