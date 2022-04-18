import socket
bufsize = 1024
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(('localhost',9000))
addr = ('localhost',9000)
for i in range(10):
    time = 0.1
    data = 'hello iot'
    while True:
        sock.send(data.encode())
        sock.settimeout(time)
        try:
            data = sock.recv(bufsize)
        except :
            time *= 2
            if time>2:
                break
        else:
            print('response', data.decode())
            break