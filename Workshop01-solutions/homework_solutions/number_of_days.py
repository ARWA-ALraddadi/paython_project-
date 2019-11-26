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

# A SOLUTION
#
# 1. Calculate the sum of the first three months
# 2. Calculate the sum of the second three months
# 3. Calculate the sum of the third three months
# 4. Calculate the sum of the fourth three months
# 5. print the value of each quarter in a message to screen

first_quarter = january + february + march      # 31 + 28 + 31 = 90
second_quarter = april + may + june             # 30 + 31 + 30 = 91
third_quarter = july + august + september       # 31 + 31 + 30 = 92
fourth_quarter = october + november + december  # 31 + 30 + 31 = 92

print('The first  quarter has', first_quarter, 'days')
print('The second quarter has', second_quarter, 'days')
print('The third  quarter has', third_quarter, 'days')
print('The fourth quarter has', fourth_quarter, 'days')



# PART 2
#
# Write an expression, or expressions, to calculate the number of days
# in each half of the calendar year, and print the result.  NB: Your
# solution to Part 2 should use your solution to Part 1.

# A SOLUTION
#
# 1. Calculate the sum of the first and second quarters
# 2. Calculate the sum of the third and fourth quarters
# 3. print the value of each half in a message to screen

first_half = first_quarter + second_quarter     # 90 + 91 = 181
second_half = third_quarter + fourth_quarter    # 92 + 92 = 184

print('The first  half of the year has', first_half, 'days')
print('The second half of the year has', second_half, 'days')



# PART 3
#
# Write an expression, or expressions, to calculate the number of days
# in the year, and print the result  NB: Your solution to Part 3
# should use your solution to Part 2.

# A SOLUTION
#
# 1. Calculate the sum of the first and second half years 
# 2. print the value of the year in a message to screen

year = first_half + second_half  # 181 + 184 = 365
print('The year has', year, 'days')

