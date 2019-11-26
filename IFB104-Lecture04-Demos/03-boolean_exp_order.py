#---------------------------------------------------------------------
#
# Demonstration - Evaluation order of Boolean expressions
#
# The following examples illustrate some of the subtleties of
# Boolean expression evaluation
#


#---------------------------------------------------------------------
#
# Mathematically the following expression is undefined when the
# denominator is zero, but we can still evaluate it in Python
# because the left-to-right evaluation of a Boolean expression stops
# as soon as a definite answer can be determined:

numerator = 5
denominator = 0

print(denominator != 0 and numerator % denominator == 0)
print()


#---------------------------------------------------------------------
#
# The execution order of Boolean expressions is also significant if
# the individual conjuncts or disjuncts have side effects.  However,
# this is bad programming practice and is discouraged anyway!
#
# Nevertheless, to demonstrate the principle, we can easily define
# a side-effecting function:

# Both print the given expression and return its value 
def show_evaluation(expression):
    print("Evaluated:", expression)
    return eval(expression)

# Some examples of Boolean expression "shortcutting":
#
# Only the first two disjuncts of the expression
#
#     4 >= 5 or 4 in [6, 3, 4, 5] or "aaa" < "bbb"
#
# get evaluated:
#
show_evaluation('4 >= 5') or \
show_evaluation('4 in [6, 3, 4, 5]') or \
show_evaluation('"aaa" < "bbb"')
print()


# Only the first three conjuncts of the expression
#
#     4 <= 5 and 4 in [6, 3, 4, 5] and 
#     "aaa" >= "bbb" and (5 - 7) == -2
#
# get evaluated:
#
show_evaluation('4 <= 5') and \
show_evaluation('4 in [6, 3, 4, 5]') and \
show_evaluation('"aaa" >= "bbb"') and \
show_evaluation('(5 - 7) == -2')
