#----------------------------------------------------------------
#
# As an example of updating a database entry from within
# a program, this Python program changes a cell in the
# Countdown database.
#
# The problem is that the year of release for Supernaut's cover
# of the Rolling Stones' "Let's Spend the Night Together" is
# wrong.  It should be 1977 not 1987.  This program corrects
# this error in the database.
#

#-----
# Import the SQL functions
from sqlite3 import *

#-----
# Create a connection to the database.
connection = connect(database = 'countdown.db')

#-----
# Get a pointer into the database.
countdown_db = connection.cursor()

#-----
# Execute an SQL script, an update statement in this case
countdown_db.execute("""
UPDATE songs SET year_released = 1977
WHERE song_name = "Let's Spend the Night Together"
""")

#-----
# Confirm that it worked by printing the number of rows affected
print('Number of rows updated:', countdown_db.rowcount)

#-----
# Commit the change to the database
connection.commit()

#-----
# Close the database
countdown_db.close()
connection.close()
