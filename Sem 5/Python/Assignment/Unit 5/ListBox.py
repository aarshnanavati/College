# Create a Python program that displays following output. Create Listbox, whenever user
# selects any option its value is printed on the label.

import tkinter as tk

root = tk.Tk()
root.title("example")
root.geometry("300x300")

def show_Selected(event):
    selected_index=listbox.curselection()
    if selected_index:
        value = listbox.get(selected_index)
        label.config(text="You selected "+value)

listbox = tk.Listbox(root,height=20,width=20)
listbox.pack(pady=15)

items = ["PHP","ROR","PYTHON","ANDROID","IOS"]
for item in items:
    listbox.insert(tk.END,item)

label = tk.Label(root, text="Select an item from the list", font=("Arial", 11))
label.pack(pady=10)

# Step 5: Bind the selection event
listbox.bind("<<ListboxSelect>>", show_Selected)

# Step 6: Start GUI loop
root.mainloop()

