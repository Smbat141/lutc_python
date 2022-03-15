from tkinter import *


# class HelloButton(Button):
#     def __init__(self, parent=None, **config):  # add callback method
#         Button.__init__(self, parent, **config)
#         self.pack()  # and pack myself
#         self.config(command=self.callback)  # could config style too
#
#     def callback(self):  # default press action
#         print('Goodbye world...')  # replace in subclasses
#         self.quit()
#
#
# if __name__ == '__main__':
#     HelloButton(text='Hello subclass world').mainloop()


# # with styles and themes
class ThemedButton(Button):
    def __init__(self, parent=None, **configs):  # config my style too
        Button.__init__(self, parent, **configs)  # used for each instance
        self.pack()
        self.config(fg='red', bg='black', font=('courier', 12), relief=RAISED, bd=5)


B1 = ThemedButton(text='spam', command=sys.exit)
B2 = ThemedButton(text='eggs')
B2.pack(expand=YES, fill=BOTH)
mainloop()