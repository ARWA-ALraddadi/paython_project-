
######################################################################
##
##  Demonstration - Overriding superclass methods
##
##  This demonstration shows how a subclass can override methods from
##  its superclass
##



######################################################################
#
# As another extension of the "bank account" class we defined earlier
# we want to create a cheque account class which charges a fee
# each time someone writes a cheque
#

# Import the bank account class
from G_bank_account import *

# A class for cheque accounts
class Cheque_Account(Bank_Account):

    # When first created a cheque account has the same
    # characteristics as a general bank account, plus a fee
    def __init__(self, depositor, opening_deposit):
        Bank_Account.__init__(self, depositor, opening_deposit)
        self.__cheque_fee = 4.00 # dollars

    # When someone tries to withdraw money from the account,
    # nastily charge the fee *before* completing the transaction
    def withdraw(self, amount): # <-- same name as in the superclass
        # Charge the fee (using the superclass's method)
        Bank_Account.withdraw(self, self.__cheque_fee)
        # Now cash the cheque
        Bank_Account.withdraw(self, amount)
             


######################################################################
#
# Some tests that show the cruel effects of the fee on a
# cheque account
#

if __name__ == '__main__':

    gingers_account = Cheque_Account('Ginger Grant', 1000.00)

    gingers_account.withdraw(200.00) # write a cheque

    print(gingers_account) # check the state of the account
    print()

    gingers_account.withdraw(700.00) # write another cheque

    print(gingers_account) # check the state of the account
    print()

    gingers_account.withdraw(90.00) # and one more, that bounces!

    print(gingers_account) # angrily recheck the balance

