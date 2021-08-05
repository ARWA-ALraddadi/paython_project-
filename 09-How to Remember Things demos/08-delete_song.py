#----------------------------------------------------------------
#
# A simple Python program to modify a database:
# Deletes the 1978 AC/DC song "Whole Lotta Rosie" because
# it wasn't a hit at all - it didn't even get onto the charts!
#

#-----
# Import the SQL functions
from sqlite3 import *

#-----
# Create a connection to the database
connection = connect(database = 'countdown.db')

#-----
# Get a pointer into the database
countdown_db = connection.cursor()

#-----
# Execute an SQLite script to delete a row
sql = "DELETE FROM songs WHERE song_name = 'Whole Lotta Rosie'"
countdown_db.execute(sql)

#-----
# Confirm that it worked by printing the total
# number of rows affected
print('Number of rows deleted:', countdown_db.rowcount)

#-----
# Commit the change to the database
connection.commit()

#-----
# Close the database
countdown_db.close()
connection.close()
