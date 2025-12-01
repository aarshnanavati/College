# When user clicks on any of the Radiobutton then show its value in the label and when
# user clicks on Quit button than window is closed.

import tkinter as tk
root = tk.Tk()
root.title("Gender Selection")
root.geometry("300x200")

gender = tk.StringVar(value="None")

def show_gender():
    label.config(text="Selected :"+gender.get())

def quit_app():
    root.destroy()

tk.Label(root,text="Select Your Gender:",font=("Arial",12,"bold")).pack(pady=10)

tk.Radiobutton(root,text="Male",variable=gender,value="Male").pack(anchor="w",padx=30)
tk.Radiobutton(root,text="Female",variable=gender,value="Female").pack(anchor="w",padx=30)

tk.Button(root,text="show",command=show_gender).pack(pady=8)
tk.Button(root,text="Quit",command=quit_app).pack(pady=4)

label = tk.Label(root,text="",font=("Arial",11))
label.pack(pady=10)
root.mainloop()