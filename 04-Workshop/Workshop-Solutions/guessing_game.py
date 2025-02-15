#-----------------------------------------------------------------
#
# Guessing Game
#
# As an example of a program involving making a decision and
# user interaction, here you will develop a simple guessing
# game in a couple of stages.
#
# Stage 1
#
# Write code that :
#
# (a) chooses a random number between 0 and 9, inclusive;
# (b) prints a prompt asking the user to guess what the number is,
#     such as "What number am I thinking of?" or similar;
# (c) reads a number typed by the user; and
# (d) prints "You're right!" if the number typed by the user
#     is the same as the random number chosen, or "Sorry." if
#     the numbers do not match.
#
# To do this you will need the "randint", "input" and "eval"
# functions as well as an IF statement.
#
# Stage 2
#
# Having gotten the code outlined above to work, you can make
# the "game" more interesting by asking the user to guess
# several times and then keeping and displaying a total score.
# To do this you will need to
#
# (a) introduce a variable to keep track of the score and
#     increment it each time the user guesses correctly;
# (b) put a FOR loop around your code so that it is run
#     several times, allowing multiple tries; and
# (c) display the score at the end.
#
# Comment: This is a hard game for the user to win!  You can
# make it fairer by reducing the range of numbers to choose
# from.
#

# Import the random integer function
from random import randint

# Initialise a variable for the user's score
score = 0

# Ask the user to guess several numbers and keep score
for guess in range(5): # how many guesses to allow
    computers_num = randint(0, 9) # choose the computer's random number
    print("I'm thinking of a number between 0 and 9. What is it? ", end = "") # prompt the user
    users_response = eval(input()) # read and evaluate the user's response
    if computers_num == users_response: # test if the two numbers are equal
        print("You're right!")
        score = score + 1
    else:
        print("Sorry, but that's not it.")

# Print the final score, being careful to use correct grammar for
# singular versus plural numbers of wins
if score == 1:
    print("Your final score was 1 point.")
else:
    print("Your final score was", score, "points.")

