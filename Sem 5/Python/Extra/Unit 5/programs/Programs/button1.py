import tkinter
#import tkMessageBox
import tkinter.messagebox
import tkinter as tkinter

def hello():
   tkinter.messagebox.showinfo( "Hello Python", "Hello World")

#create a new window
window = tkinter.Tk()
window.geometry("300x300")
btn=tkinter.Button(window,text="OK",command=hello, height=10, width=10)
btn.pack()
window.mainloop()
