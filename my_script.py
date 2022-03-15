#!/usr/bin/env python3
# print(sum(int(line) for line in [1, 5, 6]))

# for x in range(1000000): print (x)
# import sys
# print(sys.argv)
# while [1,2,3]: print (True)
# def getopts(argv):
#     opts = {}
#     while argv:
#
#         if argv[0][0] == '-':
#             opts[argv[0]] = argv[1]
#             argv = argv[2:]
#         else:
#             print(argv)
#             argv = argv[1:]
#     return opts
#
#
# if __name__ == '__main__':
#     from sys import argv
#
#     myargs = getopts(argv)
#     if '-i' in myargs:
#         print(myargs['-i'])
#     print(myargs)
# import timeit
# import math
#
#
# def prime_numbers(n):
#     for x in range(2, round(math.sqrt(n) + 1)):
#         if n % x == 0:
#             return False
#     return True


# prime_numbers = prime_numbers(857)
# print(prime_numbers)
# print(f"my version", timeit.timeit(sieve_of_eratosthenes, number=10000))
# print(f"geek", timeit.timeit(SieveOfEratosthenes, number=10000))
# import sys
#
# stdin_fileno = sys.stdin
#
# # Keeps reading from stdin and quits only if the word 'exit' is there
# # This loop, by default does not terminate, since stdin is open
# for line in sys.stdin:
#     print(f'Found line {line}')
# import sys
#
# stdout_fileno = sys.stdout
#

# sys.stdout.write("Hello\n")
# import os
#
#
# def child():
#     print('Hello from child', os.getpid())
#     os._exit(0)  # else goes back to parent loop
#
#
# def parent():
#     while True:
#         newpid = os.fork()
#         if newpid == 0:
#             child()
#         else:
#             print('Hello from parent', os.getpid(), newpid)
#         if input() == 'q': break
#
#
# parent()
# import os, time
#
# x = 888
# def counter(count):
#     print(x)
#     for i in range(count):
#         time.sleep(1)
#         print('[%s] => %s' % (os.getpid(), i))
#
#
# # run in new process
# # simulate real work
# for i in range(5):
#     pid = os.fork()
#     if pid != 0:
#         print("parent")
#     else:
#         print("child process")
#         os._exit(0)  # in parent: continue
# print('Main process exiting.')
# import os, time
# x = 999
# # Create a child process
# # using os.fork() method
# print(x)
# pid = os.fork()
#
# # pid greater than 0 represents
# # the parent process
# if pid > 0:
#     print("I am parent process:")
#     print("Process ID:", os.getpid())
#     print("Child's process ID:", pid)
#     os._exit(0)
# # pid equal to 0 represnts
# # the created child process
# else:
#     time.sleep(5)
#     print("\nI am child process:")
#     print("Process ID:", os.getpid())
#     print("Parent's process ID:", os.getppid())
#     os._exit(0)

# If any error occured while
# using os.fork() method
# OSError will be raised


# import os
#
# parm = 0
# while True:
#     parm += 1
#     pid = os.fork()
#     print('*********', pid)
#     if pid == 0:
#         # copy process
#         os.execlp('python3', 'python', './child.py', str(parm))  # overlay program
#         assert False, 'error starting program'
#         # shouldn't return
#     else:
#         print('Child is', pid)
#         if input() == 'q': break


# import _thread
#
#
# def child(tid):
#     print('Hello from thread', tid)
#
#
# def parent():
#     i = 0
#     while True:
#         i += 1
#         _thread.start_new_thread(child, (i,))
#         if input() == 'q': break
#         print('Hello from parent')
#
#
# parent()


# import _thread as thread, time
#
#
# def counter(myId, count):
#     for i in range(count):
#         time.sleep(1)
#         mutex.acquire()
#         print('[%s] => %s' % (myId, i))  # function run in threads
#         mutex.release()
#
#
# mutex = thread.allocate_lock()
# for i in range(5):
#     thread.start_new_thread(counter, (i, 5))  # spawn 5 threads
# # each thread loops 5 times
# print('Main thread exiting.')  # don't exit too early
#
# time.sleep(6)


# import _thread as thread
#
# stdoutmutex = thread.allocate_lock()
# exitmutexes = [thread.allocate_lock() for i in range(10)]
#
#
# def counter(myId, count):
#     for i in range(count):
#         stdoutmutex.acquire()
#         print('[%s] => %s' % (myId, i))
#         stdoutmutex.release()
#     exitmutexes[myId].acquire()
#
#
# # signal main thread
# for i in range(10):
#     thread.start_new_thread(counter, (i, 100))
#
# for mutex in exitmutexes:
#     print(mutex.locked())
#     while not mutex.locked(): pass
# print('Main thread exiting.')

# import _thread as thread, time
#
# stdoutmutex = thread.allocate_lock()
# numthreads = 2
# exitmutexes = [thread.allocate_lock() for i in range(numthreads)]
#
#
# def counter(myId, count, mutex):
#     for i in range(count):
#         time.sleep(1 / (myId + 1))
#         with mutex:
#             print('[%s] => %s' % (myId, i))
#     exitmutexes[myId].acquire()
#
#
# # shared object passed in
# # diff fractions of second
# # auto acquire/release: with
# # global: signal main thread
# for i in range(numthreads):
#     thread.start_new_thread(counter, (i, 5, stdoutmutex))
# while not all(mutex.locked() for mutex in exitmutexes): time.sleep(0.25)
# print('Main thread exiting.')

# import threading
#
#
# class Mythread(threading.Thread):
#
#     def __init__(self, myId, count, mutex):
#         self.myId = myId
#         self.count = count
#         self.mutex = mutex
#         threading.Thread.__init__(self)
#
#     # subclass Thread object
#     # per-thread state information
#     # shared objects, not globals
#     def run(self):
#         # run provides thread logic
#         for i in range(self.count):
#             # still sync stdout access
#             with self.mutex:
#                 print('[%s] => %s' % (self.myId, i))
#
#
# stdoutmutex = threading.Lock()
# threads = []
# for i in range(10):
#     thread = Mythread(i, 100, stdoutmutex)
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
# print('Main thread exiting.')
# same as thread.allocate_lock()
# make/start 10 threads
# starts run method in a thread
# wait for thread exits

# import threading
#
#
# def action(i):
#     print(i ** 32)
#
#
# threading.Thread(target=action, args=(5,)).start()

# import threading, time
#
# count = 0
#
#
# def adder():
#     global count
#     count = count + 1
#     time.sleep(0.5)
#     count = count + 1
#     # update a shared name in global scope
#     # threads share object memory and global names
#
#
# threads = []
# for i in range(100):
#     thread = threading.Thread(target=adder, args=())
#     thread.start()
#     threads.append(thread)
# for thread in threads: thread.join()
# print(count)
# "producer and consumer threads communicating with a shared queue"
# numconsumers = 2
# numproducers = 4
# nummessages = 4
#
# import _thread as thread, queue, time
#
#
# safeprint = thread.allocate_lock()
# # else prints may overlap
# dataQueue = queue.Queue()
#
#
# # shared global, infinite size
# def producer(idnum):
#     for msgnum in range(nummessages):
#         time.sleep(idnum)
#         dataQueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))
#
#
# def consumer(idnum):
#     while True:
#         time.sleep(0.1)
#         try:
#             data = dataQueue.get(block=False)
#         except queue.Empty:
#             pass
#         else:
#             with safeprint:
#                 print('consumer', idnum, 'got =>', data)
#
#
# if __name__ == '__main__':
#     for i in range(numconsumers):
#         thread.start_new_thread(consumer, (i,))
#
# for i in range(numproducers):
#     thread.start_new_thread(producer, (i,))
#     time.sleep(((numproducers - 1) * nummessages) + 1)
#     print('Main thread exit.')
#


# from tkinter import Tk
# from tkinter.messagebox import showinfo
# win = Tk()
# win.after(5500, lambda: showinfo('Popup', 'Spam!'))
# win.mainloop()


# import os
#
# exitstat = 0
#
#
# def child():
#     global exitstat
#     exitstat += 1
#     print('Hello from child', os.getpid(), exitstat)
#     os._exit(exitstat)
#     print('never reached')
#
# newpid = os.fork()
# print(newpid)
# if newpid == 0:
#     print("55")
#     child()
# else:
#     print("77")
#     pid, status = os.wait()
#     print('Parent got', pid, status, (status >> 8))


# import _thread as thread
#
# exitstat = 0
#
#
# def child():
#     global exitstat
#     # process global names
#     exitstat += 1
#     # shared by all threads
#     threadid = thread.get_ident()
#     print('Hello from child', threadid, exitstat)
#     thread.exit()
#     print('never reached')
#
#
# def parent():
#     while True:
#         thread.start_new_thread(child, ())
#         if input() == 'q': break
# if __name__ == '__main__': parent()


# import threading, sys, time
#
#
# def action():
#     sys.exit()
#     print('not reached')
#
#
# threading.Thread(target=action).start()
# time.sleep(2)
# print('Main exit')


# import os, time
#
#
# def child(pipeout):
#     zzz = 0
#     while True:
#         time.sleep(zzz)
#         msg = ('Spam %03d' % zzz).encode()
#         os.write(pipeout, msg)
#         zzz = (zzz + 1) % 5
#
#
# def parent():
#     pipein, pipeout = os.pipe()
#     # make 2-ended pipe
#     if os.fork() == 0:
#         child(pipeout)
#     else:
#         while True:
#             line = os.read(pipein, 32)
#             print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))
#
#
# parent()


# import os, time
#
#
# def child(pipeout):
#     zzz = 0
#     while True:
#         time.sleep(zzz)
#         msg = ('Spam %03d\n' % zzz).encode()
#         os.write(pipeout, msg)
#         zzz = (zzz + 1) % 5
#
#
# def parent():
#     pipein, pipeout = os.pipe()
#     if os.fork() == 0:
#         os.close(pipein)
#         child(pipeout)
#     else:
#         os.close(pipeout)
#         pipein = os.fdopen(pipein)
#         while True:
#             line = pipein.readline()[:-1]
#             print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))
#
#
# parent()


# import os, time, threading
#
#
# def child(pipeout):
#     zzz = 0
#     while True:
#         time.sleep(zzz)
#         msg = ('Spam %03d' % zzz).encode()
#         os.write(pipeout, msg)
#         zzz = (zzz + 1) % 5
#
#
# def parent(pipein):
#     while True:
#         line = os.read(pipein, 32)
#         print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))
#
#
# pipein, pipeout = os.pipe()
# threading.Thread(target=child, args=(pipeout,)).start()
# parent(pipein)


# import os, sys
#
#
# def spawn(prog, *args):
#     stdinFd = sys.stdin.fileno()
#     stdoutFd = sys.stdout.fileno()
#     parentStdin, childStdout = os.pipe()
#     childStdin, parentStdout = os.pipe()
#     pid = os.fork()
#
#     if pid:
#         os.close(childStdout)
#         os.close(childStdin)
#         os.dup2(parentStdin, stdinFd)
#         os.dup2(parentStdout, stdoutFd)
#     else:
#         os.close(parentStdin)
#         os.close(parentStdout)
#         os.dup2(childStdin, stdinFd)
#         os.dup2(childStdout, stdoutFd)
#         args = (prog,) + args
#         os.execvp(prog, args)
#         assert False, 'execvp failed!'
#
#
# if __name__ == '__main__':
#     mypid = os.getpid()
#     spawn('python3', "-u" 'pipes-testchild.py', 'spam')  # fork child program
#     print('Hello 1 from parent', mypid)
#     sys.stdout.flush()
#     reply = input()
#     sys.stderr.write('Parent got: "%s"\n' % reply)  #
#     print('Hello 2 from parent', mypid)
#     sys.stdout.flush()
#     reply = sys.stdin.readline()
#     sys.stderr.write('Parent got: "%s"\n' % reply[:-1])


# import os, time, sys
#
# mypid = os.getpid()
# parentpid = os.getppid()
# sys.stderr.write('Child %d of %d got arg: "%s"\n' % (mypid, parentpid, sys.argv[1]))
# for i in range(2):
#     time.sleep(3)
#     # make parent process wait by sleeping here
#     recv = input()
#     # stdin tied to pipe: comes from parent's stdout
#     time.sleep(3)
#     send = 'Child %d got: [%s]' % (mypid, recv)
#     print(send)
#     # stdout tied to pipe: goes to parent's stdin
#     sys.stdout.flush()
#     # make sure it's sent now or else process blocks


# import os, time, sys
#
# fifoname = 'pipe'
#
#
# def child():
#     pipeout = os.open(fifoname, os.O_WRONLY)
#     zzz = 0
#     while True:
#         time.sleep(zzz)
#         msg = ('Spam %03d\n' % zzz).encode()
#         os.write(pipeout, msg)
#         zzz = (zzz + 1) % 5
#
# # must open same name
# # open fifo pipe file as fd
# # binary as opened here
# def parent():
#     pipein = open(fifoname, 'r')
#     # open fifo as text file object
#     while True:
#         line = pipein.readline()[:-1]
#         # blocks until data sent
#         print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time()))
#
#
# if __name__ == '__main__':
#     if not os.path.exists(fifoname):
#         os.mkfifo(fifoname)
#
#     if len(sys.argv) == 1:
#         parent()
#     else:
#         child()

# def Fibonacci(n):
#     print(n)
#     # Check if input is 0 then it will
#     # print incorrect input
#     return Fibonacci(n - 1)
#
# input()
# # Driver Program
# print(Fibonacci(5))

from datetime import datetime
import piexif

# filename = '/home/collab06/Downloads/DSC_7528.JPG'
# exif_dict = piexif.load(filename)
# new_date = datetime.now().strftime("%Y:%m:%d %H:%M:%S")
# exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
# exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
# exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
# exif_bytes = piexif.dump(exif_dict)
# piexif.insert(exif_bytes, filename)


# import time, sys
#
# def lazy_property(fn):
#     attr_name = '_lazy_' + fn.__name__
#
#     @property
#     def _lazy_property(self):
#         if not hasattr(self, attr_name):
#             setattr(self, attr_name, fn(self))
#         return getattr(self, attr_name)
#     return _lazy_property
#
#
# class Country:
#
#     def __init__(self, name, capital):
#         self.name = name
#         self.capital = capital
#
#     @lazy_property
#     def cities(self):
#         time.sleep(2)
#         # expensive operation to get all the city names (API call)
#         print("cities property is called")
#         return ["city1", "city2"]
#
#
# china = Country("china", "beijing")
#
# # beijing
# print(china.cities)
# print(china.cities)
# # cities property is called
# # ['city1', 'city2']


########################################################################################################################


# def myDecorator(fn):
#     def nested_decordator(self, *args):
#         print("before any function")
#         x = fn(self, *args)
#         print("after any function")
#         return x
#
#     return nested_decordator
#
#
# class myMetaClass(type):
#     def __new__(cls, name, bases, local):
#         for attr in local:
#             value = local[attr]
#             if callable(value):
#                 local[attr] = myDecorator(value)
#         return type.__new__(cls, name, bases, local)
#
#
# class myClass(metaclass=myMetaClass):
#
#     def baz(self, x, y):
#         print("function implementation")
#         return x + y
#
#
# x = myClass()
# print(x.baz(5, 88))

########################################################################################################################


# import logging
# import random
# import threading
# import time
# from collections import deque
#
# logging.basicConfig(level=logging.INFO, format="%(message)s")
#
#
# def wait_seconds(mins, maxs):
#     time.sleep(mins + random.random() * (maxs - mins))
#
#
# def produce(queue, size):
#     while True:
#         if len(queue) < size:
#             value = random.randint(0, 9)
#             queue.append(value)
#             logging.info("Produced: %d -> %s", value, str(queue))
#         else:
#             logging.info("Queue is saturated")
#         wait_seconds(0.1, 0.5)
#
#
# def consume(queue):
#     while True:
#         try:
#             value = queue.popleft()
#         except IndexError:
#             logging.info("Queue is empty")
#         else:
#             logging.info("Consumed: %d -> %s", value, str(queue))
#         wait_seconds(0.2, 0.7)
#
#
# logging.info("Starting Threads...\n")
# logging.info("Press Ctrl+C to interrupt the execution\n")
#
# shared_queue = deque()
#
# threading.Thread(target=produce, args=(shared_queue, 10)).start()
# threading.Thread(target=consume, args=(shared_queue,)).start()

########################################################################################################################

from threading import Thread
from threading import Lock
import sys


class Counter:

    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        for _ in range(100000):
            self.lock.acquire()
            self.count += 1
            self.lock.release()


# Sets the thread switch interval
sys.setswitchinterval(0.005)

numThreads = 5
threads = [0] * numThreads
counter = Counter()

for i in range(0, numThreads):
    threads[i] = Thread(target=counter.increment)

for i in range(0, numThreads):
    threads[i].start()

for i in range(0, numThreads):
    threads[i].join()

if counter.count != 500000:
    print(" If this line ever gets printed, " + \
          "the author is a complete idiot and " + \
          "you should return the course for a full refund!")
else:
    print(" count = {0}".format(counter.count))