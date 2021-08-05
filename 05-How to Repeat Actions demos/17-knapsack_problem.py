##--------------------------------------------------------------------
##
##  Demonstration - Data-driven indefinite iteration
##
##  This example illustrates indefinite iteration, i.e., a situation
##  where we need to repeatedly do an action but can't predict in
##  advance how many iterations will be required.  In this
##  case the number of iterations is "data-driven".
##


#---------------------------------------------------------------------
#
# Problem statement and required strategy
#
# The "knapsack problem" is a well-known optimisation challenge.
# Here we illustrate a simplified (non-optimal) solution to the
# problem.
#
# Imagine that you are playing an adventure game in which the goal is
# to accumulate treasure which you must carry with you in a
# "knapsack" (backpack), but there's a limit to how much weight you
# can carry.  While walking through the scary forest you find a pile
# of gold ingots lying on the ground, each stamped with its weight.
#
# The aim is to define a function that tells you which ingots to
# pick up, such that you don't exceed your weight limit.  The
# required strategy is that you start with the lightest ingot and
# keep picking up increasingly heavy ones until you can carry no
# more.
#
# Comment: Although this strategy sounds sensible, the interesting
# thing about the knapsack problem is that following this algorithm
# will not necessarily produce the best possible result.  It is
# sometimes better to leave several lighter items behind in favour of
# a heavier one.  (You can find lots of information about optimal
# solutions to the knapsack problem in the "algorithms" literature.)
#


#---------------------------------------------------------------------
#
# An implementation (following the above-described strategy):
#

# Given a weight limit and a list of the weights of gold ingots,
# all weights expressed in kilograms, return a list of ingots that
# should be picked up and put in your knapsack, using the
# "lightest-to-heaviest" strategy
def knapsack(limit, ingots):

    # Sort the ingots from lightest to heaviest
    sorted_ingots = sorted(ingots)

    # Initialise the list of ingots picked up
    picked_up = []

    # As long as there are still some ingots left, and
    # picking up the next ingot will not exceed our weight
    # limit, keep accumulating treasure
    while sorted_ingots != [] and \
          (sum(picked_up) + sorted_ingots[0]) <= limit:
        picked_up = picked_up + [sorted_ingots[0]] # add ingot to knapsack
        sorted_ingots.pop(0) # remove ingot from those left

    # Return the list of ingots picked up
    return picked_up


# Quick quiz: The Boolean condition in the "while" loop above
# relies on the left-to-right evaluation order of "and" conjuncts.
# Can you see why this was necessary?

    
#---------------------------------------------------------------------
#
# Some tests:
#

# No ingots here to pick up, even though I could carry another
# 10kg worth :-(
print ('Test 1:', knapsack(10, []))

# I have no more carrying capacity, so I have to leave all the gold
# behind  :-(
print ('Test 2:', knapsack(0, [5, 2, 0.5, 0.5, 1]))

# I can carry all the gold ingots I find (and more)  :-)
print ('Test 3:', knapsack(10, [5, 2, 0.5, 0.5, 1]))

# I can carry only part of the treasure, so I pick up the
# lightest ingots and fill my knapsack :-)
print ('Test 4:', knapsack(7, [10, 3, 5, 2, 2, 6]))

# I can carry only part of the treasure, so I pick up the
# lightest ingots but walk away with some carrying capacity
# left and some ingots still on the ground :-|
print ('Test 5:', knapsack(5, [5, 2, 0.5, 0.5, 1]))

# Note in this last example that a better strategy would have been
# to pick up the 5kg ingot instead of the lightest ones, which
# only totalled 4kg by the time my weight limit was reached - this
# shows that the "lightest-to-heaviest" algorithm is not optimal
# for the knapsack problem


