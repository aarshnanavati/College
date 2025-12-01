from Tkinter import *

root = Tk()
S = Scrollbar(root)
T = Text(root, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = StringVar()
quote = """I have a simple rule to go with all my awesome dolphin sightings in the water: never surf a wave when you
know they're cruising the lineup. They're the coolest creatures ever, I love them to pieces and find them completely fascinating
and beautiful in every way possible. But geez they're wave hogs. The odds of this happening are slim to none when you find
yourself partywaving with a dolphin, but ask this kid if he wants to do it again. I have a simple rule to go with all my awesome
dolphin sightings in the water: never surf a wave when you know they're cruising the lineup. They're the coolest creatures
ever, I love them to pieces and find them completely fascinating and beautiful in every way possible. But geez they're wave hogs.
The odds of this happening are slim to none when you find yourself partywaving with a dolphin, but ask this kid if he
wants to do it again.I have a simple rule to go with all my awesome dolphin sightings in the water: never surf a wave when you
know they're cruising the lineup. They're the coolest creatures ever, I love them to pieces and find them completely fascinating
and beautiful in every way possible. But geez they're wave hogs. The odds of this happening are slim to none when you find
yourself partywaving with a dolphin, but ask this kid if he wants to do it again."""
T.insert(END, quote)
mainloop(  )

