##------------------------------------------------------------
##
##  Multi-sided dice
##
##  A simple example of a class whose objects have their
##  own internal state and external setter and getter
##  methods
##

from random import randint


#------------------------------------------------------------
# A class representing a die with multiple sides (six
# by default)
class Die:

    # When first instantiated the die's face shows '1'
    def __init__(self, num_sides = 6):
        self.__num_sides = num_sides
        self.__face = 1

    # Roll the die to get a random value
    def roll(self):
        self.__face = randint(1, self.__num_sides)

    # Return which face of the die is currently showing
    def face(self):
        return self.__face


##------------------------------------------------------------
# A main program to test the class

# Instantiate two objects from the class above
red_die = Die(9) # A 9-sided die
blue_die = Die() # A default 6-sided die

# Roll both dice once
red_die.roll()
blue_die.roll()

# Print their faces
print(red_die.face(), blue_die.face())

# Roll both dice until they come up with the same face
while red_die.face() != blue_die.face():
    red_die.roll()
    blue_die.roll()
    print(red_die.face(), blue_die.face())

