#---------------------------------------------------------------------
#
# Starburst
#
# As an example of the way object-orientation allows us to maintain
# several independent objects, each with its own attributes, here we
# create a simple visualisation of a fireworks-like starburst in which
# multiple "sparks", i.e., Turtle graphics objects, fly out from the
# centre of the screen simultaneously.
#
# Follow the instructions below to create a list of "spark" objects,
# give each of them different attributes (colours, sizes and orientations)
# and then animate them by moving them forward one step at a time.
#


# Import the necessary pre-defined functions.
from turtle import *
from random import randint, choice, uniform

#----------
# A main program to create the "spark" objects and cause them
# to fly out from the centre of the screen

# 0. Constants you should use in your solution
number_of_sparks = 20
min_step, max_step = 2, 10 # pixels
min_size, max_size = 0.5, 1.5
number_of_steps = 50
colours = ['red', 'green', 'blue', 'yellow', 'white', 'orange', 'purple', 'pink', 'gold']

# 1. Set up the drawing window
title('Starburst')
bgcolor('dark blue')

# 2. Draw the centre of the "explosion" (using the default turtle object)
color('yellow')
dot(25)

# 3. Create lots of "sparks" (turtles) using a list to hold
#    them all
sparks = []
for each in range(number_of_sparks):
    sparks.append(Turtle())

# 4. Make all the spark objects circles, make sure
#    the pen is down for each one and set a thick
#    pen width
for spark in sparks:
    spark.shape('circle')
    spark.pendown()
    spark.width(4)

# 5. Randomly make all the spark objects different
#    sizes and colours
for spark in sparks:
    spark.turtlesize(uniform(min_size, max_size))
    spark.color(choice(colours))

# 6. Point all the sparks in random directions
for spark in sparks:
    spark.left(randint(0, 359))
    
# 7. Animate the sparks by moving them each in turn,
#    up to a fixed number of steps
for step in range(number_of_steps):
    for spark in sparks:
        spark.forward(randint(min_step, max_step))    

# 8. Release the drawing window
done()
