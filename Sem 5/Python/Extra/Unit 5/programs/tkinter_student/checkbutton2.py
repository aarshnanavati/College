'''from Tkinter import *
import tkMessageBox
import Tkinter'''
import tkinter
from tkinter import*

def states():
	#print("Male{0}: \n Female{0} ",(var1.get(), var2.get()))
	selection = "You selected" + str(var1.get())
	lbl2.config(text=selection)
	
#create a new window
window = tkinter.Tk()
window.geometry("300x300")
lbl=Label(window, text="Your Hobbies:")
var1 = StringVar()
c1 = Checkbutton(window, text="Cricket",  variable=var1)
var2 = StringVar()
c2 = Checkbutton(window, text="Reading", variable=var2)
lbl2=Label(window, text="Pls select...")
b1= Button(window, text="Quit", command=window.quit)
b2= Button(window, text="Show", command=states)
lbl.pack()
lbl2.pack()
c1.pack()
c2.pack()
b1.pack()
b2.pack()
window.mainloop()
