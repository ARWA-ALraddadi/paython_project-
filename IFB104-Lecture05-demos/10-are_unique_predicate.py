##--------------------------------------------------------------------
##
##  Demonstration - Exiting a loop early
##
##  The following example illustrates a situation where we may
##  exit a "for" loop early because it's sometimes possible to
##  produce the required answer without completing all of the
##  iterations. In this case we define a predicate that stops
##  as soon as it can produce a definite answer.
##


#---------------------------------------------------------------------
#
# Requirement:
#
# Define a predicate (i.e., a Boolean-valued function) which returns
# True iff (if and only if) all items in a given sequence are unique.
# We assume an empty sequence returns True.
#
#
# An algorithm for solving this problem:
#
# Look at each item in the given list, keeping track of which items
# you've seen so far.  If you encounter an item you've seen before
# stop and return False.  If you get to the end of the list without
# finding any duplicate items return True.
#
#
# An implementation in Python:
#

# Return True iff all items in a given list are unique
def are_unique(items):

    # Keep track of those items we've seen so far
    already_seen = []

    # Look at each item in the given list
    for item in items:
        if item in already_seen:
            # Duplicate item found, so no need to look any further
            return False
        else:
            # Item has not been seen before, so add it
            # to our memory of those we've seen so far
            already_seen = already_seen + [item]

    # All items have been examined without any duplicates found
    return True


# Some tests:

print('Test 1:', are_unique([])) # returns True (by definition)
print('Test 2:', are_unique([4, 2, 7, 3])) # returns True (and doesn't exit early)
print('Test 3:', are_unique([5, 6, 9, 5, 2, 3, 1])) # returns False (and exits early)
print('Test 4:', are_unique('unique')) # returns False (and exits early)
print()

# It's claimed that the following two 15-letter words are
# the longest ones in the English language formed from
# unique characters - let's check that claim!

print('Test 5:', are_unique('uncopyrightable'))
print('Test 6:', are_unique('dermatoglyphics'))


# An experiment:
#
# To convince yourself that the above loop can exit early, insert
# the following (side-effecting) statement,
#
#   print('Examining', item)
#
# as the first statement in the "for" loop above.  Now when you run the
# tests you will see which items are examined.


# Challenge:
#
# A more concise, but less efficient, solution to this problem is
# possible using Python's "set" type.  Can you think how?
