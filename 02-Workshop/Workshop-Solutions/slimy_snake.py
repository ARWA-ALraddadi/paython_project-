#-------------------------------------------------------------
#
# Slimy Snake
#
# As an exercise in using a list to remember things,
# here you will modify a given program by adding a list
# to keep track of images stamped on the screen.
#
# The program below is a variation of the Random Scrabble
# demonstration from the lecture.  Instead of squares it
# draws circles, intended to represent the segments of
# a snake.  The animation isn't very realistic, however,
# because the snake gets longer as it moves.
#
# Your task is to modify the program so that the snake
# has a constant length, as defined by the variable
# "snake_length".  The basic strategy is that each time
# a snake segment is stamped on the screen we remember
# its identity, so that we can erase it later.  When each
# new segment is drawn, the oldest one is deleted, and
# in that way the snake's length remains constant.  To
# remember the identity of each segment stamped on the
# screen you will need to use a list.
#
# Some Python and Turtle features you can use to
# complete this exercise are:
#
# L[n] - Returns the item in list L at position n
#        (recall that the first item is at position 0)
# L.append(x) - Appends item x to the end of list L
# L.pop(n) - Deletes the item in list L at position n
# stamp() - Stamps the cursor on the screen and also
#           returns a "stamp identity" which can be
#           used to refer to this stamp later
# clearstamp(s) - erases the stamp with identity s
#

# Import the graphics and random functions required
from turtle import *
from random import choice, randint

# Define some fixed values
segment_size = 20 # pixels (size of each snake segment)
overlap = 3 # pixels (how far the segments overlap)
num_steps = 200
snake_length = 10 # how many snake segments to display

# Set up the drawing window
setup()
title("Slimy Snake")
bgcolor('black')

# Make the cursor a green circle
color('green')
shape('circle')
penup()

# Change the drawing speed, if necessary
speed('fast')

# Initialise a list of stamp identifiers to keep track
# of each snake segment
segments = []

# Draw the snake
for segment in range(snake_length):
  # Move to the next position (overlapping the previous step a little)
  forward(segment_size - overlap)
  # Draw the next segment and remember the stamp identifier
  segments.append(stamp())

# Move the snake's segments along
for step in range(num_steps):
  # Choose whether or not to turn (with going ahead more likely)
  left(choice([-90, 0, 0, 0, 0, 90]))
  # Move to the next position (overlapping the previous step a little)
  forward(segment_size - overlap)
  # Draw the next segment
  segments.append(stamp())
  # Delete the oldest segment
  clearstamp(segments[0])
  # Remove the oldest segment from the list
  segments.pop(0)

# Comment: Yes, we know that snakes aren't really slimy!

# Exit gracefully
hideturtle()
done()
