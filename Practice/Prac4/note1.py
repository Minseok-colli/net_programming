#Thread 구현 server.py

# import threading


# def square(num):
#     print( num**2)

# def cube(num):
#     print( num**3)

# t1 = threading.Thread(target=square,args=(3,))
# t2 = threading.Thread(target=cube,args=(3,))

# t1.start() 
# t2.start()


#글로벌 스레드 

# import threading
# x = 0
# def increase():
#     global x
#     x += 1

# def thread_task(lock):
#     for __ in range(1000000):
#         lock.acquire()
#         increase()
#         lock.release()

# def maintask():
#     global x
#     lock = threading.Lock()
#     x = 0

#     t1=threading.Thread(target=thread_task,args=(lock,))
#     t2=threading.Thread(target=thread_task,args=(lock,))

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

# for i in range(10):
#     maintask()
#     print('iteration {}: x={}'.format(i,x))



#멀티스레드 에코 서버

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
            
#         print('received message:',msg.decode())

#         cli.send(msg)
#     cli.close()


# while True:
#     cli, addr = sock.accept()
#     print('connected with ',addr)

#     t1 = threading.Thread(target=echo,args=(cli,))
#     t1.start()

#멀티스레드 채팅 서버

# import socket
# import threading

# def recv(cli):
#     while True:
#         msg = cli.recv(1024)
#         print("recv: ",msg.decode())

# def send(cli):
#     while True:
#         msg = input('send:')
#         cli.send(msg.encode())

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('',9000))
# sock.listen(5)

# while True:
#     cli,addr = sock.accept()
#     print('connected with ',addr)

#     t1 = threading.Thread(target=recv,args=(cli,))
#     t2 = threading.Thread(target=send,args=(cli,))
#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

#단체채팅 udp ser

# import socket

# client = []

# sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# sock.bind(('',9000))

# while True:
#     data ,addr = sock.recvfrom(1024)

#     if 'quit' in data.decode():
#         if addr in client:
#             client.remove(addr)
#             continue

#     if addr not in client:
#         client.append(addr)
#         print('new client ',addr)

#     for cli in client:
#         if cli != addr:
#             sock.sendto(data,cli)
    
#tcp multithread

# from socket import *
# import threading
# import time

# port = 3333
# BUFFSIZE = 1024

# clients = []

# def sendTask(conn):
#     while True:
#         data = conn.recv(BUFFSIZE)
#         print(data.decode())
#         if 'quit' in data.decode():
#             print(addr, 'exited')
#             clients.remove(conn)
#             break

#         print(time.asctime() + str(addr) + ':' + data.decode())

#         for client in clients:
#             if client != conn:
#                 client.send(data)
#     conn.close()

# sock = socket(AF_INET, SOCK_STREAM)
# sock.bind(('', port))
# sock.listen(5)

# while True:
#     conn, addr = sock.accept()

#     if conn not in clients:
#         print('new client', addr)
#         clients.append(conn)
        
#     th = threading.Thread(target=sendTask, args=(conn,))
#     th.start()


#select 에코 서버

# import select
# import socket

# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('',9000))
# sock.listen(4)

# socks = []
# socks.append(sock)

# while True:
#     rsock, wsock, esock = select.select(socks,[],[])

#     for s in rsock:
#         if s == sock:
#             csock,addr = sock.accept()
#             socks.append(csock)
#             print ('client ({}) connected'.format(addr))
#         else:
#             data = s.recv(1024)
#             if not data:
#                 s.close()
#                 socks.remove(s)
#                 continue
#             print("received: ",data.decode())
#             s.send(data)

#select 단체 채팅 서버
import time
import socket, select

port = 3000
BUFFSIZE = 1024
socks = [] 

s_sock = socket.socket() 
s_sock.bind(('', port))
s_sock.listen(4)

socks.append(s_sock)
print(str(port) + '에서 접속 대기 중')

while True :
    r_sock, w_sock, e_sock = select.select(socks, socks, [])

    for s in r_sock: 
        if s == s_sock: 
            c_sock, addr = s_sock.accept()
            if c_sock not in socks:
                socks.append(c_sock) 
                print('client ({}) connectes'.format(addr))
        else:
            data = s.recv(BUFFSIZE)
            if not data:
                break
            elif 'quit' in data.decode():
                if s in socks: 
                    print(addr, 'exited')
                    s.close()
                    socks.remove(s) 
                    continue
            for client in w_sock:
                    if client != s:
                        client.send(data)
            print(time.asctime() + str(addr) + ':' + data.decode())