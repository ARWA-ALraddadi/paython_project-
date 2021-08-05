######################################################################
##
##  Demonstration - Raising exceptions
##
##  The following demonstration shows how a function can raise an
##  exception to indicate that it is being used incorrectly.
##


#---------------------------------------------------------------------
#
# The requirement:
#
# Acronyms and initialisms are formed from the first letter
# of each word in a given phrase.  Define a function called
# "abbrev" that creates an abbreviation from the first letter
# in each word (string) in a given list.
#


#---------------------------------------------------------------------
#
# Observation:
#
# Note that this requirement does not say what to do, if anything,
# if the given list contains non-alphabetic strings, or values that
# are not strings at all.
#


#---------------------------------------------------------------------
#
# A fragile implementation:
#
# The following function satisfies the requirement above, but can be
# easily made to fail.
#

# Return an abbreviation formed from the first letters of
# a given list of (non-empty, alphabetic) strings
def abbrev1(words):

    # Given a non-empty string, return its first letter in
    # upper case
    def first_cap(word):
        return word[0].upper()

    # Build the result by appending the first letter of each
    # word in the list
    abbreviation = ''
    for word in words:
        abbreviation = abbreviation + first_cap(word)
    return abbreviation



#---------------------------------------------------------------------
#
# Some tests:
#

# The following tests all work:
print(abbrev1(['Central', 'Processing', 'Unit']))
print(abbrev1(['What', 'you', 'see', 'is', 'what', 'you', 'get']))
print(abbrev1(['International', 'Business', 'Machines']))

# This test produces an obscure error (comment it out to see
# subsequent tests):
print(abbrev1(['a', 'bb', 'ccc', 4444, 'eeeee']))

# As does this one (comment it out to see subsequent tests):
print(abbrev1(['a', 'bb', 'ccc', '', 'eeeee']))


#---------------------------------------------------------------------
#
# Another implementation:
#
# The following function raises an exception when it recognises that
# the input data cannot be processed.
#

# Return an abbreviation formed from the first letters of
# a given list of (non-empty, alphabetic) strings
def abbrev2(words):

    # Given a non-empty string, return its first letter in
    # upper case
    def first_cap(word):
        if not isinstance(word, str) or len(word) == 0 or not word.isalpha():
            raise Exception("Word '" + str(word) + "' does not have " + \
                            "an initial letter in first_cap")
        return word[0].upper()
    
    # Build the result by appending the first letter of each
    # word in the list
    abbreviation = ''
    for word in words:
        abbreviation = abbreviation + first_cap(word)
    return abbreviation


#---------------------------------------------------------------------
#
# Some tests:
#

# The following tests all work:
print(abbrev2(['Central', 'Processing', 'Unit']))
print(abbrev2(['What', 'you', 'see', 'is', 'what', 'you', 'get']))
print(abbrev2(['International', 'Business', 'Machines']))

# This test produces a meaningful error (comment it out to see the
# next test):
print(abbrev2(['a', 'bb', 'ccc', 4444, 'eeeee']))

# As does this one:
print(abbrev2(['a', 'bb', 'ccc', '', 'eeeee']))
