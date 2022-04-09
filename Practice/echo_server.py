from asyncio.windows_utils import BUFSIZE
from socket import *

port = 2500
BUFSIZE = 1024
sock = socket(AF_INET,SOCK_STREAM)
sock.bind(('',port))
sock.listen(1)

conn, (remothost, remoteport) = sock.accept()
print('connceted by', remothost, remoteport)
while True:
    data = conn.recv(BUFSIZE)
    print("Recevied message: ", data.decode())
    conn.send(data)

    if(data.decode()=='end'):
        conn.close()
        sock.close()
conn.close()
sock.close()