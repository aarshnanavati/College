from tkinter import *
import tkinter

languages = [("Python"),("Perl"), ("Java"),("C++"),("C")]

root = tkinter.Tk()
root.geometry("300x300")

def ShowChoice():
	choice=v.get()
	print(choice)
	if choice==0:
		print("Python")
	elif choice==1 :
		print("Perl")
	elif choice==2:
		print("Java")
	elif choice==3:
		print("C++")
	else:
		print("C")

lbl=Label(root, text="""Choose your favourite programming language:""",justify =LEFT)
lbl.pack()

v = IntVar()

for val, language in enumerate(languages):
    r1=Radiobutton(root, text=language, padx = 10, variable=v, command=ShowChoice, value=val)
    r1.pack()

root.mainloop()