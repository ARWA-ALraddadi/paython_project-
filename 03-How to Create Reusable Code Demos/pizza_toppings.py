###########################################################################
#
# Pizza Toppings
#
# This module contains two functions which are used
# by the Fat Pizza program.  Running this file on its
# own does nothing other than define the functions.
#

# Import useful functions from two of Python's pre-defined
# modules
from turtle import *
from random import randint, uniform

# Draw a single piece of grated mozzarella cheese at a
# specified location on the pizza. This function requires two
# parameters, which tell it where to put the bit of cheese,
# but the function decides for itself how big to make the bit.
# Both parameters to this function are compulsory.
def cheese(heading, distance):
    # Choose a cheesy colour and shape
    color('gold')
    shape('circle')
    # Stretch the bit of cheese a random amount
    turtlesize(uniform(0.5, 3.0), uniform(0.5, 3.0))
    # Move to the given position
    home()
    setheading(heading)
    forward(distance)
    # Stamp the image of the cheese onto the canvas
    stamp()

# Draw multiple anchovies at random locations on the pizza.
# This function has two optional parameters, which tell it
# how many pieces of pizza should have anchovies and how
# many to add in total, and a compulsory parameter which is
# the pizza's radius excluding the crust. The default
# behaviour is to add anchovies to every slice of pizza.
# (Sometimes anchovies near the edge of a slice overlap into
# the next slice. To keep the code simple we haven't bothered
# to prevent this.)
def anchovies(edible_radius, num_slices = 6, how_many = 150):
    # Choose a fishy colour, shape and size
    color('indigo')
    shape('arrow')
    turtlesize(1, 4)
    # Work out how many anchovies to draw, allowing for
    # the possibility that the number of slices may be zero,
    # in which case we shouldn't add any, regardless of
    # how many are requested
    num_anchovies = min(1, num_slices) * how_many
    # Put the required number of anchovies on the pizza
    for anchovy in range(num_anchovies):
        # Move to a random position in the range of
        # pieces (assuming the pizza is sliced into six)
        home()
        setheading(randint(0, num_slices * 60))
        forward(randint(edible_radius // 5, edible_radius))
        # Rotate the anchovy a random amount
        setheading(randint(0, 359)) 
        # Stamp the image of the anchovy onto the screen
        stamp()
