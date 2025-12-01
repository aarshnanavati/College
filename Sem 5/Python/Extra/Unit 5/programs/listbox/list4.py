from tkinter import *

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)
mainloop()

listbox.delete(0, END)
listbox.insert(END, newitem)
lb = Listbox(master)
b = Button(master, text="Delete",
           command=lambda lb=lb: lb.delete(ANCHOR))