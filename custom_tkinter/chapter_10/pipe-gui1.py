# GUI reader side: route spawned program standard output to a GUI window

from guiStreams import redirectedGuiShellCmd                       # uses GuiOutput
redirectedGuiShellCmd('python3 -u pipe-nongui.py')                 # -u: unbuffered
