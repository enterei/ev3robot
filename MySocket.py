#!/usr/bin/env python3

import socket
class MySocket:
    HOST = '192.168.0.94'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server
    data = []
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def conn(self):
        self.s.connect((self.HOST,self.PORT))
       # s.sendall(b'Hello, world')

        #data.append(s.recv(1024))
    def send(self,ar):
       # gems= [3,5,7,8]
        gems_bytes= bytes(ar)
        self.s.sendall(gems_bytes)
       # data.append(s.recv(1024))
        #gems = [3, 4, 1, 9]
        #gems_bytes = bytes(gems)
        #self.s.sendall(gems_bytes)


        print('Received', repr(self.data))