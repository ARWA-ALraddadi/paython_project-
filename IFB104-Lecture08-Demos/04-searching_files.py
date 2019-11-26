##  Finding patterns in multi-line files
##
##  The small examples in this demonstration show how we
##  can search for particular text patterns in files.  Run
##  the file to see the output.


from re import findall


##  The following code extracts the whole contents of a plain text
##  file into a single string.  It (1) opens the file for reading
##  in universal mode, and (2) reads the entire contents as a
##  single string.

file_contents = open('documents/cricket_balls.txt', 'U').read()


##  Having read the contents of the file, we can easily display
##  all capitalised words it contains.  (We have allowed for
##  the fact that one of these words contains an apostrophe.)

print("Capitalised words:")
capitals = findall("[A-Z][a-z']*", file_contents)
for word in capitals:
    print(word)
print()


##  Similarly, we can extract all numbers the file contains.

print("Numbers:")
numbers = findall("[0-9]+(?:\.[0-9]+)?", file_contents)
for number in numbers:
    print(number)
print()


##  And, of course, this is not just limited to text.  We can
##  even examine the contents of THIS Python file!

file_contents = open('04-searching_files.py').read()


##  We can now display the names of all functions called by this
##  program.  (Note that we put the result returned by the call
##  to findall in a "set" data type to remove duplicate elements.)

print("Functions called:")
functions = set(findall('([a-z]+)\(', file_contents))
for function in functions:
    print(function)
print()

##  Similarly, we can find the names of all variables assigned to.
##  (We have allowed for zero or more spaces between the variable
##  name and the "=" operator.)

print("Variables assigned:")
variables = set(findall('([a-z_]+) *=', file_contents))
for variable in variables:
    print(variable)

    
