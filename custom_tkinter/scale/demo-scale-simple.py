from tkinter import *


root = Tk()
scl = Scale(root, from_=-100, to=100, tickinterval=50, resolution=10)
scl.pack(expand=YES)


def report():
    print(scl.get())


Button(root, text='state', command=report).pack(side=RIGHT)
root.mainloop()

# # sync without variables
# def sync1(x):
#     scl2.set(x)
#
#
# def sync2(x):
#     scl1.set(x)
#
#
# root = Tk()
# scl1 = Scale(root, from_=-100, to=100, tickinterval=50, resolution=10, command=sync1)
# scl2 = Scale(root, from_=-100, to=100, tickinterval=50, resolution=10, command=sync2, orient='horizontal')
#
# scl1.pack()
# scl2.pack()
# root.mainloop()
