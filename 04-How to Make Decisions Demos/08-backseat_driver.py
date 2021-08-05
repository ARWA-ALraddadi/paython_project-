#---------------------------------------------------------------------
#
# Multi-way choice demo - Backseat Driver
#
# This little program demonstrates the ability to make
# a choice with several alternatives.  Run the program
# and respond to the prompt with a number.  (The program
# will crash if you don't enter a valid number.)
#

users_input = input("How fast do you want to go (in km/hr)? ")
speed = eval(users_input)

if speed < 5: # km/hr
    print("Hurry up!")
elif speed < 50:
    print("Go a bit quicker!")
elif speed < 90:
    print("That's fast enough!")
else:
    print("Slow down!")

print("Give me the wheel!")
