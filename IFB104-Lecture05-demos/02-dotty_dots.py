#---------------------------------------------------------------------
#
# Dotty dots - Repeating actions with minor variations
#
# Up until now the only repetition we've seen has been the same action
# done many times.  This simple demonstration shows how actions can
# be repeated with minor variations for each different value in a
# list.
#
# The program simply draws a grid of multi-coloured dots. Experiment
# with the code to produce different patterns!
#

# Some useful constant values, all in pixels
canvas_size = 600
max_coord = 250
grid_size = 20
dot_size = 15

# Set up a drawing canvas with a black background
from turtle import *
setup(canvas_size, canvas_size)
title("Dotty dots")
bgcolor('black')

# Set up some drawing characteristics
penup()
speed('fastest')

# Define a list of colours
column_colours = ['red', 'green', 'blue', 'yellow', 'white', 'orange',
                  'aqua', 'olive', 'misty rose', 'salmon', 'spring green',
                  'fuchsia', 'deep sky blue', 'silver', 'aquamarine',
                  'orange red', 'seashell', 'chocolate', 'light steel blue',
                  'tomato', 'chartreuse', 'bisque', 'dark orchid',
                  'powder blue', 'gainsboro']

# Determine how many rows we can fit between the maximum
# and minimum y-coords, separated by the given grid size
number_of_rows = max_coord * 2 // grid_size

# Do the same action multiple times, with the only
# difference being the row number
for row_number in range(number_of_rows):
    # Go to the start of the row
    goto(-max_coord, max_coord - row_number * grid_size)
    # Do the same action multiple times, with the only
    # difference being the colour
    for colour in column_colours:
        color(colour)
        dot(dot_size)
        forward(grid_size)
    
# Exit gracefully
hideturtle()
done()

