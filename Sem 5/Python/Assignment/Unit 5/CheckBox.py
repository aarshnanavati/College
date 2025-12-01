import tkinter as tk

root = tk.Tk()
root.title("Choose your favourite food")
root.geometry("420x200")

foods={
    "Bananas" :  tk.IntVar(),
    "Chicken" : tk.IntVar(),
    "Stuffed Peppers": tk.IntVar()
}

def update_label():
    selected = [name for name , var in foods.items() if var.get() == 1]
    if selected:
        text = "Selected : " + ",".join(selected)
    else:
        text = "Selected:None"
    label.config(text=text)

frame = tk.Frame(root,padx=20,pady=10)
frame.pack(anchor="w")

for name,var in foods.items():
    cb = tk.Checkbutton(frame,text=name,variable=var,command=update_label)
    cb.pack(side="left",padx=8)

label = tk.Label(root,text="Selected:None",font=("Arial",11))
label.pack(pady=12)
root.mainloop()