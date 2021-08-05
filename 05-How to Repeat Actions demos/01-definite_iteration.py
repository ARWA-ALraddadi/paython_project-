##--------------------------------------------------------------------
##
##  Demonstration - Definite iteration
##
##  Definite iteration is the situation where the number of
##  repetitions can be known before the loop begins.  The small
##  examples in this file illustrate some of the common
##  ways in which definite iteration is used in Python.
##


#---------------------------------------------------------------------
#
# Given a sequence of values we can iterate over each of the
# individual values it contains, in order:

for character in 'Hello!':
    print('-', character, '-')

print() # a blank line to separate the examples


#---------------------------------------------------------------------
#
# Alternatively, we can iterate over all of the sequence's indices
# (keeping in mind that a sequence of length N has indices 0 to
# N - 1):

message = 'Goodbye!'

length_of_message = len(message)
for index in range(length_of_message):
    print(index, message[index])

print() # a blank line to separate the examples

# Comment: Here we introduce an explicit index variable so that we
# can display the position at which each character occurs, but if
# we don't need to use an index variable explicitly then we shouldn't
# complicate the code by introducing one.


#---------------------------------------------------------------------
#
# As well as specifying how many iterations to perform, the "range"
# function can optionally take the first index as an argument:

message = 'Goodbye!'

length_of_message = len(message)
for selected_index in range(4, length_of_message):
    print(selected_index, '...', message[selected_index].upper())

print() # a blank line to separate the examples

# Comment: More generally, "for x in range(a, b):" means to do
# something for values of x from a, inclusive, to b, exclusive!


#---------------------------------------------------------------------
#
# Whereas all the elements of a character string are of the same
# type, lists can be comprised of elements of various types, so we
# can choose to do something different with each one via Python's
# "isinstance" function:

misc_data = ['George Jetson', 35, ['Judy', 'Elroy'], {('Astro', 5)}]

for item in misc_data:
    if isinstance(item, int):
        print('Found an integer:', item)
    elif isinstance(item, float):
        print('Found a floating point number:', item)
    elif isinstance(item, str):
        print('Found a character string:', item)
    elif isinstance(item, list):
        print('Found a list:', item)
    else:
        print('Found something else:', item)

print()

#---------------------------------------------------------------------
#
# As a more realistic example, the following function returns a list
# of all the items that occur uniquely in a given list.
#
# Our solution approach is:
# a) Initialise a new list to hold the unique items
# b) For each item in the given list:
#    i) If the item appears only once in the given list
#       add it to the collection of unique items
# c) Return the collection of unique items
#
# (Comment: This is a conceptually simple algorithm, but does not
# lead to the most efficient implementation because it requires
# looking through the list many times to count how often each item
# occurs.)
#


# Return a list of the unique items in a given list
def unique_items(items):

    # Keep track of those items that occur once only
    one_offs = []

    # Check how many times each item in the list occurs and
    # remember those that occur once only
    for item in items:
        if items.count(item) == 1:
            one_offs = one_offs + [item]

    # Return the final list of unique items
    return one_offs


# A test
test_list = [1, 2, 3, 4, 2, 1, 5, 6, 4]
print('The unique items in list', test_list, 'are', unique_items(test_list))
