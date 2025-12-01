#  Create a Python program that have two Radiobutton having value as:
# Your Age:
# ● Less than 18
# ● Greater than 18
# When user selects any of the Radiobutton displat proper message in label.
# Note: If user selects Less than 18 than it should give message “You are not eligible for
# voting” and if user selects Greater than 18 than it should give message “ You are eligible
# for voting”

import tkinter as tk

root = tk.Tk()
root.title("Age Eligible")
root.geometry("")

age_var = tk.StringVar(value="None")

def check_age():
    if age_var.get() == "less":
        result_label.config(text="You are not eligible for voting!")
    elif age_var.get() == "greater":
        result_label.config(text="You are eligible for voting!")

heading = tk.Label(root,text="Your Age: ",font=("Arial",12,"bold"))
heading.pack(pady=8)

rb1 = tk.Radiobutton(root,text="Less than 18",variable=age_var,value="less",command=check_age)
rb1.pack(anchor="w",padx=20,pady=5)

rb2 = tk.Radiobutton(root,text="greater than 18",variable=age_var,value="greater",command=check_age)
rb2.pack(anchor="w",padx=20,pady=5)

result_label = tk.Label(root,text="",font=("Arial",11))
result_label.pack(pady=10)

root.mainloop()