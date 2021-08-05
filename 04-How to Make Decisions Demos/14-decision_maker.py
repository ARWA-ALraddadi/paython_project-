#---------------------------------------------------------------------
#
# Demonstration - Decision maker
#
# This example shows two different ways in which we can solve a
# particular problem requiring us to choose between several
# alternative actions.  One solution uses nested IF statements
# and the other uses Boolean connectives, but both do exactly
# the same thing.
#
# Requirement:
# Many problems encountered in management can be described via
# "quadcharts", which represent the four alternatives available
# when making a decision involving two binary variables.  For
# instance, the following quadchart suggests the response you
# should make when asked to complete a job, given its level
# of difficulty and expected duration.
#
#             Easy job     Hard job
#           +------------+------------+
#  Short    |            |            |
#  deadline | Negotiate  | Decline    |
#           |            |            |
#           +------------+------------+
#  Long     |            |            |
#  deadline | Accept     | Negotiate  |
#           |            |            |
#           +------------+------------+
#
# If the job is easy and there is plenty of time you should
# accept it.  If the job is hard and there is very little
# time to complete it you should decline.  If the job is easy
# but the deadline is short you should negotiate for an
# extension of time.  If there is plenty of time to complete
# the work but the job is hard you should negotiate for more
# staff.
#
# As a management aid, define a function that accepts estimates
# of job duration (in months) and job difficulty (on a scale of
# 1 to 10) and returns a string indicating which of the three
# possible responses you should make.  Jobs with a duration of
# three months or less are considered "short" and jobs with a
# difficulty level of seven or more are considered "hard".
#

#---------------------------------------------------------------------
#
# Some acceptance tests:
#
"""
----- Test the first solution -----

>>> job_a(12, 1) # An easy job with plenty of time
'Accept'

>>> job_a(1, 9) # A hard job with very little time
'Decline'

>>> job_a(2, 5) # An easy job but with little time
'Negotiate'

>>> job_a(12, 8) # A hard job with lots of time
'Negotiate'

----- Test the second solution -----

>>> job_b(12, 1) # An easy job with plenty of time
'Accept'

>>> job_b(1, 9) # A hard job with very little time
'Decline'

>>> job_b(2, 5) # An easy job but with little time
'Negotiate'

>>> job_b(12, 8) # A hard job with lots of time
'Negotiate'

"""

#---------------------------------------------------------------------
#
# First solution - Using nested IF statements
#
# Return an Accept/Negotiate/Decline string given the duration
# of a job, in months, and its level of difficulty, on a 1 to 10
# scale, as per our management quadchart, where durations of
# three months or less are considered "short" and jobs with a
# difficulty level of seven or more are considered "hard"
#
def job_a(duration, difficulty):

    hardjob = 7 # or higher
    shortjob = 3 # months or less

    if difficulty < hardjob:
        if duration > shortjob:
            # Job is easy and there's lots of time
            return 'Accept'
        else:
            # Job is easy but the deadline is short
            return 'Negotiate'          
    else:
        if duration > shortjob:
            # Job is hard but the deadline is long
            return 'Negotiate'
        else:
            # Job is hard and there's little time
            return 'Decline'

#---------------------------------------------------------------------
#
# Second solution - Using Boolean connectives
#
# Return an Accept/Negotiate/Decline string given the duration
# of a job, in months, and its level of difficulty, on a 1 to 10
# scale, as per our management quadchart, where durations of
# three months or less are considered "short" and jobs with a
# difficulty level of seven or more are considered "hard"
#
def job_b(duration, difficulty):

    hardjob = 7 # or higher
    shortjob = 3 # months or less

    if difficulty < hardjob and duration > shortjob:
        # Job easy and lots of time
        return 'Accept'
    elif difficulty >= hardjob and duration <= shortjob:
        # Job hard and little time
        return 'Decline'
    else:
        # Job is easy but the deadline is short or
        # job is hard but the deadline is long
        return 'Negotiate'


#---------------------------------------------------------------------
#
# Run the tests automatically
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))
