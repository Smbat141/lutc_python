# wrap command-line script in GUI redirection tool to pop up its output

from tkinter import *
from packdlg import runPackDialog
from custom_tkinter.chapter_10.guiStreams import redirectedGuiFunc


def runPackDialog_Wrapped():            # callback to run in mytools.py
    redirectedGuiFunc(runPackDialog)    # wrap entire callback handler


if __name__ == '__main__':
    root = Tk()
    Button(root, text='pop', command=runPackDialog_Wrapped).pack(fill=X)
    root.mainloop()
