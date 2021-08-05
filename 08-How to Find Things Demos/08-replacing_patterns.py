##  Replacing patterns
##
##  The small examples in this demonstration show how regular
##  expressions with backreferences can be used to perform
##  automatic modifications of text.

from re import sub


##  This example shows how to "normalise" a data representation.
##  A common problem at QUT is that student numbers are
##  represented in different ways, either n7654321, N7654321,
##  07654321 or 7654321.  Here we show how to change all student
##  numbers in some text into a common zero-prefixed format.
##  (The pattern used is not very robust; it is reliable only
##  if there are no numbers other than student numbers in the
##  text.)

student_nos = \
'''Student 02723957 is to be commended for high quality
work and similarly for student n1234234, but student
1129988 needs to try harder.'''

print(sub('[nN0]?([0-9]{7})', r'0\1', student_nos))
# prints "Student 02723957 is to be commended for high quality
#         work and similarly for student 01234234, but student
#         01129988 needs to try harder."

print()

##  As another example of substitution and backreferencing, we
##  return to the copyeditor's problem of identifying accidently
##  duplicated words in text.  Not all such phrases are mistakes
##  so they need to be checked manually.  The following script
##  identifies doubled-words as before, but now surrounds them with
##  asterisks to draw them to the attention of the proofreader.
##  It also allows the two words to be separated by not only
##  blank spaces but newline characters because such errors
##  often occur at line breaks.  Notice that both ends of the
##  pattern are required to contain non-alphabetic characters to
##  ensure that we don't match parts of words.

##  The following paragraph contains several instances of accidental
##  word duplication.

unedited_text = \
'''Some of the great achievements of of recording in
recent years have been carried out on on old records.  In the
the early days of gramophones, many famous people including
Florence Nightingale, Tennyson, and and Mr. Glastone made
records.  In most cases these records, where they could be
found, were in a very bad state; not not that they had
ever been very good by today's standards. By applying
electrical re-recording, engineers reproduced the now
now long-dead voices from the wax cylinders in to
to new discs, and these famous voices which were so nearly
lost forever are now permanently recorded.'''

print(sub(r'([^a-z])(([a-z]+)[ \n]+\3)([^a-z])', r'\1**\2**\4', unedited_text))
# prints "Some of the great achievements **of of** recording in
#        recent years ..."




