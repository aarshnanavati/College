#old one
"""
import tkinter
import tkMessageBox
import tkinter as tk

def hello():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

#create a new window
window = tk.Tk()
window.geometry("300x300")
btn=tk.Button(window,text="OK",height=10, width=10)
btn.pack()
window.mainloop()
"""
#new one
import tkinter as tk
from tkinter import messagebox

def show_msg():
    messagebox.showinfo("Hello Python", "Hello World")

# create main window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x300")

# create button
button = tk.Button(root, text="OK", height=5, width=10, command=show_msg)
button.pack(pady=20)

# run loop
root.mainloop()
