#----------------------------------------------------------------
#
# Demonstration - Create your own story
#
# Python provides just one statement for choosing alternative
# actions but it can be used in a variety of ways, as illustrated
# below.
#
# As a case study in different ways of using conditional
# statements, consider a program which is intended to create the
# opening sentence of a story, based on a number of given
# values.
#


# First we establish the properties to be built into the
# story:
add_a_heading = True
hour = 19 # the hour of the day in 24-hour time
rainfall = 6 # millimetres per hour
windspeed = 7 # kilometres per hour

# Here's another set of values, which will produce a
# different story when uncommented and "dedented":
##    add_a_heading = False
##    hour = 11 # the hour of the day in 24-hour time
##    rainfall = 0 # millimetres per hour
##    windspeed = 5 # kilometres per hour


# Next we create a template for the story:
story = 'It was a BRIGHTNESS and WEATHER TIME-OF-DAY'


# A single Boolean value decides whether we add a
# chapter heading or nothing at all - this is an
# example of a "one-way" conditional statement:
#
if add_a_heading:
    story = 'Chapter 1\n' + story


# Decide whether or not it's dark - this is an example of a
# "two-way" conditional statement:
#
if 6 <= hour and hour <= 18: # i.e., it's between 6am and 6pm
    story = story.replace('BRIGHTNESS', 'bright')
    story = story.replace('TIME-OF-DAY', 'day')
else:
    story = story.replace('BRIGHTNESS', 'dark')
    story = story.replace('TIME-OF-DAY', 'night')


# Determine what the weather is like - this is
# an example of a "multi-way" conditional statement:
#
if rainfall == 0 and windspeed < 6:
    story = story.replace('WEATHER', 'sunny')
elif rainfall <= 4 and windspeed < 6:
    story = story.replace('WEATHER', 'showery')
else: # either the rain is heavy, the wind is strong or both
    story = story.replace('WEATHER', 'stormy')


# Finally, print the story opening we've created
print(story + '...')


# Postscript: This file is named in honour of Edward George
# Bulwer-Lytton whose opening sentence for his novel
# "Paul Clifford" (1830) is often cited as the worst ever.
# The default set of values above recreates his
# sentence's first part.  (Bulwer-Lytton's full sentence
# consumes an entire paragraph!)
