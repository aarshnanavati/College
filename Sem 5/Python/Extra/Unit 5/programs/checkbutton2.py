from tkinter import *
import tkinter.messagebox

def states():
    print("Male: {}\nFemale: {}".format(var1.get(), var2.get()))
    selection = "You selected " + ("Male" if var1.get() else "") + ("Female" if var2.get() else "")

#create a new window
window = Tk()
window.geometry("300x300")
lbl=Label(window, text="Your Gender:")
var1 = IntVar()
c1 = Checkbutton(window, text="Male", variable=var1 )
#var1_text = StringVar()
#var1_text.set("Male")

var2 = IntVar()
c2 = Checkbutton(window, text="Female", variable=var2)
#var2_text = StringVar()
#var2_text.set("")

lbl2=Label(window, text="Pls select...")
b1= Button(window, text="Quit", command=window.quit)
b2= Button(window, text="Show", command=states)
lbl.pack()
lbl2.pack()
c1.pack()
c2.pack()
b1.pack()
b2.pack()
window.mainloop()
