#--------------------------------------------------------------------#
#
# Uniqueness test
#
# As an example of exiting a loop early, here we develop a small
# program to determine whether or not all letters in some text
# are unique. It does so by keeping track of each letter seen and
# stopping as soon as it sees a letter it has encountered before.
#

# Define the text to be analysed
text = 'The quick brown fox jumps over the lazy dog'

# Create a list of letters already seen
already_seen = []

# Examine each character
for character in text:
    # Only consider alphabetic characters
    if character.isalpha():
        # Make the comparison case insensitive
        uppercase_letter = character.upper()
        if uppercase_letter in already_seen:
            # Alert the user to the duplicate and stop
            print('Duplicate letter found:', uppercase_letter)
            break
        else:
            # Tell the user that a new letter has been found and continue
            print('New letter found:', uppercase_letter)
            already_seen.append(uppercase_letter)


