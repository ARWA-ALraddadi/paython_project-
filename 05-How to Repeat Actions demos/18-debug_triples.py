#----------------------------------------------------------------
#
# Example of debugging some iterative code
#
# This program attempts to print a list of consecutive numbers
# in groups of three, on the assumption that they are red-green-blue
# colour values extracted from an image file, but it crashes
# whenever we run it.  To diagnose the problem we'd like to
# quickly get to the point at which it fails, without single
# stepping over every line of code executed.  To do so, we can
# set a "breakpoint" on the offending line by:
#
# 1) Turning on the debugger
# 2) Selecting the line in which the failure occurs
#    (right-click in Microsoft Windows or control-click
#    in Mac OS X)
# 3) Pressing the debugger's "Go" button to jump straight
#    to that line in each iteration
#


data = [18, 59, 93, 21, 39, 87, 45, 14, 38, 16, 93,
        0, 39, 68, 8, 70, 42, 10, 30, 57, 22, 76]

while data != []:
    print(str(data[0]).rjust(3, '0'), ':', end = '')
    print(str(data[1]).rjust(3, '0'), ':', end = '') # This is the line on which to set the breakpoint
    print(str(data[0]).rjust(3, '0'))
    data = data[3:] # Delete the first three items from the list

