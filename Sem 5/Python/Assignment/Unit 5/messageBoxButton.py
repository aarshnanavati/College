
import tkinter as tk
from tkinter import messagebox

def on_click():
    messagebox.showinfo("Hello","You clicked the button!")

root = tk.Tk()
root.title("Button+Messagebox")
root.geometry("300x150")
btn = tk.Button(root,text="click me",command=on_click)
btn.pack(expand=True,pady=30)
root.mainloop()