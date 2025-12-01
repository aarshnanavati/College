import tkinter as tk
def window_resized(event):
    label.config(text=f'Window size: {event.width}x{event.height}')
root = tk.Tk()
label = tk.Label(root, text='Resize the window')
label.pack(pady=20)
root.bind('<Configure>', window_resized)
root.mainloop()