#----------------------------------------------------------------
#
# Turtle Swarm
#
# In this demonstration we will get several Turtle objects to
# move around the screen at the same time.  It creates numerous
# turtles, the number determined by a constant, each with its
# own characteristics.
#


# Import the necessary pre-defined functions
from turtle import *
from random import randint, choice

#----------------------------------------------------------------
# This Boolean-valued function returns True if the given turtle
# is near any of the drawing window's four edges, where "nearness"
# is defined by a border of a fixed width
#
def near_edge(the_turtle):
    border = 75 # how close we must get to the edge to be "near"
    return abs(the_turtle.xcor()) > max_coord - border or \
           abs(the_turtle.ycor()) > max_coord - border

#----------------------------------------------------------------
# Define some fixed values to control the simulation
#
max_coord = 300 # maximum x and y coordinates
num_steps = 900 # how many steps to take in the simulation
step_size = 12 # how far the turtle moves in each step, in pixels
turn_angle = 20 # how far to turn to avoid the edge, in degrees
initial_sep = 50 # how far from the origin to place each turtle initially
num_turtles = 10 # how many turtle object to create

#----------------------------------------------------------------
# Set up the drawing window and other overall parameters
#
setup(max_coord * 2, max_coord * 2)
title("Turtle Swarm")
bgcolor("light green")
hideturtle() # hide the default turtle

#----------------------------------------------------------------
# Create multiple distinct Turtle objects, with varying colours
#
turtles = []
for turtle_num in range(num_turtles):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.turtlesize(2, 2)
    new_turtle.color(choice(["dark green", "red", "blue", "orange", "black", "brown"]))
    new_turtle.penup()
    new_turtle.speed('fastest')
    turtles = turtles + [new_turtle] # add the new turtle to the list

#----------------------------------------------------------------
# Start by pointing the turtles in random directions
#
for turtle in turtles:
    turtle.setheading(randint(0, 359))

#----------------------------------------------------------------
# In each step check to see if each turtle is near an
# edge and, if so, turn it
#
for step in range(num_steps):
    for turtle in turtles:
        if near_edge(turtle):
            turtle.right(turn_angle)
        turtle.forward(step_size)
        
#----------------------------------------------------------------
# Release the drawing window when finished
#
done()
