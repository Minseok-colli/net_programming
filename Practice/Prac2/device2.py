import socket
import random
from tracemalloc import stop

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 3001
addr = ('localhost',port)
data,addr = s.accept(addr)

#connect succed
connect_mesg = s.recv(1024)

if not connect_mesg:
    s.close()
elif connect_mesg != b'Request':
    s.close()
else:
    print('Server Connected')

while True:
    choose = input('Send or stop:')
    if choose == 'stop':
        s.close()
        break
    else:
        temp = random.randint(0,40)
        humid = random.randint(0,100)
        illium = random.randint(70,150)

        msg = '{},{},{}'.format(temp,humid,illium)
        s.send(msg.encode())

