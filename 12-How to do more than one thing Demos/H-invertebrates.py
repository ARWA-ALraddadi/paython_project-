#----------------------------------------------------------------
#
# Invertebrates
#
# As a demonstration creating new classes via inheritance,
# this program creates a class hierarchy built upon the
# Turtle class.  Note how, unlike in the previous demos, all
# the actions and characteristics of the new classes of
# objects are encapsulated as attributes and methods within
# the class definitions.
#


# Import the necessary pre-defined functions
from turtle import *
from random import randint


#----------------------------------------------------------------
# This class defines invertebrates to be objects that can
# move around the screen, constructed as an extension of the
# pre-defined Turtle class
#
class Invertebrate(Turtle):

    # A constructor for invertebrates which defines their
    # basic characteristic as having a visual icon and a
    # certain step size
    def __init__(self, icon, step_size):
         Turtle.__init__(self) # Call the superclass's constructor
         self.shape(icon) # Set this object's icon
         self.__step_size = step_size # Save the given step size
         self.setheading(randint(0, 359)) # Point in a random direction
         self.penup() # Most invertebrates don't leave trails

    # All invertebrates are capable of moving along the ground
    def walk(self):
        self.forward(self.__step_size)

    # All invertebrates can tell us if they're near the edge of
    # the world
    def near_edge(self):
        return abs(self.xcor()) > max_coord - border or \
               abs(self.ycor()) > max_coord - border


#----------------------------------------------------------------
# This class defines arthropods (which includes insects and
# arachnids) to be invertebrates which change direction
# frequently as they move - all other methods inherited from
# the superclass are unchanged
#
class Arthropod(Invertebrate):

    # Arthropods can change direction, by redefining the
    # "walk" method
    def walk(self):
        self.left(randint(-60, 60))
        Invertebrate.walk(self) # Call the superclass's method


#----------------------------------------------------------------
# This class defines gastropods (which includes snails and
# slugs) to be invertebrates which leave a trail as they
# move
#
class Gastropod(Invertebrate):

    # Gastropods leave a trail of slime as they move
    def __init__(self, icon, step_size):
        Invertebrate.__init__(self, icon, step_size)
        self.width(2)
        self.color("dark green")
        self.pendown()

        
#----------------------------------------------------------------
# Beetles are a subclass of arthropods which can not only
# walk but can also fly
#
class Beetle(Arthropod):

    # To display flight we need to remember the two icons
    def __init__(self, walking_icon, flying_icon, step_size):
        self.__icon = walking_icon # Remember the icons
        self.__flying_icon = flying_icon
        Arthropod.__init__(self, walking_icon, step_size)      
        self.speed("slowest") # Make sure we can see the "flight"

    # Make the beetle "fly" by rapidly changing its shape as it moves
    def fly(self):
        for each in range(45): # This should be less than the border's size
            self.shape(self.__flying_icon)
            self.forward(1) 
            self.shape(self.__icon)


#----------------------------------------------------------------
# Define some fixed values to control the simulation
#
max_coord = 300 # largest positive or negative coord
border = 50 # how close we get to the edge before stopping, in pixels
num_steps = 500 # how many steps to take in the simulation


#----------------------------------------------------------------
# Set up the drawing window and other overall parameters
#
setup(max_coord * 2, max_coord * 2)
title("Invertebrates")
bgcolor("pale green")
hideturtle() # hide the default turtle

#----------------------------------------------------------------
# Register the icons we'll be using
#
register_shape("picture_spider.gif")
register_shape("picture_ladybird.gif")
register_shape("picture_ladybird_flying.gif")
register_shape("picture_snail.gif")

#----------------------------------------------------------------
# Create the invertebrate objects
#
snail = Gastropod("picture_snail.gif", 2) # The snail is the slowest
spider = Arthropod("picture_spider.gif", 10) # The spider is faster than the beetle
ladybird = Beetle("picture_ladybird.gif", "picture_ladybird_flying.gif", 5)

#----------------------------------------------------------------
# In each step move each invertebrate and make it turn around
# if it's reached the edge of the world (however this is not a
# reliable way of keeping the objects in the window!)
#
for step in range(num_steps):   
    if snail.near_edge():
        snail.left(180)
    snail.walk()
    if spider.near_edge():
        spider.left(180)
    spider.walk()
    if ladybird.near_edge():
        ladybird.left(180)
    if randint(1, 20) == 1: # 5% chance of flying
        ladybird.fly()
    else:
        ladybird.walk()

#----------------------------------------------------------------
# Release the drawing window when finished
#
done()
