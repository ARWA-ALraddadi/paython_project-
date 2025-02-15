##  Jackson Pollock's Final Masterpiece
##
##  20th century "artists" such as Jackson Pollock achieved fame
##  by stumbling drunkenly around a canvas on the floor
##  dribbling paint out of tins. (We're not being rude - he openly
##  admitted to being drunk when creating his paintings.) However,
##  today we can achieve the same effect without getting our hands
##  dirty or taking a swig by using Python!
##  
##  Using Turtle graphics develop a program to draw many blobs 
##  (dots) of random colour, size and location on the screen.
##  The blobs should be connected by lines of "paint" of
##  various widths as if paint had been dribbled from one
##  blob to the next.  The "paint" should not go off the edge
##  of the "canvas".  Use the following solution strategy.
##
##    1. Set up the blank canvas of a known size
##    2. Ensure the pen is down
##    3. For each "blob" in a large range:
##       a. Select a random pen colour
##       b. Pick a random pen width
##       c. Go to a random location on the screen
##          (drawing as you go)
##       d. Draw a blob (dot)
##    4. Exit the program gracefully
##
##  Hint: Although you could select colours from a list of
##  names, you can get a wider range of colours, by noting
##  that Turtle's "color" function can accept three numbers
##  as arguments, representing red-green-blue pixel densities.
##  These numbers are floating point values between 0.0 and 1.0.
##  Also note that the "random" module's "uniform" function
##  produces a random floating point number.
##
##  Hint: This exercise is actually very similar to the
##  previous "Starry, Starry Night" one, so you can develop
##  your solution as an extension of that.


# Import the functions required
from turtle import *
from random import uniform, randint

# Define some fixed properties of the painting
max_coord = 300 # painting limits, in pixels
max_blob_size = 20 # pixels
max_dribble_width = 8 # pixels

# Set up the "canvas"
setup(max_coord * 2, max_coord * 2)
title("Jackson Pollock's final masterpiece")

# Paint quickly
speed('fastest')

# Make sure the pen is down
pendown()

# Generate a large range of paint blobs
for blob_num in range(300):

    # Set the blob colour using randomly selected
    # RGB values between 0.0 and 1.0
    color(uniform(0.0, 1.0), uniform(0.0, 1.0), uniform(0.0, 1.0))

    # Pick a random pen width
    width(randint(1, max_dribble_width))
    
    # Go to the location for the next blob, dribbling
    # paint as we go
    goto(randint(-max_coord, max_coord),
         randint(-max_coord, max_coord))

    # Draw a filled 'blob' of a random diameter
    dot(randint(1, max_blob_size))

# Exit gracefully
hideturtle()
done()

        
