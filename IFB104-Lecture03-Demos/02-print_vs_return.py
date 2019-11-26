#---------------------------------------------------------------------
#
# Demonstration - Printing versus returning values
#
# The small examples in this file illustrate the difference between
# printing a value from within a function and having the function
# return a value.
#
# Scenario: As a security measure, credit card and ATM receipts
# usually print only the last part of the card number, with the
# other digits replaced by asterisks.  The goal here is to produce
# a function that obscures any given string by revealing only
# the last four characters, with asterisks replacing all
# other characters.  Obscuring part of some text for security
# reasons is called "redacting".
#

#---------------------------------------------------------------------
#
# The following function RETURNS the obscured number
#

# Return an obscured version of a given secret such as a
# credit card or bank account number, assuming the secret number
# has four or more digits
#
def redact(secret):
    num_asterisks = len(secret) - 4
    asterisks = '*' * num_asterisks
    last_four_digits = secret[-4:]
    return asterisks + last_four_digits

print('Card number 5685 8675 2411 9076 redacted is ', end = '')  
print(redact('5685 8675 2411 9076')) # show the returned value

print('The type of value returned by the first function is ', end = '')
print(type(redact('5685 8675 2411 9076'))) # show its type

print()

#---------------------------------------------------------------------
#
# The following procedure PRINTS, but does not return, the obscured
# credit card number
#

# Print an obscured version of a credit card or bank card
# number, assuming the secret number has four or more digits
#
def show_redacted_number(secret): 
    num_asterisks = len(secret) - 4
    asterisks = '*' * num_asterisks
    last_four_digits = secret[-4:]
    print(asterisks + last_four_digits, end = '')

print('Card 5685 8675 2411 9076 redacted is ', end = '')
show_redacted_number('5685 8675 2411 9076')  # no need to "print" this expression
print()

print('The type returned by the second function is ', end = '')
print(type(show_redacted_number('5685 8675 2411 9076')))
# Notice the annoying side effect when the line above is "run"!
# Since the function prints something when called it interrupts
# the message we're trying to print in the main program.
