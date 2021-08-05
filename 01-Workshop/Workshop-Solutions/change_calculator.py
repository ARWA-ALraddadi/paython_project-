# Change Calculator
#
# THE PROBLEM
#
# You need to calculate how much change is due when you go shopping.
# You have a $20 note and buy the following:
#   2 cartons of milk @ $2.50
#   5 Mars bars @ $1.20 each
#   1 pkt indigestion tablets @ $3.50
#
# Write an expression to calculate the change you should be given
# from $20, after buying those groceries.  Display
# the value of the change in a message to the screen.
# (Don't worry about trailing 0s in the result.)

# HINTS:
# * You will need to use built-in mathematical operators: *, + and -
# * You may like to introduce variables to accumulate and store values
# * The Python function call "print(E)" will print the value of expression E

# A SOLUTION
#
# 1. Deduct from 20 the sum of all the purchases:
#    a.  2 multiplied by 2.50 plus
#    b.  5 multiplied by 1.20 plus
#    c.  3.50 

sum_of_purchases = 2*2.50 + 5*1.20 + 3.50
change = 20 - sum_of_purchases

# 2. Print the result as a number to the screen
print(change)


######################################################################
# Some improvements using more advanced Python features

# 2b. Print the result to the screen by converting the number to
#     a character string and adding a message at the beginning
print('The change should be $' + str(change)) # 5.5

# 2c. Format currency to two decimal places by specifying how
#     many digits should be displayed after the floating point
#     number's decimal point:
print('The change should be $%.2f' % change) # 5.50



