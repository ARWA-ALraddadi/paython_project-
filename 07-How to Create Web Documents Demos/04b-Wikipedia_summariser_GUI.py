#----------------------------------------------------------------
#
# Wikipedia Summariser with GUI
#
# This program exploits the regular structure of Wikipedia web
# pages to produce a summary of the page's contents.  It extracts
# and displays the page's title, contents list, and modification
# time.  To do so, it relies on the presence of certain text
# patterns in the web page's HTML source code.
#
# This version adds a Graphical User Interface that allows the
# user to type the URL of the Wikipedia page of interest.  Some
# examples of URLs you could try are the following Harvey
# Comics character pages.  (These are some of the pages we
# used to test our program.)
#
# http://en.wikipedia.org/wiki/Baby_Huey
# http://en.wikipedia.org/wiki/Little_Lotta
# http://en.wikipedia.org/wiki/Little_Dot
# http://en.wikipedia.org/wiki/Wendy_the_Good_Little_Witch
# http://en.wikipedia.org/wiki/Hot_Stuff_the_Little_Devil
# http://en.wikipedia.org/wiki/Stumbo_the_Giant
#

 
#-----
# Import the necessary URL and Tkinter functions
from urllib.request import urlopen
from tkinter import *


#-----
# This function is called when the user types a carriage
# return
def summarise_page(event = None):

    # Extract the Wikipedia page's contents as a Unicode string
    wikipedia_page = urlopen(page_name.get())
    html_code = wikipedia_page.read().decode('UTF-8')
    wikipedia_page.close()

    # Clear the text area
    summary_text.delete(0.0, END)

    # Find and display the Wikipedia page's title, if possible
    start_marker = '<h1 id="firstHeading" class="firstHeading" lang="en">'
    end_marker = '</h1>'
    starting_position = html_code.find(start_marker)
    end_position = html_code.find(end_marker)
    if starting_position == -1 or end_position == -1:
        summary_text.insert(END, 'Error: Unable to find unique page title\n')
    else:
        summary_text.insert(END, html_code[starting_position + len(start_marker) : end_position].upper() + '\n')

    # Find and display the date when the page was last updated
    start_marker = '<li id="footer-info-lastmod"> '
    end_marker = ','
    starting_position = html_code.find(start_marker)
    end_position = html_code.find(end_marker, starting_position)
    if starting_position == -1 or end_position == -1:
        summary_text.insert(END, 'Error: Unable to find unique modification date')
    else:
        summary_text.insert(END, html_code[starting_position + len(start_marker) : end_position] + '\n\n')
        
    # Find and display the Wikipedia page's contents list, if any
    summary_text.insert(END, 'CONTENTS\n')
    start_marker = '<span class="toctext">'
    end_marker = '</span>'
    end_position = 0
    starting_position = html_code.find(start_marker, end_position)
    end_position = html_code.find(end_marker, starting_position)
    while starting_position != -1 and end_position != -1:
        summary_text.insert(END, '* ' + html_code[starting_position + len(start_marker) : end_position] + '\n')
        starting_position = html_code.find(start_marker, end_position)
        end_position = html_code.find(end_marker, starting_position)


#-----
# The main program that creates the GUI
#

# Create a window
wiki_window = Tk()

# Give the window a title
wiki_window.title('Wikipedia Summariser')

# Just for fun, create a label widget with a "little Wikipedia" logo
wiki_image = PhotoImage(file = "WikiSummaryLogo.gif")
wiki_logo = Label(wiki_window, image = wiki_image)
wiki_logo.grid(row = 0, column = 0, padx = 2, pady = 2)

# Create a text area widget to display the summary
summary_text = Text(wiki_window, width = 40, height = 12,
                    wrap = WORD, bg = 'light grey', font = ('Arial', 18),
                    borderwidth = 2, relief = 'groove',
                    takefocus = False)
summary_text.grid(row = 0, column = 1, padx = 2, pady = 2)

# Create a text entry widget for the URL, with some initial
# text in the box to save typing
page_name = Entry(wiki_window, font = ('Courier', 16), width = 44)
page_name.grid(row = 1, column = 1, padx = 2, pady = 4, sticky = W)
page_name.insert(0, 'http://en.wikipedia.org/wiki/Little_Dot') # Prefill the text box
page_name.focus()

# Allow users to get the summary by typing a carriage return
wiki_window.bind('<Return>', summarise_page)

# Start the event loop
wiki_window.mainloop()
