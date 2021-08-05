#--------------------------------------------------------------------#
#
# HTML Document Checker - Writing to a file
#
# We have seen that HTML is a language with a specific syntax.  Web
# browsers make a "best effort" to display documents, and are often
# quite forgiving of errors in the HTML code, but there are obviously
# limits to what they can do with incorrectly marked-up documents.
#
# In this exercise you will write a Python program which reads an
# HTML document and checks that it has certain syntactic features.
#
# This exercise can be completed using Python's "S.find(T)" method
# for character strings which returns the position in string S where
# substring T first occurs or -1 if substring T does not occur in
# string S at all.
#
# Optional extension: Instead of printing your results to the shell
# window, write them out to a text file.
#

# Files to test your solution on - uncomment as appropriate
html_file = 'AdventuresOfSuperman-Good.html' # this file is syntactically correct
# html_file = 'AdventuresOfSuperman-Bad.html' # this file contains several syntax errors

# Open and read the contents of the HTML file
html_code = open(html_file).read()

# Create a text file to receive the results
report = open('html_report.txt', 'w')

# For each of the syntactic HTML features described below write
# Python code to check whether or not the file's contents are
# correct and report your findings to the user

# Put code here to say which file you are checking
report.write('Checking HTML syntax for file "' + html_file + '"\n\n')

# Put code here to confirm that the document begins with the HTML
# markup '<!DOCTYPE html>', which tells the web browser which language
# the document is written in
if html_code.find('<!DOCTYPE html>') == 0:
    report.write('File correctly identifies itself as HTML\n')
else:
    report.write('File does not tell the browser what type it is!\n')

# Put code here to confirm that the document includes a header section
# marked up as '<head> ... </head>'
start_head_pos = html_code.find('<head>')
end_head_pos = html_code.find('</head>')
if  start_head_pos != -1 and end_head_pos != -1 and \
    start_head_pos < end_head_pos:
    report.write('File has a "head" section\n')
else:
    report.write('File does not have a valid "head" section!\n')

# Put code here to confirm that the document includes a title
# marked up as '<title> ... </title>'
start_title_pos = html_code.find('<title>')
end_title_pos = html_code.find('</title>')
if  start_title_pos != -1 and end_title_pos != -1 and \
    start_title_pos < end_title_pos:
    report.write('File contains a title for the document\n')
else:
    report.write('File does not contain a valid title for the document!\n')

# Put code here to confirm that the document includes a body
# marked up as '<body> ... </body>'
start_body_pos = html_code.find('<body>')
end_body_pos = html_code.find('</body>')
if  start_body_pos != -1 and end_body_pos != -1 and \
    start_body_pos < end_body_pos:
    report.write('File contains a body for the document\n')
else:
    report.write('File does not contain a valid body for the document!\n')

# Close the report file
report.close()
