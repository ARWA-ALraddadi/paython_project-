#-----------------------------------------------------------------
#
# Twinkle, Twinkle Little Star
#
# As an introduction to creating multiple objects from the same
# class, in this exercise you will develop a program with
# multiple turtle graphics objects appearing on the screen at
# the same time.
#
# So far all of our turtle graphics programs have involved only
# a single default drawing cursor ("turtle") which limits
# what we can do.  However Turtle (with a capital "T") is actually
# a class, meaning that we can instantiate multiple objects from
# it and have several "turtles" appear on the screen at the
# same time.
#
# When you first run this file you should see a star appear on
# the screen which "twinkles" (by randomly making itself visible and
# invisible many times).  Study the code below to see how
# this star "object" is created and manipulated.  You may need to
# experiment with the "twinkling" frequency and duration to get a
# nice effect on your particular computer.
#
# Your task is to modify this code so that there is more than one
# twinkling star on the screen simultaneously.  Do this by duplicating
# the code fragments below to create as any stars as you want.  Note
# that each star object must have a distinct name, so that the
# program can distinguish them.
#
# Extra challenge: If you're comfortable with loops and lists you may
# want to extend the program so that it creates numerous stars, but
# without unnecessary duplication of code.  The "Busy Bees"
# demonstration from the lecture shows how to do this.
#


#------------------------------------------------------------------
# Import the necessary pre-defined functions.
from turtle import *
from random import randint


#------------------------------------------------------------------
# Main program starts here:
#


# 1. Set up the drawing window.
title("Twinkle, Twinkle Little Stars")
bgcolor("dark blue")


# 2. Register the star icon.
register_shape("small_star.gif")


# 3. Instantiate multiple star objects as instances
#    of the Turtle class, define their shape, and move
#    them to random positions on the screen.
max_dist = 300 # how far we can go from the centre in pixels
num_stars = 10 # how many stars to create
stars = [] # a list to hold the star objects

for star in range(num_stars):
    new_star = Turtle()
    new_star.shape("small_star.gif")
    new_star.penup()
    new_star.goto(randint(-max_dist, max_dist), randint(-max_dist, max_dist))
    stars.append(new_star)


# 4. Make the images of the stars appear and disappear randomly many
#    times.
for twinkle in range(500): # Adjust this to vary the duration of twinkling
    for star in range(num_stars):
        if randint(0, 9) <= 1: # Adjust this to vary the twinkling frequency
            stars[star].hideturtle()
        else:
            stars[star].showturtle()

        
# 5. Make sure the stars are visible at the end
for star in range(num_stars):
    stars[star].showturtle()


# 6. Release the drawing window when finished.
done()
