#-----------------------------------------------------------
#
# Web Page Downloader
#
# This simple program is a stand-alone tool to display the
# source code of a given web document. For a particular
# URL, it downloads the corresponding web document and
# prints its contents to the shell window as ASCII text.
#
# Q: Why not just look at the web page's source code in your
# favourite web browser (Firefox, Google Chrome, etc)?
#
# A: Because when a Python script uses the Hyper-Text Transfer
# Protocol to download a web document, it may not receive
# the same file you see in your browser!  Some web servers
# produce different HTML or XML code for different clients.
#
# Worse, some web servers may refuse to send documents to
# programs other than standard web browsers.  If a Python
# script requests a web document they may instead respond with
# an "access denied" message.  Therefore, to confirm that the
# HTML code you think is returned by the web server is the
# same code that your own Python program sees you can use
# this script as a test.
#

# Put your web page address here
url = 'https://www.pcworld.com/article/2010278/10-common-mobile-security-problems-to-attack.html' # this web site is nice and doesn't block access
# url = 'http://www.wayofcats.com/blog/' # this web site is nasty and blocks access by Python scripts

# Import the function for opening online documents
from urllib.request import urlopen

# Open the web document for reading
web_page = urlopen(url)

# Read the document's contents as a byte array
web_page_bytes = web_page.read()

# Convert the byte array to plain ASCII text for display in the
# shell window, replacing any Unicode characters that can't be
# rendered by Tk with equivalent multi-character mark-ups (the
# Wikipedia home page has a lot of foreign language text embedded
# in it!)
web_page_ascii = web_page_bytes.decode('ASCII', 'backslashreplace')

# Display the ASCII version of the web document's source
print(web_page_ascii)



