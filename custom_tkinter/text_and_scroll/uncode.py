from tkinter import *

# t = Text()
# t.insert('1.0', open('ldata', 'rb').read())                      # with binary don't need concern about encoding format
# t.pack()
# print(t.get('1.0', 'end'))
#
# t = Text()
# t.insert('1.0', open('ldata', 'rb', encoding='latin-1').read())  # implicitly pass encoding format
# t.pack()                                                         # or will throw exception
# print(t.get('1.0', 'end'))

t = Text()
t.insert('1.0', open('udata', 'r', encoding='utf-8').read())     # implicitly pass encoding format
t.pack()                                                         # or will throw exception
c = t.get('1.0', 'end')

# open('cdata', 'wb').write(c) # throw error
# open('cdata', 'w', encoding='latin-1').write(c)  # success
# open('cdata', 'w', encoding='utf-8').write(c) # success
# open('cdata', 'w', encoding='utf-16').write(c)
# open('cdata', 'wb').write( c.encode('latin-1') ) # manual encoding first
# open('cdata', 'w', encoding='ascii').write(c)  # throw error - still must be compatible
print(open('cdata', 'rb').read())