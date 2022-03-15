from tkinter import *


def greeting():
    print('Hello stdout world!...')


win = Frame()
# win.pack()
win.pack(side=TOP, expand=YES, fill=BOTH)


# Label(win, text='Hello container world').pack(side=TOP)
# Button(win, text='Hello', command=greeting).pack(side=LEFT)
# Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

# # try with another order
# Button(win, text='Hello', command=greeting).pack(side=LEFT)
# Label(win, text='Hello container world').pack(side=TOP)
# Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

# Button(win, text='Hello', command=greeting).pack(side=LEFT, fill=Y)
# Label(win, text='Hello container world').pack(side=TOP)
# Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=YES, fill=X)

# # anchors instead of fill
Button(win, text='Hello', command=greeting).pack(side=LEFT, anchor=SW)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)

win.mainloop()
