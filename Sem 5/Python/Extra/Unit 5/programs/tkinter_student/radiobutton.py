#from Tkinter import *
#import Tkinter
import tkinter
from tkinter import*
def sel():
	selection = "You selected the option " + str(var.get())
	label.configure(text = selection)

root = tkinter.Tk()
root.geometry("300x300")


var = StringVar()
R1 = Radiobutton(root, text="Male", variable=var, value="Male" ,command=sel)
R1.pack()

R2 = Radiobutton(root, text="Female", variable=var, value="Female" ,command=sel)
R2.pack()


label = Label(root)
label.pack()
root.mainloop()
