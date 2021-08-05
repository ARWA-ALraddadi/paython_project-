# Days calculator
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, representing the number of days in each
# month of a given (non-leap) year.

january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31

# PART 1
#
# Write an expression, or expressions, to calculate the number of days
# in each quarter (three month period) of the year, using the values
# introduced above, and print the result.
quarter_one = january + february +march
quarter_two = april + may + june
quarter_three = july + august + september
quarter_four = october + november + december
print (" the frist quarter is ", quarter_one ,'days')
print (" the second quarter is ", quarter_two ,'days')
print (" the third quarter is ", quarter_three ,'days')
print (" the fourth quarter is ", quarter_four ,'days')
# PART 2
#
# Write an expression, or expressions, to calculate the number of days
# in each half of the calendar year, and print the result.  NB: Your
# solution to Part 2 should use your solution to Part 1.
half_one = quarter_one + quarter_two
half_two =  quarter_three + quarter_four
print (" the frist half of year is ", half_one ,'days')
print (" the second half of yearis ", half_two ,'days')

# PART 3
#
# Write an expression, or expressions, to calculate the number of days
# in the year, and print the result  NB: Your solution to Part 3
# should use your solution to Part 2.

print('the day of the year is', (half_one + half_two))

