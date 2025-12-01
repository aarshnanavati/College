import Tkinter

root = Tkinter.Tk()
s = Tkinter.Scrollbar(root)
T = Tkinter.Text(root)

s.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
T.pack(side=Tkinter.LEFT, fill=Tkinter.Y)
s.config(command=T.yview)
T.config(yscrollcommand=s.set)

for i in range(40): 
   T.insert(Tkinter.END, "%d\n" % i)

Tkinter.mainloop()