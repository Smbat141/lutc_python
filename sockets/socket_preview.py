from socket import socket, AF_INET, SOCK_STREAM

port = 50001
host = 'localhost'


# portable socket api
# port number identifies socket on machine
# server and client run on same local machine here
def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        reply = 'server got: [%s]' % data
        conn.send(reply.encode())


def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name.encode())
    reply = sock.recv(1024)
    # ip addresses tcp connection
    # bind to port on this machine
    # allow up to 5 pending clients
    sock.close()
    print('client got: [%s]' % reply)


# up to 1024 bytes in message
if __name__ == '__main__':
    from threading import Thread

    sthread = Thread(target=server)
    sthread.daemon = True
    # don't wait for server thread
    sthread.start()
    # do wait for children to exit
    for i in range(5):
        Thread(target=client, args=('client%s' % i,)).start()
# from socket import socket, AF_INET, SOCK_STREAM
# import sys
#
# port = 5000
# host = 'localhost'
#
# def server():
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind(('', port))
#     sock.listen(5)
#     while True:
#         conn, addr = sock.accept()
#         data = conn.recv(1024)
#         reply = 'server got: [%s]' % data
#         print(data)
#         conn.send(reply.encode())
#
#
# def client(name):
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.connect((host, port))
#     sock.send(name.encode())
#     reply = sock.recv(1024)
#     # ip addresses tcp connection
#     # bind to port on this machine
#     # allow up to 5 pending clients
#     sock.close()
#     print('client got: [%s]' % reply)
#
#
# if __name__ == '__main__':
#     if len(sys.argv) == 1:
#         server()
#     else:
#         while True:
#             name = input()
#             client(name)
