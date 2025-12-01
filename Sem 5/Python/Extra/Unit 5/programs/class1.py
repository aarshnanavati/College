#old one
"""
from Tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
"""
#new one
import tkinter as tk  # modern import

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        # label
        self.label = tk.Label(master, text="This is our first GUI!")
        self.label.pack(pady=10)

        # greet button
        self.greet_button = tk.Button(master, text="Greet", command=self.greet)
        self.greet_button.pack(pady=5)

        # close button
        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack(pady=5)

    def greet(self):
        print("Greetings!")

# create main window
root = tk.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()