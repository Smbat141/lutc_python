"""
FAILS! -- tkinter doesn't support parallel GUI updates in threads
"""

import _thread, threading, os
from tkinter import *
from custom_tkinter.basics.quitter import Quitter
from custom_tkinter.dialogs import demoDlg
from custom_tkinter.check_button import demoCheck
from custom_tkinter.radio_button import demoRadio
from custom_tkinter.scale import demoScale

demoModules = [demoDlg, demoCheck, demoRadio, demoScale]  # changed from lutz version
parts = []


def addComponents(root):  # changed from lutz version
    for demo in demoModules:
        _thread.start_new_thread(build, (demo,))
        # threading.Thread(target=build, args=(demo,)).start()
        # build(demo)


def build(module):
    print(threading.get_ident(), os.getpid(), sep="&")
    # module = __import__(demo)                     # this has no effect
    part = module.Demo(root)                        # attach an instance
    part.config(bd=2, relief=GROOVE)                # or pass configs to Demo()
    part.pack(side=LEFT, expand=YES, fill=BOTH)     # grow, stretch with window
    parts.append(part)                              # change list in-place


def dumpState():
    for part in parts:                              # run demo report if any
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):
           part.report()
        else:
           print('none')


root = Tk()                                          # make explicit root first
root.title('Frames')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()
