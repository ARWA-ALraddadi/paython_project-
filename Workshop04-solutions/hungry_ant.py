###################################################################
#
# Hungry Ant
#
# As a graphics program that involves making decisions, this
# program aims to simulate the behaviour of a foraging ant.  The
# ant meanders about the screen at random until either it is
# exhausted or until it finds a tasty meal.  A different message is
# displayed depending upon the outcome.
#
# The program below is a minor variant of the "step to the right"
# Turtle graphics demonstration from Lecture 4.  The
# main differences are:
#
# 1) The pen is kept up, so that no line is drawn as our "ant"
#    moves around.
#
# 2) A function and some related constants have been added to draw
#    a coloured dot on the screen representing delicious ant
#    food.
#
# Your tasks are as follows.
#
# a) Foraging ants rarely walk in perfectly straight lines.  Modify
#    the code to introduce a random "wobble" in the ant's direction
#    at each step.  Hint: Add code to do a small left or right turn
#    before the ant would normally walk straight forward.  (It's best
#    to leave the ant's behaviour alone when it's turning to avoid
#    the edge of the screen, otherwise you may create a situation
#    where the ant gets stuck randomly moving along an edge.)
#
# b) Define a Boolean-valued function that returns True if and only
#    if the ant is currently within the dot representing food.
#    Hint: You will need to use the built-in distance()
#    function to determine how far the ant is from the centre
#    of the dot.
#
# c) Change the program so that it recognises when the ant has
#    wandered onto the food.  In this case the ant should stop and
#    the message "Yum, yum!" should be displayed on the screen.
#    Hint: You will need to use the built-in write() function to
#    print text in the drawing window.  Also, note that Python's
#    "break" command causes the program to exit the current loop
#    immediately, so can be used to terminate the "for" loop.
#
# d) As a further refinement, you should get the ant to say "I give
#    up!" if all of the "steps" have been completed and the food
#    has not been found.  Hint: You will need a way of remembering
#    whether the loop ended because the food was found or because
#    the ant has completed the specified number of steps.
#


########################################
# Import the necessary pre-defined functions
from turtle import *
from random import randint


########################################
# Define some fixed values to control the simulation - change
# these to alter the simulation's behaviour
#
step_size = 10 # how far the ant moves in each step, in pixels
turn_angle = 20 # how far to turn to avoid the edge, in degrees
food_x_pos, food_y_pos = -230, 250 # coordinates where the food is placed
food_radius = 100 # how big to make the food dot

wobble_angle = 50 # variability in ant's direction, in degrees


########################################
# Global variable used to keep track of whether or not we've
# found the food
#
found_it = False


########################################
# This Boolean-valued function returns True if the ant is near
# any of the drawing window's four edges 
#
border = 60 # how close we must get to be considered "near" the edge
max_x_coord = (window_width() // 2) - border # how far we can go left or right
max_y_coord = (window_height() // 2) - border # how far we can go up or down

def near_edge():
    x_distance_from_home = abs(xcor())
    y_distance_from_home = abs(ycor())
    return x_distance_from_home > max_x_coord or \
           y_distance_from_home > max_y_coord

    
########################################
# Function to draw a dot representing ant food (the
# given coords are the centre of the dot)
#
def draw_food(x_pos, y_pos, radius):
    penup()
    goto(x_pos, y_pos) # top left
    color("orange")
    dot(radius * 2)


########################################
# This Boolean-valued function returns True if the ant has
# found the food - the parameters tell us where the food is
#
def found_food(x_pos, y_pos, radius):
    return distance(x_pos, y_pos) <= radius


########################################
# Main program starts here:
# Set up the drawing window and other overall parameters.
#
title("Hungry Ant")
bgcolor("green")
penup()
speed("fastest")

########################################
# Create the "food".
#
draw_food(food_x_pos, food_y_pos, food_radius)

########################################
# Start with the ant at the origin pointing in a random direction.
#
color("black")
home()
setheading(randint(0,359))

########################################
# In each step check to see if we're near an edge and,
# if so, turn to the right, otherwise walk randomly about.
# Stop as soon as some food is found.
#
for step in range(1000): # how many steps the ant should take
    if near_edge():
        right(turn_angle)
    else: # random wobble, either left or right
        random_turn = randint(0, wobble_angle) - (wobble_angle // 2)
        left(random_turn)
    forward(step_size)
    if found_food(food_x_pos, food_y_pos, food_radius):
        found_it = True
        break # exit the loop immediately

########################################
# Display the ant's final message.
#
if found_it:
    write("   Yum, yum!", font=("Arial", 18, "bold"))
else:
    write("   I give up!", font=("Arial", 18, "normal"))

########################################
# Release the drawing window when finished.
#
done()
