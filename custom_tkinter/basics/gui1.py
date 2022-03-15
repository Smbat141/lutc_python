from tkinter import *  # get all objects

# widget = Label(None, text='Hello GUI world!')  # make one
# widget.pack(expand=YES, fill=BOTH)  # arrange it
# widget.mainloop()  # start event loop

# mainloop pseudo code
# def mainloop():
#     while the main window has not been closed:
#         if an event has occurred:
#             run the associated event handler function

# # set text as key
# widget = Label()
# widget['text'] = 'Hello GUI world!'
# widget.pack(side=TOP)
# mainloop()

# # set text with config method
# root = Tk()
# widget = Label(root)
# widget.config(text='Hello GUI world!')
# widget.pack(side=TOP, expand=YES, fill=BOTH)
# root.title('gui1.py')
# root.mainloop()

# # with one line and nostalgia like Lutz said
Label(None, {'text': 'Hello GUI world!', Pack: {'side': 'top'}}).mainloop()