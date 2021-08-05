#----------------------------------------------------------------
#
# As an example of accessing a database table from
# within a program, this Python program prints all rows
# in the table "singers" from the Countdown database.
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
# Execute an SQL script, a query in this case
countdown_db.execute('''SELECT * FROM singers
                        ORDER BY lead_singer ASC''')

#-----
# Fetch and print the list of rows returned
for row in countdown_db.fetchall():
    print (row[1] + ' (' + row[0] + ')')

#-----
# Close the database
countdown_db.close()
connection.close()
