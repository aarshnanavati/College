from tkinter import *
import tkinter
from tkinter import messagebox
#create a new window
window = Tk()
#set the window title
window.title("Commands")
#a function that changes the text of the label
def callback():
    lbl.configure(text="Button clicked!")
    #messagebox.showinfo( "Hello Python", "Hello World")
#create a label to display a message
lbl = Label(window, text="")
lbl.pack()
#create a new button, and provide an argument called 'command'
#which in this case calls a function called 'callback'
btn =Button(window, text="Click Me", command=callback)
btn.pack()

#draw the window, and start the 'application'
window.mainloop()