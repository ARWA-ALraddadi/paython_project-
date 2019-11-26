# Starry, starry night
#
# This exercise gives us some practice at creating graphics
# using random values.
#
# THE PROBLEM
#
# Draw the night sky as a black field containing 200 randomly-
# positioned white "stars" (dots), each of a randomly-chosen size.
# (The most realistic effect is achieved if the difference in
# sizes is only small.)
#
# Use the following problem-solving strategy:
#
# 1. Set up a drawing window of a known size
#    with a black background
# 2. Make the pen colour white and set the drawing
#    speed to "fastest"
# 3. Lift up the pen (so that you don't draw lines
#    between the stars)
# 4. For each star in a range of 200:
#    a. Choose a random x-y coordinate (being careful
#       that it is not off the edge of the screen)
#    b. Choose a random star size
#    c. Go to the location chosen
#    d. Draw a star (dot) of the chosen size
# 5. Hide the cursor and release the drawing window
#
# Hint: This is much easier than it sounds.  If you're not sure
# how to get started, use the "shooting gallery" demonstration
# program from the lecture as a guide.
#
# Comment: Once you get this program working, try experimenting
# with variations, e.g., by randomly changing the stars'
# colours.
#

# Import the necessary functions and draw quickly
from turtle import *
from random import randint


# A SOLUTION
#
# 0. Define some fixed values
sky_size = 800 # the sky's dimensions, in pixels
max_coord = sky_size // 2 # the largest x-y coordinate on the screen
min_star_size = 3 # the size of the smallest possible star
max_star_size = 10 # the size of the largest possible star

# 1. Draw the sky as a large black square of a certain size
bgcolor("black")
setup(sky_size, sky_size)
title("Starry, starry night")

# 2. Use a white pen to draw the stars and draw quickly
color("white")
speed("fastest")

# 3. Lift up the pen to avoid drawing lines
penup()

# 4. For each star in a range of 200:
for star_num in range(200):
    # a. Choose a random position on the screen
    star_pos_x = randint(-max_coord, max_coord)
    star_pos_y = randint(-max_coord, max_coord)
    # b. Choose a random size
    star_size = randint(min_star_size, max_star_size)
    # c. Move to the chosen position
    goto(star_pos_x, star_pos_y)
    # d. Draw a dot of the chosen size
    dot(star_size)

# 5. Exit gracefully by hiding the cursor and unlocking
#    the drawing canvas
hideturtle()
done()
