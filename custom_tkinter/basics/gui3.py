from tkinter import *
import sys


# def quit():  # a custom callback handler
#     print('Hello, I must be going...')
#     sys.exit()  # kill windows and process
#
#
# widget = Button(None, text='Hello event world', command=quit)
# widget.pack()
# widget.mainloop()

####################################################################################
# # with lambda function
# # lambda generates a function
# # but contains just an expression

# widget = Button(None,
#                 text='Hello event world',
#                 command=(lambda: print('Hello lambda world') or sys.exit()))
# widget.pack()
# widget.mainloop()

####################################################################################
# # callback running immediately when passed directly

# def handler(name):
#     print(name)
#
#
# widget = Button(text='Hello event world',command=handler('spam'))
# widget.pack()
# widget.mainloop()

####################################################################################
# # pass function with arguments by wrapping it in lambda

# def handler(name):
#     print(name)
#
#
# widget = Button(text='Hello event world', command=(lambda: handler('spam')))
# widget.pack()
# widget.mainloop()

#####################################################################################
# # pass class method to Button
#
# class Gui:
#     def handler(self, A, B):
#         print(A, B)
#
#     def makegui(self):
#         X = 42
#         Button(text='ni', command=(lambda: self.handler(X, 'spam'))).pack()
#
#
# Gui().makegui()
# mainloop()

#####################################################################################
# # recall scopes
# def normal():
#     def action():
#         return spam  # really, looked up when used
#
#     spam = 'inside'  # assigned after function
#     return action
#
#
# spam = 'outside'  # assigned before function
# act = normal()
# print(act())  # also prints 'ni'

#####################################################################################

# # scopes with lambdas
# def weird():
#     tmp = (lambda: spam * 2)  # remembers spam  even though not set till here
#     spam = 42
#     return tmp
#
#
# act = weird()
# print(act())  # prints 84

#####################################################################################
# # lambda refer to last variable
# def weird():
#     spam = 42
#     handler = (lambda: spam * 2)  # func doesn't save 42 now
#     spam = 50
#     print(handler())  # prints 100: spam looked up now
#     spam = 60
#     print(handler())  # prints 120: spam looked up again now
#
#
# weird()

#####################################################################################
# # scopes in loops
# # lambda save latest <c> variable value
# def odd():
#     funcs = []
#     for c in 'abcdefg':
#         funcs.append((lambda: c))  # c will be looked up later
#     return funcs  # does not remember current c
#
#
# for func in odd():
#     print(func(), end=' ')  # OOPS: print 7 g's, not a,b,c,... !

#####################################################################################
# # scopes in loops
# # lambda save default <c> variable value
# def odd():
#     funcs = []
#     for c in 'abcdefg':
#         funcs.append((lambda c=c: c))  # force to remember c now
#     return funcs  # defaults eval now
#
#
# for func in odd():
#     print(func(), end=' ')  # OK: now prints a,b,c,...
#####################################################################################
# # use class instead of lambda or function

# class HelloClass:
#     def __init__(self):
#         widget = Button(None, text='Hello event world', command=self.quit)
#         widget.pack()
#
#     def quit(self):
#         print('Hello class method world')  # self.quit is a bound method
#         sys.exit()  # retains the self+quit pair
#
#
# HelloClass()
# mainloop()

#####################################################################################
# # override class __call__ function
class HelloCallable:
    def __init__(self):  # __init__ run on object creation
        self.msg = 'Hello __call__ world'

    def __call__(self):
        print(self.msg)  # __call__ run later when called
        sys.exit()  # class object looks like a function


widget = Button(None, text='Hello event world', command=HelloCallable())
widget.pack()
widget.mainloop()
