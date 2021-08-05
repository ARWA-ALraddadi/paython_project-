# Pythagorean Theorem
#
# THE PROBLEM
#
# Recall from high-school geometry lessons Pythagoras' famous
# theorem about right-angled triangles:
#
#   "The square of the hypotenuse equals the sum of the squares
#    of the other two sides"
#
# Write a script to calculate and print the length of a right-angled
# triangle's hypotenuse given the lengths of the other two sides.
# For instance, given the two lengths below the answer should
# equal 5.
#
# COMMENT: This is not especially hard, but we're not going to
# give you any hints.  In particular, you will need to find out
# for yourself how to express the required mathematical formula
# in Python.  It's important that you know where to find such
# information by yourself because your Workshop Facilitators will
# not always be on hand to assist you.

side_a = 3
side_b = 4


# A (LONG-WINDED) SOLUTION
#
# 1. In natural language the expression we need to evaluate is
#    "the square root of 'side_a' squared plus 'side_b' squared".
#
# 2. Dissecting this statement we can see that we need three
#    mathematical operators to solve the problem, addition,
#    squaring and taking a square root.  The challenge then becomes
#    how to express these in Python.
#
#    a. We have already used Python's addition operator "+" many
#       times, so we probably don't need to investigate this
#       any further.  However, we can find out more about it by
#       consulting Section 5.6, "Binary Arithmetic Operations" in
#       the "Python Language Reference Manual" which defines core
#       features of the Python scripting language.
#
#    b. One way to find the square of a number is to multiply it
#       by itself, e.g., "side_a * side_a", but a way that better
#       describes the intention of the expression is to raise the
#       value to the power 2.  A search through the "Python Language
#       Reference Manual" produces a description of Python's
#       in-built power operator "**" in Section 5.4, "The Power
#       Operator".
#
#    c. Finally we need to find a square root.  There is no built-in
#       operator to do this in Python, so we turn to the "Python
#       Library Reference" which describes a vast range of extra
#       Python functions.  A search in this document reveals a
#       square root function "sqrt(x)" in Section 9.2.2, "Power
#       and Logarithmic Functions".  This function takes a numeric
#       argument "x" and returns its square root, so obviously meets
#       our needs.
#
#    d. Putting all this together means that the Python expression
#       we want is "sqrt((side_a ** 2) + (side_b ** 2))".
#
# 3. However, if we attempt to evaluate this expression in IDLE we
#    get an error message, "NameError: name 'sqrt' is not defined".
#    This is because the square root function is not in-built, so
#    we need to import it before we use it.  According to Section 9.2
#    of the "Python Library Reference" this function is part of the
#    "math" module.  There are a few different ways to refer to
#    library functions from external modules in Python, but the
#    most elegant is to declare "from MODULE import FUNCTION".  As
#    explained in Section 6.12 of the "Python Language Reference",
#    this makes the named function directly available to the
#    current program.
#
# 4. After all that effort our final solution is the following two
#    lines of code!

from math import sqrt
print(sqrt((side_a ** 2) + (side_b ** 2)))
