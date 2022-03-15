from tkinter import *
import sys

widget = Button(None, text='Hello widget world', command=sys.exit)
# widget.pack()
# widget.mainloop()

# #button with root.quit method as <command> keyword parameter
root = Tk()
# Button(root, text='press', command=root.quit).pack(side=LEFT, expand=YES)
# # with fill=X argument
# Button(root, text='press', command=root.quit).pack(side=LEFT, expand=YES, fill=X)
# # with full window of button
Button(root, text='press', command=root.quit).pack(expand=YES, fill=BOTH)
root.mainloop()
