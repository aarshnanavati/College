
import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("Canvas example")

canvas = tk.Canvas(root,width=600,height=400,bg="white")
canvas.pack(anchor=tk.CENTER,expand=True)

canvas.create_rectangle((100,100),(300,300),fill="green")

root.mainloop()