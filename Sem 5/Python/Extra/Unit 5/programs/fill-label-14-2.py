'''Fill: 
If you want to make the widgets as wide as the parent widget, 
you have to use the fill=X option: 
'''
from tkinter import *

root = Tk()
w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=X)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=X, padx=20,side="right")
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X, pady=50,expand=50)
mainloop()



