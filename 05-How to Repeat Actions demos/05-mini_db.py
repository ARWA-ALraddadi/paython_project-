#----------------------------------------------------------------
#
# Demonstration - Processing data stored in lists
#
# Lists are a commonly-used, sequential "data structure" for
# temporarily storing related values.  By creating lists whose
# elements are themselves lists we can store data in all sorts
# of ways.
#
# This demonstration shows how a "data base" of information,
# stored as a list of lists, can be processed in various ways.
#

#-----
# The list below is our so-called "data base" containing
# basic information about certain fictional individuals,
# specifically their name, age and address.  (The addresses
# are believed to be canonical, but some of the ages below
# are speculative.)
#
mini_db = [['Fred Flintstone',         40, '1313 Cobblestone Way, Bedrock, USA'],
           ['Hercule Poirot',          55, 'Apt. 56B, Whitehaven Mansions, Sandhurst Sq., London, UK'],
           ['Sherlock Holmes',         45, '221B Baker Street, London, UK'],
           ['Lily Munster',           156, '1313 Mockingbird Lane, Mockingbird Heights, USA'],
           ['Marcia Brady',            16, '4222 Clinton Way, Los Angeles, California, USA'],
           ['Fox Mulder',              36, '2630 Hegal Place, Apt. 42, Alexandria, Virginia, USA'],
           ['Clark Kent',              35, '344 Clinton St., Apt. 3B, Metropolis, USA'],
           ['Alice Kramden',           37, '328 1/2 Chauncey Street, Brooklyn, New York, USA'],
           ['Jane Marple',             65, 'Danemead, High Street, St Mary Mead, UK'],
           ['Lucy Ricardo',            34, 'Apartment 4A, 623 East 68th Street, New York, USA'],
           ['Basil Fawlty',            45, 'Fawlty Towers Hotel, Torquay, Torbay, UK'],
           ['Donald Duck',             30, '1313 Webfoot Walk, Duckburg, Calisota, USA'],
           ['Daria Morgendorffer',     16, '1111 Glen Oaks Lane, Lawndale, USA'],
           ['Samantha Stephens',      400, '1164 Morning Glory Circle, Westport, Connecticut, USA'],
           ['Jeannie',               2000, '1020 Palm Drive, Cocoa Beach, FL, USA'],
           ['Bart Simpson',            10, '742 Evergreen Terrace, Springfield, USA'],
           ['Ellie-Mae Clampett',      17, '518 Crestview Drive, Beverly Hills, California, USA'],
           ['Richie Cunningham',       17, '565 North Clinton Drive, Milwaukee, WI, USA'],
           ['Keith Partridge',         18, '698 Sycamore Road, San Pueblo, CA, USA'],
           ['SpongeBob SquarePants',   15, '124 Conch Street, Bikini Bottom, Pacific Ocean']]

           
#-----
# We can print out each of the lists in the "mini database" very
# easily
#
print('Each list in the database ...')

for entry in mini_db:
    print(entry)

print()


#-----
# To print out just one element of each list, we can index the
# individual lists as follows
#
print('Just the names ...')

for entry in mini_db:
    print(entry[0])

print()


#-----
# A better way of extracting particular items from the nested lists
# is to assign them to separate variables
#
print('Just the addresses ...')

for entry in mini_db:
    name, age, address = entry
    print(address)

print()


#-----
# An even shorter way of doing this is as follows
#
print('Just the ages ...')

for name, age, address in mini_db:
    print(age)

print()


#-----
# Normally we want to take some conditional action based
# on the particular "database" entry
#
print('Names of people older than 50 ...')

for name, age, address in mini_db:
    if age > 50:
        print(name)

print()


#-----
# Finally, as a more complicated example, we can accumulate
# information as we iterate through the values in the
# list
#

# Create some initial dummy results to get started
youngest = ['dummy', 1000000, 'dummy']
oldest = ['dummy', 0, 'dummy']

for entry in mini_db:
    age = entry[1]
    if age < youngest[1]:
        youngest = entry
    elif age > oldest[1]:
        oldest = entry

print('The youngest person in the database is', youngest[0], 'who is', youngest[1], 'years old')
print('The oldest person in the database is', oldest[0], 'who is', oldest[1], 'years old')

# (What would happen if more than one person had the same youngest/oldest age?)
