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