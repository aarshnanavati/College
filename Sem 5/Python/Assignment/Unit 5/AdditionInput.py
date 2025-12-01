import tkinter as tk
from tkinter import messagebox

def show_sum():
    try:
        a = float(entry1.get().strip())
        b = float(entry2.get().strip())
        s = a +b 
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, str(s))
        result_entry.config(state="readonly")
    except:
        messagebox.showerror("Invalid Input")
    

root = tk.Tk()
root.title("Add two numbers")
root.geometry("360x150")

tk.Label(root,text="Enter num 1:").grid(row=0,column=0,padx=8,pady=6,sticky="e")
entry1 = tk.Entry(root,width=20)
entry1.grid(row=0,column=1,pady=6)

tk.Label(root,text="Enter number 2: ").grid(row=1,column=0,padx=8,pady=6,sticky="e")
entry2 = tk.Entry(root,width=20)
entry2.grid(row=1,column=1,pady=6)

tk.Label(root,text="The sum is :").grid(row=2,column=0,padx=8,pady=6,sticky="e")
result_entry = tk.Entry(root,width=20,state="readonly")
result_entry.grid(row=2,column=1,pady=6)

tk.Button(root, text="Quit", width=10, command=root.destroy).grid(row=3, column=0, pady=10)
tk.Button(root, text="Show", width=10, command=show_sum).grid(row=3, column=1, pady=10)

root.mainloop()

# row=0,1,2
# col=0,0,0

# row=0,1,2
# col=1,1,1

# import tkinter as tk
# from tkinter import messagebox

# def show_sum():
#     try:
#         a = float(entry1.get())
#         b = float(entry2.get())
#         s = a + b
#         result_entry.config(state="normal")
#         result_entry.delete(0, tk.END)
#         result_entry.insert(0, s)
#         result_entry.config(state="readonly")
#     except:
#         messagebox.showerror("Error", "Please enter valid numbers")

# root = tk.Tk()
# root.title("Add Two Numbers")

# tk.Label(root, text="Number 1:").pack()
# entry1 = tk.Entry(root)
# entry1.pack()

# tk.Label(root, text="Number 2:").pack()
# entry2 = tk.Entry(root)
# entry2.pack()

# tk.Label(root, text="Sum:").pack()
# result_entry = tk.Entry(root, state="readonly")
# result_entry.pack()

# tk.Button(root, text="Show Sum", command=show_sum).pack(pady=5)
# tk.Button(root, text="Quit", command=root.destroy).pack(pady=5)

# root.mainloop()
