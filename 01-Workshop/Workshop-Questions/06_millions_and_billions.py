######################################################################
#
# Millions and billions
#
# The words "millions" and "billions" sound similar, and not long ago
# you were considered rich if you were a millionaire, but now rich
# people are billionaires.  So is a million really very different from
# a billion?
#
# One way to get an intuitive appreciation for how close or far apart
# two numbers are is to express them in familiar units.
# In this exercise you will calculate one million seconds in days and
# and one billion seconds in years to see the difference.
# 
# Before you begin, try guessing what the answers will be.
# How many days is a million seconds?
# How many years is a billion seconds?
#
# (Irrelevant historical aside: For the purposes of this exercise
# we assume that a million is one thousand thousands, and a billion
# is one thousand million.  However, this definition of a billion
# comes to us from the United States of America only recently.  In
# Britain a "billion" used to be defined as a *million* million.  It
# was thus a lot easier to become a billionaire in the US than the
# UK!  The old British word for a thousand million was a "milliard".
# Today, however, the US definition has become accepted worldwide.)
#

# Here are some constant values you can use in your solution

seconds_per_minute = 60

minutes_per_hour = 60

hours_per_day = 24

minutes_per_day = minutes_per_hour * hours_per_day

days_per_year = 365 # ignoring leap years


# Your challenge, part one: Below write code for calculating
# how many days there are in a million seconds and print the
# result to the screen.  Use floating point arithmetic to do
# the calculation and round off your answer to a whole number
# before printing it.

pass # this statement does nothing - replace it

million_seconds = 1000000 / seconds_per_minute
print (million_seconds)
million_mint =  million_seconds / minutes_per_hour
print (million_mint)
million_hour = million_mint / hours_per_day
print (million_hour)


million_seconds = 1000000 / seconds_per_minute
million_seconds = million_seconds/ minutes_per_day
print ( " the day in milloin sec is ",round( million_seconds), 'days')

# Your challenge, part two: Below write code for calculating
# how many years there are in a billion seconds and print the
# result to the screen.  Use floating point arithmetic to do
# the calculation and round off your answer to a whole number
# before printing it.

pass # this statement does nothing - replace it


billion_seconds = 1000000000 / seconds_per_minute
billion_hour = billion_seconds/ minutes_per_hour
billion_day= billion_hour/hours_per_day
billion_year = billion_day / days_per_year



print ( " the day in billoin sec is ", round(billion_year), 'years.')

