#------------------------------------------------------------------
#
# Busy bees
#
# As a demonstration of object-orientation, this program
# instantiates instances of the Turtle class to create a
# swarm of bee objects that fly around until they land on
# a flower.  (This code is actually an extension of the
# "hungry ant" workshop exercise.)
#


#------------------------------------------------------------------
# Import the necessary pre-defined functions
from turtle import *
from random import randint


#------------------------------------------------------------------
# Define some fixed values to control the simulation - change
# these to alter the simulation's behaviour
#
max_coord = 300 # largest positive or negative coordinate
border = 50 # how close bees get to the edge before turning, in pixels
num_steps = 1000 # how many steps to take in the simulation
step_size = 10 # how far a bee moves in each step, in pixels
turn_angle = 20 # how far a bee turns to avoid the edge, in degrees
flower_x_pos, flower_y_pos = -220, 170 # where the flower is placed
flower_size = 100 # how close we get before landing on the flower, in pixels
wobble_angle = 25 # variability in a bee's direction, in degrees
num_bees = 5 # number of bees in the swarm


#------------------------------------------------------------------
# Initialise a given bee object
#
def init_bee(bee):
    bee.shape("picture_bee.gif")
    bee.home() # start in the middle of the screen
    bee.setheading(randint(0,359)) # random starting direction
    bee.penup() # don't leave a trail
    bee.speed("fastest")


#------------------------------------------------------------------
# This Boolean-valued function returns True if the given bee
# object is near any of the drawing window's four edges 
#
def near_edge(bee):
    return abs(bee.xcor()) > max_coord - border or \
           abs(bee.ycor()) > max_coord - border


#------------------------------------------------------------------
# This Boolean-valued function returns True if the given bee
# object is near the centre of the flower
#
def found_flower(bee):
    return bee.distance(flower_x_pos, flower_y_pos) <= flower_size


#------------------------------------------------------------------
# As long as the given bee is not already on the flower, move it
#
def move_bee(bee):
     if not found_flower(bee):
        if near_edge(bee): # turn to avoid edge
            bee.right(turn_angle)
        else: # random wobble, either left or right
            random_turn = randint(-wobble_angle, wobble_angle)
            bee.left(random_turn)
        bee.forward(step_size)
    

#------------------------------------------------------------------
# Function to draw the flower at a fixed position
#
def draw_flower():
    penup()
    goto(flower_x_pos, flower_y_pos)
    shape("picture_flower.gif")
    stamp()


#------------------------------------------------------------------
# Main program starts here:
#

# 1. Set up the drawing window
setup(max_coord * 2, max_coord * 2)
title("Busy bees")
bgcolor("light blue")

# 2. Register the icons
register_shape("picture_bee.gif")
register_shape("picture_flower.gif")

# 3. Draw the flower
draw_flower()

# 4. Create a bee swarm, i.e., a list of bee objects
swarm = []
for bee_num in range(num_bees):
    new_bee = Turtle() # instantiate a new object
    init_bee(new_bee) # initialise the object
    swarm = swarm + [new_bee] # add the object to the list

# 4. Run the simulation by repeatedly moving each bee in the swarm
for step in range(num_steps):
    for bee in swarm:
        move_bee(bee)

# 5. Release the drawing window when finished
done()
