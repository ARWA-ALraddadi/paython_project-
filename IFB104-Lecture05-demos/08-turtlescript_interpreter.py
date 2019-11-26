
#--------------------------------------------------------------------#
#
#  TURTLESCRIPT INTERPRETER
#
#  We've seen that Turtle graphics provides many primitive functions
#  for drawing simple images.  However, it would often be convenient
#  to have more expressive drawing commands.  As an example
#  of processing data stored as lists, in this demonstration we
#  develop a drawing function which can interpret lists consisting of
#  three types of instructions to draw a picture:
#
#  * ['jump to', [X, Y]] - goes to coordinate (X, Y) without drawing
#
#  * ['draw dot', D, C] - draws a dot at the current location of
#    diameter D and colour C, where C can be 'light' or 'dark'
#
#  * ['draw to', [X, Y], W, C] - draws a line from the current
#    location to coordinate (X, Y), of colour C, and width W, where
#    W can be 'thick' or 'thin'
#
#  Some simple examples of drawing scripts created from these commands
#  appear below.  In a separate module, turtlescripts.py, are some
#  more complicated examples.
#
#--------------------------------------------------------------------#



#-----Test Data------------------------------------------------------#
#
#  Below are some short "turtlescripts" that draw simple images.
#  More complicated scripts can be found in the separate module
#  turtlescripts.py.
#

# A script for drawing a game of noughts and crosses which
# has just started
tic_tac_toe = [
               ['jump to', [50, 150]],
               ['draw to', [50, -150], 'thick', 'light'],
               ['jump to', [-50, 150]],
               ['draw to', [-50, -150], 'thick', 'light'],
               ['jump to', [-150, 50]],
               ['draw to', [150, 50], 'thick', 'light'],
               ['jump to', [-150, -50]],
               ['draw to', [150, -50], 'thick', 'light'],
               ['jump to', [75, 125]],
               ['draw to', [130, 75], 'thin', 'dark'],
               ['jump to', [135, 125]],
               ['draw to', [75, 75], 'thin', 'dark'],
              ]

# A script for drawing the face of a die showing 3
die_3 = [# Draw the three dots
         ['draw dot', 100, 'light'],
         ['jump to', [100, 100]],
         ['draw dot', 100, 'light'],
         ['jump to', [-100, -100]],
         ['draw dot', 100, 'light'],
         # Draw the border
         ['jump to', [200, 200]],
         ['draw to', [-200, 200], 'thick', 'dark'],
         ['draw to', [-200, -200], 'thick', 'dark'],
         ['draw to', [200, -200], 'thick', 'dark'],
         ['draw to', [200, 200], 'thick', 'dark'],
         ]

# A script for drawing a smartphone
smartphone = [# Draw the outer edge
              ['jump to', [200, 100]],
              ['draw to', [200, -100], 'thick', 'dark'],
              ['draw to', [-200, -100], 'thick', 'dark'],
              ['draw to', [-200, 100], 'thick', 'dark'],
              ['draw to', [200, 100], 'thick', 'dark'],
              # Draw the screen
              ['jump to', [150, 90]],
              ['draw to', [150, -90], 'thin', 'light'],
              ['draw to', [-170, -90], 'thin', 'light'],
              ['draw to', [-170, 90], 'thin', 'light'],
              ['draw to', [150, 90], 'thin', 'light'],
              # Draw the camera
              ['jump to', [-185, 0]],
              ['draw dot', 10, 'light'],
              # Draw the home button
              ['jump to', [175, 0]],
              ['draw dot', 30, 'dark']              
              ]

#
#--------------------------------------------------------------------#



#-----Drawing function-----------------------------------------------#
#
#  This is the function which accepts a list of "instructions" as
#  its argument and uses them to draw an image.
#

from turtle import *
    
def draw(turtlescript):

    # Set up the drawing canvas
    title("TurtleScript Interpreter")
    bgcolor('light yellow')
    penup()

    # Define the default line widths and colours
    thin, thick = 3, 6
    light, dark = 'red', 'dark blue'
    
    # Follow each of the instructions in the given script
    for instruction in turtlescript:
        action = instruction[0] # extract the action to be performed
        if action == 'jump to': # move without drawing
            coords = instruction[1]
            penup()
            goto(coords)
        elif action == 'draw to': # move while drawing
            coords, line_width, line_colour = instruction[1], instruction[2], instruction[3]
            pendown()
            if line_width == 'thick':
                width(thick)
            else:
                width(thin)
            if line_colour == 'dark':
                pencolor(dark)
            else:
                pencolor(light)
            goto(coords)
        elif action == 'draw dot': # draw a dot at the current location
            diameter, colour = instruction[1], instruction[2]
            if colour == 'dark':
                pencolor(dark)
            else:
                pencolor(light)
            dot(diameter)
        else: # something's wrong with the script!
            print("Error: Unknown command '", action, "' ignored")

    # Close down the window
    hideturtle()
    done()

#
#--------------------------------------------------------------------#



#-----Main program---------------------------------------------------#
#
#  This main program calls the "draw" function to produce a picture.
#  Change the argument to use a different "turtlescript" list from
#  the set of tests above (or create one of your own!).
#
#  Also, the module turtlescripts.py, imported below, contains five
#  more complicated scripts.

from turtlescripts import riddle, enigma, mystery, puzzle, conundrum

draw(smartphone)

#
#--------------------------------------------------------------------#
