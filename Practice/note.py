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
        

