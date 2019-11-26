#------------------------------------------------------------
#
# Whack-a-Mole
#
# Motivation: As a demonstration of a program that involves
# both definite and indefinite iteration here we develop a
# simple version of a children's game often found in arcades.
#
# Scenario: A nasty mole is digging holes in your prize front
# lawn!  It suddenly pops up its head from underground and
# spins around in circles as it creates a large hole.  Armed
# with a mallet your job is to discourage this behaviour by
# whacking the mole on the head before it finishes the hole.
# If you succeed in hitting the mole in time it gives up and
# moves elsewhere.  If you miss the mole, or it finishes
# digging, a big hole appears in your nice lawn.
#
# Your task: This is a fairly complicated program to complete
# in one workshop, so below we've provided most of the code.
# You need to fill in the missing code at the points
# marked "***".  Before doing so, study the parts of the
# code that have been supplied to ensure that you understand
# the overall program structure.
#
# Technical note: This program relies on Turtle function
# onscreenclick.  Given the name of another function
# onscreenclick "binds" that function to the "event"
# of the player clicking the mouse in the drawing
# window.  This is an example of an ASYNCHRONOUS
# function call.  We don't call the bound function explicitly
# as we normally do, it is called by the Turtle run-time
# system whenever the mouse is clicked.  Such asynchronous
# function calls are common in interactive programs, but are
# not normally used in programs that just perform some fixed
# calculation.
#
# Disclaimer: This program relies on the precise timing of
# certain events and the ability of the function bound by
# onscreenclick to INTERRUPT some other program code that
# is running (in function move_mole below).  The precision
# with which these events are synchronised is very much
# dependent on the particular operating system you're using.
# Although we've tested this program in a few different
# Python implementations we can't guarantee good timing
# behaviour in every such system.  (Turtle graphics isn't
# intended for creating interactive games!)
#
# Extension: There are many improvements that could be made
# to this "game".  The most obvious is to add a counter to
# keep track of the player's score, so that it can be
# displayed at the end.
#


#-----------------------------------------------------------
# Import various functions needed for the game
#
from turtle import *
from random import randint
from time import sleep


#-----------------------------------------------------------
# Introduce global variables needed to keep track
# of the game's state here
#
clicked = False # True when player clicks mouse button
whacked = False # True when a click occurs near the mole


#-----------------------------------------------------------
# Introduce global constants needed to control the game's
# layout and other characteristics
#
max_screen_x, max_screen_y = 400, 300 # max positive or negative screen coords
border = 50 # how close the mole can get to the edge of the screen
max_x, max_y = max_screen_x - border, max_screen_y - border # mole's max coords
num_holes = 10 # how many holes the mole will attempt to dig
num_spins = 3 # how many times the mole spins before a hole is finished


#-----------------------------------------------------------
# Call this function to get the mole to run around in a small
# circle, as if digging a hole
#
def spin_around():
    sleep(0.25) # pause for a quarter second
    circle(10) # run around in a small circle


#-----------------------------------------------------------
# Call this function to make the mole say "Ouch!" when
# whacked
#
def say_ouch():
    write("Ouch!", align="center", font=("Arial", 20, "normal"))


#-----------------------------------------------------------
# Call this function to create a hole when the player has
# failed to whack the mole in time
#
def dig_hole():
    dot(50) # pixels

    
#-----------------------------------------------------------
# This Boolean function returns True iff the given coordinates
# are near the mole's (turtle's) current position, as defined
# by a square area around the given coords
#
def near_mole(x_coord, y_coord):
    leeway = 20 # how close we need to get, in pixels
    return (x_coord - leeway <= xcor() <= x_coord + leeway) and \
           (y_coord - leeway <= ycor() <= y_coord + leeway)


    
#-----------------------------------------------------------
# This function defines the behaviour of the mole
#
def move_mole():
    global clicked, whacked
    # Move to a random location
    new_x, new_y = randint(-max_x, max_x), randint(-max_y, max_y)
    goto(new_x, new_y)
    # Spin a certain number of times or until the player clicks
    # the mouse in the window
    spin_count = 0
    while not clicked and spin_count < num_spins:
        spin_around()
        spin_count += 1
    # Decide what action to take at the end of an attempt to
    # dig a hole
    if whacked:
        say_ouch()
    else:
        dig_hole()
    # Reset global variables for next hole
    clicked = False
    whacked = False

    
#-----------------------------------------------------------
# This function is called automatically by the Turtle system
# whenever the player clicks the mouse in the window
#
# It sets some global variables to record how successful the
# player's attempt to whack the mole was
#
def whack(x_coord, y_coord):
    global clicked, whacked
    clicked = True
    whacked = near_mole(x_coord, y_coord)


#-----------------------------------------------------------
# This is the "main program"
#

# Set up the drawing screen
setup(max_screen_x * 2, max_screen_y * 2)
title("Whack-A-Mole")
bgcolor("light green")

# Adjust the drawing speed, if necessary
speed('fast')

# Create a "realistic" looking mole
register_shape("mole.gif")
shape("mole.gif")

# Lift up the pen so that the mole doesn't leave tracks
penup()

# Define which function to call when the player clicks the
# mouse button in the drawing window
onscreenclick(whack)

# Start playing the game by calling the move_mole function a
# fixed number of times
for hole in range(num_holes):
    move_mole()

# Terminate the game elegantly
hideturtle()
done()
