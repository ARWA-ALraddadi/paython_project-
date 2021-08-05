#---------------------------------------------------------------------
#
# Ants Nest
#
# As an example of the way object-orientation allows us to maintain
# several independent objects, each with its own attributes, here we
# create a simple simulation in which several Turtle graphics objects
# appear on the screen at the same time.
#
# The scenario is that you've disturbed an ants nest and the worker
# ants come rushing out to defend it.  The nest is represented by a
# black dot in the middle of the screen and each ant will be represented
# by the default Turtle cursor icon.  The ants all walk out of the nest
# in a straight line.  Importantly, however, each ant has its own "step
# size" and "orientation", so they will all walk in different directions
# at different speeds.
#
# Your task is to complete the missing code below.  You must:
#
# 1) Complete two methods in the Ant class which define how
#    ants are initialised and how they walk, respectively.
#
# 2) Fill in the code in the main program for creating and moving
#    the whole nest of ants.
#
# Extra exercise: Extend your program so that, having scared off the
# threat, the ants all turn around and return to their hole.  To do
# so you will need to add another method to the class so that the
# ant objects can be made to rotate 180 degrees.
#


# Import the necessary pre-defined functions.
from turtle import *
from random import randint


#----------
# A class which defines the behaviour of a single
# ant, from which we can create many ants, as an
# extension of the standard Turtle class
class Ant(Turtle):

    # Constructor to create a new Turtle object representing
    # an ant (Hint: Remember that variables belonging to a
    # class must be preceded by "self.")
    def __init__(self, step_size, orientation):
        # Call the superclass's constructor
        Turtle.__init__(self)
        # Here we've made the extra class attribute "private" by
        # preceding it with double underscores "__", but this
        # is not critical for this exercise
        self.__step_size = step_size
        self.setheading(orientation)
        self.penup()
        self.speed('fastest')

    # Method to move this ant forward one step
    def walk(self):
        self.forward(self.__step_size)


#----------
# A main program to create the Ant objects and cause them
# to move

# 0. Constants
number_of_ants = 20
min_step, max_step = 3, 10 # pixels
number_of_steps = 50

# 1. Set up the drawing window
title("Ants Nest")
bgcolor('green')

# 2. Draw the ant nest (using the default turtle object)
color('black')
dot(25)

# 3. Create lots of ants, each with their own step size and
#    orientation (Hint: Use a list to hold all the ant objects)
ants = []
for ant in range(number_of_ants):
    ants.append(Ant(randint(min_step, max_step), randint(0, 360)))

# 4. Move each of the ants in turn, up to a fixed number of
#    steps
for step in range(number_of_steps):
    for ant in ants:
        ant.walk()

# 5. Release the drawing window
done()
