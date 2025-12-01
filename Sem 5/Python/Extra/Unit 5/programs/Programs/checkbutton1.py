from tkinter import *
#import tkMessageBox
import tkinter.messagebox
import tkinter

#create a new window
window = tkinter.Tk()
window.geometry("300x300")
var = IntVar()
c = Checkbutton(window, text="Expand", variable=var, onvalue="1", offvalue="0")
c.select()
c.pack()
window.mainloop()
