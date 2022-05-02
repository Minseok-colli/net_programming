import socket

port = 3000
bufsize = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('',port))

while True:
    msg , addr = sock.recvfrom(1024)
    print('received,',msg.decode())

    sock.sendto(msg,addr)