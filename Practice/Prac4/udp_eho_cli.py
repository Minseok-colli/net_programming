import socket

port = 3000

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(('localhost',3000))

while True:
    msg = input("add message:")
    sock.sendto(msg.encode(),('localhost',3000))

    data,addr = sock.recvfrom(1024)
    print("server say",data.decode())