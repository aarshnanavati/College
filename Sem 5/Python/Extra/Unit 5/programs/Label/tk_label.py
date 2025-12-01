#import the 'tkinter' module
import tkinter
#import Tkinter as tkinter
#create a new window
window = tkinter.Tk()
window.geometry("300x300")
#create a label widget called 'lbl'

lbl = tkinter.Label(window, text="hello",bg="red", height="200", width="200")
#pack (add) the widget into the window
lbl.pack(padx=100)
#draw the window, and start the 'application'
window.mainloop()
