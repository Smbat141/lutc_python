"""
show one image with PIL photo replacement object
handles many more image types; install PIL first: placed in Lib\site-packages
"""

import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage  # <== use PIL replacement class

# rest of code unchanged

imgdir = '/home/collab06/Pictures/'
imgfile = '2021-03-29_17-46.png'  # does gif, jpg, png, tiff, etc.
if len(sys.argv) > 1:
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)  # now JPEGs work!
Label(win, image=imgobj).pack()
win.mainloop()
print(imgobj.width(), imgobj.height())  # show size in pixels on exit
