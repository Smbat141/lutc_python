"""
show one image with standard tkinter photo object;
as is this handles GIF files, but not JPEG images; image filename listed in
command line, or default; use a Canvas instead of Label for scrolling, etc.
"""
import os, sys
from tkinter import *                    # use standard tkinter photo object
                                         # GIF works, but JPEG requires PIL


imgdir  = '/home/collab06/Pictures/'
imgfile = '2021-03-29_17-46.png'         # random image
if len(sys.argv) > 1:                    # cmdline argument given?
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)        # display photo on a Label
Label(win, image=imgobj).pack()
print(imgobj.width(), imgobj.height())   # show size in pixels before destroyed
win.mainloop()
