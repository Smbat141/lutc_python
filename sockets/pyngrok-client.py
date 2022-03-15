# HOST="1.tcp.ngrok.io" PORT=12345 python client.py

import os
import socket

host = "e028b8f4e282.ngrok.io"
port = 12345


# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server with the socket via our ngrok tunnel
server_address = (host, port)
sock.connect(server_address)
print("Connected to {}:{}".format(host, port))

# Send the message
message = "ping"
print("Sending: {}".format(message))
sock.sendall(message.encode("utf-8"))

# Await a response
data_received = 0
data_expected = len(message)

while data_received < data_expected:
    data = sock.recv(1024)
    data_received += len(data)
    print("Received: {}".format(data.decode("utf-8")))

sock.close()