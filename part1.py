
from turtle import *
from math import *
from random import *


# variabl size for cards width and height
width_card = 200         
height_card = width_card +30


def background_card (bgcolor = "Papaya Whip"):
#  Draw card background rectangle for four theams 
     
    penup()
    setheading(0)                # set diriction of turtle 
    color(bgcolor)          # use the given colour
    pendown()

# stat coloring shape and loop to move turtle and finish drawing  
    begin_fill()
    
    for BGD in range (2):
        forward(width_card)              
        right(90)
        forward(height_card)     
        right(90)

    end_fill()
    penup()      # make sure pen up to next function to draw 



def house_of_Martell ():
# function drawing house of Martell cards

# calling function to draw backgroung
   background_card()

# set up dirctions for turtle
   penup()
   setheading(-45)
   forward(height_card //1.5)    
   left(-90)
   pendown()
   
# stat coloring shape and loop to move turtle and finish drawing  
   pencolor("Dark Orange")
   color("Goldenrod")
   begin_fill()
   
   for stars_angle in range(52):
      forward(100)
      right(175)
      forward(100)
      right(90)
      forward(10)
      right(90)
      left(2)
      
   end_fill()
   penup()     # make sure the pen up for next card

#house_of_Martell ()

def turtle_diction (cricle_color):
 # set up dirctions for turtle
   setheading(-45)
   forward(height_card //4)
   left(-90)
   pendown()
# stat coloring shape and draw circle and finish drawing  
   color(cricle_color)
   begin_fill()
   circle(width_card //2.2)
   end_fill()
   
    

def house_of_Clegane():
# function drawing house of Clegane cards

# calling function to draw backgroung
   background_card()
   
# calling function to dirctions for turtle
   turtle_diction( "Dim Gray")

# set dirictions for three dot in mid of circle    
   color("Light Sea Green")
   penup()
   backward(height_card//2.5)
   setheading(90)
   forward(-40)
   
# drawing three dot in mid of circle  
   for line_in_dot in range(3):
       penup() 
       setheading(90)
       forward(-40)
       pendown()
       dot(20)
       penup()
       
# drawing half circle in mid of circle  
   pencolor("Deep Sky Blue")
   width (8)
   pendown()
   setheading(90)
   forward(25)
   
   setheading(0)
   backward(height_card //2.9)
   left(-90)
   
   circle(width_card //2.5 , 180)
   left (90)
   forward(145)



def House_of_Tyrell ():
# function drawing house of Tyrell cards

# calling function to draw backgroung
   background_card()
   
# calling function to dirctions for turtle
   turtle_diction( "Sea Green")

   
# set up dirctions for turtle to draw sing
   pencolor("Salmon")
   width (10)
   setheading(-45)
   forward(width_card //2)

# sing loop to give turtle angel info
   for sing in range (3):
       
       circle(width_card //3 , 60)
       left(120)
       circle(width_card //3 , 60)
       left(360)
       
# to draw final line        
   setheading(-45)
   forward(width_card //2.5)

   

def House_of_Lannister ():
# function drawing house of Lannister cards

# calling function to draw backgroung
   background_card()
    
# calling function to dirctions for turtle
   turtle_diction( "Maroon")

# set up dirctions for turtle
   penup()
   pencolor("Salmon")
   setheading(-90)
   forward(width_card //2)
   
# start to draw crown
   color("Navy")
   begin_fill()
   
# botoom line 
   setheading(0)
   pendown()
   forward(width_card //1.5)
# line on right 
   setheading(95)
   forward(width_card //2.5)
   
# first crown angle
   left(-45)
   forward(-width_card //4 )
   
   setheading(90)
   forward(width_card //4)

# sec crown angle
   left(-35)
   forward(-width_card //3.5 )
   
   setheading(95)
   forward(width_card //4)
   
# third crown angle
   left(-35)
   forward(-width_card //3.5 )
   
   setheading(100)
   forward(width_card //4)
   
# fourth crown angle 
   left(-40)
   forward(-55 )
   end_fill()
  
   setheading(-80)
   forward(width_card //4)
   
def write_upside_down(string, **named_params):
    named_params['angle'] = 180
    tk_canvas = getscreen().cv
    tk_canvas.create_text(xcor(), -ycor(), named_params, text = string)



def track_of_cards(num_cards):
# function write numer in cards
   penup()
# list contain number that will be on cards
   tracker_number = ['2','3','4','5','6','7','8','9','10','J','Q','K']

   color("black")
   previous_number = num_cards 
   sety(350)
   for track in range (num_cards  ):
       write((tracker_number[track]),'left',font=('arial',14))
       sety(350 - 150)
       write_upside_down((tracker_number[track]))



       
def which_Stack (num_stack):
 # function help trutle to locate stack
 
    penup()
    if num_stack == 'Stack 1':
        goto(-449 , 375)
        
    elif num_stack == 'Stack 2':
         goto(-270 , 375)
        
    elif num_stack == 'Stack 3':
         goto(-91 , 375)
        
    elif num_stack == 'Stack 4':
          goto(88 , 375)

    elif num_stack == 'Stack 5':
          goto(267 , 375)

    elif num_stack == 'Stack 6':
          goto(446 , 375)

def which_suit (suit):
 # function help trutle to know suit
 
    if suit == 'Suit A':
        house_of_Martell()

    elif suit == 'Suit B':
        house_of_Clegane()
                 
    elif suit == 'Suit C':
        House_of_Tyrell ()
                 
    elif suit == 'Suit D':
        House_of_Lannister ()
        
def joker ():
# function drawing house of Martell cards

# calling function to draw backgroung
   background_card("LIGHT PINK")
   
# set location to stast drawing    
   penup()
   setheading(-45)
   forward(height_card //3.5)    
   left(-90)
   pendown()
# drawing boarder of circles in one location  
   pencolor("Firebrick")
   width (6)
   pendown()
   list_radusi = [2.5 ,3 ,3.5 ,4, 4.5]
   for muti_circle in list_radusi :
      circle(width_card // muti_circle)
      
# drawing stars listructors

   pencolor("Dark salmon")
   width (4)
   right(-85)
   penup()
   forward(40)
   pendown()
   for stars in range (16):
       forward (stars *10)
       right(144)
  

   


   

   
#house_of_Martell()   
#house_of_Clegane()
#House_of_Tyrell ()
#House_of_Lannister ()

joker () 

hideturtle()

