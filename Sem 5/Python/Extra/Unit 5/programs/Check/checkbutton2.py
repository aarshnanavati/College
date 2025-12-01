import tkinter as tk

def states():
    selected = []
    if var1.get():
        selected.append("Cricket")
    if var2.get():
        selected.append("Reading")

    if selected:
        selection = "You selected: " + ", ".join(selected)
    else:
        selection = "No hobby selected"
    lbl2.config(text=selection)

# create a new window
window = tk.Tk()
window.title("Checkbox Example")
window.geometry("300x300")

lbl = tk.Label(window, text="Your Hobbies:")
lbl.pack(pady=5)

# use IntVar to track state (1 = checked, 0 = unchecked)
var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(window, text="Cricket", variable=var1, onvalue=1, offvalue=0)
c2 = tk.Checkbutton(window, text="Reading", variable=var2, onvalue=1, offvalue=0)
c1.pack()
c2.pack()

lbl2 = tk.Label(window, text="Please select...")
lbl2.pack(pady=5)

b1 = tk.Button(window, text="Quit", command=window.quit)
b2 = tk.Button(window, text="Show", command=states)
b1.pack(pady=5)
b2.pack(pady=5)

window.mainloop()
