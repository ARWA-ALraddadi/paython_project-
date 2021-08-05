#--------------------------------------------------------------------
#
# Seeing stars
#
# In the lecture demonstration program "stars and stripes" we saw
# how function definitions allowed us to reuse a function that
# drew a star but was parameterised so that specific characteristics
# of the star could be changed each time.  As a further exercise in
# "parameterisation", develop a program that uses this function to
# draw a hundred stars on the screen.  Each star should be of
# a random size and colour and should appear in a random location.
# You can find a list of all the colours supported by Python at:
# http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
#
# Hint: This is very similar to last week's Starry, Starry Night
# exercise, so you can use your solution to that as a starting
# point if you're stuck.
#

# Import the function to draw stars (make sure a copy of file
# flag_elements.py is in the same folder as this one)
from flag_elements import star

# Import the turtle graphics and random functions
from turtle import *
from random import *

# Set the drawing speed, if necessary
speed("fastest")

# Define some commonly-needed constants
max_coord = 400 # pixels from the centre
min_size = 5 # smallest star in pixels
max_size = 20 # biggest star in pixels

# Set up the drawing environment
setup(max_coord * 2, max_coord * 2)
bgcolor("dark blue")
title("Seeing Stars")
penup()


# Draw a star for each of a large range of numbers
for star_num in range(100):
    # Choose random coords (here being very careful to
    # ensure that stars don't go off the edges of the
    # screen, remembering that the current coordinate is the
    # star's top point, not its centre)
    x_pos = randint(-max_coord + (max_size // 2), max_coord - (max_size // 2))
    y_pos = randint(-max_coord + max_size, max_coord)
    # Choose a random size
    size = randint(5, 20)
    # Choose a random, interestingly-named colour
    # (see http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm)
    colour = choice(['aquamarine', 'beige', 'bisque', 'blue',
                    'burlywood', 'coral', 'cornsilk', 'cyan',
                    'firebrick', 'gold', 'goldenrod', 'honeydew',
                    'ivory', 'khaki', 'lavender', 'lawn green',
                    'magenta', 'maroon', 'mint cream', 'misty rose',
                    'moccasin', 'olive drab', 'orchid', 'papaya whip',
                    'peach puff', 'peru', 'powder blue', 'salmon',
                    'tomato', 'turquoise', 'wheat', 'white smoke'])
    # Draw a star at the chosen position in the chosen size and colour
    goto(x_pos, y_pos)
    star(size, colour)

# Exit gracefully
hideturtle()
done()
