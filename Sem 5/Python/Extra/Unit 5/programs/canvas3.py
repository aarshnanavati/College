from tkinter import *
import tkinter
root = Tk()
root.geometry('600x600')
root.title('Canvas Example - Polygon')

canvas = Canvas(root, width=600, height=500, bg='white')
canvas.pack(anchor=CENTER, expand=True)
canvas.image=PhotoImage(file='index.png')
canvas.create_image(0,0, image= canvas.image, anchor='nw')
# create a polygon
canvas.create_polygon((200, 400),(300, 300),(400, 400), fill='blue')

#create Text
canvas.create_text(300, 20, text="GOOD MORNING",fill="Red", font=('Helvetica 22 bold'))

canvas.create_line(100, 100,
                     100, 400,
                     fill="green") 

canvas.create_arc(100, 100, 200, 200, start=0, extent=270,
                   fill="red")
 
'''canvas.create_oval(80, 80, 300,
                     150,
                     fill="blue") '''
root.mainloop()







