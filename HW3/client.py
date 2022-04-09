from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    print("Calculate: ")
    op = input()
    
    if op == 'q':
        break
    
    s.send(op.encode())

    print('Result : ', s.recv(1024).decode())

s.close()