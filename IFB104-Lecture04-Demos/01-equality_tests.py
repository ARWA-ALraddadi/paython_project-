#---------------------------------------------------------------------
#
# Demonstration - Expressions that return Boolean values
#
# Although they use numbers, strings and lists as operands, all
# of the operators below return Boolean values, i.e., either
# True or False.
#

#---------------------------------------------------------------------
#
# Some tests for numerical equality and inequality:
#

print(4 < 5)        # less than
print(78 >= 78)     # greater than or equal to
print(78.0 == 78)   # equals
print(78.0 != 78)   # does not equal
print(3 <= 7 <= 8)  # shorthand for two 'less than or equal' tests
print()

#---------------------------------------------------------------------
#
# A very useful operator for lists and strings (it's actually the
# set membership operator, but Python allows it to be used for
# "sequence" types as well):
#

print('c' in 'abacus')
print('d' in 'abacus')
print(7 in [3, 4, 5, 6, 7, 8])
print(7 in ['2', '3', '7', '4']) # strings are not numbers!
print()

#---------------------------------------------------------------------
#
# Various built-in methods return Boolean values too, such as the
# following string methods:
#

print('Henry'.isalpha()) # is the string alphabetic?
print('Henry'.islower()) # is the string all lower case?
print('Henry'.isnumeric()) # does the string consist of digits only?

