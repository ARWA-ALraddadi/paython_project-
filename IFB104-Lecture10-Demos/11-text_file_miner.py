#-----Description----------------------------------------------------#
#
#  TEXT FILE MINER
#
#  This program provides a Graphical User Interface that allows
#  the user to "mine" a text file for interesting text patterns
#  using Regular Expressions.  This version does not support
#  multiline mode.
#
#--------------------------------------------------------------------#



#-----Some Example Search Terms--------------------------------------#
#
# Here are some interesting search terms to try in the
# Jekyll and Hyde HTML document
#
# Things described as strange: [Ss]trange +[a-zA-Z]+
# People with titles: [DM]r\. +[A-Za-z]+
# Mr. Hyde's first name: [A-Z][a-z]* *Hyde
# Dr. Jekyll's full name: Dr\. +[A-Z][a-z]* +Jekyll
# Questions asked by characters in the book: "[A-Z][a-z ]*\?"
# Exclamations: "[A-Z][a-z ]*!"
# Sentences mentioning blood: [A-Z][A-Za-z,;\- ]*blood[A-Za-z,;\- ]*[\.!\?]
# Emphasised words: <i>([^<]*)</i>
# HTML MarkUp tags used: <([a-zA-Z\-_]+)
#
#--------------------------------------------------------------------#



#-----Main program------------------------------------ --------------#
#
#

# Import the necessary regular expression function
from re import findall

# Import the Tkinter functions
from tkinter import *

# Create a window
regex_window = Tk()

# Give the window a title
regex_window.title('Text File Miner')

# Just for fun, create a label widget with the "miner" logo
miner_image = PhotoImage(file = "TextMinerLogo.gif")
miner_logo = Label(regex_window, image = miner_image)
miner_logo.grid(row = 0, column = 0)

# Create a text area widget to display the results
instructions = '''Enter your file name and regular expression below

Results are displayed here, within single quotes'''
results_text = Text(regex_window, width = 45, height = 8,
                    wrap = WORD, bg = 'light grey', font = ('Arial', 16),
                    borderwidth = 2, relief = 'groove',
                    takefocus = False)
results_text.insert(0.0, instructions)
results_text.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)

# Create label widgets for the two text entry fields
enter_name = Label(regex_window, text = 'File name:')
enter_name.grid(row = 1, column = 1, sticky = E)

enter_regex = Label(regex_window, text = 'Regular expression:')
enter_regex.grid(row = 2, column = 1, sticky = E)

# Create a text entry widget for the file name, with the initial
# text in the box preselected for replacement and made the
# default "focus" for keyboard entry when the window is selected
file_name = Entry(regex_window, font = ('Courier', 14), width = 30)
file_name.grid(row = 1, column = 2, sticky = W)
file_name.selection_range(0, END)
file_name.focus()

# Create a text entry widget for the regular expression, with
# the text in the field preselected for replacement if you
# 'tab' into the box
reg_exp = Entry(regex_window, font = ('Courier', 14), width = 30)
reg_exp.grid(row = 2, column = 2, sticky = W)
reg_exp.selection_range(0, END)

# Function to find and display results.  This version has
# been made robust to user error, through the use of
# exception handling (a topic we'll cover later).
# The optional 'event' parameter allows this function to be
# the target of a key binding.
def find_matches(event = None):
    try:
        # Open the file, if possible
        file_contents = open(file_name.get(), 'U').read()
        
        results_text.delete(0.0, END)
        try:
            # Get the results, delete duplicates, and sort
            results = sorted(set(findall(reg_exp.get(), file_contents)))
            # Display the results, if any
            if len(results) == 0:
                results_text['bg'] = 'orange'
                results_text.insert(END, 'No matches found\n')
            else:
                # results_text.config(height = len(results)) # resize results window
                results_text['bg'] = 'light green'
                for result in results:
                    results_text.insert(END, "'" + result + "'\n")
        except: # malformed regular expression
            results_text.delete(0.0, END)
            results_text['bg'] = 'red'
            results_text.insert(END, 'Invalid regular expression\n')            
    except: # couldn't open the file
        results_text.delete(0.0, END)
        results_text['bg'] = 'red'
        results_text.insert(END, 'File not found\n')

# Create a button widget to start the search
search_button = Button(regex_window, text = ' Search ',
                       activeforeground = 'red',
                       takefocus = FALSE, command = find_matches)
search_button.grid(row = 3, column = 1, columnspan = 2, pady = 5)

# Allow users to start the search by typing a carriage return
regex_window.bind('<Return>', find_matches)

# Start the event loop
regex_window.mainloop()

#
#--------------------------------------------------------------------#

