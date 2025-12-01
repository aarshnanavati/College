from tkinter import *
import tkinter
root = Tk()
text1 = Text(root, height=20, width=30)
photo=PhotoImage(file='index.png')
text1.insert(END,'\n')
text1.image_create(END, image=photo)
text1.pack(side=LEFT)

text2 = Text(root, height=20, width=50)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('color', foreground='#476042', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.insert(END,'\nWilliam Shakespeare\n', 'big')
quote = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
William Shakespeare (baptized on April 26, 1564 to April 23, 1616)
was an English playwright, actor and poet also known as the
"Bard of Avon" and often called England's national poet. 
Born in Stratford-upon-Avon, England, he was an important
member of the Lord Chamberlain's Men company of theatrical
players from roughly 1594 onward. Written records give little 
indication of the way in which Shakespeare's professional life 
molded his artistry. All that can be deduced is that, in his 20 years
as a playwright, Shakespeare wrote plays that capture the complete 
range of human emotion and conflict.
"""
text2.insert(END, quote, 'color')
text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()

