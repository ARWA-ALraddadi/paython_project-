

# Import the Tkinter functions
from tkinter import *
from re import findall
from urllib.request  import urlopen




# Import the Tkinter functions
from tkinter import *
# Create a window
the_window = Tk()

# Give the window a title
the_window.title('EVENTS BOOK')
the_window ['bg'] = "white"


items_chosen = []
    
def save_file():
   
    output_file = open('shopping_list.txt', 'w')
    for item in items_chosen:
        output_file.write(str(item)+ '\n')
    output_file.close()    
#--------------------------------------------------------------------#



def new_window (win_title = "  " , bg_color = 'black'):
    window = Tk()
    window.title(win_title)
    window ['bg'] = bg_color
#
#--------------------------------------------------------------------#

def select_button (x):
    print ( items_chosen[ x ])


def extract_info_multi_venues ():
    
    venues_window = Tk()
    venues_window.title('Brisbane Entertainment Centre')
    color_bg = 'green'
    venues_window ['bg'] = color_bg


    first_name_label = Label(venues_window, text = 'Brisbane Entertainment Centre',
                             font = ('Arial', 20 ) , bg = color_bg).pack()
    
    multi_venues= open('Centre.html', 'U').read() # read the file's contents
    venues_name = findall('"event-title">.*[a-z]', multi_venues)
    venues_time = findall('"Event-Date">.*', multi_venues)
    
    for word in range (10):
        trac = word
        print(venues_name[word] ,'\t', venues_time[word])
        button = Checkbutton(venues_window, text = (venues_name[word][14:len(venues_name[word])-3] ,
                                                    venues_time[word][13:len(venues_time[word])-5]),
                             variable = word,
                              font = ('Arial', 16 ), bg = color_bg , command = (lambda i=word: select_button(i))).pack(anchor = "w")
        items_chosen.append( venues_name[word][14:len(venues_name[word])-3])
    print(items_chosen)
        
    



#
#--------------------------------------------------------------------#


def extract_info_art_culture ():
    
    art_culture_window = Tk()
    art_culture_window.title('Brisbane Art Guide')
    color_bg = 'blue'
    art_culture_window ['bg'] = color_bg

    first_name_label = Label(art_culture_window, text = 'Brisbane Art Guide',
                             font = ('Arial', 20 ) , bg = color_bg).pack()
    

    art_culture = open('Brisbane Art Guide .html', 'U').read() # read the file's contents

    art_culture_name = findall('"bookmark">.*[a-z]', art_culture)
    art_culture_time = findall('WHEN</span> :.*[a-z]', art_culture)
    art_culture_where = findall('blank">.*[a-z]', art_culture)
    for word in range (10):
        print(art_culture_name[word] ,'\t', art_culture_time[word],'\t' ,art_culture_where[word])
        button = Checkbutton(art_culture_window, text = (art_culture_name[word][11:len(art_culture_name[word])-7] ,
          art_culture_time[word][13:len(art_culture_time[word])-3]),variable=word ,
                              font = ('Arial', 16 ), bg = color_bg).pack(anchor = "w")
        
        items_chosen.append( art_culture_name[word][11:len(art_culture_name[word])-7])
         
#
#--------------------------------------------------------------------#


def extract_info_tv_guide ():
    tv_guide_window = Tk()
    tv_guide_window.title('TV guide')
    color_bg = 'yellow'
    tv_guide_window ['bg'] = color_bg

    first_name_label = Label(tv_guide_window, text = 'TV Guide',
                             font = ('Arial', 20 ) , bg = color_bg).pack()
    

    tv_guide = open('tv_guide.html', 'U').read() # read the file's contents

    movie_name = findall('data-name=".*', tv_guide)
    movie_time = findall('data-date=".*', tv_guide)
    #movie_channel = findall('[0-9]th.*', tv_guide)
    for word in range (10):
        print(movie_name[word] ,'\t', movie_time[word])
        button = Checkbutton(tv_guide_window, text = (movie_name[word][11:len(movie_name[word])-3] ,
           movie_time[word][11:len(movie_time[word])-1]),variable=word ,
                              font = ('Arial', 16 ), bg = color_bg ).pack(anchor = "w")
        items_chosen.append( movie_name[word][11:len(movie_name[word])-3])
#
#--------------------------------------------------------------------#


comment = '''
<html>

  <head>

    <title>EVENT BOOK </title>

  </head>
  
  <body>

    <!-- A top-level heading -->
    
    <h1 align = "center">EVENT BOOK</h1>

    <p align="center"><img src="4..png" border="3"></p>

   <h2>References</h2>

    <big>
    <ol>
      <li><a href=" https://www.tvguide.com/tv-premiere-dates/ "><em>TV Premiere Dates</em></a></li>
      <li><a href=" https://www.brisent.com.au/Event-Calendar"><em>The Brisbane Entertainment Centre</em></a></li>
      <li><a href=" https://www.museumofbrisbane.com.au/whats-on/ "><em>Museum of Brisbane </em></a></li>
    </ol>
    </big>
</body>

</html>
'''
#
#--------------------------------------------------------------------#


def save_file_t ():
    output_file = open('test.html', 'w')
    for item in items_chosen:
        output_file.write(item + '\n')
    output_file.write(comment)
    output_file.close()

#
#--------------------------------------------------------------------#

    
#create image button and put in window

media_png = PhotoImage(file = 'socialmedia.gif')
img = Button(the_window,image = media_png).grid( column = 0 ,
                                                 rowspan = 6)
#
#--------------------------------------------------------------------#


#create first lable and put in window 
first_font = ('Blackadder ITC', 20 )
color_bg = 'pink' 

first_name_label = Label(the_window,
                         text = 'EVENTS BOOK',
                         font=first_font  ,
                         bg  = color_bg)
first_name_label.grid(column = 2 ,row = 0 )

#
#--------------------------------------------------------------------#


#create frist labbel and put in window
text_label = Label(the_window, text = 'Event Categories',
                   font=first_font ,
                   bg = color_bg)
text_label.grid(column = 1 ,
                row = 2 ,
                columnspan = 2)
#
#--------------------------------------------------------------------#

 
#create first button and put in window
broadcast_tv= Button(the_window, text = 'Broadcast Television',
                     activeforeground = 'black' ,
                     bg = color_bg ,
                     command = extract_info_tv_guide)
broadcast_tv.grid(column = 1 ,row = 3)

#
#--------------------------------------------------------------------#


#create second button and put in window
art_and_culture = Button(the_window, text = 'Art and Culture',
                     activeforeground = 'black' ,
                         bg = color_bg ,
                         command = extract_info_art_culture)
art_and_culture.grid(column = 2 ,row = 3)

#
#--------------------------------------------------------------------#


#create thirrd button and put in window
multti_purpose_venues = Button(the_window, text = 'Multti Purpose Venues',
                     activeforeground = 'black' ,
                               bg = color_bg ,
                               command = extract_info_multi_venues)
multti_purpose_venues.grid(column = 3 ,row = 3)
#
#--------------------------------------------------------------------#


#create second labbel and put in window
option_label = Label(the_window, text = 'Option :',
                     font=first_font ,
                     bg = color_bg)
option_label.grid(column = 1 ,row = 4 )
#
#--------------------------------------------------------------------#


#create frist radio button  and put in window
offline_button = Radiobutton(the_window, text = 'Working offline ',
                             value = 1,
                         font = ('', 10),
                             activeforeground = 'black' ,
                             bg = color_bg)
offline_button.grid(column = 1 ,row = 5)

#
#--------------------------------------------------------------------#


#create second radio button  and put in window
offline_button = Radiobutton(the_window, text = 'Working online ',
                             value = 2,
                         font = ('Blackadder ITC', 10),
                             activeforeground = 'black' ,
                             bg = color_bg)
offline_button.grid(column = 2 ,row = 5)

#
#--------------------------------------------------------------------#


#create four button and put in window
event_printer = Button(the_window, text = 'event_printer',
                     activeforeground = 'black' ,
                               bg = color_bg ,
                               command = save_file)
event_printer.grid(column = 2 ,row = 6)

