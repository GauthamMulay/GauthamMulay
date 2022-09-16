# Import Tkinter
from tkinter import *

# define master
master = Tk()

# Vertical (y) Scroll Bar
scroll = Scrollbar(master)
scroll.pack(side=RIGHT, fill=Y)

# Text Widget
eula = Text(master, wrap=NONE, yscrollcommand=scroll.set)
eula.insert("1.0", "text")
eula.pack(side="left")

# Configure the scrollbars
scroll.config(command=eula.yview)
mainloop()
