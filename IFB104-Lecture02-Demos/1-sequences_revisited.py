#---------------------------------------------------------------------
#
#  Demonstration - More operations on sequences
#
#  Note: This file contains various expressions to be evaluated.
#  If you "run" this file in IDLE nothing will appear to happen,
#  because the expressions are evaluated but the results don't "go"
#  anywhere.  To see the value of an expression you can either:
#
#    a) copy it into IDLE's interpreter window and hit the Enter
#       key; or
#
#    b) put brackets around the expression below then precede
#       the expression with "print", which tells IDLE
#       to display the result when the file is run, and then run
#       the file.


#  Last week we saw that we could create expressions using
#  "built-in" operators such as "+", "*", etc.  However, many
#  more operations are available as named "functions" (and some
#  known as "methods").  This demonstration illustrates some of
#  the many operations available on the "sequence" types, strings
#  and lists.


#----------
# Recap from last week - Recall that strings and lists can
# be used in expressions in various ways:

"Hello" + 'World'   # print("Hello" + "World")

'Ho, ' * 3 + ' Merry' + ' Christmas!'

quote = "'Goodbye', she exclaimed"

quote[12] + quote[13] + quote[18] * 2 + quote[2]

superheroes1 = ['Superman', 'Batman']
superheroes2 = ['The Flash', 'Wonder Woman']

(superheroes1 + superheroes2)[3]


#----------
# We can easily find out how long a string is using the built-in
# length function:

len('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

len('xyz' + 'zy')

len('AAA\nBBB\nCCC')  # produces an interesting answer


#----------
# The Python Library Reference lists many helpful methods we
# can apply to strings:

'Who put the bomp in the bomp-de-bomp-de-bomp?'.count('bomp')

'Who put the bomp in the bomp-de-bomp-de-bomp?'.find('bomp')

'Who put the ram in the ram-a-lam-a-ding-dong?'.find('bomp')

'Who put the bomp in the bomp-de-bomp-de-bomp?'.replace('bomp', 'bip')


#----------
# It doesn't matter whether these operators are applied to
# specific string values, as shown above, or string-valued
# variables:

lyric = 'I love to love you, baby'

lyric[0]

lyric.find('baby')

lyric.count('love')

lyric.replace('love', 'hate')


#----------
# Keep in mind that if you want to save the result of
# evaluating a string-valued expression then you need to
# assign the value to a variable.  Python strings are
# "immutable" which means that the "replace" function
# above returned a new string value, but did not change the
# value of variable "lyric".  The following statement
# does a similar word replacement and saves the result:

new_lyric = lyric.replace('love', 'like')


#----------
# There are many useful built-in functions for manipulating
# lists:

some_numbers = [4, 6, 2, 3, 8, 9, 7]

max(some_numbers) # returns the largest number in the list

sum(some_numbers) # returns the sum of the numbers

sorted(some_numbers)  # returns a new, sorted list


#----------
# We can save the result of evaluating a list-valued expression
# by assigning it to a variable:

temperatures = [32, 38, 37] # a list of temperatures

temperatures[0]  # returns the first temperature in the list

temperatures = temperatures + [31, 30] # add some extra values and save the result

len(temperatures)  # tells us that the list now has five values


#----------
# Unlike strings, lists are "mutable", which means that some operations
# on them will change their value "in place", without the need to
# assigning the result back to the variable:

weekdays = ['Mon', 'Tue', 'May', 'Thu', 'One', 'Fri', 'Sat']  # is not right

weekdays[2] = 'Wed'  # replaces the item at index 2

weekdays.remove('One') # gets rid of an incorrect item

weekdays.append('Sun')  # adds a new item at the end

weekdays # now returns a correct list of weekdays


#----------
# Lyrics quoted from "Who Put the Bomp?" by Barry Mann and
# Gerry Goffin (1961) and "Love to Love You Baby" (1975) by
# Giorgio Moroder, Pete Bellotte and Donna Summer

