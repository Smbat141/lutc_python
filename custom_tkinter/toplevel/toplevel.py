import sys
from tkinter import *

# win1 = Toplevel()  # two independent windows
# win2 = Toplevel()  # but part of same process
#
# Button(win1, text='Spam', command=sys.exit).pack()
# Button(win2, text='SPAM', command=sys.exit).pack()
# Label(text='Popups').pack()  # on default Tk() root window
# win1.mainloop()

# # with multiple root parents (Tk)
NoDefaultRoot()
win1 = Tk()
win2 = Tk()
# two independent root windows
but1 = Button(win1, text='Spam', command=win1.destroy)
but1.master.title("through child")  # set parent title
but1.pack()
Button(win2, text='SPAM', command=win2.destroy).pack()
win1.mainloop()
