
######################################################################
##
##  Demonstration - Using superclass methods
##
##  This demonstration shows how a subclass can use methods from
##  the superclass to define its own methods
##



######################################################################
#
# As an extension of the "bank account" class we defined earlier we
# now want to create a savings account class which introduces a
# new method for awarding annual interest
#

# Import the bank account class
from G_bank_account import *

# A class for savings accounts
class Savings_Account(Bank_Account):

    # When first created a savings account has the same
    # characteristics as a general bank account, plus an
    # interest rate and a fixed interest threshold
    def __init__(self, depositor, opening_deposit, interest_rate):
        Bank_Account.__init__(self, depositor, opening_deposit)
        self.__int_rate = interest_rate # percent
        self.__threshold = 100.00 # dollars

    # Award the account annual interest, provided it is above
    # a fixed threshold, by making use of methods inherited from
    # the superclass
    def pay_interest(self):
        # Get the current balance
        balance = self.query()
        # Pay interest, if eligible
        if balance > self.__threshold:
            self.deposit((self.__int_rate * balance) / 100.0)
             


######################################################################
#
# Some tests that show how "savings account" objects can do everything
# a "bank account" object can, and more
#

if __name__ == '__main__':

    agent86 = Savings_Account('Maxwell Smart', 1500.15, 5.0)

    agent86.withdraw(250.00) # take some money out

    print(agent86) # check the balance

    agent86.deposit(50.00) # add a little in

    agent86.withdraw(300.15) # take some more out

    print(agent86) # check the balance

    agent86.pay_interest() # award annual interest

    print(agent86) # confirm that we got $50 in interest

