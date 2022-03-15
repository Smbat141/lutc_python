"""
##############################################################################
Start various examples; run me at start time to make them always available.
This file is meant for starting programs you actually wish to use; see
PyDemos for starting Python/Tk demos and more details on program start
options.  Windows usage note: this is a '.py' to show messages in a console
window when run or clicked (including a 10 second pause to make sure it's
visible while gadgets start if clicked).  To avoid Windows console pop up,
run with the 'pythonw' program (not 'python'), rename to '.pyw' suffix,
mark with 'run minimized' window property, or spawn elsewhere (see PyDemos).
##############################################################################
"""

import sys, time, os, time
from tkinter import *
from custom_multiprocessing.launchmodes import PortableLauncher           # reuse program start class
from windows import MainWindow           # reuse window tools: icon, quit


def runImmediate(mytools):
    """
    launch gadget programs immediately
    """
    print('Starting Python/Tk gadgets...')         # msgs to stdout (poss temp)
    for (name, commandLine) in mytools:
        PortableLauncher(name, f"../../9780596158118/PP4E-Examples-1.4/Examples/PP4E/{commandLine}")()     # MY VERSION; call now to start now
    print('One moment please...')
    if sys.platform[:3] == 'win':                  # windows: keep console 10 secs
        for i in range(10):
            time.sleep(1); print('.' * 5 * (i+1))


def runLauncher(mytools):
    """
    pop up a simple launcher bar for later use
    """
    root = MainWindow('PyGadgets PP4E')            # or root = Tk() if prefer
    for (name, commandLine) in mytools:
        b = Button(root, text=name, fg='black', bg='beige', border=2,
                   command=PortableLauncher(name, f"../../9780596158118/PP4E-Examples-1.4/Examples/PP4E/{commandLine}")) # MY VERSION
        b.pack(side=LEFT, expand=YES, fill=BOTH)
    root.mainloop()


mytools = [
    ('PyEdit',   'Gui/TextEditor/textEditor.py'),
    ('PyCalc',   'Lang/Calculator/calculator.py'),
    ('PyPhoto',  'Gui/PIL/pyphoto1.py ../../9780596158118/PP4E-Examples-1.4/Examples/PP4E/Gui/PIL/images'), # MY VERSION
    ('PyMail',   'Internet/Email/PyMailGui/PyMailGui.py'),
    ('PyClock',  'Gui/Clock/clock.py -size 175 -bg white'
                          ' -picture ../../9780596158118/PP4E-Examples-1.4/Examples/PP4E/Gui/gifs/pythonPowered.gif'), # MY VERSION
    ('PyToe',    'Ai/TicTacToe/tictactoe.py'
                          ' -mode Minimax -fg white -bg navy'),
    ('PyWeb',    'LaunchBrowser.pyw'
                          ' -live index.html www.rmi.net/~lutz')]
                         # ' -live ../../9780596158118/PP4E-Examples-1.4/Examples/PP4E/Gui/Internet/Web/PyInternetDemos.html localhost:80')] # MY VERSION
                         #' -file')] # PyInternetDemos assumes local server started

if __name__ == '__main__':
    prestart, toolbar = False, True
    if prestart:
        runImmediate(mytools)
    if toolbar:
        runLauncher(mytools)
