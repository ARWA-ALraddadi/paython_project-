##--------------------------------------------------------------------
##
##  Demonstration - Data abstraction
##
##  This demonstration shows how a class can be used to define a
##  data abstraction in which the representation of the data
##  structure is hidden from its users.
##

#--------------------------------------------------------------------
#
# Here we define a class for representing the current time of day,
# in minutes.  To show how the internal representation of the time
# does not need to match the user's view, we represent the time
# internally as the absolute number of minutes that have elapsed since
# midnight, but allow users to set the time using a 12-hour format,
# and display the time in a 24-hour format.
#

# A class for "wall clock" times
class Wall_Clock:

    minutes_in_hour = 60 # Initialise a constant class attribute that
                         # tells us how many minutes there are in an
                         # hour

    minutes_in_half_day = 12 * minutes_in_hour # Initialise a constant
                                               # attribute that tells us
                                               # how many minutes there
                                               # are in a 12-hour period
                                          
    minutes_in_day = 2 * minutes_in_half_day # Initialise a constant
                                             # attribute that tells us how
                                             # many minutes there are
                                             # in a 24-hour period

    # When objects are instantiated from this class,
    # initialise an attribute to keep track of the current time
    # as a natural number representing the minutes since midnight
    def __init__(self):
        self.now = 0
    
    # Given a time in 12-hour format, set the current time
    def set_time(self, hours, minutes, meridiem):
        # Sanity check on argument values (using assertions)
        assert hours in range(1, 13)
        assert minutes in range(0, 60)
        assert meridiem in ['a.m.', 'p.m.']
        # Update attribute (using conditional expressions)
        self.now = ((0 if hours == 12 else hours * self.minutes_in_hour) + \
                    minutes + \
                    (0 if meridiem == 'a.m.' else self.minutes_in_half_day)) 

    # Advance the time by the given number of minutes (default one)
    def tick(self, minutes = 1):
        assert type(minutes) == int and minutes >= 0
        self.now = (self.now + minutes) % self.minutes_in_day

    # Return the time in 24-hour format
    def __str__(self):
        return str(self.now // self.minutes_in_hour).rjust(2) + \
               ':' + \
               str(self.now % self.minutes_in_hour).zfill(2)


#--------------------------------------------------------------------
#
# Some tests that show how a "wall clock" object can be instantiated
# and used without the user being aware of its internal data
# representation.
#

mantle_clock = Wall_Clock() # create a new "wall clock" object

mantle_clock.set_time(4, 55, 'p.m.') # set its value

print('Initial time:', mantle_clock) # show the time in 24-hour format

print(mantle_clock.now) # reveal the actual representation of this
                        # time (and violate the data abstraction
                        # barrier!)

mantle_clock.tick() # advance the time one minute

mantle_clock.tick(9) # advance the time a further nine minutes

print('Later time:', mantle_clock) # display the updated time

print(mantle_clock.now) # reveal the actual representation of this
                        # time 
