#---------------------------------------------------------------
#
# Kissing Turtles
#
# So far the objects we've created have all behaved independently
# of one another.  In this exercise you will get two objects to
# interact.
#
# The code below is based on the "Two Turtles" demonstration from
# this week's lecture.  It creates two turtle objects and makes
# them both run around the screen randomly.  We've made the
# window small to increase the likelihood of the two turtles
# being in the same position at the same time.
#
# Your task is to add code to:
#
# a) recognise when the two turtles are "kissing", i.e., when
# they are a short distance from each other; and
#
# b) do something interesting when this happens.
#
# In our sample solution we get the turtles to stop and spin in
# circles when they kiss, but you could do something else such
# make them change size, colour or shape.
#
# Hints:
#
# There are several ways to do this, but a suggested solution
# strategy is as follows.
#
# 1) Add a Boolean function that uses the "distance" method to
# recognise when the two turtle objects are near one another.
# This function will take both turtles as its parameters.
# (In our solution we considered the turtles to be kissing if
# they are within 20 pixels of one another.)
#
# 2) Having created such a predicate you will need to modify the
# code in the loop at the end of the main program to call
# your predicate and then change the turtles' behaviours in
# some noticeable way when they have kissed.
#


# Import the necessary pre-defined functions
from turtle import *
from random import randint

#----------
# This Boolean-valued function returns True if the two turtles
# are near one another 
#
def kissing(turtle_a, turtle_b):
    how_close = 20 # pixels
    return turtle_a.distance(turtle_b.xcor(), turtle_b.ycor()) < how_close

#----------
# This Boolean-valued function returns True if the given turtle
# is near any of the drawing window's four edges 
#
def near_edge(the_turtle):
    return abs(the_turtle.xcor()) > max_x_coord - border or \
           abs(the_turtle.ycor()) > max_y_coord - border

#----------
# Define some fixed values to control the simulation
#
window_size = 500 # width and height of the window
max_x_coord = window_size / 2 # largest positive or negative x-cooord
max_y_coord = window_size / 2 # largest positive or negative y-coord
border = 75 # how close we get to the edge before turning, in pixels
num_steps = 2000 # how many steps to take in the simulation
step_size = 12 # how far the turtle moves in each step, in pixels
turn_angle = 20 # how far to turn to avoid the edge, in degrees
initial_sep = 50 # how far from the origin to place each turtle initially

#----------
# Set up the drawing window and other overall parameters
#
setup(window_size, window_size) # small window to maximise collisions
title("Kissing Turtles")
bgcolor("light green")
hideturtle() # hide the default turtle

#----------
# Create two distinct Turtle objects
#
big_turtle = Turtle()
big_turtle.shape("turtle")
big_turtle.turtlesize(2, 2)
big_turtle.color("dark green")
big_turtle.penup()
big_turtle.speed("fastest")

small_turtle = Turtle()
small_turtle.shape("turtle")
small_turtle.turtlesize(1, 1)
small_turtle.color("brown")
small_turtle.penup()
small_turtle.speed("fastest")

#----------
# Start by separating the turtles and
# pointing them away from one another
#
big_turtle.goto(0, initial_sep)
big_turtle.setheading(randint(0, 179))
small_turtle.goto(0, -initial_sep)
small_turtle.setheading(randint(0, 179) + 180)

#----------
# In each step check to see if each turtle is near an
# edge and, if so, turn it
#
# In this extended version the turtles also turn if
# they are kissing and only move forward if they are
# not kissing, which has the effect of making them
# spin in circles when they kiss
#
for step in range(num_steps):
    
    if near_edge(big_turtle) or kissing(big_turtle, small_turtle):
        big_turtle.right(turn_angle)
    if not kissing(big_turtle, small_turtle):
        big_turtle.forward(step_size / 2) # big turtle is slower
    
    if near_edge(small_turtle) or kissing(big_turtle, small_turtle):
        small_turtle.left(turn_angle) # small turtle turns left
    if not kissing(big_turtle, small_turtle):
        small_turtle.forward(step_size)

#----------
# Release the drawing window when finished
#
done()
