"""
set and catch alarm timeout signals in Python; time.sleep doesn't play
well with alarm (or signal in general in my Linux PC), so we call
signal.pause here to do nothing until a signal is received;
"""
import sys, signal, time


def now(): return time.asctime()


def onSignal(signum, stackframe):
    print('Got alarm', signum, 'at', now())  # python signal handler


# most handlers stay in effect
while True:
    print('Setting at', now())
    signal.signal(signal.SIGALRM, onSignal)
    signal.alarm(5)
    signal.pause()  # install signal handler
    # do signal in 5 seconds
    # wait for signals
