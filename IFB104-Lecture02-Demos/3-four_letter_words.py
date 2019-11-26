###########################################################################
#
# Four-letter words
#
# As a simple exercise in generating random values, here we present a
# program that generates "words" consisting of four randomly-chosen
# letters.
#
# To increase the likelihood of producing an actual english word we
# structure the words generated as a consonant, followed by a vowel,
# followed by any letter, and ending with a consonant.
#
# The chances of the program producing rude words is very slim, but not
# zero.  You have been warned!
#

# Create lists of letters to choose from
letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

# Import the random function
from random import choice

# Generate multiple random "words" and print one per line
for how_many in range(20):
    word = choice(consonants)
    word = word + choice(vowels)
    word = word + choice(letters)
    word = word + choice(consonants)
    print(word)
