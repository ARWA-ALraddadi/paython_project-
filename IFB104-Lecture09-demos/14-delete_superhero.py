#---------------------------------------------------------
#
# Delete a superhero from the database
#
# As another example of a program that allows the user
# to change the database, without using the MySQL
# Workbench, this program allows the user to delete a
# superhero, without the need to find all references to
# the superhero in each of the database's tables.  It
# thus clearly saves the user some effort.
#
# Example: Try deleting Superman from the database and
# then confirm that it worked by checking the database's
# contents using the "Superhero Fan" program or by
# examining it in your favourite GUI.
#


#-----
# Import the SQL functions
from sqlite3 import *

#-----
# Prompt the user for the superhero's name
superhero = input("Which superhero do you want to delete? ")

#----
# Create a connection to the database.
connection = connect(database = 'superheroes.db')

#-----
# Get a "cursor" pointing into the database of interest
hero_db = connection.cursor()

#-----
# Delete each row containing the superhero, and tell the
# user which tables were changed by checking the count of
# affected rows
template = "DELETE FROM identities WHERE superhero = 'HERO'"
sql_statement = template.replace('HERO', superhero)
hero_db.execute(sql_statement)
if hero_db.rowcount >= 1:
    print(superhero + "'s various identities deleted")

template = "DELETE FROM birthdates WHERE superhero = 'HERO'"
sql_statement = template.replace('HERO', superhero)
hero_db.execute(sql_statement)
if hero_db.rowcount >= 1:
    print(superhero + "'s birthdate deleted")

template = "DELETE FROM nicknames WHERE superhero = 'HERO'"
sql_statement = template.replace('HERO', superhero)
hero_db.execute(sql_statement)
if hero_db.rowcount >= 1:
    print(superhero + "'s nickname deleted")
    
template = "DELETE FROM powers_and_abilities WHERE superhero = 'HERO'"
sql_statement = template.replace('HERO', superhero)
hero_db.execute(sql_statement)
if hero_db.rowcount >= 1:
    print(superhero + "'s powers and abilities deleted")

template = "DELETE FROM allies WHERE superhero = 'HERO'"
sql_statement = template.replace('HERO', superhero)
hero_db.execute(sql_statement)
if hero_db.rowcount >= 1:
    print(superhero + "'s friendly relationships deleted")

template = "DELETE FROM enemies WHERE superhero = 'HERO'"
sql_statement = template.replace('HERO', superhero)
hero_db.execute(sql_statement)
if hero_db.rowcount >= 1:
    print(superhero + "'s hostile relationships deleted")

template = "DELETE FROM vulnerabilities WHERE superhero = 'HERO'"
sql_statement = template.replace('HERO', superhero)
hero_db.execute(sql_statement)
if hero_db.rowcount >= 1:
    print(superhero + "'s vulnerabilities deleted")

print('Done!')

#-----
# Commit the changes to the database
connection.commit()

#-----
# Release the database cursor and server connection
hero_db.close()
connection.close()
