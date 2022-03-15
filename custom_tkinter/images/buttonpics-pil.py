# INSTALLATION PILLOW
# pip3 install Pillow
# sudo apt-get install python3-pil python3-pil.imagetk

from tkinter import *                # get base widget set
from PIL import ImageTk              # overrides tkinter PhotoImage class
from glob import glob                # filename expansion list
from custom_tkinter.check_button import demoCheck  # attach checkbutton demo to me
import random                        # pick a picture at random

pngdir = '/home/collab06/Pictures/'  # default dir to load PNG files


class ButtonPicsDemo(Frame):
    def __init__(self, pngdir=pngdir, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.lbl = Label(self,  text="none", bg='blue', fg='red')
        self.pix = Button(self, text="Press me", command=self.draw, bg='white')
        self.lbl.pack(fill=BOTH)
        self.pix.pack(pady=10)
        demoCheck.Demo(self, relief=SUNKEN, bd=2).pack(fill=BOTH)
        files = glob(pngdir + "*.JPG")
        self.images = [(x, ImageTk.PhotoImage(file=x)) for x in files]
        print(files)

    def draw(self):
        name, photo = random.choice(self.images)
        self.lbl.config(text=name)
        self.pix.config(image=photo, width=200, height=200)


if __name__ == '__main__': ButtonPicsDemo().mainloop()
