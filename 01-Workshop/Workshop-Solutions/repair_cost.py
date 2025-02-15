# Total repair cost
#
# THE PROBLEM
#
# Assume the following values have already been entered into the
# Python interpreter, representing the vehicle repair costs in dollars
# from several suppliers following a motor accident, and the deposit
# paid for the work:

panel_beating = 1500
mechanics = 895
spray_painting = 500
tyres = 560

deposit = 200

# Write an expression to calculate the total cost outstanding
# after the deposit has been paid, and the repairs completed.
# Then print an appropriate message to screen including the
# amount owing.

# Use the following problem solving strategy:
# 1. Calculate the sum of all the costs
# 2. Deduct the amount of the deposit already paid
# 3. Display the result

# A SOLUTION

costs = panel_beating + mechanics + spray_painting + tyres
outstanding = costs - deposit
print(outstanding) # The answer should be $3255


#####################################################################
# A nicer display
#
# The number is converted to a string and a message is added in
# front of it

print('The amount outstanding is $' + str(outstanding))


