from tkinter import *
from sys import exit


class Hello(Frame):  # an extended Frame
    def __init__(self, parent=None):
        Frame.__init__(self, parent)  # do superclass init
        self.pack()
        self.data = 0
        self.make_widgets()  # attach widgets to self

    def make_widgets(self):
        widget = Button(self, text='Hello frame world!', command=self.message)
        widget.pack(side=LEFT)

    def message(self):
        self.data += 1
        print('Hello frame world %s!' % self.data)


# if __name__ == '__main__': Hello().mainloop()

###################################################################################################
# # components inheritance example

# parent = Frame(None)  # make a container widget
# parent.pack()
# Hello(parent).pack(side=RIGHT)  # attach Hello instead of running it
#
# Button(parent, text='Attach', command=exit).pack(side=LEFT)
# parent.mainloop()


# class HelloContainer(Frame):
#     def __init__(self, parent=None):
#         Frame.__init__(self, parent)
#         self.pack()
#         self.makeWidgets()
#
#     def makeWidgets(self):
#         Hello(self).pack(side=RIGHT)  # attach a Hello to me
#         Button(self, text='Attach', command=self.quit).pack(side=LEFT)
#
#
# if __name__ == '__main__': HelloContainer().mainloop()


class HelloExtender(Hello):
    def make_widgets(self):  # extend method here
        Hello.make_widgets(self)
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)

    def message(self):
        print('hello', self.data)  # redefine method here


if __name__ == '__main__': HelloExtender().mainloop()
