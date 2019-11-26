#---------------------------------------------------------------------
#
# Shopkeeper
#
# This short demo highlights how keyboard input can be used.
# Just run this file and respond to the prompts.  (This program
# will crash if the user types something unexpected.  We will
# learn later in the semester how to prevent this.)
#
# When we enter text at the keyboard it is returned as a character
# string.  If we want to know its value as a Python expression
# (if any) we must "evaluate" it.
#

# A list of the products we stock
inventory = ['bread', 'milk', 'ice cream', 'lemonade', 'chocolate']
# A list of prices corresponding to each of the products
prices = [3.55, 1.10, 4.75, 2.25, 6.80]

# Here we use the text entered at the keyboard as a string
print("Hello, I'm your friendly local shopkeeper.")
product = input("What would you like? ")
product = product.lower() # convert the string entered to lower case to match the inventory

if not (product in inventory):
    print("I'm sorry, we don't stock that!")
else:
    # Here we assume the user will enter a whole number
    how_many = input("And how many would you like? ")
    quantity = eval(how_many) # evaluate the string to get an integer (we hope!)
    price = prices[inventory.index(product)] # find the price corresponding to the product
    total_cost = quantity * price  
    print("That will be ${0:.2f}, please.".format(total_cost)) # format the cost to two decimal places

print("Thank you for your patronage!")

