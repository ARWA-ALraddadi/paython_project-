#----------------------------------------------------------------
#
# Two Turtles
#
# As a demonstration of how a program can have multiple "objects"
# created from the same "class", this extension of a
# previous demonstration program creates two separate
# turtle objects, each with their own characteristics.


# Import the necessary pre-defined functions
from turtle import *
from random import randint


#----------------------------------------------------------------
# This Boolean-valued function returns True if the given turtle
# is near any of the drawing window's four edges 
#
def near_edge(the_turtle):
    return abs(the_turtle.xcor()) > max_coord - border or \
           abs(the_turtle.ycor()) > max_coord - border

#----------------------------------------------------------------
# Define some fixed values to control the simulation
#
max_coord = 300 # largest positive or negative coord
border = 75 # how close we get to the edge before turning, in pixels
num_steps = 2000 # how many steps to take in the simulation
step_size = 12 # how far the turtle moves in each step, in pixels
turn_angle = 20 # how far to turn to avoid the edge, in degrees

#----------------------------------------------------------------
# Set up the drawing window and other overall parameters
#
setup(max_coord * 2, max_coord * 2)
title("Stay in the window, little turtles")
bgcolor("light green")
hideturtle() # hide the default turtle

#----------------------------------------------------------------
# Create two distinct Turtle objects
#
big_turtle = Turtle()
big_turtle.shape("turtle")
big_turtle.turtlesize(2, 2)
big_turtle.color("dark green")
big_turtle.penup()
big_turtle.speed('fast')

small_turtle = Turtle()
small_turtle.shape("turtle")
small_turtle.turtlesize(1, 1)
small_turtle.color("brown")
small_turtle.penup()
small_turtle.speed('fast')

#----------------------------------------------------------------
# Start by pointing the two turtles in random directions
#
big_turtle.setheading(randint(0,359))
small_turtle.setheading(randint(0,359))

#----------------------------------------------------------------
# In each step check to see if each turtle is near an
# edge and, if so, turn it
#
for step in range(num_steps):
    
    if near_edge(big_turtle):
        big_turtle.right(turn_angle) # big turtle turns right
    big_turtle.forward(step_size / 2) # big turtle is slower
    
    if near_edge(small_turtle):
        small_turtle.left(turn_angle) # small turtle turns left
    small_turtle.forward(step_size)

#----------------------------------------------------------------
# Release the drawing window when finished
#
done()
