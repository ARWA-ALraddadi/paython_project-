#----------------------------------------------------------------
#
# GUI Prototype
#
# This program provides a basic version of the GUI front-end
# but
#
# a) no attempt has been made to make the interface attractive
#    or intuitive, and
#
# b) there are no back-end functions, so they have been
#    simulated via stubs.
#


#----------------------------------------------------------------
# Import necessary external modules
#

# Import the Tkinter functions
from tkinter import *


#----------------------------------------------------------------
#
# These stubs represent the intended behaviour of the back-end
# functions.  They have the same signatures as the real
# functions but always return fixed values.  They allow us
# to make progress on the GUI without waiting for the back-end
# functions to be completed.
#

#-----
# Find all actors starring in a given movie (STUB)
#
def actors_starring_in_a_movie(movie_name):
    return """Humphrey Bogart
Lauren Bacall
Harrison Ford
Woody Allen"""

#-----
# Find all movies starring a given actor (STUB)
#
def movies_starring_an_actor(actors_name):
    return """Star Wars
What's New Pussycat?
Goldfinger
The Towering Inferno
Diplomaniacs"""

#-----
# Return all actors in order of their "productivity" (STUB)
#
def productive_actors():
    return """John Wayne (45)
Errol Flynn (22)
Anna Lee (15)
Audrey Hepburn (8)"""

#-----
# Return all actors in order of their "popularity" (STUB)
#
def popular_actors():
    return """10: Boris Karloff
9: Christopher Lee
8: Lon Chaney, Jr
7: David Carradine
6: Bela Lugosi
5: Glenn Strange"""



#----------------------------------------------------------------
#
# The front end main program which creates the GUI.
#

#-----
# These four functions interface to the back-end functions and
# display the results in the text area.
#
def display_actors_starring_in_a_movie():
    results_text.delete(0.0, END)
    results_text.insert(END, actors_starring_in_a_movie(movie.get()))
    
def display_movies_starring_an_actor():
    results_text.delete(0.0, END)
    results_text.insert(END, movies_starring_an_actor(actor.get()))

def display_productive_actors():
    results_text.delete(0.0, END)
    results_text.insert(END, productive_actors())

def display_popular_actors():
    results_text.delete(0.0, END)
    results_text.insert(END, popular_actors())

#-----
# Define a large font for legibility
big_font = ('Arial', 22)

#-----
# Create the main window
movie_survey = Tk()

#-----
# Create a text field to display the results (NB: On macOS
# this text box allows vertical scrolling with the mouse wheel
# but this feature hasn't been tested under Microsoft Windows)
results_text = Text(movie_survey, width = 40, height = 6,
                    border = 1, relief = 'solid', font = big_font)
results_text.pack()

#-----
# Introduce a variable to link the radio buttons
button_chosen = StringVar()

#-----
# Define the radio buttons and text entry boxes
Radiobutton(movie_survey, text = 'Popular', font = big_font,
            variable = button_chosen, value = 'a',
            command = display_popular_actors).pack()

Radiobutton(movie_survey, text = 'Productive', font = big_font,
            variable = button_chosen, value = 'b',
            command = display_productive_actors).pack()

Radiobutton(movie_survey, text = 'Starring...', font = big_font, 
            variable = button_chosen, value = 'c',
            command = display_movies_starring_an_actor).pack()
actor = Entry(movie_survey, font = big_font)
actor.pack()

Radiobutton(movie_survey, text = ' Actors in...', font = big_font,
            variable = button_chosen, value = 'd',
            command = display_actors_starring_in_a_movie).pack()
movie = Entry(movie_survey, font = big_font)
movie.pack()

#-----
# Start the event loop
movie_survey.mainloop()

