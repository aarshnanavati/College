#import the 'tkinter' module
import Tkinter
import Tkinter as tkinter
#create a new window
window = tkinter.Tk()
window.geometry("300x300")
#create a label widget called 'lbl'
lbl = tkinter.Label(window, text="Label",activebackground="00ffff")
#pack (add) the widget into the window
lbl.pack()

#draw the window, and start the 'application'
window.mainloop()
