#---------------------------------------------------------------------
#
# Where's Superman?
#
# To illustrate how we can find simple patterns in a text file using
# Python's built-in "find" method, this demonstration searches for
# some patterns in an HTML file.
#

# Read the contents of the file as a single string
text_file = open('documents/Superman.html')
text = text_file.read()
text_file.close()

# Make sure we've read the text properly
print("Number of characters read:", len(text))
print()

# Find the first occurrence of the word 'Superman' in the text
print("Superman's name first occurs at position", text.find('Superman'))
print()

# Find the first occurrence of the word 'Batman' in the text
print("Batman's name first occurs at position", text.find('Batman'))
print()

# Find all occurrences of the word 'Superman' in the text
print("Superman's name appears in the following positions:")
location = text.find('Superman') # Find first occurrence, if any
while location != -1:
    print(location)
    location = text.find('Superman', location + 1) # Find next occurrence, if any
print()

# Find and display all names that have been strongly emphasised in the text, i.e.,
# those appearing between the HTML tags <strong> and </strong>.
print("Names which are strongly emphasised in the text are:")
start_tag = '<strong>'
end_tag = '</strong>'
start_location = text.find(start_tag) # Find first occurrence of start tag, if any
while start_location != -1:
    end_location = text.find(end_tag, start_location) # Find matching end tag
    print(text[start_location + len(start_tag) : end_location]) # Print text between the tags
    start_location = text.find(start_tag, end_location) # Find next occurrence of start tag, if any

# This last example is MUCH simpler with regular expressions!

