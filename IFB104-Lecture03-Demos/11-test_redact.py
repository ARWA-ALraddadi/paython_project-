#---------------------------------------------------------------------
#
# Demonstration - Documenting our tests for a function
#
# This file illustrates the way we can use Python's "doctest"
# strings to keep a record of the tests a function must satisfy.
#
# Scenario: As a security measure, credit card and ATM receipts
# usually print only the last four digits of the card number,
# with the rest of the number replaced by asterisks.  The goal
# here is to produce a function that obscures any given string
# by returning only the last four characters, with asterisks
# replacing all other characters.  Obscuring part of some text
# for security reasons is called "redacting".
#


#---------------------------------------------------------------------
#
# The following triple-quoted string contains the various tests that
# the function must pass.  Note that they're written in
# exactly the same way they would appear if you ran each test
# manually in the shell window.  The first tests are "typical" ones,
# but these are followed by some more extreme tests.
#
'''

A typical test involving a credit card number:
>>> redact('1234 5678 9012')
'**********9012'

A typical test using letters instead of digits:
>>> redact('Top secret')
'******cret'

A typical test using various symbols:
>>> redact('!%$#?.,"+=^@')
'********+=^@'

A case in which most of a long secret is obscured:
>>> redact('The price of security is eternal vigilance!')
'***************************************nce!'

A case is which very little of the secret is obscured,
so it's easy to guess what word it is:
>>> redact('pizza')
'*izza'

An extreme case - the shortest possible length string,
in which case nothing is obscured:
>>> redact('1234')
'1234'

Another unusual case (is the 'secret' text really
obscured?):
>>> redact('********')
'********'

'''


#---------------------------------------------------------------------
#
# This is the function we want to test.  It returns an obscured
# version of a given secret such as a credit card or bank account
# number.
#
def redact(secret):
    # Work out how many asterisks we need
    num_asterisks = len(secret) - 4
    # Create that many asterisks
    asterisks = '*' * num_asterisks
    # Extract the last four characters in the secret
    last_four_digits = secret[-4:]
    # Return the asterisks and the last four characters
    return asterisks + last_four_digits


#---------------------------------------------------------------------
#
# Here's a main program containing some instructions for the demo
#
print('''
To test the 'redact' function, run this module so that the
function is defined, then copy tests from the 'docstring' into
the shell window and confirm that they all produce the
expected result...  Tedious isn't it?

When you get sick of all the cutting and pasting, try
uncommenting the code at the end of the Python file. It will
run all the tests automatically and print the outcome, saving
you a lot of work!
''')

# Code to run all the tests automatically and report the outcome
##from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
##print(testmod(verbose = False,
##              optionflags = REPORT_ONLY_FIRST_FAILURE))
