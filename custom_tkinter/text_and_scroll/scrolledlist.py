"a simple customizable scrolled listbox component"

from tkinter import *


class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                        # make me expandable
        self.makeWidgets(options)

    def handleList(self, event):
        index = self.listbox.curselection()                     # on list double-click
        label = self.listbox.get(index)                         # fetch selection text
        self.runCommand(label)                                  # and call action here
        # or get(ACTIVE)

        # selections = self.listbox.curselection()              # use for multiple select only
        # selections = [int(x) + 1 for x in selections]         # tuple of digit strs, 0..N-1
        # self.runCommand(selections)

    def makeWidgets(self, options):
        # # with vertical and horizontal scrolls
        # vscroll = Scrollbar(self)
        # hscroll = Scrollbar(self, orient='horizontal')
        # listbox = Listbox(self)
        #
        # # move listbox when scroll moved
        # vscroll.config(command=listbox.yview, relief=SUNKEN)
        # hscroll.config(command=listbox.xview, relief=SUNKEN)
        # # move scroll when listbox moved
        # listbox.config(yscrollcommand=vscroll.set, relief=SUNKEN)
        # listbox.config(xscrollcommand=hscroll.set)
        # vscroll.pack(side=RIGHT, fill=Y)
        # hscroll.pack(side=BOTTOM, fill=X)
        # listbox.pack(side=LEFT, expand=YES, fill=BOTH)

        # # with vertical scroll
        sbar = Scrollbar(self)
        list = Listbox(self, relief=SUNKEN)
        sbar.config(command=list.yview)  # xlink sbar and list
        list.config(yscrollcommand=sbar.set)  # move one moves other
        sbar.pack(side=RIGHT, fill=Y)  # pack first=clip last
        list.pack(side=LEFT, expand=YES, fill=BOTH)  # list clipped first
        pos = 0
        for label in options:  # add to listbox
            list.insert(pos, label)  # or insert(END,label)
            pos += 1  # or enumerate(options)
        # list.config(selectmode=EXTENDED, setgrid=1)               # select,resize modes
        list.bind('<Double-1>', self.handleList)                    # set event handler
        self.listbox = list

    def runCommand(self, selection):                                # redefine me lower
        print('You selected:', selection)


if __name__ == '__main__':
    options = (('Lumberjack-%s' % x) for x in range(20))  # or map/lambda, [...]
    ScrolledList(options).mainloop()
