from tkinter import *
root = Tk()
root.geometry('180x200')
listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)
# Inserting the listbox items
listbox.insert(1, "Data Structure")
listbox.insert(2, "Algorithm")
listbox.insert(3, "Data Science")
listbox.insert(4, "Machine Learning")
listbox.insert(5, "Blockchain")
def selected_item():
	for i in listbox.curselection():	
		print(listbox.get(i))
def delete_item():
	listbox.delete(listbox.curselection())
btn = Button(root, text='Print Selected', command=selected_item)
btn1 = Button(root, text='Delete Selected', command=delete_item)
btn.pack()
btn1.pack()
listbox.pack()
root.mainloop()
