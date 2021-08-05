#----------------------------------------------------------------
#
# Wikipedia Summariser
#
# This program exploits the regular structure of Wikipedia web
# pages to extract and displays the page's title and last
# modification time.  To do so, it relies on the presence of
# certain text patterns in the web page's HTML source code.
# It will probably crash if applied to documents that don't have
# this structure.
#
 
#-----
# Import the necessary URL function
from urllib.request import urlopen

#-----
# Define some Wikipedia URLs to experiment with, here all
# featuring characters from Harvey Comics
url1 = 'http://en.wikipedia.org/wiki/Baby_Huey'
url2 = 'http://en.wikipedia.org/wiki/Little_Lotta'
url3 = 'http://en.wikipedia.org/wiki/Little_Dot'
url4 = 'http://en.wikipedia.org/wiki/Wendy_the_Good_Little_Witch'
url5 = 'http://en.wikipedia.org/wiki/Hot_Stuff_the_Little_Devil'
url6 = 'http://en.wikipedia.org/wiki/Stumbo_the_Giant'

#-----
# Get a link to the web page from the server, using one
# of the URLs above
wikipedia_page = urlopen(url3)

#-----
# Extract the web page's content as a Unicode string
html_code = wikipedia_page.read().decode('UTF-8')

#----
# close the connection to the web server
wikipedia_page.close()

#-----
# Find and print the Wikipedia page's title, if possible.
# We assume the title appears in a heading of the form
#
#    <h1 id="firstHeading" class="firstHeading" lang="en">TITLE</h1>
#
# and that there is only one such pattern in the code.
#
start_marker = '<h1 id="firstHeading" class="firstHeading" lang="en">'
end_marker = '</h1>'
starting_position = html_code.find(start_marker)
end_position = html_code.find(end_marker)
if starting_position == -1 or end_position == -1:
    print('Error: Unable to find page title')
else:
    print(html_code[starting_position + len(start_marker) : end_position].upper())

#-----
# Find and print the date when the page was last updated.
# We assume that this information occurs between the
# following tag and punctuation mark (note the space after
# the tag):
#
#    <li id="footer-info-lastmod"> DATE,
#
start_marker = '<li id="footer-info-lastmod"> '
end_marker = ','
starting_position = html_code.find(start_marker)
end_position = html_code.find(end_marker, starting_position)
if starting_position == -1 or end_position == -1:
    print('Error: Unable to find modification date')
else:
    print(html_code[starting_position + len(start_marker) : end_position])
print()


#-----
# Find and print the Wikipedia page's contents list.
# We assume each content item appears in the following form,
#
#    <span class="toctext">HEADING</span>
#
# although not all Wikipedia pages will have a contents list.
# An indefinite loop is used because we don't know how many
# items the contents list will contain.
#
# Also, this code does not allow for nested sub-lists within
# the table of contents.
#
print('Contents')
start_marker = '<span class="toctext">'
end_marker = '</span>'
end_position = 0
starting_position = html_code.find(start_marker, end_position)
end_position = html_code.find(end_marker, starting_position)
while starting_position != -1 and end_position != -1:
    print('*', html_code[starting_position + len(start_marker) : end_position])
    starting_position = html_code.find(start_marker, end_position)
    end_position = html_code.find(end_marker, starting_position)

