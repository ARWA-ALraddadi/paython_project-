
#----------------------------------------------------------------
#
# 1 label, 8 buttons (as per diagram)
# Initially, the title is empty.
# When the user hits one of the buttons, the title is changed (as per diagrams):
# When the user hits one of the Buttons, the title display changes depending on the Button:
# Monty Python Button changes the title to: "And now for something completely different..."
# The Actor1 Button changes the title to: "John Cleese".
# The Actor2 Button changes the title to: "Michael Palin".
# The Actor3 Button changes the title to: "Terry Gilliam".
# The Actor4 Button changes the title to: "Eric Idle, yes as in IDLE".
# The Actor5 Button changes the title to: "Terry Jones".
# The Actor6 Button changes the title to: "Graham Chapman".
# The Clear Title Button clears the title (i.e., nothing is displayed in the title).

#----------------------------------------------------------------


# Import the Tkinter functions
from tkinter import *

# Create a window
the_window = Tk()

# Give the window a title
the_window.title('')

# PUT YOUR CODE HERE-------------------------------------------------#

the_window ['bg'] = "old lace"
the_window.config(highlightbackground = "old lace")



def changing_text_Monty_Python_tag_button():
    the_window.title("And now for something completely different...")
    the_window.mainloop()

def changing_text_The_Actor1_button():
    the_window.title("John Cleese")
    the_window.mainloop()

def changing_text_The_Actor2_button():
    the_window.title("Michael Palin")
    the_window.mainloop()

def changing_text_The_Actor3_button():
    the_window.title("Terry Gilliam")
    the_window.mainloop()

def changing_text_The_Actor4_button():
    the_window.title("Eric Idle, yes as in IDLE")
    the_window.mainloop()

def changing_text_The_Actor5_button():
    the_window.title("Terry Jones")
    the_window.mainloop()

def changing_text_The_Actor6_button():
    the_window.title("Graham Chapman")
    the_window.mainloop()

def changing_text_clear_button():
    the_window.title(" ")
    the_window.mainloop()


    
    
#create first lable and put in window 
first_font = ('Arial', 28)
first_name_label = Label(the_window, text = 'Set The Title',font=first_font , bg= "old lace")
first_name_label.grid(column = 0 , columnspan = 7)


#create first button and put in window
Monty_Python_tag_button = Button(the_window, text = 'Monty Python tag',
                     activeforeground = 'gray',command = changing_text_Monty_Python_tag_button  , bg= "old lace").grid(column = 0 ,row = 1 ,padx=5, pady=5)



#create second button and put in window
The_Actor1_button = Button(the_window, text = 'Actor1',
                     activeforeground = 'gray',command = changing_text_The_Actor1_button  , bg= "old lace")
The_Actor1_button.grid(column = 1 ,row = 1 ,padx=5, pady=5)



#create third button and put in window

The_Actor2_button = Button(the_window, text = 'Actor2',
                     activeforeground = 'gray',command = changing_text_The_Actor2_button  , bg= "old lace")
The_Actor2_button.grid(column = 2 ,row = 1,padx=5, pady=5)


#create fouth button and put in window

The_Actor3_button = Button(the_window, text =  'Actor3',
                     activeforeground = 'gray',command = changing_text_The_Actor3_button  , bg= "old lace")
The_Actor3_button.grid(column = 3 ,row = 1 ,padx=5, pady=5)



#create fifth button and put in window

The_Actor4_button = Button(the_window, text = 'Actor4',
                     activeforeground = 'gray',command = changing_text_The_Actor4_button  , bg= "old lace")
The_Actor4_button.grid(column = 4 ,row = 1,padx=5, pady=5)


#create sixth button and put in window

The_Actor5_button = Button(the_window, text = 'Actor5',
                     activeforeground = 'gray',command = changing_text_The_Actor5_button  , bg= "old lace")
The_Actor5_button.grid(column = 5 ,row = 1,padx=5, pady=5)


#create seventh button and put in window

The_Actor6_button = Button(the_window, text = 'Actor6',
                     activeforeground = 'gray',command = changing_text_The_Actor6_button  , bg= "old lace")
The_Actor6_button.grid(column = 6 ,row = 1,padx=5, pady=5)


#create eghith button and put in window

clear_title_button = Button(the_window, text = ' clear title ', bg = 'gray',
                     activeforeground = 'gray',command = changing_text_clear_button )
clear_title_button.grid( columnspan = 7 ,row = 3 ,ipadx= 35 , ipady= 4)

#----------------------------------------------------------------


# Start the event loop to react to user inputs
the_window.mainloop()
