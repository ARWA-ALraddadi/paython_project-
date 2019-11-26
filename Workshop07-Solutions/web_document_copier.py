#-----------------------------------------------------------
#
# Web Document Copier
#
# The Python script below reads the contents of a web
# document, the Wikipedia home page, and prints it to the
# shell window.  Since Tk windows cannot handle all Unicode
# characters, it converts the text to an equivalent ASCII
# character string before printing it.
#
# To make this program more useful, modify it in two
# ways:
#
# 1) Instead of hardwiring the web document's address in the
#    Python code, prompt the user for the address of the web
#    document they want to copy.
#
# 2) Instead of printing the contents of the web document
#    to the shell window, write them to an HTML file, so
#    that you have a permanent copy of the document.  In this
#    situation you should save the text as Unicode rather
#    than ASCII.  (However, if you view the document in a web
#    browser you may be disappointed to discover that some of
#    the links to images and other "external" document elements
#    no longer work properly, depending on whether the URLs
#    involved are relative or absolute.)
#
# 3) Once your "copier" is working, use it to download a number
#    of web pages to your computer, then open the files in a
#    text editor or a web browser.  Examine the document's
#    source code and ensure that you can identify the main
#    elements in the document such as the head and body
#    sections, the document title, headings within the body,
#    etc.
#
# NB: If you examine the downloaded web pages in a web browser
# you may find that some hyperlinks are broken.  This can
# happen when the HTML source code contains links relative to
# current file, rather than using a full URL address.  By
# copying the code to a new place, but not adjusting the
# relative links accordingly, we can "break" them.
# 

from urllib.request import urlopen

# Prompt the user for the address of the web document to
# copy, e.g., http://www.wikipedia.org/
url = input('Please enter URL: ') 

# Open the web page
web_page = urlopen(url)
# Read its contents as raw bytes
web_page_bytes = web_page.read()
# Convert the bytes to Unicode
web_page_text = web_page_bytes.decode('UTF-8')

# Write the downloaded web page source to a local Unicode file
filename = 'download.html'
html_file = open(filename, 'w', encoding = 'UTF-8')
html_file.write(web_page_text)
html_file.close()

# Tell the user we're finished
print("HTML file '" + filename + "' written")

