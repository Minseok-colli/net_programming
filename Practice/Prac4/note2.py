#멀티스레드 에코 클라이언트
# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('localhost',9000))

# while True:
#     msg = input('enter the message:')
#     sock.send(msg.encode())

#     data = sock.recv(1024)
#     if not data:
#         sock.close()
#         break

#     print('echo: ',data.decode())

#멀티스레드 채팅 클라이언트

# import socket
# import threading

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('localhost',9000))

# def recv(sock):
#     while True:
#         msg =sock.recv(1024)
#         print( 'recv' ,msg.decode())

# def send(sock):
#     while True:
#         msg = input('send:')
#         sock.send(msg.encode())

# t1 = threading.Thread(target=recv,args=(sock,))
# t2 = threading.Thread(target=send,args=(sock,))

# t1.start()
# t2.start()

#멀티스레드 단체채팅 udp cli

# import socket
# import threading

# def recv(sock):
#     while True:
#         data,msg = sock.recvfrom(1024)
#         print(data.decode())

# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# id = input('Enter your name: ')
# sock.sendto(id.encode(),('localhost',9000))

# t1 = threading.Thread(target=recv,args=(sock,))
# t1.daemon = True
# t1.start()

# while True:
#     msg = '['+id+']' + input()
#     sock.sendto(msg.encode(),('localhost',9000))


# tcp 멀티스레드 단체 채팅 클라이언트
import socket
import threading

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',3000))

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

