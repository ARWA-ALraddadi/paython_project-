######################################################################
##
##  Demonstration - Overriding methods and adding attributes
##
##  This demonstration combines method overriding and addition of
##  new attributes in a subclass
##


######################################################################
#
# Here we define a class for "debit card" objects, which have the
# same capabilities as a "bank account" object, but also provide the
# ability to print a statement listing all transactions since the
# previous statement was produced
#

# Import the superclass
from G_bank_account import *

# A (sub)class for debit card accounts
class Debit_Card_Account(Bank_Account):

    # When a debit card account object is created, initialise the
    # owner's name, opening balance and the statement
    def __init__(self, depositor, opening_deposit):
        # Initialise the basic account
        Bank_Account.__init__(self, depositor, opening_deposit)
        # Initialise the transaction statement
        self.__statement = []

    # Override the bank account's deposit method to record
    # the transaction (as a nicely-formatted string)
    def deposit(self, amount):
        Bank_Account.deposit(self, amount)
        self.__statement = self.__statement + ['+$%.2f' % amount]

    # Override the bank account's withdrawal method to maintain
    # the statement, provided the withdrawal will succeed
    def withdraw(self, amount):
        if self.query() >= amount:
            self.__statement = self.__statement + ['-$%.2f' % amount]
        Bank_Account.withdraw(self, amount)

    # Produce the printable form of a debit card account object
    # as a statement of transactions since the last
    # statement was printed, plus the balance
    def __str__(self):
        # Initialise statement with a heading
        this_statement = 'Recent transactions:\n'
        # Add the transactions to the statement, if any
        if self.__statement == []:
            this_statement = this_statement + 'Nil\n' 
        else:
            for transaction in self.__statement:
                this_statement = this_statement +  transaction + '\n'
        # Add the current balance to the end of the statement
        this_statement = this_statement + \
                         Bank_Account.__str__(self) + '\n'
        # Reset the list of transactions
        self.__statement = []
        # Return the statement
        return this_statement
               


######################################################################
#
# Some tests that show how the printable form of a debit card account
# object is a statement of recent transactions
#

if __name__ == '__main__':

    munsters = Debit_Card_Account('Herman Munster', 45.00) # open account

    munsters.deposit(7.00) # deposit some money

    munsters.withdraw(25.50) # use EFTPOS

    print()

    print(munsters) # print a statement

    print(munsters) # print another statement

    munsters.withdraw(15.00) # make another withdrawal

    munsters.withdraw(100.00) # attempt another (unsuccessfully)

    munsters.deposit(10.00) # deposit some more money

    print()

    print(munsters) # print a statement
