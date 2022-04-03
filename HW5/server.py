from socket import *
import time

BUF_SIZE = 1024
LENGTH = 20

while True:
    user_input = input()

    socket1 = socket(AF_INET, SOCK_STREAM)
    socket1.connect(('localhost', 7777))

    socket2 = socket(AF_INET, SOCK_STREAM)
    socket2.connect(('localhost', 7778))

    if user_input == '1':
        socket1.send(b'Request')
        msg = socket1.recv(BUF_SIZE)

        temp, humid, lilum = msg.decode().split(',')
        current_time = time.strftime('%c', time.localtime(time.time()))
        string = current_time + f': Device1: Temp={temp}, Humid={humid}, Illum={lilum}\n'
        print(string)

        f = open('data.txt', 'a')
        f.write(string)
        f.close()

    elif user_input == '2':
        socket2.send(b'Request')
        msg = socket2.recv(BUF_SIZE)

        heartbeat, steps, cal = msg.decode().split(',')
        current_time = time.strftime('%c', time.localtime(time.time()))
        string = current_time + f': Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}\n'
        print(string)
        
        f = open('data.txt', 'a')
        f.write(string)
        f.close()

    elif user_input == 'quit':
        socket1.send(b'quit')
        socket2.send(b'quit')
        break