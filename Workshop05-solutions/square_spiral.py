#---------------------------------------------------------
#
# Square spiral
#
# This problem can be solved either iteratively (with a
# WHILE or FOR loop) or recursively (via a function that
# calls itself), but for practice we recommend you try
# solving it recursively.
#
# You are to develop a recursive function to draw a "spiral"
# formed from straight lines.  The spiral should be made of
# lines of increasing length at right angles to each other.
#
# 1) Your recursive function should have one parameter, the
#    current line length.
# 2) At each recursive step the function should draw
#    just one line, turn 90 degrees and then call itself
#    with a slightly longer length.
# 3) To limit the recursion, the function should just
#    call the "hideturtle" method when the given line
#    length exceeds a fixed limit.
#
# See file "square_spiral.pdf" for an example of the
# expected output.
#

from turtle import *

#---------------------------------------------------------
#

#### DEFINE YOUR square_spiral FUNCTION HERE

def square_spiral(line_length):
    
    max_line_length = 400 # pixels
    increased_length = 3 # pixels

    if line_length < max_line_length: # Recursive case
        forward(line_length) # draw this line
        right(90) # turn right
        square_spiral(line_length + increased_length) # draw the rest
    else: # Base case
        hideturtle()

#---------------------------------------------------------
#
# This main program calls your function to start the
# process
#
setup()
title("Square spiral")
speed("fast")
square_spiral(1) # start with a line one pixel long
done()
