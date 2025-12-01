import tkinter as tk
def show_selection():
    selected = [listbox.get(i) for i in listbox.curselection()]
    label.config(text='You selected: ' + ', '.join(selected))
root = tk.Tk()
listbox = tk.Listbox(root, selectmode='multiple', height=6)
items = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'Go']
for item in items:
    listbox.insert('end', item)
listbox.pack()
tk.Button(root, text='Show Selection', command=show_selection).pack(pady=5)
label = tk.Label(root, text='You selected: None')
label.pack()
root.mainloop()