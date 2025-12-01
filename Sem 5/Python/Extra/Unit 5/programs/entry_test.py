#new one
import tkinter as tk

def show():
    # create display string
    disp = "Hi " + var1.get() + " " + var2.get()
    lbl3.config(text=disp)

# main window
root = tk.Tk()
root.title("Greeting Form")
root.geometry("300x300")

# labels
lbl1 = tk.Label(root, text="First Name")
lbl2 = tk.Label(root, text="Last Name")
lbl1.pack(pady=5)
lbl2.pack(pady=5)

# variables & entry fields
var1 = tk.StringVar()
var2 = tk.StringVar()

e1 = tk.Entry(root, textvariable=var1)
e2 = tk.Entry(root, textvariable=var2)
e1.pack(pady=5)
e2.pack(pady=5)

# buttons
b1 = tk.Button(root, text='Quit', command=root.quit)
b2 = tk.Button(root, text='Show', command=show)
b1.pack(pady=5)
b2.pack(pady=5)

# result label
lbl3 = tk.Label(root, font=("Arial", 12), fg="blue")
lbl3.pack(pady=10)

# run
root.mainloop()


#old one
"""
from Tkinter import *
import Tkinter

def show():
   #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   disp = "Hi " + str(var1.get()) + str(var2.get())
   #print(disp)
   lbl3.configure(text = disp)

root = Tkinter.Tk()
root.geometry("300x300")

lbl1=Label(root, text="First Name")
lbl2=Label(root, text="Last Name")
lbl1.pack()
lbl2.pack()

var1 = StringVar()
var2 = StringVar()

e1 = Entry(root, textvariable=var1)
e2 = Entry(root, textvariable=var2)
e1.pack()
e2.pack()

b1=Button(root, text='Quit', command=root.quit)
b2=Button(root, text='Show', command=show)
b1.pack()
b2.pack()

lbl3 = Label(root)
lbl3.pack()

mainloop( )
"""