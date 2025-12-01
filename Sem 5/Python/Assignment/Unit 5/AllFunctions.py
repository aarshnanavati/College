# Write a python program to create a Tkinter as below:
# • Name – To take a student name
# • Hobbies – create a check box
# • Listbox - add a option FY, SY and TY
# • Radio button – Male/Female
# Add a submit button to add the details on a label. If Hobbies is not selected then raise an
# exception.

import tkinter as tk
from tkinter import messagebox

def submit_details():
    try:
        name = name_entry.get().strip()
        gender = gender_var.get()
        selected_class = class_listbox.get(tk.ACTIVE)

        hobbies = []
        if hobby1_var.get() == 1:
            hobbies.append("Reading")
        if hobby2_var.get() == 1:
            hobbies.append("Sports")
        if hobby3_var.get() == 1:
            hobbies.append("Music")

        # Raise exception if no hobby selected
        if not hobbies:
            raise ValueError("No hobbies selected!")

        # Display details
        details = f"Name: {name}\nGender: {gender}\nClass: {selected_class}\nHobbies: {', '.join(hobbies)}"
        result_label.config(text=details)

    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Main window
root = tk.Tk()
root.title("Student Information Form")
root.geometry("400x500")

# Name
tk.Label(root, text="Enter Name:").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Gender
tk.Label(root, text="Select Gender:").pack()
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# Hobbies
tk.Label(root, text="Select Hobbies:").pack()
hobby1_var = tk.IntVar()
hobby2_var = tk.IntVar()
hobby3_var = tk.IntVar()

tk.Checkbutton(root, text="Reading", variable=hobby1_var).pack()
tk.Checkbutton(root, text="Sports", variable=hobby2_var).pack()
tk.Checkbutton(root, text="Music", variable=hobby3_var).pack()

# Class Listbox
tk.Label(root, text="Select Class:").pack()
class_listbox = tk.Listbox(root, height=3)
for item in ["FY", "SY", "TY"]:
    class_listbox.insert(tk.END, item)
class_listbox.pack(pady=5)

# Submit button
tk.Button(root, text="Submit", command=submit_details, bg="lightgreen").pack(pady=10)

# Result label
result_label = tk.Label(root, text="", justify="left", font=("Arial", 10))
result_label.pack(pady=10)

root.mainloop()