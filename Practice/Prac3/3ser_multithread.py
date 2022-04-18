#TCP multi thread calculator

import socket
import socket
import threading

sock = socket.socket()
sock.bind(('',9000))
sock.listen(4)

cal = []
oper = ['+','-','*','/']

def recv(sock):
    while True:
        msg = sock.recv(1024)
        mesg = msg.decode().replace(" ","")
        print(mesg)
        for x in mesg:
            if x in oper:
                a,b = mesg.split(x)
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

                for k in cal:
                    if k == sock:
                        k.send(str(result).encode())

while True:
    conn,addr = sock.accept()
    recvth = threading.Thread(target=recv,args=(conn,))

    if addr not in cal:
        cal.append(conn)

    recvth.start()
            

