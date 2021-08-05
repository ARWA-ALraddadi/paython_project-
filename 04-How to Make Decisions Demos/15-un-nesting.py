#---------------------------------------------------------------------
#
# "Un-nesting" some conditional statements
#
# There are usually multiple ways to express the
# same thing in program code.  As an instructive
# exercise in using conditional statements, consider
# the code below which decides whether or not
# an applicant will get a mortgage based on their
# income and their job status.  Your challenge
# is to change the code so that it does exactly the
# same thing but only uses a single IF statement.
# In other words, you must "un-nest" the two nested
# IF statements.  To do so you will not only need
# to change the IF statements, you will also need
# to devise new Boolean expressions involving the
# AND connector.

# Some test values - uncomment as necessary

# An applicant who doesn't earn enough
salary = 25000
years_in_job = 3

### An applicant who doesn't have a steady job
##salary = 45000
##years_in_job = 1

### An applicant who qualifies for a loan
##salary = 55000
##years_in_job = 3

# Two nested IF statements to be "flattened" into one
if salary >= 30000:
    if years_in_job >= 2:
        print('You qualify for the loan')
    else:
        print('You must have worked in your',
              'current job for at least two',
              'years to qualify for a loan')
else:
    print('You must earn at least $30,000',
          'to qualify for a loan')

