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
# the code fragments below to create as many stars as you want.  Note
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


# 3. Instantiate three star objects as instances
#    of the Turtle class, define their shape, and move
#    them to random positions on the screen.
max_dist = 300 # how far we can go from the centre in pixels

star_one = Turtle()
star_one.shape("small_star.gif")
star_one.penup()
star_one.goto(randint(-max_dist, max_dist), randint(-max_dist, max_dist))

star_two = Turtle()
star_two.shape("small_star.gif")
star_two.penup()
star_two.goto(randint(-max_dist, max_dist), randint(-max_dist, max_dist))

star_three = Turtle()
star_three.shape("small_star.gif")
star_three.penup()
star_three.goto(randint(-max_dist, max_dist), randint(-max_dist, max_dist))

# 4. Make the images of the stars appear and disappear randomly many
#    times.
for twinkle in range(500): # Adjust this to vary the duration of twinkling
    if randint(0, 9) <= 1: # Adjust this to vary the twinkling frequency
        star_one.hideturtle()
    else:
        star_one.showturtle()
    if randint(0, 9) <= 1: # Adjust this to vary the twinkling frequency
        star_two.hideturtle()
    else:
        star_two.showturtle()
    if randint(0, 9) <= 1: # Adjust this to vary the twinkling frequency
        star_three.hideturtle()
    else:
        star_three.showturtle()
        
# 5. Make sure the stars are visible at the end
star_one.showturtle()
star_two.showturtle()
star_three.showturtle()

# 6. Release the drawing window when finished.
done()
