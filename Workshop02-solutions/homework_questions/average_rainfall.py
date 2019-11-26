# Highest average rainfall
#
# THE PROBLEM
#
# This exercise tests your ability to use lists in Python.
# Assume the following values have already been entered into the
# Python interpreter, denoting the rainfall in millimetres recorded
# for several Queensland towns over a one month period.  No
# record was made for days when it didn't rain, so each of the
# lists is of a different length.

aurukun =  [15, 9, 11, 4, 10, 20, 95]
burdekin = [13, 9, 5, 80, 150, 145]
cardwell = [115, 90, 100, 46, 130, 200, 195, 10, 3, 8]
daintree = [140, 120, 110, 53, 100, 50, 175]
tully =    [115, 90, 100, 130, 200, 195]

# Write code to calculate the highest average rainfall
# and print the result in a meaningful message to the screen.
#
# HINTS:
# * Use the following built-in functions: sum, len and max.
# * Your task is to find the highest average rainfall - NOT the
#   town with the highest average rainfall.
# * The correct answer is 138mm.

# A SOLUTION
#
# 1. Calculate the average rainfall for each town 
#    a. Calculate the total rainfall for the town
#    b. Calculate the average by dividing the total by the
#       number of readings

aurukun_avg = sum(aurukun) // len(aurukun)   # 23
burdekin_avg = sum(burdekin) // len(burdekin) # 67
cardwell_avg = sum(cardwell) // len(cardwell) # 89
daintree_avg = sum(daintree) // len(daintree) # 106
tully_avg = sum(tully) // len(tully)       # 138

# 2. Find the maximum of the averages 
biggest_rainfall = max(aurukun_avg, burdekin_avg, cardwell_avg,
                       daintree_avg, tully_avg)

# 3. Print the highest average in a message to screen
print ('The highest average rainfall was', biggest_rainfall, 'millimetres')

# The answer is 138mm, so Tully is the winner!
