#---------------------------------------------------------------------
# Demonstration - Random Numbers
#
# The trivial demonstrations in this file show how the
# functions from the "random" module may produce a different
# result each time they're called


# Normally when we call a function with the same parameters
# it produces the same answer

print('The maximum of 3 and 9 is', max(3, 9))
print('The maximum of 3 and 9 is still', max(3, 9))
print('The maximum of 3 and 9 remains', max(3, 9))
print()

# The random functions are the exception because they may
# produce a different result each time they're called

from random import randint
print('A random number between 3 and 9 is', randint(3, 9))
print('Another random number between 3 and 9 is', randint(3, 9))
print('A third random number between 3 and 9 is', randint(3, 9))
print()

# As a slightly more realistic example, imagine that you
# needed to schedule a meeting on a certain day.  Any time
# between 9am and 4pm is available except 12pm, when you
# have lunch.  The following code will produce a random
# time for the meeting that never conflicts with your
# lunch break.  The outcome is printed in 24-hour time.

from random import choice

# Pick a time between 9am and 11am, inclusive
morning_time = randint(9, 11) 
morning_option = str(morning_time) + 'am'

# Pick a time between 1pm and 4pm, inclusive
afternoon_time = randint(1, 4) 
afternoon_option = str(afternoon_time) + 'pm'

# Choose between the morning and afternoon options
final_choice = choice([morning_option, afternoon_option])

#Display the outcome
print("We'll meet at", final_choice)


