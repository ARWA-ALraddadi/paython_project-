#---------------------------------------------------------------------
# Target shooting game - Demonstration of some Turtle graphics
# and list features
#
# This program shows how to use a few Turtle graphics features
# to simulate a target shooting game.  It draws a multi-coloured
# target and fires several random "shots" at it.  It also uses a
# list to keep track of the shots fired so that it can print
# statistics about the game at the end (in the shell window).
#
# See the Python Library Reference, Section 24.5, for details of
# the Turtle functions used below.


# Import all the functions in the turtle module
from turtle import *

# Import a function from the random number module
from random import randint


# Define some fixed values used in the program
#
# NB: Giving such values names at the beginning of a program
# makes the code easier to understand and maintain

screen_size = 600 # pixels
bullseye_radius = 50 # pixels
middle_radius = 150 # pixels
outer_radius = 250 # pixels
num_shots = 15 # how many "shots" to fire
bullet_hole_size = 20 # diameter of bullet hole in pixels


# Step 1: Set up the screen's size, title and colour
setup(screen_size, screen_size)
title("Hit the bullseye and win a prize!")
bgcolor("gray")

   
# Step 2: Draw the target as three coloured circles with
# black borders
#
# Notice that each circle is drawn in exactly the same way,
# apart from their radius and colour.  In next week's lecture
# we'll learn how to avoid repeating the same code more
# than once!
#
# a1. Draw the outermost circle
penup()
home()
pendown()
color("yellow")
dot(outer_radius * 2)
# a2. Draw the outermost circle's border
goto(outer_radius, 0) # easternmost point of circle
setheading(90) # turn to face north
color("black")
circle(outer_radius) # walk in a circle to create the border

# b1. Draw the middle circle
penup()
home()
pendown()
color("orange")
dot(middle_radius * 2)
# b2. Draw the middle circle's border
goto(middle_radius, 0) # easternmost point of circle
setheading(90) # turn to face north
color("black")
circle(middle_radius) # walk in a circle to create the border

# c1. Draw the bullseye
penup()
home()
pendown()
color("red")
dot(bullseye_radius * 2)
# c2. Draw the bullseye's border
goto(bullseye_radius, 0) # easternmost point of circle
setheading(90) # turn to face north
color("black")
circle(bullseye_radius) # walk in a circle to create the border


# Step 3: Adjust the drawing speed
#
# Make sure we can clearly see each shot (comment this line out
# to speed up the simulation)
speed("slow")


# Step 4: Draw the randomly-positioned bullet holes
color("black")
max_coord = (screen_size - bullet_hole_size) // 2 # don't go off the screen
distances = [] # keep a list of distances from the centre
for shot in range(num_shots): # do all the actions below once per shot
    # Choose a random coordinate
    x_pos = randint(-max_coord, max_coord) 
    y_pos = randint(-max_coord, max_coord)
    # Go to that coordinate and draw the bullet hole
    penup()
    goto(x_pos, y_pos)
    pendown()
    dot(bullet_hole_size)
    # Remember how far from the centre the bullet hole was
    distances.append(round(distance(0, 0)))


# Step 5: Print some final statistics about the game
print ("There were", len(distances), "shots fired")
print ("The best shot was", min(distances), "pixels from the centre")
print ("The worst shot was", max(distances), "pixels from the centre")
print ("The average of the shots was", sum(distances)//len(distances), "pixels off centre")


# Step 6 : Exit gracefully
hideturtle() # make the cursor (turtle) invisible
done() # release the drawing window
