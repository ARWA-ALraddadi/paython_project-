#---------------------------------------------------------------------
#
# Fill-in-the-Blanks Story
#
# As a simple example of generating an HTML document using Python,
# here you will create a children's story using words supplied by
# the user to fill in the blanks.
#
# The story in this case is "The Witch Next Door" from the "Activity
# Village" web site.
#
# Your task is to develop a program which prompts the user for six
# words and uses these words to fill in the blanks in the story
# below.  You must then create an HTML file containing the completed
# story.  To ensure that the story is formatted nicely, you will need
# to add some HTML tags into the text provided below.
#

# This is the text of the story with the blanks marked WORD1 to
# WORD6.  You should add HTML tags into the text as necessary to
# make it display nicely in a web browser.
the_story = '''
<h1>
The Witch Next Door
</h1>

<p>
Sam and Amy lived next door to a very strange old woman. She always wore
a black crooked hat, she kept a black cat, and she'd give a cackling laugh
whenever she spoke. On Halloween, they decided to knock on her door to see
if she would give them any lollies. But when she opened the door she said,
"Like lollies, do you? Well, I'd better give you some then."
</p>

<p>
There was a puff of smoke and Sam realised that his WORD1 had
turned into a WORD2! There was another puff of smoke and Amy
had a huge WORD3 where her WORD4 had been!
</p>

<p>
Just as there was another puff, the black cat jumped up into the smoke. When
it fell down to the ground it had turned into a very large, cross-looking
WORD5. The WORD5 chased the old woman back into her house,
clawing at her WORD6.
</p>

<p>
Sam and Amy's bodies went back to normal after a while, but they didn't eat a
WORD2 or WORD3 for a long time afterwards!
</p>
'''

# Get the six words from the user, which will be used in place of the
# blanks in the story.  The words needed to complete the story are:
#
# 1. A part of the body
# 2. A lolly (sweet)
# 3. A chocolate bar
# 4. Another body part
# 5. An animal you'd find in a pet shop other than a cat
# 6. An item of female clothing
#
print ()
print ("Enter six single words...")
word1 = input('A part of your body: ')
word2 = input('Your favourite lolly: ')
word3 = input('Your favourite chocolate bar: ')
word4 = input('Another part of your body: ')
word5 = input('A pet-shop animal other than a cat: ')
word6 = input('An item of female attire: ')

# Replace the "blank" placeholders in the story
the_story = the_story.replace('WORD1', word1)
the_story = the_story.replace('WORD2', word2)
the_story = the_story.replace('WORD3', word3)
the_story = the_story.replace('WORD4', word4)
the_story = the_story.replace('WORD5', word5)
the_story = the_story.replace('WORD6', word6)

# Open the output file for writing
story_file = open('storytime.html', 'w')

# Write standard HTML "header" markups into your file, up to
# and including the <body> tag.  Give your web document a
# meaningful title
story_file.write('''<!DOCTYPE html>
<html>
  <head>
      <title>A Simple Story</title>
  </head>
  <body>
''')

# Write the content of the web document (the story) into
# the file
story_file.write(the_story)

# Write the standard HTML "footer" markups into your file
# to complete the document
story_file.write('''
  </body>
</html>''')

# Close your HTML file (which you can now view in a web browser)
story_file.close()
