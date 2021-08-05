#----------------------------------------------------------------
#
# File writer
#
# Here we show how data can be stored in a form that persists
# after our program finsihes by writing it to a text file as
# comma-separated values.  After running this program, open the
# file created, 'birthdates.csv', with your favourite text editor
# or spreadsheet application to see the result.
#


# The data to be saved - superhero "dates of birth"
superhero_birthdates = [['Superman', 1938],
                        ['Batman', 1939],
                        ['Wonder Woman', 1941],
                        ['Mary Marvel', 1942],
                        ['Black Canary', 1947],
                        ['The Flash', 1940]]


# Code to store this data in a file which can be accessed
# by other applications, such as a text editor

# Open the output file for writing
text_out = open('birthdates.csv', 'w')
# Write each superhero's data into the file with comma separators
for name, year in superhero_birthdates:
    text_out.write(name + ',' + str(year) + '\n')
# Close the text file
text_out.close()
