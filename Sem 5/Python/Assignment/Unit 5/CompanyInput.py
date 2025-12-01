import tkinter as tk

def show_details():
    fn = e_first.get().strip()
    ln = e_last.get().strip()
    des = e_desig.get().strip()
    comp = e_company.get().strip()
    country = e_country.get().strip()

    text = (f"First Name: {fn or '(not provided)'}\n"
            f"Last Name: {ln or '(not provided)'}\n"
            f"Designation: {des or '(not provided)'}\n"
            f"Company: {comp or '(not provided)'}\n"
            f"Country: {country or '(not provided)'}")
    result_label.config(text=text)

root = tk.Tk()
root.title("User Details Form")
root.geometry("420x260")

# Form labels and entries
tk.Label(root, text="First Name:").grid(row=0, column=0, padx=10, pady=6, sticky="e")
e_first = tk.Entry(root, width=30); e_first.grid(row=0, column=1, pady=6)

tk.Label(root, text="Last Name:").grid(row=1, column=0, padx=10, pady=6, sticky="e")
e_last = tk.Entry(root, width=30); e_last.grid(row=1, column=1, pady=6)

tk.Label(root, text="Designation:").grid(row=2, column=0, padx=10, pady=6, sticky="e")
e_desig = tk.Entry(root, width=30); e_desig.grid(row=2, column=1, pady=6)

tk.Label(root, text="Company:").grid(row=3, column=0, padx=10, pady=6, sticky="e")
e_company = tk.Entry(root, width=30); e_company.grid(row=3, column=1, pady=6)

tk.Label(root, text="Country:").grid(row=4, column=0, padx=10, pady=6, sticky="e")
e_country = tk.Entry(root, width=30); e_country.grid(row=4, column=1, pady=6)

# Buttons
tk.Button(root, text="Quit", width=10, command=root.destroy).grid(row=5, column=0, pady=12)
tk.Button(root, text="Show", width=10, command=show_details).grid(row=5, column=1, pady=12)

# Label to display result (multi-line)
result_label = tk.Label(root, text="", justify="left", anchor="w")
result_label.grid(row=6, column=0, columnspan=2, padx=12, sticky="w")

root.mainloop()
