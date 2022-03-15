import sys
from tkinter import *
from slideShow import SlideShow

if len(sys.argv) == 2:
    picdir = sys.argv[1]
else:
    picdir = '/home/collab06/projects/lutc_python/9780596158118/PP4E-Examples-1.4/Examples/PP4E/Gui/gifs'

root = Tk()
Label(root, text="Two embedded slide shows: Frames").pack()
SlideShow(parent=root, picdir=picdir, bd=3, relief=SUNKEN).pack(side=LEFT)
SlideShow(parent=root, picdir=picdir, bd=3, relief=SUNKEN).pack(side=RIGHT)
root.mainloop()
