from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    fname = req[0].split()[1][1:]

    if fname == 'index.html':
        f = open(fname, 'r', encoding='utf-8')
        mimeType = 'text/html'
        data = f.read()

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(data.encode('euc-kr', 'ignore'))

    elif fname == 'iot.png':
        f = open(fname, 'rb')
        mimeType = 'image/png'
        data = f.read()
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(data)

    elif fname == 'favicon.ico':
        f = open(fname, 'rb')
        mimeType = 'image/x-icon'
        data = f.read()
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(data)

    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')


    c.close()
