#----------------------------------------------------------------
#
# A simple Python program to access a database:
# Retrieves and displays the number of distinct
# songs in the Countdown database.
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

#----
# Execute an SQL script, a query in this case which
# counts the number of results returned when we select
# all columns and rows
countdown_db.execute('SELECT COUNT(*) FROM hits')

#-----
# Retrieve the first row from the result set produced by the query.
# Each "fetch" operation returns a row from the results (only
# one in this case)
row = countdown_db.fetchone()

#----
# Display the first value in the row
print ('Number of songs:', row[0])

#----
# Release the database "cursor"
countdown_db.close()

#----
# Unlock the database connection so that other
# people can connect to it.  NB: If this program
# crashes before this statement is executed the
# database will become inaccessible!
connection.close()
