from http import client
from operator import truediv
from pydoc import cli
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client,addr = s.accept()
    print("connection from : ",addr)
    client.send(b'hello '+addr[0].encode())
    client.close()