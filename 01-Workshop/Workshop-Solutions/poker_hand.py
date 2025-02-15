# Poker Hand
#
# THE PROBLEM
#
# This is a simple exercise to check your understanding of lists.
# The list "hand" below represents a hand of playing cards, 
# where picture cards have the following values:
# Ace = 1; Jack = 11; Queen = 12; King = 13
#
# The cards are grouped into the four suits (Hearts, Diamonds,
# Clubs, Spades, in that order) using sub-lists of the main one.

hand = [[5], [], [6, 8], [11, 7]]

# Write an expression, or expressions, to find the card with the
# highest face value in the hand, regardless of suit,
# and print its value.  Note that given a list L of numbers the
# expression 'max(L)' will return the largest number in the list.
#
# (Motivation: Sometimes in poker it is necessary to compare players'
# largest cards in order to determine the winning hand.)
#
#
# A SOLUTION STRATEGY
#
# 1. Combine the sublists into one list
# 2. Find the highest card value in that list
# 3. Print that card's value



# A SOLUTION
#
# 1. Combine the sublists into one list
combined_hand = hand[0] + hand[1] + hand[2] + hand[3]

# 2. Find the highest card value
highest_card = max(combined_hand)

# 3. Print that card's value
print(highest_card) # prints 11 (the Jack of Spades)


# ANOTHER SOLUTION
#
# As is often the case, this sequence of steps can be expressed more
# concisely.  However, some would argue that the following version
# is harder to understand.

print(max(hand[0] + hand[1] + hand[2] + hand[3])) # also prints 11
