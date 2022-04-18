from asyncio.windows_utils import BUFSIZE
import socket

port = int(input("Port No: "))
address = ("localhost", port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while  True:
    msg = input("Message to Send: ")
    s.send(msg.encode())
    data = s.recv(BUFSIZE)
    print("Recevied message: %s" % data.decode())
    if(data.decode() == 'end'):
        s.close()
s.close()