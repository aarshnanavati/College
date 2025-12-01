#import the 'tkinter' module
from Tkinter import *
#create a new window
window = Tk()
#set the window title
window.title("Colours")

#create a list variable containing colours
colours = ['red','yellow','pink','green','purple','orange','blue']

#loop through each colour
for c in colours:
    #create a new button, using the text/bg of the list item
    b = Button(text=c, bg=c)
    #pack the button, filling up the X axis
    b.pack()

#draw the window, and start the 'application'
window.mainloop()