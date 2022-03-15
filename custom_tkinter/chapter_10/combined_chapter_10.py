# ::::::::::::::::::::textpak=>big_gui.py
# """
# GUI demo implementation - combines maker, mixin, and this
# """
#
# import sys, os
# from tkinter import *                        # widget classes
# from guimixin import *        # mix-in methods: quit, spawn, etc.
# from guimaker import *        # frame, plus menu/toolbar builder
#
#
# class Hello(GuiMixin, GuiMakerWindowMenu):   # or GuiMakerFrameMenu
#     def start(self):
#         self.hellos = 0
#         self.master.title("GuiMaker Demo")
#         self.master.iconname("GuiMaker")
#         def spawnme(): self.spawn('big_gui.py')        # defer call vs lambda
#
#         self.menuBar = [                               # a tree: 3 pull downs
#           ('File', 0,                                  # (pull-down)
#               [('New...',  0, spawnme),
#                ('Open...', 0, self.fileOpen),          # [menu items list]
#                ('Quit',    0, self.quit)]              # label,underline,action
#           ),
#
#           ('Edit', 0,
#               [('Cut',    -1, self.notdone),           # no underline|action
#                ('Paste',  -1, self.notdone),           # lambda:0 works too
#                'separator',                            # add a separator
#                ('Stuff',  -1,
#                    [('Clone', -1, self.clone),         # cascaded submenu
#                     ('More',  -1, self.more)]
#                ),
#                ('Delete', -1, lambda:0),
#                [5]]                                    # disable 'delete'
#           ),
#
#           ('Play', 0,
#               [('Hello',     0, self.greeting),
#                ('Popup...',  0, self.dialog),
#                ('Demos',     0,
#                   [('Toplevels', 0,
#                        lambda: self.spawn(r'..\Tour\toplevel2.py')),
#                    ('Frames',    0,
#                        lambda: self.spawn(r'..\Tour\demoAll-frm-ridge.py')),
#                    ('Images',    0,
#                        lambda: self.spawn(r'..\Tour\buttonpics.py')),
#                    ('Alarm',     0,
#                        lambda: self.spawn(r'..\Tour\alarm.py', wait=False)),
#                    ('Other...', -1, self.pickDemo)]
#                )]
#           )]
#
#         self.toolBar = [                                     # add 3 buttons
#           ('Quit',  self.quit,     dict(side=RIGHT)),        # or {'side': RIGHT}
#           ('Hello', self.greeting, dict(side=LEFT)),
#           ('Popup', self.dialog,   dict(side=LEFT, expand=YES)) ]
#
#     def makeWidgets(self):                                   # override default
#         middle = Label(self, text='Hello maker world!',      # middle of window
#                        width=40, height=10,
#                        relief=SUNKEN, cursor='pencil', bg='white')
#         middle.pack(expand=YES, fill=BOTH)
#
#     def greeting(self):
#         self.hellos += 1
#         if self.hellos % 3:
#             print("hi")
#         else:
#             self.infobox("Three", 'HELLO!')    # on every third press
#
#     def dialog(self):
#         button = self.question('OOPS!',
#                                'You typed "rm*" ... continue?',  # old style
#                                'questhead', ('yes', 'no'))       # args ignored
#         [lambda: None, self.quit][button]()
#
#     def fileOpen(self):
#         pick = self.selectOpenFile(file='big_gui.py')
#         if pick:
#             self.browser(pick)     # browse my source file, or other
#
#     def more(self):
#         new = Toplevel()
#         Label(new,  text='A new non-modal window').pack()
#         Button(new, text='Quit', command=self.quit).pack(side=LEFT)
#         Button(new, text='More', command=self.more).pack(side=RIGHT)
#
#     def pickDemo(self):
#         pick = self.selectOpenFile(dir='..')
#         if pick:
#             self.spawn(pick)    # spawn any Python program
#
#
# if __name__ == '__main__':  Hello().mainloop()   # make one, run one
# ::::::::::::::::::::textpak=>guimaker.py
# """
# ###############################################################################
# An extended Frame that makes window menus and toolbars automatically.
# Use GuiMakerFrameMenu for embedded components (makes frame-based menus).
# Use GuiMakerWindowMenu for top-level windows (makes Tk8.0 window menus).
# See the self-test code (and PyEdit) for an example layout tree format.
# ###############################################################################
# """
#
# import sys
# from tkinter import *                     # widget classes
# from tkinter.messagebox import showinfo
#
# class GuiMaker(Frame):
#     menuBar    = []                       # class defaults
#     toolBar    = []                       # change per instance in subclasses
#     helpButton = True                     # set these in start() if need self
#
#     def __init__(self, parent=None):
#         Frame.__init__(self, parent)
#         self.pack(expand=YES, fill=BOTH)        # make frame stretchable
#         self.start()                            # for subclass: set menu/toolBar
#         self.makeMenuBar()                      # done here: build menu bar
#         self.makeToolBar()                      # done here: build toolbar
#         self.makeWidgets()                      # for subclass: add middle part
#
#     def makeMenuBar(self):
#         """
#         make menu bar at the top (Tk8.0 menus below)
#         expand=no, fill=x so same width on resize
#         """
#         menubar = Frame(self, relief=RAISED, bd=2)
#         menubar.pack(side=TOP, fill=X)
#
#         for (name, key, items) in self.menuBar:
#             mbutton  = Menubutton(menubar, text=name, underline=key)
#             mbutton.pack(side=LEFT)
#             pulldown = Menu(mbutton)
#             self.addMenuItems(pulldown, items)
#             mbutton.config(menu=pulldown)
#
#         if self.helpButton:
#             Button(menubar, text    = 'Help',
#                             cursor  = 'gumby',
#                             relief  = FLAT,
#                             command = self.help).pack(side=RIGHT)
#
#     def addMenuItems(self, menu, items):
#         for item in items:                     # scan nested items list
#             if item == 'separator':            # string: add separator
#                 menu.add_separator({})
#             elif type(item) == list:           # list: disabled item list
#                 for num in item:
#                     menu.entryconfig(num, state=DISABLED)
#             elif type(item[2]) != list:
#                 menu.add_command(label     = item[0],         # command:
#                                  underline = item[1],         # add command
#                                  command   = item[2])         # cmd=callable
#             else:
#                 pullover = Menu(menu)
#                 self.addMenuItems(pullover, item[2])          # sublist:
#                 menu.add_cascade(label     = item[0],         # make submenu
#                                  underline = item[1],         # add cascade
#                                  menu      = pullover)
#
#     def makeToolBar(self):
#         """
#         make button bar at bottom, if any
#         expand=no, fill=x so same width on resize
#         this could support images too: see Chapter 9,
#         would need prebuilt gifs or PIL for thumbnails
#         """
#         if self.toolBar:
#             toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
#             toolbar.pack(side=BOTTOM, fill=X)
#             for (name, action, where) in self.toolBar:
#                 Button(toolbar, text=name, command=action).pack(where)
#
#     def makeWidgets(self):
#         """
#         make 'middle' part last, so menu/toolbar
#         is always on top/bottom and clipped last;
#         override this default, pack middle any side;
#         for grid: grid middle part in a packed frame
#         """
#         name = Label(self,
#                      width=40, height=10,
#                      relief=SUNKEN, bg='white',
#                      text   = self.__class__.__name__,
#                      cursor = 'crosshair')
#         name.pack(expand=YES, fill=BOTH, side=TOP)
#
#     def help(self):
#         "override me in subclass"
#         showinfo('Help', 'Sorry, no help for ' + self.__class__.__name__)
#
#     def start(self):
#         "override me in subclass: set menu/toolbar with self"
#         pass
#
#
# ###############################################################################
# # Customize for Tk 8.0 main window menu bar, instead of a frame
# ###############################################################################
#
# GuiMakerFrameMenu = GuiMaker           # use this for embedded component menus
#
# class GuiMakerWindowMenu(GuiMaker):    # use this for top-level window menus
#     def makeMenuBar(self):
#         menubar = Menu(self.master)
#         self.master.config(menu=menubar)
#
#         for (name, key, items) in self.menuBar:
#             pulldown = Menu(menubar)
#             self.addMenuItems(pulldown, items)
#             menubar.add_cascade(label=name, underline=key, menu=pulldown)
#
#         if self.helpButton:
#             if sys.platform[:3] == 'win':
#                 menubar.add_command(label='Help', command=self.help)
#             else:
#                 pulldown = Menu(menubar)  # Linux needs real pull down
#                 pulldown.add_command(label='About', command=self.help)
#                 menubar.add_cascade(label='Help', menu=pulldown)
#
#
# ###############################################################################
# # Self-test when file run standalone: 'python guimaker.py'
# ###############################################################################
#
# if __name__ == '__main__':
#     from guimixin import GuiMixin            # mix in a help method
#
#     menuBar = [
#         ('File', 0,
#             [('Open',  0, lambda:0),         # lambda:0 is a no-op
#              ('Quit',  0, sys.exit)]),       # use sys, no self here
#         ('Edit', 0,
#             [('Cut',   0, lambda:0),
#              ('Paste', 0, lambda:0)]) ]
#     toolBar = [('Quit', sys.exit, {'side': LEFT})]
#
#     class TestAppFrameMenu(GuiMixin, GuiMakerFrameMenu):
#         def start(self):
#             self.menuBar = menuBar
#             self.toolBar = toolBar
#
#     class TestAppWindowMenu(GuiMixin, GuiMakerWindowMenu):
#         def start(self):
#             self.menuBar = menuBar
#             self.toolBar = toolBar
#
#     class TestAppWindowMenuBasic(GuiMakerWindowMenu):
#         def start(self):
#             self.menuBar = menuBar
#             self.toolBar = toolBar    # guimaker help, not guimixin
#
#     root = Tk()
#     TestAppFrameMenu(Toplevel())
#     TestAppWindowMenu(Toplevel())
#     TestAppWindowMenuBasic(root)
#     root.mainloop()
# ::::::::::::::::::::textpak=>guimixin.py
# """
# ###############################################################################
# a "mixin" class for other frames: common methods for canned dialogs,
# spawning programs, simple text viewers, etc; this class must be mixed
# with a Frame (or a subclass derived from Frame) for its quit method
# ###############################################################################
# """
#
# from tkinter import *
# from tkinter.messagebox import *
# from tkinter.filedialog import *
# from custom_tkinter.text_and_scroll.scrolledtext import ScrolledText     # or tkinter.scrolledtext
# from custom_multiprocessing.launchmodes import PortableLauncher, System  # or use multiprocessing
#
#
# class GuiMixin:
#     def infobox(self, title, text, *args):                               # use standard dialogs
#         return showinfo(title, text)                                     # *args for bkwd compat
#
#     def errorbox(self, text):
#         showerror('Error!', text)
#
#     def question(self, title, text, *args):
#         return askyesno(title, text)                                     # return True or False
#
#     def notdone(self):
#         showerror('Not implemented', 'Option not available')
#
#     def quit(self):
#         ans = self.question('Verify quit', 'Are you sure you want to quit?')
#         if ans:
#             Frame.quit(self)                                             # quit not recursive!
#
#     def help(self):
#         self.infobox('RTFM', 'See figure 1...')                          # override this better
#
#     def selectOpenFile(self, file="", dir="."):                          # use standard dialogs
#         return askopenfilename(initialdir=dir, initialfile=file)
#
#     def selectSaveFile(self, file="", dir="."):
#         return asksaveasfilename(initialfile=file, initialdir=dir)
#
#     def clone(self, args=()):                                            # optional constructor args
#         new = Toplevel()                                                 # make new in-process version of me
#         myclass = self.__class__                                         # instance's (lowest) class object
#         myclass(new, *args)                                              # attach/run instance to new window
#
#     def spawn(self, pycmdline, wait=False):
#         if not wait:  # start new process
#             PortableLauncher(pycmdline, pycmdline)()                     # run Python progam
#         else:
#             System(pycmdline, pycmdline)()                               # wait for it to exit
#
#     def browser(self, filename):
#         new = Toplevel()                                                 # make new window
#         view = ScrolledText(new, file=filename)                          # Text with Scrollbar
#         view.text.config(height=30, width=85)                            # config Text in Frame
#         view.text.config(font=('courier', 10, 'normal'))                 # use fixed-width font
#         new.title("Text Viewer")                                         # set window mgr attrs
#         new.iconname("browser")                                          # file text added auto
#
#     """
#     def browser(self, filename):                         # if tkinter.scrolledtext
#         new  = Toplevel()                                # included for reference
#         text = ScrolledText(new, height=30, width=85)
#         text.config(font=('courier', 10, 'normal'))
#         text.pack(expand=YES, fill=BOTH)
#         new.title("Text Viewer")
#         new.iconname("browser")
#         text.insert('0.0', open(filename, 'r').read() )
#     """
#
#
# if __name__ == '__main__':
#     class TestMixin(GuiMixin, Frame):  # standalone test
#         def __init__(self, parent=None):
#             Frame.__init__(self, parent)
#             self.pack()
#             Button(self, text='quit', command=self.quit).pack(fill=X)
#             Button(self, text='help', command=self.help).pack(fill=X)
#             Button(self, text='clone', command=self.clone).pack(fill=X)
#             Button(self, text='spawn', command=self.other).pack(fill=X)
#
#         def other(self):
#             self.spawn('guimixin.py')                                    # spawn self as separate process
#
#
#     TestMixin().mainloop()
# ::::::::::::::::::::textpak=>mytools.py
# #!/usr/bin/python3
# """
# ################################################################################
# provide type-specific option sets for application
# ################################################################################
# """
#
# from shellgui import *                 # type-specific option gui
# from custom_tkinter.ShellGui.packdlg  import runPackDialog     # dialogs for data entry
# from custom_tkinter.ShellGui.unpkdlg  import runUnpackDialog   # they both run app classes
#
#
# class TextPak1(ListMenuGui):
#     def __init__(self):
#         self.myMenu = [('Pack  ', runPackDialog),      # simple functions
#                        ('Unpack', runUnpackDialog),    # use same width here
#                        ('Mtool ', self.notdone)]       # method from guimixin
#         ListMenuGui.__init__(self)
#
#     def forToolBar(self, label):
#         return label in {'Pack  ', 'Unpack'}           # 3.x set syntax
#
#
# class TextPak2(DictMenuGui):
#     def __init__(self):
#         self.myMenu = {'Pack  ': runPackDialog,        # or use input here...
#                        'Unpack': runUnpackDialog,      # instead of in dialogs
#                        'Mtool ': self.notdone}
#         DictMenuGui.__init__(self)
#
#
# if __name__ == '__main__':                           # self-test code...
#     from sys import argv                             # 'menugui.py list|^'
#     if len(argv) > 1 and argv[1] == 'list':
#         print('list test')
#         TextPak1().mainloop()
#     else:
#         print('dict test')
#         TextPak2().mainloop()
# ::::::::::::::::::::textpak=>shellgui.py
# #!/usr/bin/python3
# """
# ################################################################################
# tools launcher; uses guimaker templates, guimixin std quit dialog;
# I am just a class library: run mytools script to display the GUI;
# ################################################################################
# """
#
# from tkinter import *                               # get widgets
# from guimaker import *                              # menu/toolbar builder
# from guimixin import GuiMixin                       # get quit, not done
#
#
# class ShellGui(GuiMixin, GuiMakerWindowMenu):       # a frame + maker + mixins
#     def start(self):                                # use GuiMaker if component
#         self.setMenuBar()
#         self.setToolBar()
#         self.master.title("Shell Tools Listbox")
#         self.master.iconname("Shell Tools")
#
#     def handleList(self, event):                    # on listbox double-click
#         label = self.listbox.get(ACTIVE)            # fetch selection text
#         self.runCommand(label)                      # and call action here
#
#     def makeWidgets(self):                          # add listbox in middle
#         sbar = Scrollbar(self)                      # cross link sbar, list
#         list = Listbox(self, bg='white')            # or use Tour.ScrolledList
#         sbar.config(command=list.yview)
#         list.config(yscrollcommand=sbar.set)
#         sbar.pack(side=RIGHT, fill=Y)                     # pack 1st=clip last
#         list.pack(side=LEFT, expand=YES, fill=BOTH)       # list clipped first
#         for (label, action) in self.fetchCommands():      # add to listbox
#             list.insert(END, label)                       # and menu/toolbars
#         list.bind('<Double-1>', self.handleList)          # set event handler
#         self.listbox = list
#
#     def forToolBar(self, label):                          # put on toolbar?
#         return True                                       # default = all
#
#     def setToolBar(self):
#         self.toolBar = []
#         for (label, action) in self.fetchCommands():
#             if self.forToolBar(label):
#                 self.toolBar.append((label, action, dict(side=LEFT)))
#         self.toolBar.append(('Quit', self.quit, dict(side=RIGHT)))
#
#     def setMenuBar(self):
#         toolEntries  = []
#         self.menuBar = [
#             ('File',  0, [('Quit', -1, self.quit)]),    # pull-down name
#             ('Tools', 0, toolEntries)                   # menu items list
#             ]                                           # label,underline,action
#         for (label, action) in self.fetchCommands():
#             toolEntries.append((label, -1, action))     # add app items to menu
#
# ################################################################################
# # delegate to template type-specific subclasses
# # which delegate to app tool-set-specific subclasses
# ################################################################################
#
#
# class ListMenuGui(ShellGui):
#     def fetchCommands(self):             # subclass: set 'myMenu'
#         return self.myMenu               # list of (label, callback)
#
#     def runCommand(self, cmd):
#         for (label, action) in self.myMenu:
#             if label == cmd: action()
#
#
# class DictMenuGui(ShellGui):
#     def fetchCommands(self):
#         return self.myMenu.items()
#
#     def runCommand(self, cmd):
#         self.myMenu[cmd]()
# ::::::::::::::::::::textpak=>text_packer_1.txt
# I am from text_packer_1.txt
# ::::::::::::::::::::textpak=>text_packer_2.txt
# I am from text_packer_2.txt
# ::::::::::::::::::::textpak=>widgets.py
# """
# wrap up widget construction in functions for easier use, making some
# assumptions (e.g., expansion); use extras kw args for width, font/color
# """
#
# from tkinter import *
#
#
# def frame(root, side=TOP, **extras):
#     widget = Frame(root)
#     widget.pack(side=side, expand=YES, fill=BOTH)
#     if extras: widget.config(**extras)
#     return widget
#
#
# def label(root, side, text, **extras):
#     widget = Label(root, text=text, relief=RIDGE)        # default config
#     widget.pack(side=side, expand=YES, fill=BOTH)        # pack automatically
#     if extras: widget.config(**extras)                   # apply any extras
#     return widget
#
#
# def button(root, side, text, command, **extras):
#     widget = Button(root, text=text, command=command)
#     widget.pack(side=side, expand=YES, fill=BOTH)
#     if extras: widget.config(**extras)
#     return widget
#
#
# def entry(root, side, linkvar, **extras):
#     widget = Entry(root, relief=SUNKEN, textvariable=linkvar)
#     widget.pack(side=side, expand=YES, fill=BOTH)
#     if extras: widget.config(**extras)
#     return widget
#
#
# if __name__ == '__main__':
#     app = Tk()
#     frm = frame(app, TOP)               # much less code required here!
#     label(frm, LEFT, 'SPAM')
#     button(frm, BOTTOM, 'Press', lambda: print('Pushed'))
#     mainloop()
