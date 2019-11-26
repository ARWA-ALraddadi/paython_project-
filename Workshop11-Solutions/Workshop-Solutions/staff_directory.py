#--------------------------------------------------------------------#
#
# Staff Directory Front-End
#
# This is the front-end of the staff directory application. It
# creates a Graphical User Interface which can be used with any
# of the back-end functions.
#

# Import the Tkinter functions
from tkinter import *

# Import one of the back-end functions (uncomment whichever
# back-end module below you wish to use)

from backend_strings import find_employees # Char string version
#from backend_db import find_employees # SQLite version
#from backend_regex import find_employees # Regex version


#--------------------------------------------------------------------#
# Function to find and display the list of employees, if any. 
# (The optional 'event' parameter allows this function to be
# the target of a key binding.)
#
def show_employees(event = None):
    # Clear the results box
    results.delete(0.0, END)
    # Get the name to search for
    name_prefix = name.get()
    # Call the back-end function to get the list of matching employees
    matches = find_employees(name_prefix)
    # Display the results, if any
    if len(matches) == 0:
        results.insert(END, 'No matching employees found')
    else:
        for emp_no, first_name, last_name, birth_date in matches:
           results.insert(END, emp_no + ': ' + first_name + ' ' + \
                          last_name + ' (' + birth_date + ')\n')

        
#----------------------------------------------------------------#
# The GUI front end
#

# Create a window
staff_window = Tk()

# Give the window a title
staff_window.title('Staff Directory')

# Just for fun, create a label widget with the app's logo
reader_image = PhotoImage(file = "staff-directory.gif")
reader_logo = Label(staff_window, image = reader_image)
reader_logo.grid(row = 0, column = 0, rowspan = 4)

# Create a text area widget to display the results
results = Text(staff_window, width = 36, height = 12,
                    wrap = WORD, bg = 'light grey', font = ('Arial', 22),
                    borderwidth = 2, relief = 'groove',
                    takefocus = False)
results.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)

# Create a label widget for the text entry field
enter_prefix = Label(staff_window, text = "Employee name:", font = ('Arial', 22))
enter_prefix.grid(row = 1, column = 1, sticky = E)

# Create a text entry widget for the employee name, with the initial
# text in the box preselected for replacement and made the
# default "focus" for keyboard entry when the window is selected
name = Entry(staff_window, font = ('Courier', 20), width = 16)
name.grid(row = 1, column = 2, sticky = W)
name.selection_range(0, END)
name.focus()

# Create a button widget to start the search
search_button = Button(staff_window, text = ' Find employees ',
                       font = ('Arial', 22),
                       takefocus = FALSE, command = show_employees)
search_button.grid(row = 3, column = 1, columnspan = 2, pady = 5)

# Allow users to start the search by typing a carriage return
staff_window.bind('<Return>', show_employees)

# Start the event loop
staff_window.mainloop()

#
#--------------------------------------------------------------------#

