#---------------------------------------------------------------------
#
# Demonstration - Pacman
#
# As an introduction to drawing using Turtle graphics, here we'll
# draw a picture of the pioneering computer games character, Pacman.
# (Why Pacman? Because he's easy to draw!)
#
# Then, having successfully drawn Pacman once, we'll use random
# numbers to draw multiple "Pacmen" of different sizes.
#

# Import the Turtle graphics functions
from turtle import *

# Import the random integer function
from random import randint

# These two values tell us how big to make the image and where to
# put it - changing these values will change the image's size and
# location
diameter = 350 # the diameter of Pacman's big yellow head
position = [0, 0] # where to draw him

# Draw a black canvas
setup() # create window
title('Pacman') # put a title on the window
bgcolor('black') # make the background black

# Choose drawing colours: black for lines and dots, and yellow
# for filled-in regions
pencolor('black')
fillcolor('yellow')

# The following code for repeatedly drawing different "Pacmen"
# is commented out.  To make it work, uncomment the next three
# lines and indent the two code blocks below.
##for pacman in range(10):
##    diameter = randint(50, 250) # choose a random size
##    position = [randint(-300, 300), randint(-300, 300)] # choose a random place

# Draw a big yellow circle for Pacman's head,
# with a 60 degree slice taken out to form his mouth
penup()
goto(position) # starting point - centre of Pacman's head
pendown()
begin_fill()
setheading(30) # point east-north-east
forward(diameter // 2) # walk from centre to edge
left(90)
circle(diameter // 2, extent = 300) # walk part way around
goto(position) # go back to centre
end_fill()

# Draw a small black dot for Pacman's eye
penup()
setheading(90) # point north
forward(diameter // 4)
dot(diameter // 7)

# Finish the drawing
hideturtle() # hide the cursor
done() # release the drawing canvas so it can be closed
