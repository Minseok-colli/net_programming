import socket

sock = socket.socket()
sock.connect(('localhost',9000))

sock.send(b'minseok')

data = sock.recv(1024)
print(int.from_bytes(data,'big'))