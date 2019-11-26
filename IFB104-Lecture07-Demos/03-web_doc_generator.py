#---------------------------------------------------------------------
#
# Web document generator
#
# As a simple example of generating a web document using Python
# this program produces a GUI that allows the user to enter some
# text which is used as the basis of an HTML document which is
# written to a file.
#

# Import the Tkinter functions
from tkinter import *

# Get a function for accessing the system clock
from time import asctime

# HTML template, with blanks marked by asterisks
html_template = """<!DOCTYPE html>
<html>

  <head>

    <meta charset = 'UTF-8'>
  
    <title>***TITLE***</title>

  </head>

  <body>

      <h1>***TITLE***</h1>

      <p>***TEXT***</p>

      <p>This document generated automatically on ***TIME***</p>
  
  </body>

</html>
"""

# This is the function that generates the HTML document
def generate_html():
    # Get the document's title
    title = title_entry.get()
    # Get the document's text
    text = text_entry.get(0.0, END)
    # Strip off trailing newlines
    text = text.strip('\n')
    # Get the current time
    time = asctime()
    # Replace the blanks in the HTML template
    html_code = html_template.replace('***TITLE***', title)
    html_code = html_code.replace('***TEXT***', text)
    html_code = html_code.replace('***TIME***', time)
    # Write the HTML code to a Unicode text file
    html_file = open(title + '.html', 'w', encoding = 'UTF-8')
    html_file.write(html_code)
    html_file.close()


# Define a big, readable font and a background colour
big_font = ('Arial', 32)
bg_colour = 'orange'

# Create a window
grid_window = Tk()
grid_window['bg'] = bg_colour

# Give the window a title
grid_window.title('Simple Web Document Generator')

# Create the labels
title_label = Label(grid_window, text = 'Document title:',
                    font = big_font, bg = bg_colour)
title_label.grid(row = 1, column = 1)

text_label = Label(grid_window, text = 'Document text:',
                   font = big_font, bg = bg_colour)
text_label.grid(row = 2, column = 1)

# Create the text entry boxes
title_entry = Entry(grid_window, width = 20, font = big_font)
title_entry.grid(row = 1, column = 2, sticky = W, pady = 10, padx = 5)
title_entry.focus()

text_entry = Text(grid_window, width = 20, height = 5, font = big_font,
                  border = 2, relief = 'groove', wrap = WORD)
text_entry.grid(row = 2, column = 2, sticky = W, pady = 10, padx = 5)

# Create the "print" button
print_button = Button(grid_window, text = ' Print document ', font = big_font,
                      command = generate_html,
                      activeforeground = 'orange',
                      highlightbackground = bg_colour)
print_button.grid(row = 3, column = 2, sticky = W, pady = 10)

# Start the event loop
grid_window.mainloop()
