from tkinter import *

root = Tk()
mbutton = Menubutton(root, text='Food', underline=0)  # the pull-down stands alone
picks = Menu(mbutton)
mbutton.config(menu=picks)
picks.add_command(label='spam', command=root.quit, underline=0) # use shortcut(Alt+f+s)
picks.add_command(label='eggs', command=root.quit)
picks.add_command(label='bacon', command=root.quit)
mbutton.pack()
mbutton.config(bg='white', bd=4, relief=RAISED)
root.mainloop()
