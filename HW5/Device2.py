from asyncio.windows_utils import BUFSIZE
from socket import *
import random

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7778))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUFSIZE)

    if not msg:
         conn.close()
         continue

    elif msg == b'quit':
        conn.close()
        continue
    
    elif msg == b'Request':
        heart = random.randint(40, 140)
        walk = random.randint(2000, 6000)
        kcal = random.randint(1000, 4000)

        conn.send(f'{heart},{walk},{kcal}'.encode())