from tkinter import *
import tkinter

def show():
   #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   disp = "Hi " + str(var1.get()) + str(var2.get())
   print(disp)
   lbl3.configure(text = disp)

root = tkinter.Tk()
root.geometry("300x300")

lbl1=Label(root, text="First Name").grid(row=0)
lbl2=Label(root, text="Last Name").grid(row=1)

var1 = StringVar()
var2 = StringVar()

e1 = Entry(root, textvariable=var1)
e2 = Entry(root, textvariable=var2)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1=Button(root, text='Quit', command=root.quit).grid(row=3, column=0)
b2=Button(root, text='Show', command=show).grid(row=3, column=1)


lbl3 = Label(root).grid(row=4, column=0)  # Do not write like this
lbl3 = Label(root)
lbl3.grid(row=4, column=0)

mainloop( )