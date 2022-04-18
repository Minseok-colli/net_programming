import socket
import selectors

oper = ['+','-','*','/']

def accept(conn,mask):
    cli, addr = conn.accept()
    print('new connect with ',addr)
    sel.register(cli,selectors.EVENT_READ,recv)

def recv(cli,mask):
    msg = cli.recv(1024).decode()
    msg = msg.replace(" ","")

    print (msg)

    for x in msg:
        if x in oper:
            a,b = msg.split(x)
            a = int(a)
            b = int(b)

            if x == '+':
                result = a+b
            elif x == '-':
                result = a-b
            elif x == '*':
                result = a*b
            elif x == '/':
                result = round(float(a/b),1)
            print (result)

            cli.send(str(result).encode())




sock = socket.socket()
sock.bind(('',9000))
sock.listen(4)

sel = selectors.DefaultSelector()

sel.register(sock,selectors.EVENT_READ,accept)

while True:
    events = sel.select()
    for key,mask in events:
        callback = key.data
        callback(key.fileobj,mask)