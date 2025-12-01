#import the 'tkinter' module
#import tkFont
import tkinter
#import Tkinter as tkinter
#create a new window
window = tkinter.Tk()
window.geometry("300x300")
#create a label widget called 'lbl'
lbl = tkinter.Label(window, text="Label\nhello to all\ngood evening",bg="red", bd=10, font=('comic',36, 'bold'),justify="right")
#pack (add) the widget into the window
lbl.pack()

#draw the window, and start the 'application'
window.mainloop()
