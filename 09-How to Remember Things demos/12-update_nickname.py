#----------------------------------------------------------------
#
# Update nickname
#
# As an example of updating a database entry from within
# a program, this Python program allows the user to change the
# nickname associated with a superhero.
#
# Examples:
#
# 1) Try using this program to update Batman's 1960's
# nickname, the "The Caped Crusader", to the current day
# "Dark Knight".
#
# 2) The world's maddest mad scientist, Dr. Sivana,
# used to insultingly refer to his foe Captain Marvel as
# "The Big Red Cheese" but after a while this became an
# affectionate nickname used even by the Captain's friends.
# Update Captain Marvel's nickname in the database to
# reflect this change.
#
# Check that your changes worked by looking up the
# nicknames table in your preferred database GUI.
#

#-----
# Import the SQL functions
from sqlite3 import *

#----
# Create a connection to the database.
connection = connect(database = 'superheroes.db')

#-----
# Get a "cursor" pointing into the database of interest
hero_db = connection.cursor()

#-----
# Ask the user for whose nickname to change
superhero = input("Which superhero's nickname do you want to change? ")

#-----
# Check to see if the superhero has a nickname
hero_db.execute("SELECT COUNT(*) FROM nicknames WHERE superhero = '" + superhero + "'")

#-----
# If the superhero doesn't have a nickname do nothing, otherwise
# get the new nickname from the user and update the database
if hero_db.fetchone()[0] != 1:
    print('Sorry, but', superhero, 'does not have a nickname to change.')
else:
    # Get the new nickname
    new_nickname = input("What is " + superhero + "'s new nickname? ")
    # Protect any apostrophes in the nickname
    new_nickname = new_nickname.replace("'", "\\'")
    # Update the table
    hero_db.execute("UPDATE nicknames SET nickname = '" + new_nickname +
                    "' WHERE superhero = '" + superhero + "'")
    # Commit the new nickname to the database and tell the user
    connection.commit()
    print('Done!')

#-----
# Unlock the database
hero_db.close()
connection.close()
