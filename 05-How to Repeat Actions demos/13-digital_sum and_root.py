##--------------------------------------------------------------------
##
##  Demonstration - Digital Sum and Root
##
##  Here we show how to solve a problem requiring indefinite
##  iteration.  The "digital root" of a decimal number is the value
##  produced by repeatedly summing all its digits until only
##  one digit is left.  For instance, the digital root of
##  65,536 is 7, because 6 + 5 + 5 + 3 + 6 = 25 and 2 + 5 = 7.
##
##  Digital roots can be used as "checksums" to confirm
##  the integrity of numerical data.  This is a good example
##  to illustrate condition-controlled iteration because it's
##  difficult to know in advance how many steps will be
##  required to reduce a given number to a single digit.
##


#---------------------------------------------------------------------
#
# A solution
#
# The key to solving this problem is to note that if we divide
# a decimal number by 10 we remove the right-hand digit, and
# the remainder of dividing it by 10 has the value of the right-hand
# digit.  We use a "helper" function to calculate the "digital
# sum" of a number, which is simply the sum of its digits.
#

# Given a natural number, return the sum of its digits
#
def digital_sum(decimal_number):
    # Initialise the sum of the digits
    digit_total = 0
    # Loop as long as the number has some digits left
    while decimal_number != 0:
        # Add the right-hand digit to the total
        digit_total = digit_total + (decimal_number % 10)
        # Remove the right-hand digit
        decimal_number = decimal_number // 10
    # Return the digital sum
    return digit_total

# Given a natural number, return its digital root
#
def digital_root(decimal_number):
    # Loop as long as the number has more than one digit
    while decimal_number >= 10:
        decimal_number = digital_sum(decimal_number)
    # Return the digital root
    return decimal_number


#---------------------------------------------------------------------
#
# Some tests:
#
print ('The digital root of 4 is', digital_root(4))
print ('The digital root of 12 is', digital_root(12))
print ('The digital root of 105 is', digital_root(105))
print ('The digital root of 0 is', digital_root(0))
print ('The digital root of 987 is', digital_root(987))
print ('The digital root of 65,536 is', digital_root(65536))
