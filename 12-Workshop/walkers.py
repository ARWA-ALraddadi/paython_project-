#---------------------------------------------------------------------
#
# Extending a class definition
#
# The program below defines a class of objects called Walkers, which
# pace around the screen in a square pattern.  It creates one
# such object and makes it take a fixed number of steps.
#
# This program is rather boring!  Your job is to make it more
# interesting by extending the class definition and its application
# in a number of ways.  Things you may consider doing include
# the following.
#
# * Extend the main program so that it creates multiple concurrent
#   walkers.
#
# * Add a method to the Walker class which allows the object's colour
#   to be changed, and extend the main program so the walkers change
#   colour periodically.
#
# * Create a subclass called Expanding_Walker whose objects get
#   bigger as they walk.  This could be done either by overriding
#   the "step" method or by adding a separate "grow" function.
#   The size of a turtle object can be changed with the "turtlesize"
#   method which accepts two integers, specifying the horizontal
#   and vertical sizes.
#


from turtle import *
from random import randint, choice

#----------
# The class from which "Walker" objects can be created
#
class Walker(Turtle):

    # This constructor accepts the walker's initial position
    # and heading and then sets local constants and
    # variables
    def __init__(self, x_pos, y_pos, heading):
        Turtle.__init__(self)
        self.penup()
        self.shape('turtle')
        self.speed('slowest')
        self.goto(x_pos, y_pos)
        self.setheading(heading)
        self.__max_steps = 100 # max before turning
        self.__step_size = 4
        self.__step_count = 0

    # This method moves the walker along one step, turning
    # it ninety degrees after a fixed number of steps
    def step(self):
        if self.__step_count > self.__max_steps:
            self.left(90)
            self.__step_count = 0
        self.__step_count += 1
        self.forward(self.__step_size)

    # This method allows the walker's colour to be changed
    def change_colour(self, new_colour):
        self.color(new_colour)


#----------
# The subclass derived from the "Walker" class allows the
# size of objects to be changed.  In this case this is
# done by overriding the "step" method so that walkers get
# bigger and smaller as they move.
#
class Expanding_Walker(Walker):

    # Add an attribute to keep track of the object's size
    # and whether it's expanding or contracting
    def __init__(self, x_pos, y_pos, heading):
        Walker.__init__(self, x_pos, y_pos, heading)
        self.__walker_expanding = True
        self.__walker_size = 1
        
    # Move the object and make it bigger, up to a certain
    # limit, then smaller again
    def step(self):
        max_size = 10
        min_size = 1
        # Change direction when we reach one of the limits
        if self.__walker_size >= max_size:
            self.__walker_expanding = False
        elif self.__walker_size <= min_size:
            self.__walker_expanding = True
        # Expand or contract as appropriate
        if self.__walker_expanding:
            self.__walker_size += 0.5
        else:
            self.__walker_size -= 0.25
        self.turtlesize(self.__walker_size, self.__walker_size)
        Walker.step(self)
            


#----------
# This is the main program that creates and controls walkers

# Set up the drawing window
title("Walkers")
bgcolor("light yellow")

# Define some colours for use when changing the walkers'
# colour
colours = ['red', 'green', 'blue', 'orange', 'brown', 'purple']

# Create a walker and an expanding walker
# and get them to each take 1000 steps, with
# the ordinary walker changing colour after
# a certain number of steps
walker_one = Walker(200, -200, 90)
walker_two = Expanding_Walker(-200, 200, 270)
for step_num in range(1000):
    walker_one.step()
    walker_two.step()
    if step_num % 30 == 0: # Change every thirty steps
        walker_one.change_colour(choice(colours))

# Release the window when finished
done()
            
        
        
