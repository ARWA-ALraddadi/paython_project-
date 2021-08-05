#----------------------------------------------------------------
#
# As an example of updating a database table from within
# a program, this Python program inserts new rows into
# the "songs" table from the Countdown database.
#
# (The data in one of the new rows is incorrect! We will
# fix this in a later demo.)
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
# Execute an SQLite script to insert rows
sql = """
INSERT INTO songs VALUES
    ('Nothing Stays the Same Forever', 1977, 'Hush'),
    ("Let's Spend the Night Together", 1987, 'Supernaut')
"""
countdown_db.execute(sql)

#-----
# Show that it worked by printing how many rows changed
print('Number of rows inserted:', countdown_db.rowcount)

#-----
# Commit the changes to the database
connection.commit()

#-----
# Close the database
countdown_db.close()
connection.close()
