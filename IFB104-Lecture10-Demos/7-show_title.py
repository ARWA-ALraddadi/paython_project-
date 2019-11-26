#----------------------------------------------------------------
#
# Show title
#
# A well-structured HTML/XML file will have a "TITLE" markup
# which contains the heading to be displayed in the Web
# browser's window or tab.  Given a URL, this program attempts
# to download the corresponding Web document, extract its
# title, and print it.  However, the program will crash if
# given an invalid address.  Uncommenting the exception
# handling code below, and indenting the original code,
# will make the program immune to this failure.
#
# Some URLs to try are as follows.  The first two will
# work correctly but the last two won't!
#
# http://en.wikipedia.org
# https://archive.org/web/
# www.incompleteaddress.com/oops
# htttp://wwww.thing.org
#
 
#-----
# Import the necessary URL and RE functions
from urllib.request import urlopen
from re import findall

#-----
# Try to access the Web document
#
##try:

#-----
# Get the URL from the user
#
url = input('Please enter an address: ')

#-----
# Get a link to the Web document
#
web_doc = urlopen(url)

#-----
# Extract the Web document's content as a string
#
html_code = web_doc.read().decode("utf8")

#-----
# Find and print the document's title
#
# NB: Our regular expression relies on the
# assumption that there is only one pair of
# "title" markups in the document
#
title = findall('<title>(.*)</title>', html_code)
print('Document title:', title[0])

#----
# Close the connection to the Web document
#
web_doc.close()

#----
# Print a message if something goes wrong
#
##except IOError:
##    print('Cannot access Web document')
