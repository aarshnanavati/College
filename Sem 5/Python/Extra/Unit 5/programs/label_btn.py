#new one
import tkinter as tk

# create a new window
window = tk.Tk()
window.title("Commands")
window.geometry("300x200")

# function that changes the text of the label
def callback():
    lbl.config(text="Button clicked!")

# label to display a message
lbl = tk.Label(window, text="Nothing happened yet", font=("Arial", 12))
lbl.pack(pady=20)

# button that calls callback function
btn = tk.Button(window, text="Click Me", command=callback)
btn.pack(pady=10)

# run the application
window.mainloop()

#old one
"""
from Tkinter import *
import Tkinter
#create a new window
window = Tkinter.Tk()
#set the window title
window.title("Commands")

#a function that changes the text of the label
def callback():
    lbl.configure(text="Button clicked!")

#create a label to display a message
lbl = Label(window, text="Nothing happened yet")
lbl.pack()

#create a new button, and provide an argument called 'command'
#which in this case calls a function called 'callback'
btn =Button(window, text="Click Me", command=callback)
btn.pack()

#draw the window, and start the 'application'
window.mainloop()
"""