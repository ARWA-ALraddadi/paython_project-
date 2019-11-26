#----------------------------------------------------------------
#
# File reader
#
# In the previous demo we stored data as comma-separated
# values in a text file called 'birthdates.csv'.  This
# program recovers this data and prints it to the screen
# in a human-readable form, with each superhero's
# year of creation in brackets following their name.
#
# Importantly, however, we needed to know how the data had
# been stored in order to write this program successfully.
#

# Open the text file for reading
text_in = open('birthdates.csv', 'r')

# For each line in the file, delete the newline character
# at the end, split apart the commas-separated fields,
# and print them to the screen
for line in text_in:
    no_newline = line.replace('\n', '')
    name, year = no_newline.split(',')
    print(name + ' (' + year + ')')

# Close the text file
text_in.close()
