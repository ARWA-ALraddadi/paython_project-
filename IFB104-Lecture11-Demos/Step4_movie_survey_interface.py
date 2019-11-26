#----------------------------------------------------------------
#
# Movie Survey Interface
#
# This is the final "IT System", integrating the improved GUI,
# as delivered to the (grateful and highly satisfied) customer.
#


#----------------------------------------------------------------
# Unit tests for the back-end functions (assuming we are using
# the Movie Survey database dumped on 2013-09-14 18:45:55).
# These tests do not check any exception handling behaviour.
#
"""
To save space, we just print the first part of the results in the
first two tests

>>> print(popular_actors()[:222])
859: Tom Hanks
598: Harrison Ford
547: Robert DeNiro
503: Al Pacino
483: Sean Connery
416: Tom Cruise
410: Mel Gibson
381: Nicolas Cage
376: Julia Roberts
348: Denzel Washington
319: Jodie Foster
309: Arnold Schwarzenegger

>>> print(productive_actors()[:194])
John Wayne (62)
Dennis Hopper (60)
Gene Hackman (59)
Christopher Lee (55)
Samuel L. Jackson (55)
Christopher Walken (54)
Alec Baldwin (53)
Harvey Keitel (53)
Clint Eastwood (52)
James Woods (52)

>>> print(actors_starring_in_a_movie('Arsenic and Old Lace'))
Cary Grant
Peter Lorre

>>> print(actors_starring_in_a_movie('The Great Race'))
Jack Lemmon
Natalie Wood
Peter Falk
Tony Curtis

>>> print(actors_starring_in_a_movie('Unmade Movie'))
No actors found

>>> print(movies_starring_an_actor('Natalie Wood'))
Bob & Carol & Ted & Alice
Gypsy
Kings Go Forth
Marjorie Morningstar
Meteor
Miracle on 34th Street
Rebel Without a Cause: Special Edition
Splendor in the Grass
The Ghost and Mrs. Muir
The Great Race
The Star
This Property Is Condemned
West Side Story

>>> print(movies_starring_an_actor('Lillian Gish'))
Broken Blossoms
Commandos Strike at Dawn
Duel in the Sun
Follow Me
Orphans of the Storm
Portrait of Jennie
Sweet Liberty
The Birth of a Nation
The Night of the Hunter
The Unforgiven
The Whales of August
Way Down East

>>> print(movies_starring_an_actor('Joe Unknown'))
No movies found
"""


#----------------------------------------------------------------
# A function to support unit testing of the back-end
# functions.  Make sure you run this whenever any change
# is made to the back-end functions!
#
def run_unit_tests():
    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
    print(testmod(verbose = False,
                  optionflags = REPORT_ONLY_FIRST_FAILURE))


#----------------------------------------------------------------
# Import necessary external modules
#

# Import the Tkinter functions
from tkinter import *

# Import the SQLite functions
from sqlite3 import *


#----------------------------------------------------------------
#
# These are the back-end functions that access the database
# and process the results returned.  Each one returns a
# single string suitable for display in the front-end GUI.
# The signatures of these functions are the agreed-upon interface
# connecting the two development teams.
#

#-----
# Find all actors starring in a given movie
#
def actors_starring_in_a_movie(movie_name):
    try:
        # Connect to the "movie survey" database
        connection = connect(database='movie_survey.db')
        movies_db = connection.cursor()
        # Define an appropriate SQL query
        query = """SELECT actor FROM actors_movies
                   WHERE movie = '""" + movie_name + """'
                   ORDER BY actor"""
        # Initialise the results
        results = ''
        try:
            # Execute the query
            movies_db.execute(query)
            # Format the results, if any
            for row in movies_db.fetchall():
                results += row[0] + '\n'
            if results == '':
                results = 'No actors found'
            else:
                results = results[:-1] # delete final newline char
        except:
            # Something was wrong with the user's query
            results = 'Cannot process query\n\nPlease do not use apostrophes or other special characters'
        # Unlock the database
        movies_db.close()
        connection.close()
    except:
        # Something went wrong with accessing the database
        results = 'Unable to access Movie Survey database'
    # Return the results
    return results

#-----
# Find all movies starring a given actor
#
def movies_starring_an_actor(actors_name):
    try:
        # Connect to the "movie survey" database
        connection = connect(database='movie_survey.db')
        movies_db = connection.cursor()
        # Define an appropriate SQL query
        query = """SELECT movie FROM actors_movies
                   WHERE actor = '""" + actors_name + """'
                   ORDER BY movie"""
        # Initialise the results
        results = ''
        try:
            # Execute the query, if possible
            movies_db.execute(query)
            # Format the results, if any
            for row in movies_db.fetchall():
                results += row[0] + '\n'
            if results == '':
                results = 'No movies found'
            else:
                results = results[:-1] # delete final newline char
        except:
            # Something was wrong with the user's query
            results = 'Cannot process query\n\nPlease do not use apostrophes or other special characters'
        # Unlock the database
        movies_db.close()
        connection.close()
    except:
        # Something went wrong with accessing the database
        results = 'Unable to access Movie Survey database'
    # Return the results
    return results

#-----
# Return all actors in order of their "productivity", i.e., the
# number of movies the actors have appeared in.
#
def productive_actors():
    try:
        # Connect to the "movie survey" database
        connection = connect(database='movie_survey.db')
        movies_db = connection.cursor()
        # Define an appropriate SQL query
        query = """SELECT actor, number_of_movies FROM actors
                   ORDER BY number_of_movies DESC, actor ASC"""
        # Execute the query
        movies_db.execute(query)
        # Format the results, if any
        results = ''
        for row in movies_db.fetchall():
            results += row[0] + ' (' + str(row[1]) + ')\n'
        if results == '':
            results = 'No actors found'
        else:
            results = results[:-1] # delete final newline char
        # Unlock the database
        movies_db.close()
        connection.close()
    except:
        # Something went wrong with accessing the database
        results = 'Unable to access Movie Survey database'
    # Return the results
    return results

#-----
# Return all actors in order of their "popularity", measured by
# the number of people who voted for them in the movie survey.
#
def popular_actors():
    try:
        # Connect to the "movie survey" database
        connection = connect(database='movie_survey.db')
        movies_db = connection.cursor()
        # Define an appropriate SQL query
        query = """SELECT actor, count(actor) FROM favorite_actors
                   GROUP BY actor
                   ORDER BY count(actor) DESC, actor ASC"""
        # Execute the query
        movies_db.execute(query)
        # Format the results, if any
        results = ''
        for row in movies_db.fetchall():
            results += str(row[1]).rjust(3) + ': ' + row[0] + '\n'
        if results == '':
            results = 'No actors found'
        else:
            results = results[:-1] # delete final newline char
        # Unlock the database
        movies_db.close()
        connection.close()
    except:
        # Something went wrong with accessing the database
        results = 'Unable to access Movie Survey database'
    # Return the results
    return results



#----------------------------------------------------------------
#
# The front end main program which creates the GUI.
#

#-----
# These four functions interface to the back-end functions and
# display the results in the text area.  (There is a lot of
# duplicated code here!  In a future release these functions
# should be refactored to eliminate redundancy!)
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
# Define global constants
bg_colour = 'white'
box_colour = 'light grey'

#-----
# Define some large fonts for legibility
big_font = ('Arial', 24)
huge_font = ('Arial', 28)
#-----
# Create the main window
movie_survey = Tk()
movie_survey.configure(background = bg_colour)
movie_survey.title('Movie Survey Interface')

#-----
# Create the "cinema" image
star_image = PhotoImage(file = 'cinema-logo.gif')
Label(movie_survey, image = star_image, border = 1).\
                 grid(row = 0, column = 0, padx = 5, pady = 5,
                      sticky = E)

#-----
# Create a text field to display the results (NB: On Mac OS X
# this text box allows vertical scrolling with the mouse wheel
# but this feature hasn't been tested under Microsoft Windows)
results_text = Text(movie_survey, width = 33, height = 13,
                    wrap = WORD, bg = box_colour, font = big_font,
                    border = 0, state = NORMAL, takefocus = False)
results_text.grid(row = 0, column = 1, padx = 5, pady = 5,
                  sticky = W)

#-----
# Create a frame to hold the radiobuttons and text entry boxes defined below
buttons = Frame(movie_survey, background = bg_colour)
buttons.grid(row = 1, column = 0, columnspan = 2,
             pady = 8, padx = 5, sticky = E)

#-----
# Introduce a variable to link the radio buttons
button_chosen = StringVar()

#-----
# Define and position the radio buttons
Radiobutton(buttons, text = ' Most popular actors ', font = huge_font,
            variable = button_chosen, value = 'a', background = bg_colour,
            command = display_popular_actors, takefocus = False).\
            grid(row = 0, column = 0, sticky = W)
Radiobutton(buttons, text = ' Most productive actors ', font = huge_font,
            variable = button_chosen, value = 'b', background = bg_colour,
            command = display_productive_actors, takefocus = False).\
            grid(row = 1, column = 0, sticky = W)
Radiobutton(buttons, text = ' Movies starring....', font = huge_font,
            variable = button_chosen, value = 'c', background = bg_colour,
            command = display_movies_starring_an_actor, takefocus = False).\
            grid(row = 0, column = 1, sticky = W)
Radiobutton(buttons, text = ' Actors starring in..', font = huge_font,
            variable = button_chosen, value = 'd', background = bg_colour,
            command = display_actors_starring_in_a_movie, takefocus = False).\
            grid(row = 1, column = 1, sticky = W)

#-----
# Create a text entry field for the name of a movie star
actor = Entry(buttons, font = huge_font, justify = LEFT,
              width = 24, border = 0, background = box_colour,
              highlightbackground = bg_colour)
actor.grid(row = 0, column = 2, sticky = E)

#-----
# Create a text entry field for the name of a movie
movie = Entry(buttons, font = huge_font, justify = LEFT,
              width = 24, border = 0, background = box_colour,
              highlightbackground = bg_colour)
movie.grid(row = 1, column = 2, sticky = E)

#-----
# Start the event loop
movie_survey.mainloop()

