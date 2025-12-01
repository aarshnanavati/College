
import tkinter as tk

def choose_color(c):
    display_label.config(text = c.upper(),bg = c, fg="white" if c not in ("yellow","pink","orange")else "black")

root = tk.Tk()
root.title("Colors")
root.geometry("220x320")

display_label = tk.Label(root,text="choose a color",font=("Arial",12,"bold"),width=20,height=2)
display_label.pack(pady=10)

colors = ["red","yellow","green","pink","purple","orange","blue"]

for col in colors:
    b = tk.Button(root,text=col.capitalize(),bg=col,width=18,command=lambda c=col:choose_color(c))
    b.pack(pady=3)

root.mainloop()