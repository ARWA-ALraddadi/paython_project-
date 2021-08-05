#----------------------------------------------------------------
#
# Powers Tables
#
# Define a function to print a table representing each of the numbers
# from 1 up to a given base limit, raised to the powers of 1 up to a
# given power limit.  The parameters therefore will need to be
# the base limit and the power limit.
#
# See the test cases below for examples. of the expected output.
#
# Hint: Print each column to a width of 10 character spaces
# and for the purpose of formatting, test only to limits of 9.
# You will find the string method "rjust" helpful for
# creating strings of a specific width.
#

 
#---------------------------------------------------------
# These are the tests your function must pass.
#
""" 
>>> powers_table(5, 5) # Test 1 (normal case)
--------------------------------------------------------
n       n**1       n**2       n**3       n**4       n**5
1          1          1          1          1          1
2          2          4          8         16         32
3          3          9         27         81        243
4          4         16         64        256       1024
5          5         25        125        625       3125
--------------------------------------------------------


>>> powers_table(1, 2) # Test 2 (normal case)
-----------------------
n       n**1       n**2
1          1          1
-----------------------


>>> powers_table(2, 7) # Test 3 (normal case)
------------------------------------------------------------------------------
n       n**1       n**2       n**3       n**4       n**5       n**6       n**7
1          1          1          1          1          1          1          1
2          2          4          8         16         32         64        128
------------------------------------------------------------------------------


>>> powers_table(9, 9) # Test 4 (normal case)
----------------------------------------------------------------------------------------------------
n       n**1       n**2       n**3       n**4       n**5       n**6       n**7       n**8       n**9
1          1          1          1          1          1          1          1          1          1
2          2          4          8         16         32         64        128        256        512
3          3          9         27         81        243        729       2187       6561      19683
4          4         16         64        256       1024       4096      16384      65536     262144
5          5         25        125        625       3125      15625      78125     390625    1953125
6          6         36        216       1296       7776      46656     279936    1679616   10077696
7          7         49        343       2401      16807     117649     823543    5764801   40353607
8          8         64        512       4096      32768     262144    2097152   16777216  134217728
9          9         81        729       6561      59049     531441    4782969   43046721  387420489
----------------------------------------------------------------------------------------------------


>>> powers_table(0, 0) # Test 5 (boundary case)
-
n
-

"""


#---------------------------------------------------------
#
# Suggested solution strategy:
#
# 1. Print the table's top border (to the correct width,
#    10 characters per column)
# 2. Print the table's heading row
# 3. For each number from 1 to the base:
#    a. Print the number
#    b. For each power from 1 to the power:
#       i. Print the value of the base raised to that power 
# 4. Print the table bottom border
#

##### DEVELOP YOUR powers_table FUNCTION HERE


# Given a base limit and power limit, a procedure to print a
# table representing each of the numbers from 1 to the base limit,
# raised to the powers of 1 to the power limit
#
def powers_table(base, power):

    COLUMN_WIDTH = 10

    # Print the table's top border
    print '-' * ((power * (COLUMN_WIDTH + 1)) + 1)
    print 'n',

    # Print the table's heading row
    for pow in range(1, power + 1):
        header = 'n**' + str(pow)
        print header.rjust(COLUMN_WIDTH),
    print

    # For each number from 1 to base
    for num in range(1, base + 1):

        print num,
        
        # For each power from 1 to power
        for pow in range(1, power + 1):

            # Raise the number to that power and print the result
            # (right justified to column width)
            print str(num ** pow).rjust(COLUMN_WIDTH),
            
        # Print a carriage return at the end of each line of powers
        print 

    # Print the table's bottom border
    print '-' * ((power * (COLUMN_WIDTH + 1)) + 1)


#---------------------------------------------------------
# This main program executes the tests above when this
# file is run.
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE)
