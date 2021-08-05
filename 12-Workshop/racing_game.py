#------------------------------------------------------------------
#
# "And they're racing!"
#
# As a major exercise involving concurrent actions, this program
# creates instances of the Turtle class representing race horses
# that run from a starting line to a finishing line.  At each
# iteration each horse should take a randomly-sized step so that
# the outcome of the race cannot be predicted in advance.
# The winner is indicated by turning the first horse to complete
# the race into a trophy icon, using a global variable to keep
# track of whether or not the race has been won.
#
# Development hint: This is a hard exercise.  Tackle it one
# piece at a time.  First work out how to get a single horse to
# run the course, then start creating multiple horses.
#
# Historical note: Mechanical racing games with random outcomes
# like this were popular in the ninteenth century, as were board
# games where the length of each horse's step was determined by
# rolling a die.  An interesting twentieth-century variation
# was vinyl records of a race-caller calling a race where the
# winner was different each time the record was played.  (Can
# you figure out how this was done?  Hint: How many grooves are
# there on a normal vinyl record?) 
#


#------------------------------------------------------------------
# Import the necessary pre-defined functions.
from turtle import *
from random import randint


#------------------------------------------------------------------
# Introduce a global variable to track whether or not there
# has been a winner yet.
race_won = False


#------------------------------------------------------------------
# Define some fixed values to control the simulation - change
# these to alter the simulation's appearance and behaviour.
#
# Note that the racecourse runs left-to-right, so its "length"
# is in the x direction and its "width" is in the y direction.
# Also the "horse" sizes defined here assume that the supplied
# GIF icons are used.  You will need to change these constants
# if you use your own images.
#
racecourse_length = 1000 # pixels
racecourse_width = 520 # pixels
horse_length = 120 # pixels
horse_height = 73 # pixels
horiz_border = 290 # pixels
vert_border = 120 # pixels
max_step_size = 15 # longest step a horse can take, in pixels


#------------------------------------------------------------------
# Instantiate and initialise a horse object.
#
# Given a colour, this function needs to instantiate a new Turtle
# object, register its shape, set the object to use this shape,
# set its heading and other essential drawing characteristics,
# and then return the new object itself.
#
def create_horse(colour):
    register_shape("racehorse_" + colour + ".gif")
    horse = Turtle()
    horse.hideturtle() # make horse invisible initially
    horse.shape("racehorse_" + colour + ".gif")
    horse.setheading(0) # face east
    horse.penup()
    horse.speed("slow")
    return horse


#------------------------------------------------------------------
# Move the given horse object by a random step.
#
def move_horse(horse):
    horse.forward(randint(1, max_step_size))


#------------------------------------------------------------------
# This Boolean-valued function returns True iff the given horse
# object has passed the finishing line, and turns the horse into
# a trophy if it's first past the finishing line.
#
def finished(horse):
    global race_won
    horse_finished = horse.xcor() > ((racecourse_length + horse_length) / 2)
    if horse_finished:
        if not race_won:
            race_won = True
            horse.shape("gold_trophy.gif")
        else:
            horse.hideturtle()
    return horse_finished


#------------------------------------------------------------------
# Main program starts here:
#


# 1. Set up the drawing window.
title(str(racecourse_length) + " Pixel Handicap")
setup(racecourse_length + horiz_border, \
      racecourse_width + vert_border)
bgcolor("green")


# 2. Draw the starting and finishing lines (using the
#    default turtle object).
width(10)
color("yellow")
# Draw the starting line on the left
penup()
goto(-(racecourse_length / 2), -(racecourse_width / 2))
pendown()
goto(-(racecourse_length / 2), (racecourse_width / 2))
# Draw the finishing line on the right
penup()
goto((racecourse_length / 2), -(racecourse_width / 2))
pendown()
goto((racecourse_length / 2), (racecourse_width / 2))
penup()
hideturtle()


# 3. Create a list of racehorse objects.
horses = [create_horse("blue"), \
          create_horse("red"), \
          create_horse("yellow"), \
          create_horse("green"), \
          create_horse("white"), \
          create_horse("brown"), \
          create_horse("grey"), \
          create_horse("purple")]


# 4. Register the winner's trophy icon
register_shape("gold_trophy.gif")


# 5. Put each horse object behind the starting line (using
#    the constants that determine the racecourse's and each
#    horse's dimensions).
for horse_no in range(len(horses)):
    horses[horse_no].goto(-((racecourse_length + horse_length) / 2), \
                          -(racecourse_width / 2) + horse_no * horse_height)
    horses[horse_no].showturtle()


# 6. Run the race by repeatedly moving each horse object until
#    they've all crossed the finishing line.  (Hint: Once a
#    horse has crossed the line the object can be removed from
#    the list.)
while horses != []:
  for horse in horses:
      move_horse(horse)
      if finished(horse):
          horses.remove(horse)


# 7. Release the drawing window when finished.
done()
