import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',9000))

while True:
    msg = input("enter the message:")
    sock.send(msg.encode)

    print("echo : ",sock.recv(1024).decode)