from Tkinter import *
import tkMessageBox
import Tkinter

def states():
	#print("Male{0}: \n Female{0} ",(var1.get(), var2.get()))
	selection = "You selected" + str(var1.get())
	lbl2.config(text=selection)
	
#create a new window
window = Tkinter.Tk()
window.geometry("300x300")
lbl=Label(window, text="Your Sex:")
var1 = IntVar()
c1 = Checkbutton(window, text="Male", variable=var1)
var2 = IntVar()
c2 = Checkbutton(window, text="Female", variable=var2)
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