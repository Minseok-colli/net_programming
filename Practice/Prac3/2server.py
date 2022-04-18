import socket

sock = socket.socket()
sock.bind(('',9000))
sock.listen(2)

while True:
    cli,addr = sock.accept()

    name = cli.recv(1024)
    print(name.decode())

    num = 20191505
    cli.send(num.to_bytes(8,'big'))