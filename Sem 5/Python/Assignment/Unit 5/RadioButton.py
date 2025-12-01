import tkinter as tk

root = tk.Tk()
root.title("Choose your favourite porgramming language")
root.geometry("350x260")

selected_lang = tk.StringVar(value="None")

def update_label():
    label.config(text="selected: " +selected_lang.get()) 

langs = ["Python","Perl","Java","C++","C"]
for lang in langs:
    rb = tk.Radiobutton(root,text=lang,variable=selected_lang,value=lang,command=update_label)
    rb.pack(anchor="w",padx=20,pady=2)

label = tk.Label(root,text="selected : none",font=("Arial",11))
label.pack(pady=12)
root.mainloop()