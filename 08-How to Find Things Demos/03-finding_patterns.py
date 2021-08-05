##  Finding patterns in text
##
##  The small examples in this demonstration show how regular
##  expressions can be used to extract occurrences of specific
##  patterns from data.  For convenience all of these examples
##  search through small text strings, but obviously the true
##  advantage of this capability is in processing very large
##  amounts of data.

from re import findall


# A full stop denotes any single character

print(findall('d.g', 'Do you dig Doug the dog?'))
# prints ['dig', 'dog']


# Sets of characters in square brackets match any one
# of the characters

print(findall('b[aiuo]t', 'I bet a fair bit you bought a bat'))
# prints ['bit', 'bat']


# Ranges can be used in sets (and to use special regular
# expression characters, such as '$' and '.', as literals
# in a pattern we must escape them with a preceding '\')

print(findall('\$1[0-5]\.00', 'Did it cost $17.00 or $12.00?'))
# prints ['$12.00']


# Sometimes it's easier to say which characters DON'T match

print(findall('12[^A-Z]34', 'Was the secret code 12934 or 12G34?'))
# prints ['12934']


##  The following example shows how we can extract strings
##  that follow a particular format for temperatures.

search_string = '''Telling me that the temperature is 40 isn't
meaningful unless you specify the units of measurement, e.g.,
40C or equivalently about 103F.  We can also include a sign
at the front, such as -15C, but we wouldn't recognise +F as a
valid temperature.'''

print(findall('[+-]?[0-9]+[CF]', search_string))
# prints ['40C', '103F', '-15C']


##  The following example shows how we can extract telephone
##  numbers from text, allowing for the fact that they can
##  be written in different ways.

search_string = '''Sometimes telephone numbers are written
as 8765 4321 and sometimes as 8765-4321.  However, -5556 is
not a valid telephone number and nor is 4329-, so these
numbers shouldn't be returned by the regular expression
below.'''

print(findall('[0-9]+[ -][0-9]+', search_string))
# prints ['8765 4321', '8765-4321']


# We can choose between entire (sub-)patterns using the '|'
# operator (and recall that "non-capturing" brackets are
# written as (?:...) in Python)

print(findall('h(?:is|er)[a-z]*', "I hear it's his, hers or its!"))
# prints ['his', 'hers']


# The various repetition operators allow us to specify how
# many times a sub-pattern may appear consecutively
sentence = "'Tra-lah-laah-laaah,' she trilled."
print(findall('laa?h', sentence)) # one or zero matches
print(findall('laa+h', sentence))  # one or more matches
print(findall('laa*h', sentence))  # zero or more matches
print(findall('laa{2}h', sentence)) # a specific no. of matches
# prints ['lah', 'laah']
#    and ['laah', 'laaah']
#    and ['lah', 'laah', 'laaah']
#    and ['laaah']


##  The following example shows how we can use grouping
##  brackets to extract just part of a match.  In this
##  case we want to extract web addresses, but not
##  return the common "http://" prefix.

search_string = '''Google's URL is http://www.google.com.au, the
Queensland University of Technology's is http://www.qut.edu.au and
Wikipedia's is http://www.wikipedia.org!'''

print(findall('http://([a-z.]+)', search_string))
# prints ['www.google.com.au', 'www.qut.edu.au', 'www.wikipedia.org']


##  The following complex example shows how we can extract
##  valid email addresses from some text, ignoring strings
##  that look a little like an address but aren't properly
##  formed.  (Notice that we have used "capturing" brackets
##  at the outermost level, so that just the part of the
##  match of interest is returned.)

search_string = '''A well-formed email address, such as
fred.nerk@qut.edu.au will have some characters before
the @ symbol and will end with a non-empty domain
identifer, so @qut.edu.au and frank.blank@ are both invalid.
Furthermore, we assume that full stops can be used as
separators, but may not begin or end the user name or
domain, so although we allow joe.c.smith@enterprise.net,
we don't accept harry@.my.home or .jones@thing.org as
valid.'''

print(findall('[^a-z.]((?:[a-z]+\.)*[a-z]+@(?:[a-z]+\.)*[a-z]+)[^a-z.]', \
              search_string))
# prints ['fred.nerk@qut.edu.au', 'joe.c.smith@enterprise.net']


# And there are many more regular expression operators!
# Check the Python documentation for details.
