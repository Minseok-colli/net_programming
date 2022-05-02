# from cv2 import sort


# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# addr = ('localhost',9000)
# sock.connect(addr)

# msg = sock.recv(1024)
# print(msg.decode())

# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# addr = ('localhost',9000)
# sock.connect(addr)

# msg = sock.recv(1024)
# print(msg.decode())
# name = "Park Minseok"

# sock.send(name.encode())

# msg = sock.recv(1024)
# print(int.from_bytes(msg,'big'))
# sock.close()

# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# port = int(input('Enter the port: '))
# addr = ('localhost',port)
# sock.connect(addr)

# while True:
#     msg = input("Enter the Message: ")
#     sock.send(msg.encode())

#     data = sock.recv(1024)
#     print('Received message : %s' % data.decode())

# sock.close()

# import socket

# port = int(input('Enter the port num: '))
# addr = ('localhost',port)

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(addr)

# msg = sock.recv(1024)
# print(msg.decode())

# sock.close()

# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# addr = ('localhost',2000)
# sock.connect(addr)

# while True:
#     msg = input("Message to Send: ")
#     try:
#         SentByte = sock.send(msg.encode())
#     except:
#         break;
#     else:
#         print('%d bytes are sent.' %SentByte)
    
#     try:
#         data = sock.recv(1024)
#     except:
#         break;
#     else:
#         if not data:
#             break;
#         print("Received Data: %s" %data.decode())

# sock.close()


# import socket

# addr = ('localhost',3000)
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(addr)

# while True:
#     msg = input('number to send 1~3')
#     if msg == 'q':
#         break

#     sock.send(msg.encode())

#     data = sock.recv(1024)
#     print(data.decode())
# sock.close()

# import socket

# addr = ('localhost',2000)
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(addr)

# msg = input('Enter the seek: ')
# sock.send(msg.encode())

# result = sock.recv(1024)
# print(result.decode())

# sock.close()

# import os
# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# port = 9999
# s.bind(('',port))
# s.listen(1)

# while True:
#     cli, addr = s.accept()
#     print(addr,' connected')
    
#     #recv hello
#     msg = cli.recv(1024)

#     if not msg:
#         cli.close()
#         continue
#     elif msg != b'Hello':
#         cli.close()
#         print('clinet: ',addr,msg.decode())
#         continue
#     else:
#         print('client: ',addr,msg.decode())

#     cli.send(b'Filename')

#     bfilenname = cli.recv(1024)
#     if not bfilenname:
#         cli.close()
#         continue

#     filename = bfilenname.decode()
#     print('client:',filename,'request.')

#     try:
#         filesize = os.path.getsize(filename)
#     except:
#         cli.send(b'nofile')
#         cli.close()
#         continue
#     else:
#         cli.send(str(filesize).encode())
    
#     f = open(filename,'rb')
#     data = f.read()
#     cli.sendall(data)

#     msg = cli.recv(1024)
#     if msg == b'bye':
#         print('client',msg.decode())
#         cli.close()
#         f.close()

# import os
# import socket
# import time

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('',9999))
# s.listen(1)

# cli,addr = s.accept()
# while True:
#     print('Client Connected')
#     cli.send(b'Request')

#     data = cli.recv(1024)
#     print(data.decode())

#     temp,humid,light = data.decode().split()
#     current_time = time.strftime('%c', time.localtime(time.time()))
#     string = current_time + ':' + ' Temp:' + temp + ' Humid:' + humid + ' lilum:'+light +'\n'

#     f = open('data','a')
#     f.write(string)
#     f.close()

# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# while True:
#     msg = input('Enter a message:')
#     if msg == 'q':
#         break
#     sock.sendto(msg.encode(),('localhost',9999))
#     data,addr = sock.recvfrom(1024)
#     print("server says: ",data.decode())
# sock.close()

# import socket
# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# while True:
#     send = input('Send: ')
#     sock.sendto(send.encode(),('localhost',3000))
#     if send == 'q':
#         sock.close()
#     data,addr = sock.recvfrom(1024)
#     print("Received: ",data.decode())

# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# for i in range(10):
#     time = 0.1
#     data = 'hi iot'
#     while True:
#         s.sendto(data.encode(),('localhost',4000))
#         print('packet({}) : Waiting up to {} secs for ack'.format(i,time))
#         s.settimeout(time)
#         try:
#             data,addr = s.recvfrom(1024)
#         except:
#             time *= 2
#             if time >2.0:
#                 break
#         else:
#             print('Response',data.decode(),i)
#             break

# import socket
# port = 3000

# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# while True:
#     msg = input('Enter the message("send mboxID message" or "receive mboxID"): ')

#     if msg.startswith('send'): 
#         sock.sendto(msg.encode(), ('localhost', port))
#         print('OK')
    
#     elif msg.startswith('receive'):
#         sock.sendto(msg.encode(), ('localhost', port))
#         data, addr = sock.recvfrom(1024)
#         print(data.decode())
    
#     elif msg == 'quit':
#         sock.sendto('quit'.encode(), ('localhost', port))
#         break

# sock.close()

# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# while True:
#     command = input('Enter the message("send mboxID message" or "receive mboxID"): ')

#     if command.startswith('send'):
#         s.sendto(command.encode(),('localhost',3000))
#         print('OK')

#     elif command.startswith('receive'):
#         s.sendto(command.encode(),('localhost',3000))
#         msg , addr = s.recvfrom(1024)
#         print(msg.decode())

#     elif command.startswith('quit'):
#         s.sendto(b'quit',('localhost',3000))
#         s.close()
#         break

#     else:
#         continue

# import threading
# import datetime

# class mythread(threading.Thread):
#     def __init__(self,name,counter):
#         super().__init__()
#         self.name = name
#         self.counter = counter

#     def run(self):
#         print('\nStarting {}[{}]'.format(self.name,self.counter))
#         print_date(self.name,self.counter)
#         print('\nExiting {}[{}]'.format(self.name,self.counter))

# def print_date(threadname,counter):
#     today = datetime.date.today()
#     print('\n{}[{}]: {}'.format(threadname,counter,today))

# thread1 = mythread('th',1)
# thread2 = mythread('th',2)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print('\nExiting the program')

# import socket
# import threading

# port = 3000
# bufsize = 1024

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('localhost',port))

# while True:
#     msg = input('enter the message:')
#     if msg == 'q':
#         sock.close()
#     sock.send(msg.encode())
#     data = sock.recv(bufsize)
#     if not data:
#         break
#     print('server: {}'.format(data.decode()))


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
#         recv = socket.recv(bufsize)
#         print("receive : {}".format(recv.decode()))

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('localhost',port))

# sendth = threading.Thread(target = sendtask,args=(sock,))
# recvth = threading.Thread(target=recvtask,args=(sock,))

# sendth.start()
# recvth.start()

# import socket
# import threading

# def senddata(sock,id):
#     while True:
#         msg = '['+id+']' + input('enter message:')
#         sock.sendto(msg.encode(),addr)

#         if msg == 'quit':
#             sock.close()
#             break

# def recvdata(sock):
#     while True:
#         msg,addr = sock.recvfrom(1024)
#         print(msg.decode())

# addr = ('localhost',3000)
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# id = input('enter the id: ')    
# s.sendto(str(id).encode(),addr)

# sendth = threading.Thread(target=senddata,args=(s,id,))
# recvth = threading.Thread(target=recvdata,args=(s,))

# sendth.start()
# recvth.start()

# import socket
# import threading

# port = 3333
# bufsize = 1024

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# addr = ('localhost',port)
# s.connect(addr)

# id = input('Enter the id:')
# s.send(id.encode())

# def recvTask(sock):
#     while True:
#         data = sock.recv(bufsize)
#         print(data.decode())    

# tk = threading.Thread(target=recvTask,args=(s,))
# tk.start()

# while True:
#     send = '['+id+']'+':'+ input('Enter: ')
#     s.send(send.encode())
    

# import socket
# port = 3000
# addr= ('localhost',port)

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(addr)

# while True:
#     msg = input('enter the data:')
#     s.send(msg.encode())

#     data = s.recv(1024)
#     print('echo:',data.decode())

# import socket
# import threading

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('localhost',3333))
# id = '[' + input('Enter the name: ')+']'
# s.send(id.encode())

# def recvTask(sock):
#     while True:
#         data = sock.recv(1024)
#         print(data.decode())

# th = threading.Thread(target=recvTask,args=(s,))
# th.start()

# while True:
#     msg = id + input('Enter the message:')
#     s.send(b'\n'+str(msg).encode())
#     if 'quit' in msg:
#         break

# a = {'kim':[23,21,34], 'moon':'guntai','park':183}

# for i in a:
#     print(i)

# for i in a.items():
#     print(i)

# sort(a)

# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('localhost',9000))

# sock.send(b'minseokPark')

# num = sock.recv(1024)
# print(int.from_bytes(num,'big'))ffro

# import socket

# sock = socket.socket()
# sock.connect(('localhost',4000))
# while True:
#     msg = input('enter the message:')
#     sock.send(msg.encode())
#     recv = sock.recv(1024)
#     print("received: ",recv.decode())

# from concurrent.futures import thread
# import threading
# import datetime

# class mythread(threading.Thread):
#     def __init__(self,name,counter):
#         super().__init__()
#         self.name = name
#         self.counter = counter

#     def run(self):
#         print('\nstarting {}[{}]'.format(self.name,self.counter))
#         print_date(self.name,self.counter)
#         print('\n exit {}[{}]'.format(self.name,self.counter))

# def print_date(name,counter):
#     today = datetime.date.today()
#     print('\n{}[{}]: {}'.format(name,counter,today))


# thread1 = mythread('th',1)
# thread2 = mythread('th',2)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('localhost',9000))
# while True:
#     msg = input('Message to send:')
#     sock.send(msg.encode())

#     data = sock.recv(1024)
#     if not data: break
#     print('received message: ',data.decode())

# import socket
# import threading

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('localhost',9000))

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
#     sendth = threading.Thread(target=send,args=(sock,))
#     recvth = threading.Thread(target=recv,args=(sock,))

#     sendth.start()
#     recvth.start()

# import socket
# import threading

# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# addr = ('localhost',9000)

# id = '['+input('Enter the ID:')+']'
# sock.sendto(id.encode(),addr)

# def send(sock):
#     while True:
#         data = input("\nEnter Message: ")
#         msg = id + data
#         sock.sendto(msg.encode(),addr)
    
# def recv(sock):
#     while True:
#         msg, data = sock.recvfrom(1024)
#         print(msg.decode())

# sendth = threading.Thread(target=send,args=(sock,))
# recvth = threading.Thread(target=recv,args=(sock,))

# sendth.start()
# recvth.start()

#multithread 
# import socket
# import threading

# sock = socket.socket()
# sock.connect(('localhost',9000))

# id = '[' + input("Enter the ID:") + ']'
# sock.send(id.encode())

# def send(sock):
#     while True:
#         msg = id +': '+ input()
#         sock.send(msg.encode())

# def recv(sock):
#     while True:
#         data = sock.recv(1024)
#         if not data:
#             sock.close()
        
#         print(data.decode())

# sendth = threading.Thread(target=send,args=(sock,))
# recvth = threading.Thread(target=recv,args=(sock,))

# sendth.start()
# recvth.start()

# import socket

# sock = socket.socket()
# sock.connect(('localhost',9000))

# print(int(sock.recv(1024).decode()))
# sock.close()

# import socket 

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# sock.connect(('localhost',9000))
# while True:
#     msg = input('Enter the msg')

#     sock.send(msg.encode())

#     data = sock.recv(1024)
#     print('received message',data.decode())

import socket
import threading

sock = socket.socket()
sock.connect(('localhost',9000))

def recvTask(sock):
    while True:
        data = sock.recv(1024)
        print('<-', data.decode())


th = threading.Thread(target=recvTask, args=(sock,))
th.start()

my_id = input('Enter your ID: ')
sock.send(('['+my_id+']').encode())

while True:
    msg = '[' + my_id + ']' + input()
    sock.send(msg.encode())