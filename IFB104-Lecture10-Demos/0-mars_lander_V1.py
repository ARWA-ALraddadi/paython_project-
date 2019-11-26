#--------------------------------------------------------------------#
#
# Mars lander example - Checking input validity
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
# In this version the program checks to ensure that the
# barometer reading received is an integer and requests
# another if it isn't.
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
    # Return the result
    return pressure_at_surface - barometer_reading

# Main program to decide when to fire the retros
while altitude != 0:
    # Read a valid integer from the barometer (the user in this case!)
    raw_air_pressure = input('Enter barometer reading: ')
    while match('^-?[0-9]+$', raw_air_pressure) == None:
        raw_air_pressure = input('Re-enter barometer reading: ')
    air_pressure = int(raw_air_pressure)        
    # Calculate the lander's altitude
    altitude = altimeter(air_pressure)
    # Decide whether or not the retros should be firing
    if altitude == 0 or altitude > 25:
        retros_off()
    else:
        retros_on()
        
# We made it!
print('Houston, the Eagle has landed!')

    
    
