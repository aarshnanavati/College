import tkinter as tk
def left_click(event):
    label.config(text=f'Left Click at ({event.x}, {event.y})')
root = tk.Tk()
label = tk.Label(root, text='Click inside', width=40, height=5, bg='lightblue')
label.pack(pady=20)
label.bind('<Button-1>', left_click)
root.mainloop()
