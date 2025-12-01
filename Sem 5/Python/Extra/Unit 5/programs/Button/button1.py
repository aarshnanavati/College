'''import Tkinter
import tkMessageBox
import Tkinter as tkinter
for normal tkMessageBox'''
import tkinter
from tkinter import*
from tkinter import messagebox
def hello():
   messagebox.showinfo( "Hello Python", "Hello World")

#create a new window
window = tkinter.Tk()
window.geometry("300x300")
btn=tkinter.Button(window,text="OK",command=hello, height=10, width=10)
btn.pack()
window.mainloop()
