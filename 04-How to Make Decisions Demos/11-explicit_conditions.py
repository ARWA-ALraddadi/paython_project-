#---------------------------------------------------------------------
#
# Demonstration - Completing conditional statement alternatives
#
# A common source of programming errors is failure to fully
# appreciate the conditions in which a particular alternative action
# will be performed, especially when conditional statements are
# nested or contain "else" alternatives that don't explicitly
# say when they are chosen.  Fortunately, we can use a basic
# understanding of Boolean algebra to calculate exactly when an
# alternative will be selected as shown by the following examples.
#



#---------------------------------------------------------------------
#
# Since the conditions associated with alternatives are evaluated
# in order, each condition implicitly assumes that all of
# its predecessors were False:
#

# Prints Goldilocks' reaction to a given porridge temperature (in
# degrees Celsius)
def goldilocks(porridge_temp):
    if porridge_temp <= 20:
        # This alternative is selected if
        #     porridge_temp <= 20
        print("Too cold!")
    elif porridge_temp >= 35:
        # This alternative is selected if
        #     not(porridge_temp <= 20) and porridge_temp >= 35
        # which is the same as
        #     porridge_temp >= 35
        print("Too hot!")
    else:
        # This alternative is selected if
        #     not(porridge_temp <= 20) and not(porridge_temp >= 35)
        # which is the same as
        #     20 < porridge_temp < 35
        print("Just right!")




#---------------------------------------------------------------------
#
# In a "two-way" conditional statement an "else" alternative
# is performed if the condition on the first alternative is False:
#


# Print a welcome message for a club where ladies who are old
# enough get a complimentary drink (loosely based on an example
# in Section 3.2.2 of the textbook "Python for Rookies")
#
def print_welcome(age, gender):
    # Types: "age" is a natural number and "gender" is a string
    # with two possible values, 'Male' and 'Female'
    if age >= 18 and gender == 'Female':
        print('Welcome - you get a free drink!')
    else:
        print('Welcome to the club.')


# Under exactly which circumstances will the second alternative
# be chosen in the code above?
#
# a) The second alternative is chosen if the condition on the
#    first alternative is False, i.e., when:
#
#        not(age >= 18 and gender == 'Female')
#
# b) We can reexpress this Boolean condition in a form that's
#    easier to understand as:
#
#        age < 18 or gender == 'Male'
#
# It would be a good idea to add this condition as a comment to
# the "else" alternative in the code above


# Aside: Note the subtle change from "and" to "or" in the two
# versions of the condition above.  Nevertheless, both of these
# conditions are equivalent.  Formally, this is an application
# of a Boolean algebra rule called De Morgan's Law, which states:
#
#     not(A and B)   ==   (not A) or (not B)
