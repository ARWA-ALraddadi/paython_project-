#---------------------------------------------------------------------
#
# Demonstration - Predicates
#
# A "predicate" is a function that returns a Boolean value.
# The "procedural abstraction" created by defining predicates with
# suitably evocative names makes program code easier to understand
# and maintain.
#

#---------------------------------------------------------------------
#
# The following banking example is loosely inspired by one
# in Section 3.1.1 of the textbook "Python for Rookies"


# Given someone's annual salary (in dollars) decide whether or not
# it exceeds a fixed "good income" threshold
def good_income(salary):
    return salary >= 25000


# Given the value of a property (in dollars) decide whether or
# not it is within the price range we consider reasonable for
# offering loans - too cheap and it's not worth the paperwork, too
# expensive and it's too big a risk
def safe_loan(property_value):
    return 20000 <= property_value <= 1000000


# We can now express our decisions in a natural way:

applicants_salary = 45000 # dollars
house_cost = 250000 # dollars

offerMortgage = good_income(applicants_salary) and \
                safe_loan(house_cost)

# Do we offer this particular applicant a loan?
print(offerMortgage)
