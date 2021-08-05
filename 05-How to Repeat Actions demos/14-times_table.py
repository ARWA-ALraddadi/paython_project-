##-----------------------------------------------------------------
##
##  Demonstration - Indefinite iteration
##
##  This example illustrates an example of indefinite iteration
##  in which the number of iterations depends on interaction
##  with the user.
##
##  The aim is to develop an educational (but boring!)
##  game which aims to teach the user multiplication tables.
##
##  Note in the code below that the number of iterations is
##  entirely determined by the user's inputs.
##

#------------------------------------------------------------------
#
# Prompt the user for answers to increasingly large multiplication
# results for a given multiplicand, stopping when the user gets
# an answer wrong
#
def times_table(multiplicand):

    # Initialise the loop variables
    multiplier = 0
    answer_typed = 0
    correct_answer = 0

    # Increment the multiplier as long as the user types
    # the right answer
    while answer_typed == correct_answer:
        multiplier = multiplier + 1
        test =  str(multiplicand) + ' * ' + str(multiplier)
        correct_answer = multiplicand * multiplier
        answer_typed = eval(input('What is ' + test + '? '))

    # Print a closing message
    print('Sorry, but ' + test + ' equals ' + str(correct_answer))


#------------------------------------------------------------------
#
# A test
#
times_table(4)
