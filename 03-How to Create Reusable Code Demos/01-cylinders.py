#--------------------------------------------------------------------
#
# Demonstration - Cylinders
#
# The small examples in this file show how simple numerical functions
# can be defined and called.  Recall that the area of a circle is
# pi times its radius squared, and that the volume of a cylinder is
# the area of its end times its height.
#

# Import the constant pi (or at least an approximation to it!)
from math import pi

#--------------------------------------------------------------------
# Imagine that we had to calculate the volume of a water tank
# with radius 5 metres and height 10 metres.  The following code
# does this, but can only do so for this particular tank.  (Here
# we've chosen to round the result off to a whole number.)

area_of_end = pi * (5 ** 2)
volume_of_tank = area_of_end * 10
print("The tank's volume is", round(volume_of_tank), "metres cubed")
print()

#--------------------------------------------------------------------
# If we needed to do this for several tanks, we would be wise
# to define reusable functions to do the calculation.  Not only
# does this avoid repeating the code, but it also means that if
# we need to change the code we only have to do so in one place.
# It also has the advantage of giving a meaningful name to the
# code segment, making the program as a whole easier to understand.

# Function to return the area of a circle, given its radius
def circle_area(radius):
    return pi * (radius ** 2)

# Function to return the volume of a cylinder, given both its
# radius and height, as a whole number
def cylinder_volume(radius, height):
    volume = circle_area(radius) * height
    return round(volume)

# Now we can calculate the volume of several tanks, using the
# same code
print("Tank A's volume is", cylinder_volume(5, 10), "metres cubed")
print("Tank B's volume is", cylinder_volume(2, 5), "metres cubed")
print("Tank C's volume is", cylinder_volume(2, 10), "metres cubed") # twice Tank B's volume

