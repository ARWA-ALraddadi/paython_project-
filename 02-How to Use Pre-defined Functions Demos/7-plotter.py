###########################################################################
#
# Plotter
#
# As a visual example that shows the use of a list to remember items,
# this program moves the Turtle to random coordinates on the canvas,
# drawing dots as it goes, and keeps a record of each coordinate visited.
#
# We set up a canvas of a certain width and height, so to avoid going off
# the edge we make the maximum coordinate in either the positive or
# negative direction half the canvas's size, less a small margin.
#
# At the end it prints the list of coordinates visited.  Rather than
# printing the "raw" list, it inserts some newline characters and
# removes some other unnecessary punctuation marks, so that the list
# is nicely formatted with each coordinate on a separate line.
#

# Import the drawing and random functions
from turtle import *
from random import randint

# Define some constants to say how big to make the image
canvas_size = 600
dot_size = 20
max_coord = (canvas_size // 2) - dot_size

# Create a drawing canvas
setup(canvas_size, canvas_size)
title('Plotter')

# Initialise the list of coordinates visited
been_there = []

# Go to random places and draw dots, remembering
# where we've been
for place in range(10):
    location = [randint(-max_coord, max_coord),
                randint(-max_coord, max_coord)]
    goto(location)
    dot(dot_size)
    been_there.append(location) # remember being here

# Print the coordinates we've been to, one per line
print('Coordinates visited:')
print(str(been_there).replace('[[', '[').replace(']]', ']').replace('], ', ']\n'))

# Exit gracefully
hideturtle()
done()
