import os
from multiprocessing import Pool


def powers(x):
    # print(os.getpid()) # enable to watch children
    return 2 ** x


# enable to watch children
if __name__ == '__main__':
    workers = Pool(processes=5)
    results = workers.map(powers, [2] * 100)
    print(results[:16])
    print(results[-2:])
    results = workers.map(powers, range(100))
    print(results[:16])
    print(results[-2:])

# # set the process as a daemon to keep the shell running
# from multiprocessing import Process
# import time
#
#
# def action(arg1, arg2):
#     print(arg1, arg2)
#     time.sleep(5)  # normally prevents the parent from exiting
#
#
# if __name__ == '__main__':
#     p = Process(target=action, args=('spam', 'eggs'))
#     p.daemon = True
#     p.start()
