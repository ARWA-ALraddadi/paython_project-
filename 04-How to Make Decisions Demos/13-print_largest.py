#---------------------------------------------------------------------
#
# Demonstration - Comprehending conditional statements
#
# The following example programs and questions are designed to
# show how different outcomes can be produced by similar-looking
# conditional statements,
#
# This is an exercise in code comprehension - this program file
# doesn't do anything when you run it - the goal is for you
# to read the code below and see if you understand what it does.

#---------------------------------------------------------------------
#
# The story: A somewhat confused programmer is asked to produce a
# function called "print_largest" which accepts two numbers and
# prints a single message to say whether the first or the second
# number is largest, if any.
#
# Unwisely, the programmer does not follow a stepwise refinement
# approach to solve the problem and instead just guesses what the
# code should be - this is never a good problem-solving strategy!
#
# Unsure what the solution should be, the programmer produces
# several similar-looking attempts:

def print_largest_1(first_num, second_num):
    if first_num >= second_num:
        print('The first number is largest')
    if second_num >= first_num:
        print('The second number is largest')
    if first_num == second_num:
        print('Both numbers are the same')

def print_largest_2(first_num, second_num):
    if first_num >= second_num:
        print('The first number is largest')
    elif second_num >= first_num:
        print('The second number is largest')
    elif first_num == second_num:
        print('Both numbers are the same')
        
def print_largest_3(first_num, second_num):
    if first_num < second_num:
        print('The second number is largest')
    elif second_num < first_num:
        print('The first number is largest')
    elif first_num == second_num:
        print('Both numbers are the same')
                
def print_largest_4(first_num, second_num):
    if second_num > first_num:
        print('The second number is largest')
    else:
        if first_num > second_num:
            print('The first number is largest')
        else:
            print('Both numbers are the same')

# In an attempt to choose between these alternative "solutions", try
# to answer the following questions by inspecting the program code.
# (Solutions appear far below.)
#
# a. Do print_largest_1 and print_largest_2 always produce
#    the same result when given two numbers, the first of
#    which is (strictly) larger?
#
# b. Do print_largest_1 and print_largest_2 always produce
#    the same result when given two equal numbers?
#
# c. Do print_largest_2 and print_largest_3 always produce
#    the same result when given two numbers, the first of
#    which is (strictly) smaller?
#
# d. Do functions print_largest_2 and print_largest_3 always
#    produce the same results?
#
# e. Do functions print_largest_3 and print_largest_4 always
#    produce the same results?
#
# f. Which function, or functions, satisfies the original
#    requirements specification?








































# Answers:
#
# a. Yes.  They will both print their first message.
#
# b. No.  Function print_largest_1 will produce three messages,
#    but print_largest_2 will only produce one.  (Arguably all
#    the messages printed are correct, but function print_largest_2
#    produces the output we really want.)
#
# c. Yes.  Function print_largest_2 prints its second message and
#    print_largest_3 prints its first message, both of which are
#    the same (and correct).
#
# d. No.  When given two equal numbers they produce different
#    messages.  (Although it could be argued that print_largest_2's
#    response is strictly true in this case, function
#    print_largest_3 produces the most informative output.)
#
# e. Yes.  Functions print_largest_3 and print_largest_4 are
#    semantically equivalent.
#
# f. Functions print_largest_3 and print_largest_4 both
#    satisfy the original requirement (which said to print a
#    SINGLE message).
