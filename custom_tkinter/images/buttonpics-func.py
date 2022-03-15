from tkinter import *  # get base widget set
from glob import glob  # filename expansion list
import random  # pick a picture at random
from custom_tkinter.check_button import demoCheck  # attach checkbutton demo to me

pngdir = '/home/collab06/Pictures/'  # where to look for GIF files


def draw():
    name, photo = random.choice(images)
    lbl.config(text=name)
    pix.config(image=photo)


root = Tk()
lbl = Label(root, text="none", bg='blue', fg='red')
pix = Button(root, text="Press me", command=draw, bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)
demoCheck.Demo(root, relief=SUNKEN, bd=2).pack(fill=BOTH)

files = glob(pngdir + "*.png")  # PNGs for now
images = [(x, PhotoImage(file=x)) for x in files]  # load and hold
print(files)
root.mainloop()
