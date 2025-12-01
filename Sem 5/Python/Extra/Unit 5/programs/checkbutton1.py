#old one
"""
from Tkinter import *
import tkMessageBox
import Tkinter

#create a new window
window = Tkinter.Tk()
window.geometry("300x300")
var = IntVar()
c = Checkbutton(window, text="Expand", variable=var, onvalue="1", offvalue="0")
c.select()
c.pack()
window.mainloop()
"""
#new one
import tkinter as tk
from tkinter import messagebox

def show_state():
    value = var.get()
    print("Checkbutton value:", value)  # prints in console
    messagebox.showinfo("State", f"Checkbutton value = {value}")

root = tk.Tk()
root.title("Tkinter Checkbutton Example")
root.geometry("300x300")

var = tk.IntVar()

c = tk.Checkbutton(root, text="Expand", variable=var, onvalue=1, offvalue=0)
c.select()  # checked by default
c.pack(pady=10)

# button to check state
btn = tk.Button(root, text="Show Value", command=show_state)
btn.pack(pady=10)

root.mainloop()