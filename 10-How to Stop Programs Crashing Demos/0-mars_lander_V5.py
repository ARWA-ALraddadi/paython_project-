#--------------------------------------------------------------------#
#
# Mars lander example - Exception handling
#
# This simple program allows us to experiment with defensive
# programming, assertions and exception handling. It is based on
# a real-life example in which a software failure caused
# a Mars lander to crash.
#
# To run the program the user is meant to simulate a barometer
# and enter an increasing series of air pressure readings
# between 0 and 100, e.g., 1, 4, 10, 50, 80, 100.
#
# Retro rockets will fire while the pressure equals or
# exceeds 75 and will stop when the pressure reaches 100,
# which is assumed to be the air pressure at ground level.
#
# In this version exception handling code is added to the
# main loop to catch any kind of altimeter failure and
# respond with a default action.
#

# Import the regular expression match function
from re import match

# Two utility functions to tell us whether the retro rockets
# are on or off
def retros_on():
    print("-- Retro rockets are firing --")

def retros_off():
    print("-- Retro rockets are off --")

altitude = 1000000 # initialise with a big number

pressure_at_surface = 100 # constant

# Calculate altitude based on atmospheric
# pressure - higher pressure means lower altitude
def altimeter(barometer_reading):
    # Assertion to raise an exception if air pressure is negative
    assert barometer_reading >= 0, 'Barometer failure detected!'
    # Return the result (if we make it this far!)
    return pressure_at_surface - barometer_reading

# Main program to decide when to fire the retros
while altitude > 0:   
    # The default action for any kind of altimeter failure
    # is to assume we are at a low altitude - it's better
    # to waste fuel than crash!
    try:
        # Calculate the lander's altitude, if possible
        altitude = altimeter(int(input('Enter barometer reading: ')))
    except ValueError:
        print('** Altimeter type error - Firing retros! **')
        retros_on() 
    except AssertionError:
        print('** Altimeter range error - Firing retros! **')
        retros_on() 
    else:
        # Decide whether or not the retros should be firing
        if altitude <= 0 or altitude > 25:
            retros_off()
        else:
            retros_on()
        
# We made it!
print('Houston, the Eagle has landed!')

    
    
