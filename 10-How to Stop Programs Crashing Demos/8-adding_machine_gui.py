######################################################################
##
##  Demonstration - Adding machine with GUI
##
##  The following example shows how an exception handler can be
##  used to recover gracefully from input errors
##
##  This is similar to the text-based "adding machine"
##  demonstration, but with the addition of a graphical user
##  interface
##


#---------------------------------------------------------------------
#
# Requirement:
#
# The aim is to define an easy-to-use adding machine that lets the
# user enter numbers with a subtotal displayed after each
#


#---------------------------------------------------------------------
#
# A robust implementation:
#
# The following program implements the requirement and additionally
# handles non-numerical input by alerting the user to the error
#

# Import the GUI API
from tkinter import *

# Initialise the running total
total = 0


#----------
# A back-end function to get the current number in the
# text entry field, add it to the total and display
# the result (or indicate to the user that the number
# is malformed in some way)
def add_to_total(event = None):
    global total
    try:
        total = total + int(next_number.get())
        total_display['text'] = total
        next_number['bg'] = 'white'
        next_number.delete(0, END) # clear the field for the next input
    except:
        next_number['bg'] = 'red'


#----------
# The GUI main program

# Create the interactive window
adding_window = Tk()
adding_window.title('Adding Machine')

# Create a label to display the current total
total_display = Label(adding_window, text = total,
                      font = ('Arial', 36))
total_display.pack()

# Create a text entry field for the user to enter numbers
next_number = Entry(adding_window, width = 6, justify = 'right',
                    font = ('Arial', 30))
next_number.pack(padx = 15)
next_number.focus()

# Create a button that adds to the total
add_button = Button(adding_window, text = ' Add ',
                    font = ('Arial', 28), activeforeground = 'red',
                    command = add_to_total)
add_button.pack(pady = 5)

# Allow users to add the next number by typing a carriage return
adding_window.bind('<Return>', add_to_total)

# Start the event loop to react to user inputs
adding_window.mainloop()
