#---------------------------------------------------------------------
#
# Battle damage
#
# We need WHILE loops to control repetitive behaviours when we can't
# easily tell in advance how many repetitions will be needed.  This
# can be due to the loop being dependent upon external inputs or,
# as in this case, randomness in the calculation.
#
# As a simple example of a loop requiring an unknown number of
# iterations, the following code simulates a battle from an
# adventure game.
#
# Question: Is our hero guaranteed to win this fight?
#

from random import randint, choice

print('''Our hero has encountered an evil troll blocking his
path. They draw swords and a savage battle ensues!
''')

trolls_health = 100

# Continue fighting as long as the troll is undefeated
while trolls_health > 0:

    # The troll swings first
    if choice([True, False]):
        print ('The troll swings wildly and misses!')
    else:
        print ("The troll's blow is blocked by our hero's shield!")

    # Our hero retaliates
    if choice([True, False]):
        print ('Our hero swings his sword, but the troll is too quick.')
    else:
        print ('Our hero strikes the evil troll with his mighty sword!!!')
        damage = randint(20, 80)
        trolls_health = trolls_health - damage

# Our hero wins
print('''
Having vanquished the troll our hero continues on his
noble quest!''')
