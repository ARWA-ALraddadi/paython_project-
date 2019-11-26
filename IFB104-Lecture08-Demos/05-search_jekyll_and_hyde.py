#  Search The Strange Case of Dr. Jekyll and Mr. Hyde
#
#  As a demonstration of using regular expressions to search
#  for patterns in large amounts of text, this program allows
#  the user to type regular expressions which are then used
#  to match text from the book "The Strange Case of Dr. Jekyll
#  and Mr. Hyde" by Robert Louis Stevenson.  The book is an HTML
#  file (although it contains very few mark ups).

# Import the regular expression function of interest
from re import findall

# Print an explanatory message
print("Search 'The Strange Case of Dr. Jekyll and Mr. Hyde' for regex patterns")
print()

# Open the file and read all of its contents
file_contents = open('documents/JekyllAndHyde.html', 'U').read()

# Keep reading regular expressions until the user says to stop
reg_exp = input('Search for: ')
while not reg_exp.lower() in ['stop', 'quit', 'exit']:
    try:
        # Find and print all distinct patterns found, in ascending order
        for result in sorted(set(findall(reg_exp, file_contents))):
            print(result)
    except:
        # The regular expression function has raised an exception
        print('Illegal regular expression')
    print()
    reg_exp = input('Search for: ')


# Some interesting search terms to try...
#
# Things described as strange: [Ss]trange +[a-zA-z]+
# People with titles: [DM]r\. +[A-Za-z]+
# Mr. Hyde's first name: [A-Z][a-z]* *Hyde
# Dr. Jekyll's full name: Dr\. +[A-Z][a-z]* +Jekyll
# Questions asked by characters in the book: "[A-Z][a-z ]*\?"
# Exclamations: "[A-Z][a-z ]*!"
# Sentences in which blood is mentioned: [A-Z][A-Za-z,;\- ]*blood[A-Za-z,;\- ]*[\.!\?]
# Emphasised words: <i>([^<]*)</i>
# The title of the book: <TITLE>([^<]*)</TITLE>
# HTML MarkUp tags used: <([a-zA-Z\-_]+)

