"create two linked scales used to launch dialog demos"

from tkinter import *                                    # get base widget set
from custom_tkinter.dialogs.dialogTable import demos     # button callback handlers
from custom_tkinter.basics.quitter import Quitter        # attach a quit frame to me


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Scale demos").pack()
        self.var = IntVar()
        Scale(self, label='Pick demo number',
                    command=self.onMove,                   # catch moves
                    variable=self.var,                     # reflects position
                    from_=0, to=len(demos)-1).pack()
        Scale(self, label='Pick demo number',
                    command=self.onMove,                   # catch moves
                    variable=self.var,                     # reflects position
                    from_=0, to=len(demos)-1,
                    length=200, tickinterval=2, resolution=2,
                    showvalue=YES, orient='horizontal').pack() # showvalue=YES(default)
        Quitter(self).pack(side=RIGHT)
        Button(self, text="Run demo", command=self.onRun).pack(side=LEFT)
        Button(self, text="State",    command=self.report).pack(side=RIGHT)

    def onMove(self, value):
        print('in onMove', value)

    def onRun(self):
        pos = self.var.get()
        print('You picked', pos)
        demo = list(demos.values())[pos]    # map from position to value (3.X view)
        print(demo())                       # or demos[ list(demos.keys())[pos] ]()

    def report(self):
        print(self.var.get())


if __name__ == '__main__':
    print(list(demos.keys()))
    Demo().mainloop()
