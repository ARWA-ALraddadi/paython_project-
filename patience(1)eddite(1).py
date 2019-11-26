
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: PUT YOUR STUDENT NUMBER HERE
#    Student name: PUT YOUR NAME HERE
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
# PATIENCE
#
# This assignment tests your skills at processing data stored in
# lists, creating reusable code and following instructions to display
# a complex visual image.  The incomplete Python program below is
# missing a crucial function, "deal_cards".  You are required to
# complete this function so that when the program is run it draws a
# game of Patience (also called Solitaire in the US), consisting of
# multiple stacks of cards in four suits.  See the instruction sheet
# accompanying this file for full details.
#
# Note that this assignment is in two parts, the second of which
# will be released only just before the final deadline.  This
# template file will be used for both parts and you will submit
# your final solution as a single Python 3 file, whether or not you
# complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be installed separately, because the markers
# will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

# Constants defining the size of the card table
table_width = 1100 # width of the card table in pixels
table_height = 800 # height (actually depth) of the card table in pixels
canvas_border = 30 # border between playing area and window's edge in pixels
half_width = table_width // 2 # maximum x coordinate on table in either direction
half_height = table_height // 2 # maximum y coordinate on table in either direction

# Work out how wide some text is (in pixels)
def calculate_text_width(string, text_font = None):
    penup()
    home()
    write(string, align = 'left', move = True, font = text_font)
    text_width = xcor()
    undo() # write
    undo() # goto
    undo() # penup
    return text_width

# Constants used for drawing the coordinate axes
axis_font = ('Consolas', 10, 'normal') # font for drawing the axes
font_height = 14 # interline separation for text
tic_sep = 50 # gradations for the x and y scales shown on the screen
tics_width = calculate_text_width("-mmm -", axis_font) # width of y axis labels

# Constants defining the stacks of cards
stack_base = half_height - 25 # starting y coordinate for the stacks
num_stacks = 6 # how many locations there are for the stacks
stack_width = table_width / (num_stacks + 1) # max width of stacks
stack_gap = (table_width - num_stacks * stack_width) // (num_stacks + 1) # inter-stack gap
max_cards = 10 # maximum number of cards per stack

# Define the starting locations of each stack
stack_locations = [["Stack " + str(loc + 1),
                    [int(-half_width + (loc + 1) * stack_gap + loc * stack_width + stack_width / 2),
                     stack_base]] 
                    for loc in range(num_stacks)]

# Same as Turtle's write command, but writes upside down
def write_upside_down(string, **named_params):
    named_params['angle'] = 180
    tk_canvas = getscreen().cv
    tk_canvas.create_text(xcor(), -ycor(), named_params, text = string)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# create the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the coordinate axes displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_axes = True):

    # Set up the drawing canvas
    setup(table_width + tics_width + canvas_border * 2,
          table_height + font_height + canvas_border * 2)

    # Draw as fast as possible
    tracer(False)

    # Make the background felt green and the pen a lighter colour
    bgcolor('green')
    pencolor('light green')

    # Lift the pen while drawing the axes
    penup()

    # Optionally draw x coordinates along the bottom of the table
    if show_axes:
        for x_coord in range(-half_width + tic_sep, half_width, tic_sep):
            goto(x_coord, -half_height - font_height)
            write('| ' + str(x_coord), align = 'left', font = axis_font)

    # Optionally draw y coordinates to the left of the table
    if show_axes:
        max_tic = int(stack_base / tic_sep) * tic_sep
        for y_coord in range(-max_tic, max_tic + tic_sep, tic_sep):
            goto(-half_width, y_coord - font_height / 2)
            write(str(y_coord).rjust(4) + ' -', font = axis_font, align = 'right')

    # Optionally mark each of the starting points for the stacks
    if show_axes:
        for name, location in stack_locations:
            # Draw the central dot
            goto(location)
            color('light green')
            dot(7)
            # Draw the horizontal line
            pensize(2)
            goto(location[0] - (stack_width // 2), location[1])
            setheading(0)
            pendown()
            forward(stack_width)
            penup()
            goto(location[0] -  (stack_width // 2), location[1] + 4)
            # Write the coordinate
            write(name + ': ' + str(location), font = axis_font)

    #Draw a border around the entire table
    penup()
    pensize(3)
    goto(-half_width, half_height) # top left
    pendown()
    goto(half_width, half_height) # top
    goto(half_width, -half_height) # right
    goto(-half_width, -half_height) # bottom
    goto(-half_width, half_height) # left

    # Reset everything, ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any partial drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the deal_cards function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_game function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_game function.
#

# Each of these fixed games draws just one card
fixed_game_0 = [['Stack 1', 'Suit A', 1, 0]]
fixed_game_1 = [['Stack 2', 'Suit B', 1, 0]]
fixed_game_2 = [['Stack 3', 'Suit C', 1, 0]]
fixed_game_3 = [['Stack 4', 'Suit D', 1, 0]]

# Each of these fixed games draws several copies of just one card
fixed_game_4 = [['Stack 2', 'Suit A', 4, 0]]
fixed_game_5 = [['Stack 3', 'Suit B', 3, 0]]
fixed_game_6 = [['Stack 4', 'Suit C', 2, 0]]
fixed_game_7 = [['Stack 5', 'Suit D', 5, 0]]

# This fixed game draws each of the four cards once
fixed_game_8 = [['Stack 1', 'Suit A', 1, 0],
                ['Stack 2', 'Suit B', 1, 0],
                ['Stack 3', 'Suit C', 1, 0],
                ['Stack 4', 'Suit D', 1, 0]]

# These fixed games each contain a non-zero "extra" value
fixed_game_9 = [['Stack 3', 'Suit D', 4, 4]]
fixed_game_10 = [['Stack 4', 'Suit C', 3, 2]]
fixed_game_11 = [['Stack 5', 'Suit B', 2, 1]]
fixed_game_12 = [['Stack 6', 'Suit A', 5, 5]]

# These fixed games describe some "typical" layouts with multiple
# cards and suits. You can create more such data sets yourself
# by calling function random_game in the shell window

fixed_game_13 = \
 [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0],
  ['Stack 5', 'Suit B', 1, 1],
  ['Stack 2', 'Suit C', 4, 0]]
 
fixed_game_14 = \
 [['Stack 1', 'Suit C', 1, 0],
  ['Stack 5', 'Suit D', 2, 1],
  ['Stack 3', 'Suit A', 2, 0],
  ['Stack 2', 'Suit A', 8, 5],
  ['Stack 6', 'Suit C', 10, 0]]

fixed_game_15 = \
 [['Stack 3', 'Suit D', 0, 0],
  ['Stack 6', 'Suit B', 2, 0],
  ['Stack 2', 'Suit D', 6, 0],
  ['Stack 1', 'Suit C', 1, 0],
  ['Stack 4', 'Suit B', 1, 1],
  ['Stack 5', 'Suit A', 3, 0]]

fixed_game_16 = \
 [['Stack 6', 'Suit C', 8, 0],
  ['Stack 2', 'Suit C', 4, 4],
  ['Stack 5', 'Suit A', 9, 3],
  ['Stack 4', 'Suit C', 0, 0],
  ['Stack 1', 'Suit A', 5, 0],
  ['Stack 3', 'Suit B', 5, 0]]

fixed_game_17 = \
 [['Stack 4', 'Suit A', 6, 0],
  ['Stack 6', 'Suit C', 1, 1],
  ['Stack 5', 'Suit C', 4, 0],
  ['Stack 1', 'Suit D', 10, 0],
  ['Stack 3', 'Suit B', 9, 0],
  ['Stack 2', 'Suit D', 2, 2]]
 
# The "full_game" dataset describes a random game
# containing the maximum number of cards
stacks = ['Stack ' + str(stack_num+1) for stack_num in range(num_stacks)]
shuffle(stacks)
suits = ['Suit ' + chr(ord('A')+suit_num) for suit_num in range(4)]
shuffle(suits)
full_game = [[stacks[stack], suits[stack % 4], max_cards, randint(0, max_cards)]
             for stack in range(num_stacks)]

#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a game
# of Patience to be drawn.  Your program must work for any data set 
# returned by this function.  The results returned by calling this 
# function will be used as the argument to your deal_cards function 
# during marking. For convenience during code development and marking 
# this function also prints the game data to the shell window.
#
# Each of the data sets generated is a list specifying a set of
# card stacks to be drawn. Each specification consists of the
# following parts:
#
# a) Which stack is being described, from Stack 1 to num_stacks.
# b) The suit of cards in the stack, from 'A' to 'D'.
# c) The number of cards in the stack, from 0 to max_cards
# d) An "extra" value, from 0 to max_cards, whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#
# There will be up to num_stacks specifications, but sometimes fewer
# stacks will be described, so your code must work for any number
# of stack specifications.
#
def random_game(print_game = True):

    # Percent chance of the extra value being non-zero
    extra_probability = 20

    # Generate all the stack and suit names playable
    game_stacks = ['Stack ' + str(stack_num+1)
                   for stack_num in range(num_stacks)]
    game_suits = ['Suit ' + chr(ord('A')+suit_num)
                  for suit_num in range(4)]

    # Create a list of stack specifications
    game = []

    # Randomly order the stacks
    shuffle(game_stacks)

    # Create the individual stack specifications 
    for stack in game_stacks:
        # Choose the suit and number of cards
        suit = choice(game_suits)
        num_cards = randint(0, max_cards)
        # Choose the extra value
        if num_cards > 0 and randint(1, 100) <= extra_probability: 
            option = randint(1,num_cards)
        else:
            option = 0
        # Add the stack to the game, but if the number of cards
        # is zero we will usually choose to omit it entirely
        if num_cards != 0 or randint(1, 4) == 4:
            game.append([stack, suit, num_cards, option])
        
    # Optionally print the result to the shell window
    if print_game:
        print('\nCards to draw ' +
              '(stack, suit, no. cards, option):\n\n',
              str(game).replace('],', '],\n '))
    
    # Return the result to the student's deal_cards function
    return game

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "deal_cards" function.
#


# variabl size for cards width and height
width_card = 190         
height_card = width_card +30


def background_card (bgcolor = "Papaya Whip"):
#  Draw card background rectangle for four theams
# take Papaya Whip as defult color but in joker backgound different 
     
    penup()
    setheading(0)                # set diriction of turtle 
    color(bgcolor)         # use the given colour
    pendown()

# stat coloring shape and loop to move turtle and finish drawing  
    begin_fill()
    
    for BGD in range (2):
        forward(width_card)              
        right(90)
        forward(height_card)     
        right(90)

    end_fill()
    penup()      # make sure pen up to next function to draw 



def house_of_Martell ():
# function drawing house of Martell cards

# calling function to draw backgroung
   background_card()

# set up dirctions for turtle
   penup()
   setheading(-45)
   forward(height_card //1.5)    
   left(-90)
   pendown()
   
# stat coloring shape and loop to move turtle and finish drawing  
   pencolor("Dark Orange")
   color("Goldenrod")
   width (2)
   begin_fill()
   
   for stars_angle in range(52):
      forward(100)
      right(175)
      forward(100)
      right(90)
      forward(10)
      right(90)
      left(2)
      
   end_fill()
   penup()  # make sure the pen up for next card
   setheading (-180)
   forward(height_card //2.1)



def turtle_diction (cricle_color):
# function locate circle in card

 # set up dirctions for turtle
   setheading(-45)
   forward(height_card //4)
   left(-90)
   pendown()
   
# stat coloring shape and draw circle and finish drawing  
   color(cricle_color)
   begin_fill()
   circle(width_card //2.2)
   end_fill()
   
 

def house_of_Clegane():
# function drawing house of Clegane cards

# calling function to draw backgroung
   background_card()
   
# calling function to dirctions for turtle
   turtle_diction( "Dim Gray")
   
# set dirictions for three dot in mid of circle    
   color("Light Sea Green")
   penup()
   backward(height_card//2.5)
   setheading(90)
   forward(-40)
   
# drawing three dot in mid of circle  
   for line_in_dot in range(3):
       penup() 
       setheading(90)
       forward(-40)
       pendown()
       dot(20)
       penup()
       
# drawing half circle in mid of circle  
   pencolor("Deep Sky Blue")
   width (8)
   pendown()
   setheading(90)
   forward(25)
   
   setheading(0)
   backward(height_card //2.9)
   left(-90)
   
   circle(width_card //2.5 , 180)
   left (90)
   forward(145)
   
# make sure the pen up for next card
   penup()
   forward(31.5)



def House_of_Tyrell ():
# function drawing house of Tyrell cards

# calling function to draw backgroung
   background_card()
    
# calling function to dirctions for turtle
   turtle_diction( "Sea Green")

   
# set up dirctions for turtle to draw sing
   pencolor("Salmon")
   width (10)
   setheading(-45)
   forward(width_card //2)

# sing loop to give turtle angel info
   for sing in range (3):
       
       circle(width_card //3 , 60)
       left(120)
       circle(width_card //3 , 60)
       left(360)
       
# to draw final line        
   setheading(-45)
   forward(width_card //2.5)
     
# make sure the pen up for next card
   penup()
   setheading(90)
   left(70)
   forward(width_card - 25)  




 

def House_of_Lannister ():
# function drawing house of Lannister cards

# calling function to draw backgroung
   background_card()
    
# calling function to dirctions for turtle
   turtle_diction( "Maroon")


# set up dirctions for turtle
   penup()
   pencolor("Salmon")
   setheading(-90)
   forward(width_card //2)
   
# start to draw crown
   color("Navy")
   begin_fill()
   
# botoom line 
   setheading(0)
   pendown()
   forward(width_card //1.5)
# line on right 
   setheading(95)
   forward(width_card //2.5)
   
# first crown angle
   left(-45)
   forward(-width_card //4 )
   
   setheading(90)
   forward(width_card //4)

# sec crown angle
   left(-35)
   forward(-width_card //3.5 )
   
   setheading(95)
   forward(width_card //4)
   
# third crown angle
   left(-35)
   forward(-width_card //3.5 )
   
   setheading(100)
   forward(width_card //4)
   
# fourth crown angle 
   left(-40)
   forward(-55 )
   end_fill()
  
   setheading(-80)
   forward(width_card //4)

# make sure the pen up for next card
   penup() 
   setheading(0)
   right(55)
   forward(-width_card //3.5)

   
def joker ():
# function drawing house of Martell cards

# calling function to draw backgroung
   background_card("LIGHT PINK")
   
# set location to stast drawing    
   penup()
   setheading(-45)
   forward(height_card //3.5)    
   left(-90)
   pendown()
# drawing boarder of circles in one location  
   pencolor("Firebrick")
   width (6)
   pendown()
   list_radusi = [2.5 ,3 ,3.5 ,4, 4.5]
   for muti_circle in list_radusi :
      circle(width_card // muti_circle)
      
# drawing stars listructors

   pencolor("Dark salmon")
   width (4)
   right(-85)
   penup()
   forward(40)
   pendown()
   for stars in range (16):
       forward (stars *10)
       right(144)
# make sure the pen up for next card
   penup() 
   setheading(0)
   right(180)
   forward(width_card //1.5)

  

def track_of_cards(num_cards):
# function write numer in cards
   penup()
# list contain number that will be on cards
   tracker_number = ['2','3','4','5','6','7','8','9','10','J','Q','K']

   color("black")
   previous_number = num_cards 
   setheading(90)
   for track in range (num_cards  ):
       
       write((tracker_number[track]),'left',font=('arial',14))
       write_upside_down(tracker_number[track])
       forward(-height_card // 2.3)

       
def which_Stack (num_stack):
 # function help trutle to locate stack
 
    penup()
    if num_stack == 'Stack 1':
        goto(-545 , 375)
        
    elif num_stack == 'Stack 2':
         goto(-340 , 375)
        
    elif num_stack == 'Stack 3':
         goto(-150 , 375)
        
        
    elif num_stack == 'Stack 4':
          goto(0 , 375)

    elif num_stack == 'Stack 5':
          goto(200 , 375)

    elif num_stack == 'Stack 6':
          goto(380 , 375)
        
        

def which_suit (suit):
 # function help trutle to know suit
 
    if suit == 'Suit A':
        house_of_Martell()

    elif suit == 'Suit B':
        house_of_Clegane()
                 
    elif suit == 'Suit C':
        House_of_Tyrell ()
                 
    elif suit == 'Suit D':
        House_of_Lannister ()
        

        
   

def deal_cards(fixed_game_0):
       
# test which four type of card to draw

     list_of_instructions = []
     list_of_instructions = fixed_game_0
     
#  for instruct in element     
     for element in list_of_instructions:
    
         which_Stack (element[0])
         if element[2] > 0 :
             
             for repet_num in range (element[2]):
                 which_suit (element[1])
                 penup()
                 setheading(-90)
                 
     for element in list_of_instructions:
    
         which_Stack (element[0])
         setheading(-90)
         forward(20)
         if element[2] > 0 :
            
             track_of_cards(element[2])
             penup()
                 
         
         
                 
                
                 
                
             
 
        
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing the card game.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and stack locations
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your cards' theme
title("GAME OF THRONES HOUSES CARDS")

### Call the student's function to draw the game
### ***** While developing your program you can call the deal_cards
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_game()" as the
### ***** argument to the deal_cards function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_game function.
#deal_cards(fixed_game_13) # <-- used for code development only, not marking
#deal_cards(full_game) # <-- used for code development only, not marking
deal_cards(random_game()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#

