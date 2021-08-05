#--------------------------------------------------------------------#
#
# Average rainfall calculator
#
# One of the reasons we need indefinite iteration is to handle unknown
# inputs from outside our program. As a simple example, here we
# develop a program where the inputs come from the user, so our
# program has to respond to however many inputs the user chooses to
# enter.
#

# Create a list for holding rainfall figures
rainfall = []

# Get the user's first input
rain_today = input("Enter the first day's rainfall (in millimetres): ")

# Continue reading rainfall values until the user says to stop
while not rain_today.lower() in ['stop', 'exit', 'quit', 'end']:
    # Save the current input and ask for the next one
    rainfall.append(int(rain_today))
    rain_today = input("Enter the next day's rainfall (in millimetres): ")

# The user has stopped entering numbers, so calculate the result, if any
if len(rainfall) == 0:
    print('No rainfall data entered')
else:
    print('The average daily rainfall over',
    len(rainfall), 'days was',
    sum(rainfall) // len(rainfall), 'millimetres')
