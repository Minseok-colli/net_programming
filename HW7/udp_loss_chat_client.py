import socket
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0
    while reTx <=3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(),('localhost',port))
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except :
            reTx += 1
            continue
        else:
            break
        
    sock.settimeout(None)   
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack',addr)
            print('<-',data.decode())
            break