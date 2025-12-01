from tkinter import *
import tkinter

languages = [("Python"),("Perl"), ("Java"),("C++"),("C")]
root = tkinter.Tk()
root.geometry("300x300")

def ShowChoice():
	choice=str(v.get())
	print(choice)

lbl=Label(root, text="""Choose your favourite programming language:""",justify =LEFT)
lbl.pack()

v = StringVar()

for val, language in enumerate(languages):
    r1=Radiobutton(root, text=language, padx = 10, variable=v, command=ShowChoice, value=language)
    r1.pack()

root.mainloop()





