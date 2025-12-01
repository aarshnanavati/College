"""
import tkinter as tk
root = tk.Tk()
root.title("My First Window")
root.geometry("400x300")
root.mainloop()
"""
"""
import tkinter as tk
root = tk.Tk()
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)
root.mainloop()
"""
"""
import tkinter as tk
def say_hello():
	print("Button Clicked!")
root = tk.Tk()
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=10)
root.mainloop()
"""
"""
import tkinter as tk
root = tk.Tk()
entry = tk.Entry(root, width=30)
entry.pack(pady=5)
text = tk.Text(root, height=5, width=30)
text.pack(pady=5)
root.mainloop()
"""
"""
import tkinter as tk
root = tk.Tk()
var1 = tk.IntVar()
var2 = tk.IntVar()
cb1 = tk.Checkbutton(root, text="Python", variable=var1)
cb2 = tk.Checkbutton(root, text="Java", variable=var2)
cb1.pack()
cb2.pack()
root.mainloop()
"""
"""
import tkinter as tk
root = tk.Tk()
var = tk.StringVar(value="Python")
r1 = tk.Radiobutton(root, text="Python", variable=var, value="Python")
r2 = tk.Radiobutton(root, text="Java", variable=var, value="Java")
r1.pack()
r2.pack()
root.mainloop()
"""
"""
import tkinter as tk
root = tk.Tk()
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text = tk.Text(root, wrap="word", yscrollcommand=scrollbar.set)
text.pack(expand=True, fill="both")
scrollbar.config(command=text.yview)
for i in range(50):
	text.insert(tk.END, f"Line {i+1}\n")
root.mainloop()
"""
"""
import tkinter as tk
root = tk.Tk()
listbox = tk.Listbox(root)
listbox.pack()
for item in ["Python", "Java", "C++", "JavaScript"]:
	listbox.insert(tk.END, item)
root.mainloop()
"""
"""
import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200, bg="lightblue")
canvas.pack()
canvas.create_rectangle(50, 50, 150, 100, fill="red")
canvas.create_oval(50, 120, 150, 180, fill="green")
root.mainloop()
"""

import tkinter as tk
from tkinter import messagebox
def show_msg():
	messagebox.showinfo("Message", "Hello Tkinter!")
root = tk.Tk()
button = tk.Button(root, text="Show Message", command=show_msg)
button.pack()
root.mainloop()

"""
import tkinter as tk
root = tk.Tk()
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New File")
filemenu.add_command(label="Open File")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
menubar.add_cascade(label="Edit", menu=editmenu)
root.config(menu=menubar)
root.mainloop()
"""

