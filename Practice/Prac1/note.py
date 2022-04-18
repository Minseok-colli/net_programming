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


# import socket
# from collections import deque

# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('',3000))

# mboxID = {}
# while True:
#     data, addr = s.recvfrom(1024)
#     temp = data.decode().split()

#     # print ('temp:', temp)

#     command = temp[0]
#     boxid = temp[1]
#     msg_tmp = temp[2:]
#     msg = ''
#     # print ('msg_tmp:', msg_tmp)
#     for i in msg_tmp:
#         msg = msg + str(i) + ' '
#     # print('msg:', msg)

#     print('command: {}, boxid: {}, msg: {}'.format(command,boxid,msg))

#     if command == 'send':
#         if boxid not in mboxID:
#             mboxID[str(boxid)] = deque()
#             mboxID[str(boxid)].append(msg)
        
#         else:
#             mboxID[str(boxid)].append(msg)

#         # print(msg,'is stored at ',mboxID[str(boxid)])

#     elif command == 'receive':
#         if boxid not in mboxID:
#             s.sendto(b'No messages',addr)    
        
#         if mboxID[str(boxid)]:
#             send_msg = mboxID[str(boxid)].popleft()
#             s.sendto(send_msg.encode(),addr)

#         else:
#             s.sendto(b'No messages',addr)    
    
#     elif command == 'quit':
#         s.close()
#         break


# from concurrent.futures import thread
# import threading

# x = 0

# def increment():
#     global x
#     x+=1

# def thread_task(lock):
#     for _ in range(300000):
#         lock.acquire()
#         increment()
#         lock.release()

# def main_task():
#     global x
#     x = 0

#     lock = threading.Lock()

#     t1 = threading.Thread(target = thread_task, args=(lock,))
#     t2 = threading.Thread(target = thread_task, args=(lock,))

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

# for i in range(10):
#     main_task()
#     print('iteration {0}: x={1}'.format(i,x))


# import threading

# def prtSquare(num):
#     print('sqaure: {}'.format(num**2))

# def prtCube(num):
#     print('cuba:{}'.format(num**3))

# t1 = threading.Thread(target=prtSquare,args=(10,))
# t2 = threading.Thread(target=prtCube,args=(40,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print('done')

# import socket
# import threading

# port = 2500
# bufsize = 1024

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('',port))
# sock.listen(5)

# def echo(sock):
#     while True:
#         data = sock.recv(bufsize)
#         if not data:
#             break
#         print('recevied data: {} '.format(data.decode()))
#         sock.send(data)

#     sock.close()

# while True:
#     conn, addr = sock.accept()
#     print('connect with {}'.format(addr))
#     th = threading.Thread(target=echo,args=(conn,))
#     th.start()

# import threading
# import socket

# port = 3000
# bufsize = 1024

# def sendtask(socket):
#     while True:
#         send = input('send:')
#         socket.send(send.encode())

# def recvtask(socket):
#     while True:
#         msg = socket.recv(1024)
#         if not msg:
#             break
#         print('receive: {}'.format(msg.decode()))

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('',port))
# sock.listen(1)

# conn,addr = sock.accept()
# sendth = threading.Thread(target=sendtask,args=(conn,))
# recvth = threading.Thread(target=recvtask,args=(conn,))

# sendth.start()
# recvth.start()

# import socket
# import time

# client = []

# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('',3000))

# print('server start')

# while True:
#     data, addr = s.recvfrom(1024)
#     if 'quit' in data.decode():
#         client.remove(addr)
#         continue

#     if addr not in client:
#         client.append(addr)
#         print('new client')

#     print(time.asctime() + str(addr) +':'+data.decode())

#     for i in client:
#         if i != addr:
#             s.sendto(data,i)


#TCP multi Thread Server

# import socket
# import time
# import threading

# port = 3333
# bufsize = 1024
# client = []

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',port))
# s.listen(5)

# def recvTask(conn):
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             break

#         elif 'quit' in data.decode():
#             if conn in  client:
#                 print(conn,' exitted.')
#                 client.remove(conn)
        
#         for cli in client:
#             if cli != conn:
#                 cli.send(data)
#                 print(time.asctime() + str(addr) + ":" + data.decode())
    

# while True:
#     conn, addr = s.accept()

#     if addr not in client:
#         client.append(conn)
#         print('new client joined: '+addr)

#     recvtk = threading.Thread(target = recvTask,args=(conn,))
#     recvtk.start()


# import socket
# import time
# import threading

# port = 3333
# bufsize = 1024
# client = []

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',port))
# s.listen(5)

# def serverTask(conn,addr):
#     while True:    
#         msg = conn.recv(bufsize)
#         if msg.decode() == 'quit':
#             client.remove(conn)
#             conn.close()
#             print(addr,'removed')
        
#         for x in client:
#             if x != conn:
#                 x.send(msg)

# while True:
    
#     conn, addr = s.accept()
#     data = conn.recv(bufsize)
    
#     if addr not in client:
#         client.append(conn)
#         print('new client joined: '+str(addr))

#     tk = threading.Thread(target=serverTask,args=(conn,addr))
#     tk.start()

    
# import socket
# import threading

# port = 3000
# bufsize = 1024

# sharedadta = 0

# def threadplus(sock):
#     global sharedadta, lock
#     for _ in range(30000000):
#         lock.acquire()
#         sharedadta +=1
#         lock.release()
#     print(sharedadta)
#     sock.send(str(sharedadta).encode())
#     sock.close()

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',port))
# s.listen(6)

# lock = threading.Lock()
# while True:
#     client, addr = s.accept()
#     print('connected by ',addr)
#     tk = threading.Thread(target=threadplus,args=(client,))
#     tk.start()


# import socket
# import select

# socks = []
# buffer = 1024
# port = 2500

# s_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s_sock.bind(('',port))
# s_sock.listen(5)

# socks.append(s_sock)
# print(str(socks) + 'is waiting:')

# while True:
#     r_sock,w_sock,x_sock = select.select(socks,[],[])

#     for s in r_sock:
#         if s == s_sock:
#             c_sock, addr = s_sock.accept()
#             socks.append(c_sock)
#             print('client ({}) connected'.format(addr))
#         else:
#             data = s.recv(buffer)
#             if not data:
#                 s.close()
#                 socks.remove(s)
#                 continue
#         print('Received:',data.decode())
#         s.send(data)



# import socket
# import select

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',3000))
# s.listen(5)

# socks = []

# socks.append(s)
# while True:
#     r_sock,w_sock,x_sock = select.select(socks,[],[])

#     for k in r_sock:
#         if k == s:
#             csock,addr = s.accept()
#             socks.append(csock)
#             print('client ({}) is connected.'.format(addr))
#         else:
#             data = k.recv(1024)
#             if not data:
#                 k.close()
#                 socks.remove(k)
#                 continue
#             print('receive from ({}):'.format(addr),data.decode())
#             k.send(data)

# import socket
# import select
# import time

# port = 3000
# bufsize = 1024

# sockets = []

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',port))
# s.listen(5)

# sockets.append(s)
# print('Server Started')

# while True:
#     r_sock,w_sock,e_sock = select.select(sockets,sockets,[])

#     for k in r_sock:
#         if k == s:
#             cli,addr = s.accept()
#             print('new client ({})'.format(addr))
#             sockets.append(cli)
#         else:
#             data = k.recv(bufsize)
#             if not data:
#                 k.close()
#                 sockets.remove(k)
#                 continue

#             for sd in w_sock:
#                 if sd!=cli:
#                     sd.send(data)
#             print(time.asctime() + '({})'.format(str(addr))+ ':' +data.decode())
                

# import time
# import socket, select

# port = 3333
# BUFFSIZE = 1024
# socks = []

# s_sock = socket.socket()
# s_sock.bind(('', port))
# s_sock.listen(4)

# socks.append(s_sock)
# print(str(port) + '에서 접속 대기 중')

# while True :
#     r_sock, w_sock, e_sock = select.select(socks, socks, [])

#     for s in r_sock:
#         if s == s_sock:
#             c_sock, addr = s_sock.accept() 
#             if c_sock not in socks:
#                 socks.append(c_sock)
#                 print('client ({}) connectes'.format(addr))
#         else:
#             data = s.recv(BUFFSIZE)
#             if not data:
#                 break
#             elif 'quit' in data.decode():
#                 if s in socks:
#                     print(addr, 'exited')
#                     s.close()
#                     socks.remove(s)
#                     continue

#             for client in w_sock:
#                 if client != s:
#                     client.send(data)
#             print(time.asctime() + str(addr) + ':' + data.decode())


# from asyncio import events
# import selectors
# import socket

# sel = selectors.DefaultSelector()

# def acept(sock,mask):
#     conn,addr = sock.accept()
#     print('conncet from',addr)
#     sel.register(conn,selectors.EVENT_READ,read)

# def read(conn,mask):
#     data = conn.recv(1024)
#     if not data:
#         sel.unregister(conn)
#         conn.close()
#         return
#     print('receive data:',data.decode())
#     conn.send(data)

# sock = socket.socket()
# sock.bind(('',2500))
# sock.listen(5)

# sel.register(sock,selectors.EVENT_READ,acept)
# while True:
#     events = sel.select()
#     for key,mask in events:
#         callback = key.data
#         callback(key.fileobj,mask)

# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('',9000))
# sock.listen()

# cli,addr = sock.accept()

# print('Connect from ({},{})'.format(addr[0],addr[1]))
# data = cli.recv(1024)
# print(data.decode())

# num = 20191505
# cli.send(num.to_bytes(8,'big'))

# import socket
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('google.com',80))
# sock.send(b'GET / HTTP/1.1 \r\n\r\n')
# data = sock.recv(1024)
# print(data.decode())
# sock.close()


# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('',4000))
# sock.listen(3)

# cli,addr = sock.accept()
# while True:
#     msg = cli.recv(1024)
#     if not msg:
#         cli.close()
#         sock.close()
        
#     print('arrived:',msg.decode())
#     cli.send(msg)

# import threading
# from turtle import done

# def prtSquare(num):
#     print("Square: {}".format(num**2))

# def ptrCube(num):
#     print("Cube {}".format(num**3))

# t1 = threading.Thread(target=prtSquare,args=(10,))
# t2 = threading.Thread(target=ptrCube,args=(4,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print('done')

# import threading

# x = 0 

# def increment():
#     global x
#     x += 1

# def thread_task(lock):
#     for __ in range(1000000):
#         lock.acquire()
#         increment()
#         lock.release()
# def main_task():
#     global x
#     x = 0
#     lock = threading.Lock()
#     t2 = threading.Thread(target=thread_task,args=(lock,))
#     t1 = threading.Thread(target=thread_task,args=(lock,))

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

# for i in range(10):
#     main_task()
#     print('interaction {0}: x = {1}'.format(i,x))

#server

# import socket
# import threading

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('',9000))
# sock.listen(5)

# def echo(cli):
#     while True:
#         msg = cli.recv(1024)
#         if not msg:
#             break
#         print('Received message: ',msg.decode())
#         cli.send(msg)
#     cli.close()

# while True:
#     cli,addr = sock.accept()
#     print('connected by ',addr)
#     recvth = threading.Thread(target=echo,args=(cli,))
#     recvth.start()

# from calendar import c
# import socket
# import threading

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('',9000))
# sock.listen(4)

# def send(conn):
#     while True:
#         msg = input('Enter the msg')
#         conn.send(msg.encode())


# def recv(conn):
#     while True:
#         msg = conn.recv(1024)
#         if not msg:
#             conn.close()
#             break

#         print('\nreceived: ',msg.decode())

# while True:
#     conn, addr = sock.accept()
#     print('Connceted by',addr)

#     sendth = threading.Thread(target=send,args=(conn,))
#     recvth = threading.Thread(target=recv,args=(conn,))

#     sendth.start()
#     recvth.start()

# from pydoc import cli
# import socket
# import threading

# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# sock.bind(('',9000))

# print('server started')
# client = []

# while True:
    
#     data,addr = sock.recvfrom(1024)
#     if 'quit' in data.decode():
#         if addr in client:
#             client.remove(addr)
#             print(addr,'is quit.')
#             continue
#     if addr not in client:
#         client.append(addr)
#         print('new client',addr)

#     for c in client:
#         if c != addr:
#             sock.sendto(data,c) 

#multi thread
# import socket
# import threading
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('',9000))
# sock.listen(5)

# client = []

# while True:
#     cli, addr = sock.accept()

#     #check client
#     if cli not in client:
#         client.append(cli)
#         print('connected with ',addr)

#     def send(cli):
#         while True:
#             msg = cli.recv(1024)
#             if not msg:
#                 cli.close()


#             if 'quit' in msg.decode():
#                 client.remove(cli)
#                 print(cli,'is quit')
#                 continue

#             print(msg.decode())
#             for c in client:
#                 if c != cli:
#                     c.send(msg)
#     sendth = threading.Thread(target = send, args=(cli,))
#     sendth.start()  

# import socket
# import threading

# sdata = 0
# lock = threading.Lock()
# sock = socket.socket()
# sock.bind(('',9000))
# sock.listen(4)

# def share(cli):
#     global sdata, lock
#     lock.acquire()
#     for __ in range(10000000):
#         sdata += 1
#     lock.release()
#     print (sdata)
#     cli.send(str(sdata).encode())
#     cli.close()

# while True:
#     cli, addr = sock.accept()

#     print('connected by:', addr)
#     th = threading.Thread(target = share,args=(cli,))
#     th.start()

# import select
# import socket

# sock = socket.socket()
# sock.bind(('',9000))
# sock.listen(4)

# socks = []

# socks.append(sock)
# while True:
#     r,w,e = select.select(socks,[],[])

#     for s in r:
#         if s == sock:
#             newsock , addr = sock.accept()
#             socks.append(newsock)
#             print('clinet ({}) is connected'.format(addr))
        
#         else:
#             data = s.recv(1024)
#             if not data:
#                 s.close()
#                 socks.remove(s)
#                 continue
#             print('received',data.decode())
#             s.send(data)

# import selectors
# import socket

# sel = selectors.DefaultSelector()

# sock = socket.socket()
# sock.bind(('',9000))
# sock.listen(4)

# def accept(sock, mask):
#     conn, addr = sock.accept()
#     print(' connect from',addr)
#     sel.register(conn,selectors.EVENT_READ,read)

# def read(sock, mask):
#     data  = sock.recv(1024)
#     if not data:
#         sel.unregister(sock)
#         sock.close()
#         return
#     print("received data: ",data.decode())
#     sock.send(data)

# sel.register(sock,selectors.EVENT_READ,accept)
# while True:
#     events = sel.select()
#     for key, mask in events:
#         callback = key.data
#         callback(key.fileobj,mask)


import socket
import selectors

sock = socket.socket()
sock.bind(('',9000))
sock.listen(4)


def accept(sock,mask):
    conn,addr = sock.accept()
    print('connected from',addr)
    sel.register(conn,selectors.EVENT_READ,recv)

def recv(sock,mask):
    data = sock.recv(1024)
    if not data:
        sel.unregister()
        sock.close()
        return

    print('received data: ',data.decode())
    sock.send(data)

while True:
    sel = selectors.DefaultSelector()
    sel.register(sock,selectors.EVENT_READ,accept)

    while True:
        events = sel.select()
        for key,mask in events:
            callback = key.data
            callback(key.fileobj,mask)
