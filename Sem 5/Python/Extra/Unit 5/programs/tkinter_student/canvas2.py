import tkinter as tk

root = tk.Tk()
root.geometry('600x600')
root.title('Canvas Example - Polygon')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

# create a polygon
canvas.create_polygon((100, 300),(200, 200),(300, 300), fill='blue')

root.mainloop()