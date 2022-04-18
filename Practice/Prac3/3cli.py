import socket

sock = socket.socket()
sock.connect(('localhost',9000))

while True:
    msg = input('enter the message:')
    sock.send(msg.encode())

    data = sock.recv(1024)
    if not data:
        sock.close
        break

    print("Anser is ",data.decode())
