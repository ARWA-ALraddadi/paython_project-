#----------------------------------------------------------------
#
# Demonstration - Data structures created using lists
#
# As an example of how we can choose different data structures
# to store information, the functions in this file illustrate
# two distinct, but equally valid, ways of storing the same
# data.
#
# Recall that the pixels (picture elements) in digital images
# are made up of three brightness values, one each for red,
# green and blue.  Usually these are numbers in the range
# 0 to 255.  A complete digital picture therefore consists
# of a sequence of red-green-blue triples, one for each pixel.
#
# The variables below show two different ways of storing
# this information in lists.  The first approach is to create
# a single list of triple values.  The second aproach is to
# create three lists of single values.  Either approach is
# an effective "data structure" for storing this information.
#

#-----
# The single variable below shows the first way of storing
# some pixel values, as a list of triples.
#
rgb_pixels = [[169,  84,  45],
              [127, 110,  99],
              [145,  12,   9],
              [185,  42, 136],
              [  5, 133,  48],
              [244, 236,  19],
              [163,  24,  27],
              [ 20,   8, 122],
              [135,  52, 204],
              [ 80, 184, 194]]

#-----
# The three variables below show the second way of storing
# the same pixel values, as three lists of single values.
#
red =   [169, 127, 145, 185,   5, 244, 163,  20, 135,  80]
green = [ 84, 110,  12,  42, 133, 236,  24,   8,  52, 184]
blue =  [ 45,  99,   9, 136,  48,  19,  27, 122, 204, 194]

#-----
# This function prints the red-green-blue triples stored in
# the first data structure.  For neatness, each numerical
# value has been right justified in three spaces so that
# leading zeros are displayed.  Note that the loop iterates
# over the elements of each sublist in the given list.
#
def print_triples(triples):
    for red, green, blue in triples:
        print(str(red).rjust(3, '0') + ':' + \
              str(green).rjust(3, '0') + ':' + \
              str(blue).rjust(3, '0'))

#-----
# This function prints the red-green-blue values stored in
# the second data structure.  Note that the loop iterates
# over the number of items in the first list (which is assumed
# to be the same for the other two lists).
#
def print_lists(red_values, green_values, blue_values):
    list_length = len(red_values)
    for pixel_number in range(list_length):
        print(str(red_values[pixel_number]).rjust(3, '0') + ':' + \
              str(green_values[pixel_number]).rjust(3, '0') + ':' + \
              str(blue_values[pixel_number]).rjust(3, '0'))

#-----
# To prove that the information stored in the two different
# data structures is equivalent, this main program
# calls both functions above to display the pixel values
# stored in both.
#
print('List of triples...')
print_triples(rgb_pixels)
print()
print('Trio of lists...')
print_lists(red, green, blue)
