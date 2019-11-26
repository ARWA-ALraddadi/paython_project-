#--------------------------------------------------------------------#
#
# Mars lander example - No error handling
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
# Here, in the program's original form, if the barometer produces
# incorrect numbers when the lander is near the ground it may
# hit the surface without the retro rockets being on, destroying
# the craft.
#
# Also, if the barometer produces non-number values the whole
# program will crash and control of the retro rockets will be
# entirely lost.
#
# Finally, there's a weakness in the way the loop is programmed
# which means that if the lander doesn't stop at a height of
# exactly zero (e.g., if it lands in a deep crater) the retro
# rockets will fire while it's on the ground, possibly toppling
# the craft over.
#

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
    # Read from the barometer (the user in this case!)
    air_pressure = int(input('Enter barometer reading: '))
    # Calculate the lander's altitude
    altitude = altimeter(air_pressure)
    # Decide whether or not the retros should be firing
    if altitude == 0 or altitude > 25:
        retros_off()
    else:
        retros_on()
        
# We made it!
print('Houston, the Eagle has landed!')

    
    
