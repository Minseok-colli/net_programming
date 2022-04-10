# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',9000))
# s.listen(2)

# while True:
#     client, addr = s.accept()
#     print('connet from ', addr)

#     client.send(b'hello ' + str(addr[1]).encode())
#     client.close()

# from pydoc import cli
# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',9000))
# s.listen(2)

# while True:
#     name,addr = s.accept()
    
#     print('Connect from ',addr)
#     name.send(b'hello '+ addr[0].encode())
    
#     msg = name.recv(1024)
#     print(msg.decode())

#     id = 20191505
#     name.send(id.to_bytes(4,'big'))
#     name.close()

# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('www.google.com',80))
# s.send(b'Get / HTTP/1.1\r\n\r\n')

# data = s.recv(10000)
# print(data.decode())

# s.close()

# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',5000))
# s.listen(2)

# client,addr = s.accept()
# print('connect with ',addr)
# while True:
#     msg = client.recv(1024)
#     print('recevie data : ', msg.decode())
#     client.send(msg)

# client.close()
# s.close()

# import socket
# import time

# port = 5000

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',port))
# s.listen(2)

# while True:
#     client,addr = s.accept()
#     print('connect with ',addr)
#     client.send(time.ctime(time.time()).encode())
#     client.close()

# from pydoc import cli
# import socket

# port = 2000
# bufsize = 1024

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',port))
# s.listen(1)

# client, addr = s.accept()
# print(addr,' is connected')

# while True:
#     try:
#         msg = client.recv(bufsize)
#     except:
#         break
    
#     else:
#         if not msg:
#             break
#         print("Received Data: %s" % msg.decode())

#     try:
#         client.send(msg)
#     except:
#         break

# client.close()


# import socket

# table = {'1':'one','2':'two','3':'three'}
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',3000))
# s.listen(1)

# client,addr = s.accept()

# while True:
#     request = client.recv(1024)
#     print(request.decode()," is received.")
#     if not request:
#         break;

#     try:
#         eng = table[request.decode()]
#     except: break
#     else:
#         client.send(eng.encode())

# client.close()
# s.close()


# from dataclasses import replace
# import socket
# op=['+','-','*','/']

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',2000))
# s.listen(1)

# cal, addr = s.accept()

# while True:
#     recevie = cal.recv(1024)
#     if not recevie:
#         break;

#     data = recevie.decode()
#     data_nonSpace = data.replace(' ','')
#     print(data_nonSpace)

#     for i in data_nonSpace:
#         if i in op:
#             a,b = data_nonSpace.split(i)

#             if i == '+':
#                 send = int(a)+int(b)
#             elif i == '-':
#                 send = int(a)-int(b)
#             elif i == '*':
#                 send = int(a)*int(b)
#             elif i == '/':
#                 send = round((int(a)/int(b)),3)
#     cal.send(str(send).encode())
        

# import sys
# import socket

# length = 4
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# addr = ('localhost',9999)
# sock.connect(addr)

# sock.send(b'Hello')

# msg = sock.recv(1024)

# if not msg:
#     sock.close()
#     sys.exit()

# elif msg != b'Filename':
#     sock.close()
#     sys.exit()

# else:
#     print('server : ',msg.decode())

# filename = input("Enter the file name")
# sock.send(filename.encode())

# msg = sock.recv(1024)
# if not msg:
#     sock.close()
#     sys.exit()

# elif msg == b'noFile':
#     sock.close()
#     sys.exit()

# else:
#     rx_size = len(msg)
#     data = msg
#     while rx_size < length:
#         msg = sock.recv(1024)
#         if not msg:
#             sock.close()
#             sys.exit()
#         data = data + msg
#         rx_size += len(msg)
#     if rx_size<length:
#         sock.close()
#         sys.exit()

#     filesize = int.from_bytes(data,'big')
#     print('server : ',filesize)

# rx_size = 0
# f = open(filename,'wb')
# while rx_size < filesize:
#     data = sock.recv(1024)
#     if not data:
#         break
#     f.write(data)
#     rx_size += len(data)

# if rx_size<filesize:
#     sock.close()
#     sys.exit()

# print('download complete')
# sock.send(b'bye')
# f.close()
# sock.close()


# import sys
# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# addr = ('localhost',9999)
# s.connect(addr)
# print('connected')

# s.send(b'Hello')

# #recv 'filename'
# msg = s.recv(1024)
# if not msg:
#     s.close()
#     sys.exit()
# elif msg != b'Filename':
#     s.close()
#     sys.exit()
# else:
#     print(msg.decode())
#     filename = input('Enter the file name:')

# s.send(filename.encode())

# #filesize

# msg = s.recv(1024)
# if not msg:
#     s.close()
#     sys.exit()
# elif msg == b'nofile':
#     s.close()
#     sys.exit()

# filesize = int(msg.decode())
# print('filesize: ',filesize)

# f = open(filename,'wb')
# rx_size = 0

# while rx_size < filesize:
#     data = s.recv(1024)
#     if not data:
#         s.close()
#         sys.exit()
#     f.write(data)
#     rx_size += len(data)

# if rx_size < filesize:
#     s.close()
#     sys.exit()

# print('Download complete')
# s.send(b'bye')

# s.close()
# sys.exit()

# import socket
# import random

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# addr = ('localhost',9999)

# s.connect(addr)
# print('connect completed')

# msg = s.recv(1024)
# if not msg:
#     s.close()
# elif msg != b'Request':
#     s.close()
# else:
#     print('Server: ',msg.decode())

# temp = random.randint(0,40)
# humid = random.randint(0,100)
# light = random.randint(70,150)

# data = str(temp) +' '+ str(humid) +' '+ str(light)
# print(type(data))
# print(data)

# s.send(data.encode())

# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('',9999))

# while True:
#     msg, addr = s.recvfrom(1024)
#     print('Received: ',msg.decode())

#     s.sendto(msg,addr)

# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('',3000))

# while True:
#     data, addr = s.recvfrom(1024)
#     print("received: ",data.decode())
#     if data.decode() == 'q':
#         s.close()
#     send = input('Send: ')
#     s.sendto(send.encode(),addr)


# import socket
# import random
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('',4000))

# while True:
#     data, addr = s.recvfrom(1024)
#     if random.randint(1,10) <= 8:
#         print("packet from {} is lost!".format(addr))
#         continue
#     print('packet is {} from {}'.format(data.decode(),addr))
#     s.sendto('ack'.encode(),addr)


#server

# import socket
# from collections import deque

# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('',3000))
# box = {}
# while True:
#     rec, addr = s.recvfrom(1024)
#     rec = rec.decode()
    
#     if rec.startswith('send'):
#         temp = list(rec.split())

#         id = temp[1]
#         msg = temp[2:]
#         mesg = ''
        
#         for i in msg:
#             mesg = str(mesg) + str(i) + ' '

#         if id not in box:
#             box[str(id)] = deque()
#             box[str(id)].append(mesg)

#         elif id in box:
#             box[str(id)].append(mesg)
        
#     elif rec.startswith('receive'):
#         recv_box = temp.split()[2]
        
#         if recv_box in box:
#             if box[str(recv_box)]:
#                 sndMsg = box[str(recv_box)].popleft()
#                 s.sendto(sndMsg.encode(),addr)
#             else:
#                 s.sendto("no messages".encode(),addr)
        
#         else:
#             s.sendto("no messages".encode(),addr)

#     elif rec.startswith('quit'):
#         s.close()


import socket
from collections import deque

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',3000))

mboxID = {}
while True:
    data, addr = s.recvfrom(1024)
    temp = data.decode().split()

    # print ('temp:', temp)

    command = temp[0]
    boxid = temp[1]
    msg_tmp = temp[2:]
    msg = ''
    # print ('msg_tmp:', msg_tmp)
    for i in msg_tmp:
        msg = msg + str(i) + ' '
    # print('msg:', msg)

    print('command: {}, boxid: {}, msg: {}'.format(command,boxid,msg))

    if command == 'send':
        if boxid not in mboxID:
            mboxID[str(boxid)] = deque()
            mboxID[str(boxid)].append(msg)
        
        else:
            mboxID[str(boxid)].append(msg)

        # print(msg,'is stored at ',mboxID[str(boxid)])

    elif command == 'receive':
        if boxid not in mboxID:
            s.sendto(b'No messages',addr)    
        
        if mboxID[str(boxid)]:
            send_msg = mboxID[str(boxid)].popleft()
            s.sendto(send_msg.encode(),addr)

        else:
            s.sendto(b'No messages',addr)    
    
    elif command == 'quit':
        s.close()
        break