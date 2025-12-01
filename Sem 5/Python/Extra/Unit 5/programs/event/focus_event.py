import tkinter as tk
def got_focus(event):
    status.config(text='Entry is active')
root = tk.Tk()
entry = tk.Entry(root)
entry.pack(pady=10)
status = tk.Label(root, text='Click inside or outside Entry')
status.pack()
entry.bind('<FocusIn>', got_focus)
root.mainloop()