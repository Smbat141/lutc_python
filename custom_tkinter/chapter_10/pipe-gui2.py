# GUI reader side: like pipes-gui1, but make root window and mainloop explicit

from tkinter import *
from guiStreams import redirectedGuiShellCmd


def launch():
    redirectedGuiShellCmd('python3 -u pipe-nongui.py')


window = Tk()
Button(window, text='GO!', command=launch).pack()
window.mainloop()
