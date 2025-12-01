import tkinter as tk

def show_selection():
    label.config(text="You selected: " + gender.get())

root = tk.Tk()
root.title("Radio Button Example")

gender = tk.StringVar(value="Male")  # default value

tk.Radiobutton(root, text="Male", variable=gender, value="Male", command=show_selection).pack(anchor="w")
tk.Radiobutton(root, text="Female", variable=gender, value="Female", command=show_selection).pack(anchor="w")
tk.Radiobutton(root, text="Other", variable=gender, value="Other", command=show_selection).pack(anchor="w")

label = tk.Label(root, text="You selected: Male")
label.pack(pady=10)

root.mainloop()
