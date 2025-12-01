import tkinter as tk
root = tk.Tk()
text = tk.Text(root, wrap='word', width=40, height=10)
scroll = tk.Scrollbar(root, orient='vertical', command=text.yview)
text.configure(yscrollcommand=scroll.set)
text.pack(side='left', fill='both', expand=True)
scroll.pack(side='right', fill='y')
for i in range(1, 51):
    text.insert('end', f'Line {i}\n')
root.mainloop()