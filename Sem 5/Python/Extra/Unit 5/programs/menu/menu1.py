import tkinter as tk
def new_file():
    label.config(text='New File created!')
def exit_app():
    root.destroy()
root = tk.Tk()
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit_app)
label = tk.Label(root, text='Use the menu to create or exit')
label.pack(pady=20)
root.mainloop()
