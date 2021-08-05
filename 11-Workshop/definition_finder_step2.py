#-----Description----------------------------------------------------#
#
#  Definition Finder (Step 2)
#
#  Given a word, this program displays the corresponding definition
#  from "The Foolish Dictionary" by Gideon Wurdz (1904).  This is
#  the complete system, integrating the front-end GUI with the
#  back-end search function.  To integrate the results of the
#  previous steps you must do the following.
#
#  a) Modify the back-end function so that instead of accepting
#     the word as a parameter it gets the word from the text Entry
#     widget.
#
#  b) Modify the back-end function so that instead of printing the
#     definition it inserts it into the appropriate GUI Text widget.
#
#  Time permitting you may also want to make other improvements to
#  the integrated system, such as the following.
#
#  c) Make the back-end function robust to the possibility that
#     the text file containing the dictionary can't be opened.
#
#  d) Extend the GUI so that the user can initiate a search by
#     hitting the 'Enter' key, as well as pushing the button.
#
#--------------------------------------------------------------------#


# Import the necessary regular expression functions
from re import findall, sub

# Import the Tkinter functions
from tkinter import *


#--------------------------------------------------------------------#
# Back-end function to find and display the definition, if any. 
# (The optional 'event' parameter allows this function to be
# the target of a key binding.)
#
def show_definition(event = None):
    try:
        # Open and read the file containing the dictionary
        dictionary = open('TheFoolishDictionary_GideonWurdz_1904.txt').read()
        # Clear the definition box
        definition.delete(0.0, END)
        # Get the word to search for, converted to upper case
        search_term = word.get().upper()
        # Search for the definition, assuming the word of interest is
        # surrounded by equals signs and the definition ends either at
        # the next equals sign or an asterisk
        results = findall('=' + search_term + '=[ \n]([^=*]*)', dictionary)
        # Display the unique definition, if any
        if len(results) != 1:
            definition.insert(END, 'This word does not appear in the dictionary!')
        else:
            text = results[0]
            text = text.replace('\n', ' ') # Remove line breaks
            text = text.strip() # Remove leading and trailing spaces
            text = sub(' +', ' ', text) # Eliminate multiple spaces
            definition.insert(END, text)
    except:
        # Couldn't open the file
        definition.delete(0.0, END)
        definition.insert(END, 'Could not open the dictionary!')

        
#----------------------------------------------------------------#
# The GUI front end
#

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
search_button = Button(dictionary_window, text = 'Find definition',
                       takefocus = FALSE, command = show_definition)
search_button.grid(row = 3, column = 1, columnspan = 2, pady = 5)

# Allow users to start the search by typing a carriage return
dictionary_window.bind('<Return>', show_definition)

# Start the event loop
dictionary_window.mainloop()

#
#--------------------------------------------------------------------#

