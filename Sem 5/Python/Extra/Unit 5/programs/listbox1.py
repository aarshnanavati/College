from tkinter import *

root = Tk()
root.title("ListBox")

def onSelect(val):
	sender = val.widget #get the sender of the event. It is our listbox widget
	idx = sender.curselection()  #find out the index of the selected item using the curselection() method. 
	value = sender.get(idx) #actual value is retrieved with the get() method, which takes the index of the item.
	var.set(value)

lang = ['PHP', 'ROR', 'PYTHON', 'ANDROID', 'IOS']
lb = Listbox(root)
for i in lang:
	lb.insert(END,i)
lb.bind("<<ListboxSelect>>",onSelect) #select an item in the listbox, the <<ListboxSelect>> event is generated. We bind the onSelect() method to this event.
lb.pack()
var = StringVar()
lbl = Label(root, textvariable = var)
lbl.pack()
	
root.mainloop()





