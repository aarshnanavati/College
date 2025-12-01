import tkinter as tk
def key_pressed(event):
    label.config(text=f'Key Pressed: {event.keysym}')
root = tk.Tk()
label = tk.Label(root, text='Press any key', width=40, height=5, bg='lightgreen')
label.pack(pady=20)
root.bind('<KeyPress>', key_pressed)
root.mainloop()