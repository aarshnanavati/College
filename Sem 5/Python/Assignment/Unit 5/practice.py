import tkinter as tk

root = tk.Tk()
root.title("Choose your fav programming language")
root.geometry("350x260")

selected_lang = tk.StringVar(value="NOne")

def update_label():
    label.config(text = "selected" + selected_lang.get())

langs = ["Python","perl","Java","C++","C"]

for lang in langs:
    rb = tk.Radiobutton(root,text=lang,variable=selected_lang,value=lang,command=update_label)
    rb.pack(anchor="w",padx=20,pady=2)

label = tk.Label(root,text="selected:none")
label.pack(pady=12)
root.mainloop()