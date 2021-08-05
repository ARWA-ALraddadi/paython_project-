#---------------------------------------------------------------------
#
# Demonstration - Scoping of variables
#
# The small examples in this file illustrate the way the scope of
# variables is restricted to the function in which they are
# introduced.
#
# Some of this code creates errors when run, so is commented out.
#
# Programming style: Since there is no purpose to the code segments
# below we have used meaningless single-character identifiers but
# this is NOT good coding style in general. In your assignments you
# will be required to give meaningful names to all your variables.
#

#---------------------------------------------------------------------
#
# Variables are implicitly "declared" when we first assign to them
# in Python:
#

x = 5 # this assignment implicitly declares an integer variable called "x"

y = 7 # similarly for a variable called "y"

z = x + y # we can use the variables after their introduction

# a = x + b  # but this statement creates an error - why?

b = 8

#---------------------------------------------------------------------
# Programming style: Since variable declarations are implicit     
# in Python, you should get into the habit of using comments to
# document the type and purpose of new variables at the point
# where they are first introduced
#---------------------------------------------------------------------


#---------------------------------------------------------------------
#
# Variables and parameters introduced within functions are visible
# only within the scope of that function:
#

def local_scope(n): # introduces a locally-scoped parameter
    m = 5 # introduces a locally-scoped variable
    p = m + n # this statement is legal
    return p

# q = m + n # but this one creates an error - why?


#---------------------------------------------------------------------
#
# Functions nested within a wider scope can access the variables in
# the outer scope:
#

r = 9 # introduces a globally-scoped variable

def nested_scope(u):
    s = 4
    t = r + s + u # this statement is legal - why?
    return t

# r = s + u # but this one is not - why?


#---------------------------------------------------------------------
#
# Variable and parameter names introduced within a nested scope take
# precedence over the same name in an outer scope:
#

e = 6
f = 7

def duplicate_names(e):
    f = 9
    return e + f

duplicate_names(8) # returns 13 or 17?

#---------------------------------------------------------------------
# Programming style: Using the same names in both "inner" and "outer"
# scopes is confusing and should be avoided
#---------------------------------------------------------------------
