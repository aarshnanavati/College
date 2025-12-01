#old name
"""
from Tkinter import *
import Tkinter

def show_entry_fields():
	print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
def del1():
	e1.delete(0,END)
	e2.delete(0,END)

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)
e1.insert(10,"GLS")
e2.insert(10,"University")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1)
Button(master, text='Delete', command=del1).grid(row=3, column=2)


mainloop( )
"""

#new one
import tkinter as tk

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def del1():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

# main window
master = tk.Tk()
master.title("Entry Form")

# labels
tk.Label(master, text="First Name").grid(row=0, column=0, padx=5, pady=5)
tk.Label(master, text="Last Name").grid(row=1, column=0, padx=5, pady=5)

# entry fields
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.insert(0, "GLS")          # insert at beginning
e2.insert(0, "University")

e1.grid(row=0, column=1, padx=5, pady=5)
e2.grid(row=1, column=1, padx=5, pady=5)

# buttons
tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, pady=10)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, pady=10)
tk.Button(master, text='Delete', command=del1).grid(row=3, column=2, pady=10)

# run
master.mainloop()
