###########################################################################
#
# Fat Pizza ("They're big and they're cheesy")
#
# In this demonstration we incrementally develop a
# program that draws a pizza.  Most importantly, it
# does so by importing some functions defined in
# another file ("module") and by calling them to
# complete the drawing.  For the purposes of
# illustration the module contains two different
# kinds of function, one with compulsory parameters,
# and one with optional parameters.
#
# The final solution appears below, and in the
# accompanying "pizza toppings" file, but in class
# we will develop it incrementally as a series of
# distinct steps.  The "step numbers" below correspond
# to the order in which we develop the code, not the
# order in which it's executed.
#

# Import the pre-defined Turtle graphics and random
# functions
from turtle import *
from random import randint, uniform

# Import the "toppings" functions from our module
from pizza_toppings import cheese, anchovies

# Step 1: Set up the drawing environment
setup(900, 700)
title('Fat Pizza')
tablecloth = 'sea green'
bgcolor(tablecloth)
penup() # the drawing is mainly done by "stamping" shapes
speed('fastest')

# Step 3: Set some constants that control the pizza's size
diameter = 600
radius = diameter // 2
crust = 50

# Step 4: Create the pizza base
pencolor('tan')
dot(diameter)

# Step 5: Spread tomato paste all over it
pencolor('dark red')
dot(diameter - crust)

# Step 7: Sprinkle bits of grated mozzarella cheese over it
tracer(False) # don't show all the steps - it takes forever!
for cheese_bit in range(550):
    cheese(randint(0, 360), randint(radius // 7, radius - crust))

# Step 8: Put anchovies on the pizza, optionally specifying how
# many slices should have them and how many anchovies there
# should be. (Some people don't like anchovies!?! How weird!)
anchovies(radius - crust, how_many = 75)

# Step 6: Slice up the finished pizza (Yum!)
tracer(True) # make sure that we're still drawing
penup()
home()
pendown()
pencolor(tablecloth)
shape('classic')
width(8)
for portion in range(6):
    forward(radius)
    goto(0, 0)
    left(60)

# Step 2: Tidy up
hideturtle()
done()
