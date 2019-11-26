#---------------------------------------------------------
#
# Linear Curve
#
# Define a function called "linear_curve" that uses Turtle
# graphics to draw a linear curve by drawing straight lines
# between increasing/decreasing points on the x-axis to
# decreasing/increasing points on the y-axis.  Part of the
# function has been given below, but not the crucial loop
# that draws each line.
#
# See the enclosed file "linear_curve.pdf" for an example
# of the expected output.
#
# Extra challenge:  Extend your function so that it
# draws a "full circle" linear curve.
#

# Import required functions
from turtle import *


#---------------------------------------------------------
#
# Suggested solution strategy to complete the linear_curve function:
#
# 1. For each line to be drawn:
#    a. Calculate the distance D the line must be offset from the corner
#    b. Draw a line from one axis to the next that is offset on
#       the y-axis by D and on the x-axis by the line length minus D
#


# A function to draw a linear curve
#
def linear_curve():
 
    # Set the length of each line
    line_length = 300

    # Set the separation between successive lines on the axes
    line_sep = 10

    # Calculate how many lines must be drawn
    num_lines = line_length // line_sep

    ##### COMPLETE THE linear_curve FUNCTION HERE

    # For each of the points along the axis:
    for line_num in range(num_lines + 1):

        # Calculate the current line's offset from the corner
        offset = line_num * line_sep

        # Draw one line of the linear curve
        penup()
        goto(line_length, offset) # Draw from the y-axis to ...
        pendown()
        goto(line_length - offset, line_length) # ... the x-axis


##        # Challenge: Draw four linear curves, to form a circle
##
##        # A helper function to draw one line for the "challenge" code
##        #
##        def draw_line(start_x, start_y, finish_x, finish_y):
##            penup()
##            goto(start_x, start_y)
##            pendown()
##            goto(finish_x, finish_y)
##
##        # Spread the four corners out so they don't overlap
##        curve_sep = line_length * 0.75
##
##        # Top right corner (already done above)
##        ## draw_line(line_length, offset, line_length - offset, line_length)
##        # Bottom left corner
##        draw_line(0 - curve_sep, line_length - offset - curve_sep,
##                  offset - curve_sep, 0 - curve_sep)
##        # Bottom right corner            
##        draw_line(offset, 0 - curve_sep, line_length, offset - curve_sep)
##        # Top left corner            
##        draw_line(0 - curve_sep, offset, offset - curve_sep, line_length)

    
#---------------------------------------------------------
# Main program to call your linear_curve function
#
setup()
title("Linear curve")
speed('fastest')
linear_curve()
hideturtle()
done()
