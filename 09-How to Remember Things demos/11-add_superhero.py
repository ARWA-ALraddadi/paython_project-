#---------------------------------------------------------
#
# Add a new superhero to the database
#
# As an example of a Python program that provides an
# interface to a database, this program allows you to
# add new superheroes to the Superhero database.  It
# provides a simpler interface for the user than manually
# updating relevant tables using the DB Browser or a
# similar generic GUI.
#
# Having loaded the Superhero database dump, try
# running this program to insert the following data
# about two new superheroes.  Note that data is not
# available about all tables in the database.  For
# instance, we have said nothing about The Flash's
# friends.  The program allows for optional data such
# as this, but it assumes that all superheroes have a
# name, nickname and secret identity, so these must
# be provided.
#
# Name: The Flash
# Birthdate: 1940
# Nickname: The Fastest Man Alive
# Secret identity: Jay Garrick
# Powers and abilities: Super speed
# Friends and allies: Joan Williams
# Foes: The Rival, The Fiddler, The Shade, The Thinker
#
# Name: Robin
# Birthdate: 1940
# Nickname: The Boy Wonder
# Secret identity: Dick Grayson
# Friends and allies: Alfred Pennyworth
# Foes: The Riddler, The Joker, The Penguin, Catwoman
#


#-----
# Import the SQL functions
from sqlite3 import *


#-----
# Prompt the user for all the facts we need about the
# new superhero
superhero = input("What is the superhero's name? ")
birthdate = input("In which year was " + superhero + " created? ")
nickname = input("What is " + superhero + "'s nickname? ")
secret_id = input("What is " + superhero + "'s secret identity? ")
real_name = input("What is " + superhero + "'s 'real' identity, " +
                      "if different from his/her secret identity? ")
powers = input("List " + superhero + "'s powers and abilities, " +
                   "separated by commas: ")
friends = input("List " + superhero + "'s friends and allies, " +
                   "separated by commas: ")
enemies = input("List " + superhero + "'s foes, " +
                   "separated by commas: ")


#----
# Create a connection to the database.
connection = connect(database = 'superheroes.db')


#-----
# Get a "cursor" pointing into the database of interest
hero_db = connection.cursor()


#-----
# Insert each new row into the appropriate table, and tell
# the user whether or not the database operation succeeded;
# we assume *all* superheroes have a name, birthdate, nickname
# and secret identity but the other fields are optional
print()
template = "INSERT INTO identities VALUES ('HERO', 'IDENT', null)"
sql_statement = template.replace('HERO', superhero).replace('IDENT', secret_id)
hero_db.execute(sql_statement)
print(superhero + "'s secret identity was added to the database")

template = "INSERT INTO birthdates VALUES ('HERO', YEAR)"
sql_statement = template.replace('HERO', superhero).replace('YEAR', birthdate)
hero_db.execute(sql_statement)
print(superhero + "'s birthdate was added to the database")

template = "INSERT INTO nicknames VALUES ('HERO', \"NICKNAME\")" # there may be apostrophes in the nickname
sql_statement = template.replace('HERO', superhero).replace('NICKNAME', nickname)
hero_db.execute(sql_statement)
print(superhero + "'s nickname was added to the database")

if real_name != '': 
    template = "UPDATE identities SET real_name = 'REALNAME' WHERE superhero = 'HERO'"
    sql_statement = template.replace('HERO', superhero).replace('REALNAME', real_name)
    hero_db.execute(sql_statement)
    print(superhero + "'s real name was added to the database")

if powers != '':
    template = "INSERT INTO powers_and_abilities VALUES ('HERO', 'POWER')"
    # Insert each of the comma-separated powers
    for power in powers.split(','):
        sql_statement = template.replace('HERO', superhero)
        sql_statement = sql_statement.replace('POWER', power.strip())
        hero_db.execute(sql_statement)
    print(superhero + "'s powers and abilities were added to the database")

if friends != '':
    template = "INSERT INTO allies VALUES ('FRIEND', 'HERO')"
    # Insert each of the comma-separated friends
    for friend in friends.split(','):
        sql_statement = template.replace('HERO', superhero)
        sql_statement = sql_statement.replace('FRIEND', friend.strip())
        hero_db.execute(sql_statement)
    print(superhero + "'s friends were added to the database")
    
if enemies != '':
    template = "INSERT INTO enemies VALUES ('ENEMY', 'HERO')"
    # Insert each of the comma-separated enemies
    for enemy in enemies.split(','):
        sql_statement = template.replace('HERO', superhero)
        sql_statement = sql_statement.replace('ENEMY', enemy.strip())
        hero_db.execute(sql_statement)
    print(superhero + "'s enemies were added to the database")


#-----
# Commit the changes to the database
connection.commit()


#-----
# Close the cursor and release the server connection
hero_db.close()
connection.close()
