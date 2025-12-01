from Tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()

text.tag_add("temp", "1.0", "1.4")
text.tag_add("temp1", "1.8", "1.13")
text.tag_config("temp", background="yellow", foreground="blue")
text.tag_config("temp1", background="black", foreground="green")
root.mainloop()