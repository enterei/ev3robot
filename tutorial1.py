#!/usr/bin/env python3

import socket
import json

HOST = '192.168.0.179'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #def conn(self):
    s.connect((HOST, PORT))
    # s.sendall(b'Hello, world')
    data=[]
    #data.append(s.recv(1024))
    gems= [3,5,7,8]
    gems_bytes= bytes(gems)
    s.sendall(gems_bytes)
    data.append(s.recv(1024))
    gems = [3, 4, 1, 9]
    gems_bytes = bytes(gems)
    s.sendall(gems_bytes)


    print('Received', repr(data))