#----------------------------------------------------------------
#
# An automated superhero fan
#
# As an example of a program that queries a database in various
# ways, this Python program interacts with the Superhero database
# to automatically generate answers to a number of important
# questions about superheroes.
#


#-----
# Import the SQL functions
from sqlite3 import *

#----
# Create a connection to the database.
connection = connect(database = 'superheroes.db')

#-----
# Get a cursor on the database
hero_db = connection.cursor()

#-----
# Print a welcoming message
print("Hello, I'm the Superhero Fan!")
print()
hero_db.execute("SELECT COUNT(*) FROM identities")
print("I know everything there is to know about", hero_db.fetchone()[0], "superheroes!")
print("Since we'll be sitting next to each other during this three")
print("hour cruise, let me tell you all about them!")
print()

#-----
# Do a simple lookup of the value associated with a primary key
hero_db.execute("SELECT secret_identity FROM identities WHERE superhero = 'Batman'")
real_name = hero_db.fetchone()[0]
print("Did you know that Batman's secret identity is '" + real_name + "'?")
print()

#-----
# Do a lookup by sorting rows based on a numeric field
hero_db.execute("SELECT superhero FROM birthdates ORDER BY birthdate ASC")
oldest_hero = hero_db.fetchone()[0]
print("Did you know the first superhero created was '" + oldest_hero + "'?")
print()

#-----
# Print a list of bad guys in the database in alphabetical
# order, avoiding duplicates
print("Did you know that the following people are supervillains?")
hero_db.execute("SELECT DISTINCT enemy FROM enemies ORDER BY enemy")
for row in hero_db.fetchall():
    print(' ', row[0])
print()

#-----
# Search for data values having a specific property
print("Did you know that the following superheroes are really strong?")
hero_db.execute('''SELECT DISTINCT superhero FROM powers_and_abilities
                   WHERE power LIKE '%strength%' OR
                         power LIKE '%power%' ''')
for row in hero_db.fetchall():
    print(' ', row[0])
print()

#-----
# Join two tables together via their primary key to relate enemies to
# allies via superheroes
hero_db.execute('''SELECT enemy, enemies.superhero, friend
                   FROM enemies, allies
                   WHERE enemies.superhero = allies.superhero''')
for row in hero_db.fetchall():
    enemy, hero, friend = row
    print('Did you know that ' + enemy + ' hates ' + friend + ' because ' + \
          friend + ' likes ' + hero + '?')
print()

#-----
# Print a closing message
print("Did you know ... Hey, where are you going?")
print("There's lots more I can tell you!")

#------
# Unlock the database
hero_db.close()
connection.close()
