import socket
import random
bufsize= 1024
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('',9000))
while True:
    data, addr = sock.recvfrom(bufsize)
    if random.randint(1,10) <= 9:
        print('packet from {} is loss'.format(addr))
        continue
    print('packet is {} from {}'.format(data.decode(),addr))

    sock.sendto('ack'.encode(),addr)