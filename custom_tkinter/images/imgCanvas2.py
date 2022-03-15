from sys import argv
from tkinter import *

filename = argv[1] if len(argv) > 1 else 'python.png'  # name on cmdline?
win = Tk()
img = PhotoImage(file=filename)
can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())     # size to img size
can.create_image(2, 2, image=img, anchor=NW)
win.mainloop()
