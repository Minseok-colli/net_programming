import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',9000))
sock.listen(9)

cli, addr = sock.accept()

while True:
    msg = cli.recv(1024)
    print(msg.decode(),"is received from",addr)

    cli.send(msg)