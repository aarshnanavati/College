from tkinter import *
#import tkMessageBox
import tkinter
#www.plus2net.com
#https://www.plus2net.com/python/tkinter-listbox.php
'''top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()
top.mainloop()

my_w = Tk()
my_w.geometry("500x300")  # Size of the window 

l1 = Listbox(my_w,height=3)
l1.grid(row=1,column=1) 

l1.insert(1,'PHP')   # Adding one element to Listbox 
l1.insert(2,'Python')
l1.insert(3,'MySQL')

my_w.mainloop()  '''
my_w = Tk()
my_w.geometry("500x500")  # Size of the window 

l1 = Listbox(my_w)
l1.grid(row=1,column=1) 

l1.insert(1,'PHP')   # Adding one element to Listbox 
l1.insert(2,'Python')
l1.insert(3,'MySQL')

print(l1.get(0))  # Output PHP
print(l1.get(2))  # Output MySQL

my_w.mainloop()  # Keep the window open









