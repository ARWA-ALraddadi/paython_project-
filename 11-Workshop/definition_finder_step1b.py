#-----Description----------------------------------------------------#
#
#  Definition Finder - GUI Mock Up (Step 1b)
#
#  In this step your team will create a mock-up of the Graphical
#  User Interface for the definition finder.  It should have all
#  the necessary widgets and GUI functionality, but the back-end
#  search function will be just a stub.
#
#  The stub function has been provided below.  When called all it
#  does is print a message to the Python shell window to remind
#  the development team that this stub needs to be replaced.
#
#  Your team needs to implement the GUI front-end that calls this
#  stub.  The GUI must have at least the following features:
#
#  a) A Text widget to display the dictionary definition (or error
#     messages.
#
#  b) A text Entry widget to allow the user to type in the word
#     they want defined.
#
#  c) A Button widget which, when pressed, calls the back-end
#     "show_definition" function to search for and display the
#     definition from the dictionary (which, of course, won't
#     work until the stub is replaced).
#
#--------------------------------------------------------------------#


#--------------------------------------------------------------------#
# Back-end function to find and display the definition, if any. 
# TODO: This is just a stub!
#
def show_definition():
    print('FIXME: This is a stub for the back-end search function')

        
#----------------------------------------------------------------#
# The GUI front end
#

# Import the Tkinter functions
from tkinter import *

# Create a window
dictionary_window = Tk()

# Give the window a title
dictionary_window.title('The Foolish Dictionary')

# Just for fun, create a label widget with the app's logo
reader_image = PhotoImage(file = "definition_finder.gif")
reader_logo = Label(dictionary_window, image = reader_image)
reader_logo.grid(row = 0, column = 0)

# Create a text area widget to display the results
definition = Text(dictionary_window, width = 38, height = 8,
                    wrap = WORD, bg = 'light grey', font = ('Arial', 16),
                    borderwidth = 2, relief = 'groove',
                    takefocus = False)
definition.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)

# Create a label widget for the text entry fields
enter_word = Label(dictionary_window, text = "Word to define:")
enter_word.grid(row = 1, column = 1, sticky = E)

# Create a text entry widget for the file name, with the initial
# text in the box preselected for replacement and made the
# default "focus" for keyboard entry when the window is selected
word = Entry(dictionary_window, font = ('Courier', 14), width = 28)
word.grid(row = 1, column = 2, sticky = W)
word.selection_range(0, END)
word.focus()

# Create a button widget to start the search
search_button = Button(dictionary_window, text = 'Show definition',
                       takefocus = FALSE, command = show_definition)
search_button.grid(row = 3, column = 1, columnspan = 2, pady = 5)

# Start the event loop
dictionary_window.mainloop()

#
#--------------------------------------------------------------------#

