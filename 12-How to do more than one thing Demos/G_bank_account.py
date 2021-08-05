######################################################################
##
##  Demonstration - Object instantiation
##
##  This demonstration shows how a class can be used to instantiate
##  multiple objects, each of which maintains its own distinct
##  state
##



######################################################################
#
# Here we define a class for "bank account" objects, each of
# which maintains the depositor's name and their current balance
#

# A basic class for bank accounts
class Bank_Account:

    # When a bank account object is created, initialise the
    # owner's name and opening balance
    def __init__(self, depositor, opening_deposit):
        # Sanity checks on arguments
        assert type(opening_deposit) == float and opening_deposit > 0.0
        assert type(depositor) == str
        # Initialise private object attributes
        self.__owner = depositor
        self.__balance = opening_deposit

    # Get the value of the "current balance" attribute
    def query(self):
        return self.__balance

    # Add to the value of the "current balance" attribute
    def deposit(self, amount):
        assert type(amount) == float and amount >= 0.0
        self.__balance = self.__balance + amount
        print('Deposit accepted')

    # Allow a withdrawal only if there are sufficient funds
    # in the account
    def withdraw(self, amount):
        assert type(amount) == float and amount >= 0.0
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
            print('Withdrawal complete')
        else: # amount > self.balance
            print('Insufficient funds')

    # Produce the printable form of a bank-account object (using
    # sprint-style formatting of the floating point number)
    def __str__(self):
        return self.__owner + ': $%.2f' % self.__balance
               


######################################################################
#
# Apart from directly accessing methods of the object, we can also
# define functions that manipulate objects via their methods
#

# A function that pays 5% interest to a given bank account, provided
# it has a balance no less than $100
def pay_interest(bank_account):

    # Interest payment threshold
    threshold = 100.0 # dollars

    # Interest paid
    interest = 5.0 # percent

    # Deposit the interest payment, if the account is eligible
    balance = bank_account.query()
    if balance > threshold:
        bank_account.deposit((interest * balance) / 100.0)



######################################################################
#
# Some tests that show how multiple "bank account" objects can be
# instantiated and manipulated, while each maintains its own
# internal data values
#

if __name__ == '__main__':
    
    # 1. Create two bank account objects

    jetsons = Bank_Account('George Jetson', 1500.15)
    flintstones = Bank_Account('Fred Flintstone', 50.00)

    # 2. Show their printable forms (confirming that they have their
    #    own distinct states)

    print(jetsons)
    print(flintstones)
    print()

    # 3. Add to one of the accounts and then show that the other one
    #    remains unchanged

    flintstones.deposit(25.50)

    print(jetsons)
    print(flintstones)
    print()

    # 4. Similarly for a couple of withdrawals (one unsuccessful)

    jetsons.withdraw(120.00)
    flintstones.withdraw(120.00)

    print(jetsons)
    print(flintstones)
    print()

    # 5. Use the query methods to access the values of the attributes

    print('The Jetsons have $%.2f more than the Flintstones ' % \
          (jetsons.query() - flintstones.query()))
    print('(not considering 7,000,000 years of inflation)')
    print()

    # 6. Award annual interest (if any) to both accounts and print the
    #    outcome

    pay_interest(flintstones)
    pay_interest(jetsons)

    print(jetsons)
    print(flintstones)
