#----------------------------------------------------------------
#
# Join the dots
#
# This exercise gives you practice at both Turtle graphics and
# using lists.  It would be helpful to review your solution to 
# the "Starry, starry night" exercise from Workshop 2 before
# attempting this one.
#
# THE PROBLEM
#
# You are required to firstly draw 25 (or more)
# randomly-positioned dots on the screen and then
# draw a line connecting them together in the same
# order that they were drawn.  Draw the dots and the
# connecting line in different colours.
#
# NB: You cannot start drawing the line until AFTER
# you've finished drawing all the dots.  This means
# you'll need to find a way of remembering where all
# the dots are and the order in which they appeared.
#
# Hint: A list is a good way of remembering a sequence of
# numbers!
#
# Extra challenge: Use Turtle's "write" function to write
# consecutive numbers next to each dot as you draw them.
# This makes your solution look more like a real join-the-dots
# puzzle.
#

# Import the necessary functions
from turtle import *
from random import randint

# Adjust the drawing speed, if necessary
speed("fastest")


# A SOLUTION
#
# This version puts a number next to each dot to
# show their order.


# 0. Define some fixed values
screen_size = 800 # the screen's dimensions, in pixels
dot_size = 15 # the size of the dots, in pixels
max_coord = (screen_size - 30) / 2 # the largest x-y coord for dots
line_thickness = 3 # thickness of the line, in pixels
num_dots = 25 # how many dots to draw


# 1. Create the drawing canvas
setup(screen_size, screen_size)
title("Join the dots")


# 2. Create list(s) to record the coordinates of the dots
x_coords = []
y_coords = []


# 3. Draw the dots.  For each one:
color("dark blue")
for dot_num in range(num_dots):
    # a. Choose a random position on the screen
    dot_pos_x = randint(-max_coord, max_coord)
    dot_pos_y = randint(-max_coord, max_coord)
    # b. Move to the chosen position and draw a dot
    #    (optionally, you can also number the dots)
    penup()
    goto(dot_pos_x, dot_pos_y)
    dot(dot_size)
    write('     ' + str(dot_num),
          font=('Arial', 14, 'normal')) # write this dot's number
    pendown()
    # c. Record the position of the dot in your list(s)
    x_coords.append(dot_pos_x)
    y_coords.append(dot_pos_y)


speed("slow")

# 4. Draw the connecting line
#    a. Change to an appropriate pen color and size
color("red")
width(line_thickness)
hideturtle()
#    b. Go to the position of the first dot, without drawing
penup()
goto(x_coords[0], y_coords[0])
#    c. For each position recorded in the list(s), go to that
#       position, drawing as you go
pendown()
for dot_num in range(num_dots):
    goto(x_coords[dot_num], y_coords[dot_num])


# 5. Exit gracefully by unlocking the screen
done()
