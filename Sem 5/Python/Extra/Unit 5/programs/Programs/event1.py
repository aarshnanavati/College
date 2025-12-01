
from Tkinter import *

def handleButtonPress() :
    """This is the event handler for the button: It copies
       the text typed into the textentry to the label, and it
       clears the textentry.
    """
    message = textentry.get()   # get the text from the textentry
    label.configure(text = message)   # reset the label's text
    textentry.delete(0, END)          # clear the textentry


myfont = ("Arial", 14, "bold")

window = Tk()
window.title("Event Handling")
window.geometry("220x150")

frame = Frame(window)
frame.grid()

textentry = Entry(frame, width = 15, font = myfont, fg = "red")
textentry.grid()

button1 = Button(frame, text = "Copy", command = handleButtonPress,
                 font = myfont, fg = "blue", bg = "yellow")
button1.grid()

label = Label(frame, text = "********", font = myfont)
label.grid()

window.mainloop()
