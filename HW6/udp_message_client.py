from socket import *

port = 5555
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("send [mBoxID] message" or "receive [mBoxID] : ')
    
    if msg.startswith('send'): 
        sock.sendto(msg.encode(), ('localhost', port))
        print('OK')
    
    elif msg.startswith('receive'):
        sock.sendto(msg.encode(), ('localhost', port))
        data, addr = sock.recvfrom(BUFF_SIZE)
        print(data.decode())
    
    elif msg == 'quit':
        sock.sendto('quit'.encode(), ('localhost', port))
        break

sock.close()