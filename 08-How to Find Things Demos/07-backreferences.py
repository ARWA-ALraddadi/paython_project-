##  Backreferences
##
##  As a simple example of using a "backreference", here we
##  define a regular expression for identifying duplicated words
##  in text.  It's often been noted that when proofreading text
##  people tend to overlook duplicated words, as in the following
##  famous example:
##
##           Paris
##           in the
##         the Spring
##
##  Few people reading this familiar phrase quickly notice the
##  duplicated definite article "the".  

from re import findall

##  The following paragraph contains several instances of accidental
##  word duplication.

unedited_text = '''Some of the great achievements of
of recording in recent years have been carried out on on
old records.  In the the early days of gramophones, many
famous people including Florence Nightingale, Tennyson, and
and Mr. Glastone made records.  In most cases these records,
where they could be found, were in a very bad state; not
not that they had ever been very good by today's standards. 
By applying electrical re-recording, engineers reproduced the
now now long-dead voices from the wax cylinders in to
to new discs, and these famous voices which were so nearly lost
forever are now permanently recorded.'''


##  With a backreference, it's easy to find instances of the
##  same word appearing consecutively, whether separated by
##  spaces or newlines.  (Note that at each end of the pattern
##  we've been careful to avoid partial-word matches, e.g., so
##  that it won't think "lo" is a duplicated word in the phrase
##  "solo lost".)

print(findall(r'[^a-z]([a-z]+)[ \n]+\1[^a-z]', unedited_text))
# prints ['of', 'on', 'the', 'and', 'not', 'now', 'to']

