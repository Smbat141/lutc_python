"""
FAILS! -- tkinter doesn't support parallel GUI updates in threads
"""

import _thread, threading, os
from tkinter import *
from custom_tkinter.dialogs import demoDlg
from custom_tkinter.check_button import demoCheck
from custom_tkinter.radio_button import demoRadio
from custom_tkinter.scale import demoScale

demoModules = [demoDlg, demoCheck, demoRadio, demoScale]  # changed from lutz version


def makePopups(modnames):
    demoObjects = []
    for modname in modnames:
        _thread.start_new_thread(build, (modname,))
        # threading.Thread(target=build, args=(modname,)).start()
        # build(modname)
    return demoObjects


def build(module):
    print(threading.get_ident(), os.getpid(), sep="&")
    window = Toplevel()  # make a new window
    demo = module.Demo(window)                          # parent is the new window
    window.title(module.__name__)
    # demoObjects.append(demo)


def allstates(demoObjects):
    for obj in demoObjects:
        if hasattr(obj, 'report'):
            print(obj.__module__, end=' ')
            obj.report()


root = Tk()                                             # make explicit root first
root.title('Popups')
demos = makePopups(demoModules)
Label(root, text='Multiple Toplevel window demo', bg='white').pack()
Button(root, text='States', command=lambda: allstates(demos)).pack(fill=X)
root.mainloop()
