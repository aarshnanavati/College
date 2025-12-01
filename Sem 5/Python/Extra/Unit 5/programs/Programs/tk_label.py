#import the 'tkinter' module
import tkinter
import tkinter as tkinter
#create a new window
window = tkinter.Tk()
window.geometry("300x300")
#create a label widget called 'lbl'
lbl = tkinter.Label(window, text="Label")
#pack (add) the widget into the window
lbl.pack()

#draw the window, and start the 'application'
window.mainloop()
