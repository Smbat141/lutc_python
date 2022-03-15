# """
# PyDraw-threads: use threads to move objects; works okay on Windows
# provided that canvas.update() not called by threads (else exits with
# fatal errors, some objs start moving immediately after drawn, etc.);
# at least some canvas method calls must be thread safe in tkinter;
# this is less smooth than time.sleep, and is dangerous in general:
# threads are best coded to update global vars, not change GUI;
# """
#
# import _thread as thread, time, sys, random
# from tkinter import Tk, mainloop
# from movingpics import MovingPics, pickUnits, pickDelays
#
#
# class MovingPicsThreaded(MovingPics):
#     def __init__(self, parent=None):
#         MovingPics.__init__(self, parent)
#         self.mutex = thread.allocate_lock()
#         import sys
#         # sys.setcheckinterval(0) # switch after each vm op: doesn't help
#
#     def onMove(self, event):
#         object = self.object
#         if object and object not in self.moving:
#             msecs = int(pickDelays[0] * 1000)
#             parms = 'Delay=%d msec, Units=%d' % (msecs, pickUnits[0])
#             self.setTextInfo(parms)
#             # self.mutex.acquire()
#             self.moving.append(object)
#             # self.mutex.release()
#             thread.start_new_thread(self.doMove, (object, event))
#
#     def doMove(self, object, event):
#         canvas = event.widget
#         incrX, reptX, incrY, reptY = self.plotMoves(event)
#         for i in range(reptX):
#             canvas.move(object, incrX, 0)
#             # canvas.update()
#             time.sleep(pickDelays[0])  # this can change
#         for i in range(reptY):
#             canvas.move(object, 0, incrY)
#             # canvas.update()                 # update runs other ops
#             time.sleep(pickDelays[0])  # sleep until next move
#         # self.mutex.acquire()
#         self.moving.remove(object)
#         if self.object == object: self.where = event
#         # self.mutex.release()
#
#
# if __name__ == '__main__':
#     root = Tk()
#     MovingPicsThreaded(root)
#     mainloop()
import _thread as thread

stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]


def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
        
    exitmutexes[myId].acquire()


# signal main thread
for i in range(10):
    thread.start_new_thread(counter, (i, 100))

for mutex in exitmutexes:
    while not mutex.locked(): pass
print('Main thread exiting.')