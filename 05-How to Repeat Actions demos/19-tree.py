#----------------------------------------------------------------
#
# Tree - A demonstration of recursion
#
# This program gives a visual demonstration of recursion
# by drawing a tree.  (This program is quite complicated,
# but the complexity is all to do with getting the drawing
# to look nice, not the recursive part.)
#


# Import the turtle graphics functions
from turtle import *



#----------------------------------------------------------------
# Draw a branch as a stick with a leaf on the end.  The leaf
# is normally three times wider than the branch's width, but
# a minimum size is introduced so that leaves don't become
# invisibly small.
#
def draw_branch(branch_length, branch_width):
    # Smallest possible leaf size, in pixels
    min_size = 15
    # Draw the stick
    pendown()
    color("brown")
    width(branch_width)
    forward(branch_length)
    # Draw the leaf at the end
    color("green")
    dot(max(min_size, branch_width * 3))
    penup()



#----------------------------------------------------------------
# Draw a tree as a branch and its sub-branches, if any.
#
# Base case: Draw a single branch.
#
# Recursive case: Same as the base case but with
# two sub-branches sticking out an an angle to the left
# and right.
#
def draw_tree(depth, branch_length, branch_width):
        
    # Angles between sub-branches and this one
    right_angle = 35 # degrees
    left_angle = 45 # degrees
    
    # Proportional size of sub-branches
    right_proportion = 0.7 # percent
    left_proportion = 0.6 # percent
        
    # Remember starting position and orientation
    start_x, start_y, start_heading = xcor(), ycor(), heading()

    # Draw a single branch (base case)
    draw_branch(branch_length, branch_width)

    # Add sub-branches, if any (recursive case)
    if depth > 0:

        # Draw the left sub-branch
        # 1. Go to left sub-branch's starting point and orientation
        penup()
        goto(start_x, start_y)
        setheading(start_heading)
        forward(branch_length * left_proportion)
        left(left_angle)
        # 2. Recursive call to draw the left sub-branch
        draw_tree(depth - 1, \
                  branch_length * left_proportion, \
                  branch_width * left_proportion)

        # Draw the right sub-branch
        # 1. Go to right sub-branch's starting point and orientation
        penup()
        goto(start_x, start_y)
        setheading(start_heading)
        forward(branch_length * right_proportion)
        right(right_angle)
        # 2. Recursive call to draw the right sub-branch
        draw_tree(depth - 1, \
                  branch_length * right_proportion, \
                  branch_width * right_proportion)



############################################################
# The main program
#
title("Tree")
speed("fastest") # control drawing speed
goto(0, -100) # move down a little to centre the drawing
setheading(90) # start by pointing upwards
draw_tree(6, 200, 18) # draw a tree
hideturtle() # exit elegantly
done()
