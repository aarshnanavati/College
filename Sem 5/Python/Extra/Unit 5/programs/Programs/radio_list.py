from Tkinter import *
import Tkinter

languages = [("Python",1),("Perl",2), ("Java",3),("C++",4),("C",5)]

root = Tkinter.Tk()
root.geometry("300x300")

def ShowChoice():
    print(v.get())

lbl=Label(root, text="""Choose your favourite programming language:""",justify =LEFT)
lbl.pack()

v = StringVar()

for val, language in enumerate(languages):
    r1=Radiobutton(root, text=language, padx = 20, variable=v, command=ShowChoice, value=val)
    r1.pack()

root.mainloop()