## Bouncing Ball
##
## Just as printing "Hello World" is the standard first
## example completed in a new programming language, games
## packages are usually introduced with a "Bouncing Ball"
## demonstration in which a ball bounces around
## the screen.  Turtle graphics is not designed for
## creating games, but we can still produce a convincing
## bouncing ball simulation.
##
## The incomplete program below creates a black window and
## makes the cursor look like a beachball.  (Make sure the
## file 'beachball.gif' is in the same folder as this
## program.)
##
## Your job is to make the ball bounce realistically around
## the walls.  Use the following strategy.
##
## 1. Set up the window size to a known value so that you
##    know the maximum x and y coordinates (i.e., where the
##    borders are)
## 2. Lift the pen, because we don't want to leave a trail
## 3. For each of a large range of "bounces":
##    a. Choose a random position on the top border
##    b. Move the cursor to that position
##    c. Choose a random position on the left border
##    d. Move the cursor to that position
##    e. Choose a random position on the bottom border
##    f. Move the cursor to that position
##    g. Choose a random position on the right border
##    h. Move the cursor to that position
##
## Experiment with different ways of choosing the random
## positions to get the most realistic bouncing effect.
## (We found that it's best to keep the ball away from
## the corners.)

# Import the functions required
from turtle import *
from random import randint

# Set up the playing field
setup()
title('Bouncing Ball')
bgcolor('black')

# Create the ball's image from a file
register_shape('beachball.gif')
shape('beachball.gif') # make the turtle look like a ball

# Set the drawing speed, if necessary
speed('slow')

# Fix the window's size so that we know where the borders are
max_coord =300 # pixels
setup(max_coord * 2, max_coord * 2)

# Lift the pen, so that we don't leave a trail
penup()

# Limit how far we can get from the middle of the wall
dist_from_middle = max_coord / 2

# Bounce off of each of the four walls multiple times,
# keeping the ball away from the corners
for bounce_num in range(30):
    goto(randint(-dist_from_middle, dist_from_middle), max_coord) # Top border,
    goto(-max_coord, randint(-dist_from_middle, dist_from_middle)) # Left border
    goto(randint(-dist_from_middle, dist_from_middle), -max_coord) # Bottom border
    goto(max_coord, randint(-dist_from_middle, dist_from_middle)) # Right border

# Comment: Turtle is mainly a drawing package, so its ability
# to support games and simulations is limited. If you're keen
# on these kinds of animations we suggest you look online for the
# PyGame package which can be used to create "real" games in
# Python.

# Exit gracefully
done()

        
