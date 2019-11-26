#-------------------------------------------------------------
#
# Demonstration - Random Scrabble
#
# As a simple demonstration of how we can create a pattern
# by calling functions from the Turtle and Random modules,
# this program draws a random image that looks like a
# game of Scrabble, consisting of vertically and
# horizontally arranged white squares on a grey background.
# Each square has a randomly chosen alphabetic letter in it.
#

# Import the graphics and random functions required
from turtle import *
from random import choice, randint

# Define some fixed values
square_size = 20 # pixels
border = 2 # pixels (around each square)
how_many_squares = 100 # how many squares to draw
offset = 8 # how many pixels the letters are offset from the square's centre

# Set up the drawing window
setup()
title("Random Scrabble")
bgcolor('grey')

# Make the cursor a white square
color('white')
shape('square')
penup()

# Create a list of all the alphabetic letters
from string import ascii_uppercase, ascii_lowercase
letters = ascii_uppercase + ascii_lowercase

# Do the same action several times
for square_num in range(how_many_squares):
  # Choose whether or not to turn (with going ahead most likely)
  left(choice([-90, 0, 0, 0, 0, 90]))
  # Move to the next position (leaving a little gap for the border)
  forward(square_size + border)
  # Draw the next square
  stamp()
  # Write a random letter exactly in the middle of the square
  color('black')
  letter = choice(letters) # Choose a random alphabetic letter
  goto(xcor(), ycor() - offset) # Move down a little bit
  write(letter, font=('Arial', 12, 'normal')) # Print the letter
  goto(xcor(), ycor() + offset) # Move back to where we were
  color('white')

# Exit gracefully
hideturtle()
done()
