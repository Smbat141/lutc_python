# from tkinter import *
# from tkinter.messagebox import showinfo
#
#
# class MyGui(Frame):
#     def __init__(self, parent=None):
#         Frame.__init__(self, parent)
#         button = Button(self, text="Press", command=self.reply)
#         button.pack()
#
#     def reply(self):
#         showinfo(title="popup", message="Button pressed")
#
#
# # if __name__ == "__main__":
# #     window = MyGui()
# #     window.pack()
# #     window.mainloop()
#
# mainwin = Tk()
# # mainwin.iconbitmap('py-blue-trans-out.ico')
# Label(mainwin, text="My first gui file").pack()
#
# popup = Toplevel()
# Label(popup, text="Attach").pack(side=LEFT)
# MyGui(popup).pack(side=RIGHT)
# mainwin.mainloop()
from tkinter import *
import random

fontsize = 30
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'purple']


def onSpam():
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Popup', bg='black', fg=color).pack(fill=BOTH)
    mainLabel.config(fg=color)


def onFlip():
    mainLabel.config(fg=random.choice(colors))
    main.after(250, onFlip)


def onGrow():
    global fontsize
    fontsize += 5
    mainLabel.config(font=('arial', fontsize, 'italic'))
    main.after(100, onGrow)


main = Tk()
mainLabel = Label(main, text='Fun Gui!', relief=RAISED)
mainLabel.config(font=('arial', fontsize, 'italic'), fg='cyan', bg='navy')
mainLabel.pack(side=TOP, expand=YES, fill=BOTH)
Button(main, text='spam', command=onSpam).pack(fill=X)
Button(main, text='flip', command=onFlip).pack(fill=X)
Button(main, text='grow', command=onGrow).pack(fill=X)
main.mainloop()


