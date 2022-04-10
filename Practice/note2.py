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

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    command = input('Enter the message("send mboxID message" or "receive mboxID"): ')

    if command.startswith('send'):
        s.sendto(command.encode(),('localhost',3000))
        print('OK')

    elif command.startswith('receive'):
        s.sendto(command.encode(),('localhost',3000))
        msg , addr = s.recvfrom(1024)
        print(msg.decode())

    elif command.startswith('quit'):
        s.sendto(b'quit',('localhost',3000))
        s.close()
        break

    else:
        continue