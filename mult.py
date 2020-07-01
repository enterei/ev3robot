import argparse
import selectors
import socket
import types
import sys
import json
import time


####  Grundmechaniken zur Kommunikation entnommen von:
####  https://realpython.com/python-sockets/
####
####  Das Beispiel wurde vor allem in der Struktur( aufteilung senden empfangen) verändert
####  und meinen Voraussetzungen angepasst
####  klasse wurde verändert aufgeteilt und angepasst
####  zusätzliche informationen von:
####  https://docs.python.org/3/howto/sockets.html   über korrekte SOcket umplementierung

from SystemHandler import SystemHandler

messages = [b'Message 1 from client.', b'Message 2 from client.']
messages ={'event':"ecke",'a':2}

# initializing dictionary
messages = {'Aktion': 'Test', 'is': 2, 'Case':"case1"}
messages = {'Aktion': 'Test', 'is': 2, 'Case':"case2"}

messages = {'Aktion': 'Befehl'}

message_handler=SystemHandler()
# printing original dictionary
#print("The original dictionary is : " + str(test_dict))

# using encode() + dumps() to convert to bytes
res_bytes = json.dumps(messages).encode('utf-8')

sel = selectors.DefaultSelector()
def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print('starting connection', connid, 'to', server_addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(connid=connid,
                                     msg_total=sum(len(m) for m in messages),
                                     recv_total=0,
                                     messages=list(messages),
                                     outb=b'')
        sel.register(sock, events, data=data)



def send(key,mask,m):
   # print("loop in send ")

    sock = key.fileobj
    data = key.data
    data.outb=m
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            print("in not data")
            data.outb = res_bytes
        if data.outb:
            print("in data, data.outb: ")
            print('sending', repr(data.outb), 'to connection', data.connid)
            #            print(json.dumps(data.outb).encode('utf-8'))
            sent = sock.send(m)  # Should be ready to write
            data.outb = data.outb[sent:]
            data.messages = None
            print("send is over")
def recv(key,mask):
    sock = key.fileobj
    data = key.data
    recv_data = None
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            print('received', repr(recv_data), 'from connection', data.connid)
            data.recv_total += len(recv_data)
            return recv_data
        if not recv_data or data.recv_total == data.msg_total:
            print('closing connection', data.connid)
            sel.unregister(sock)
            sock.close()
if len(sys.argv) != 4:
    print("usage:", sys.argv[0], "<host> <port> <num_connections>")
    host  = '192.168.0.179'
    port = '65432'
    num_conns=1

start_connections(host, int(port), int(num_conns))
returnMessage = {'x':1}

loop =True
try:
    while loop:
        events = sel.select(timeout=1)
        if events:

            for key, mask in events:


                send(key,mask,res_bytes)
                res = recv(key,mask)
                res_bytes=None
                if res:
                    print("len OUT: " + str(len(res)))

                    mes= message_handler.handleMessage(res)
                    if mes !=None:
                        send(key,mask,mes)

        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()