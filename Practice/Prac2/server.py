import socket
import time
import os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',3000))
cli1 = sock.accept()

sock2.bind(('',3001))
cli2 = sock.accept()

sock.listen(2)


while True:
    input = input('Enter the 1 or 2)')
    
    if input == '1':
        print('device connected')
        cli1.send(b'Request')

        data = cli1.recv(1024)
        if not data:
            cli1.close()
            print('no data')
        elif data == b'exit':
            cli1.close()
            sock.close()
            break

        data = data.decode()
        temp, humid, illium = data.split(',')
        filedata = 'temp = {}, humid = {}, illium = {} \n'.format(temp,humid,illium)

        f = open('data','a')
        f.write(filedata)

    if input =='2':
        print('device connected')
        cli2.send(b'Request')

        data = cli2.recv(1024)
        if not data:
            cli2.close()
            print('no data')
        elif data == b'exit':
            cli2.close()
            sock.close()
            break

        data = data.decode()
        temp, humid, illium = data.split(',')
        filedata = 'park = {}, min = {}, seok = {} \n'.format(temp,humid,illium)

        f = open('data','a')
        f.write(filedata)

    
    