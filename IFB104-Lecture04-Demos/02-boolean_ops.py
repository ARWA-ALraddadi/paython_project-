#----------------------------------------------------------------
#
# Demonstration - Boolean operators
#
# The Boolean operators allow us to create logical expressions
# from Boolean values and (in)equality tests
#
# Python supports the basic Boolean operators "and", "or" and
# "not" (although other logical operations such as implication
# can be created from these)
#

# The following example is based on one in Section 3.1.1 of
# the textbook "Python for Rookies":

age = 21 # years

gender = 'F' # alternatives are 'M' or 'F'

# Set variable "isMale" to a Boolean value
isMale = gender == 'M'
print(isMale)
print(type(isMale))

# Is the result True or False?
isAdultFemale = age >= 18 and not isMale 
print(isAdultFemale)


# Another simple example, this time involving the "or" operator:

temperature = 5 # degrees Celsius

# It's time for our favourite TV show!
goodShowOnTV = True 

# Should we go out?
stayInside =  temperature < 10 or temperature >= 30 or \
              goodShowOnTV
print(stayInside)
