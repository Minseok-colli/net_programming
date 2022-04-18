# # # import ipaddress
# # # addr4 = ipaddress.ip_address('192.0.2.1')
# # # print(addr4)

# # # addr6 = ipaddress.ip_address('2001:A8::1')
# # # print(addr6)

# # # print(addr6.version)
# # # print(addr4.version)

# # import ipaddress
# # net = ipaddress.ip_network('117.81.220.0/24')
# # print(net.with_netmask)

# # print(net.num_addresses)
# # print(net.netmask)
# # print(net.hostmask)

# import ipaddress

# net = ipaddress.ip_network('114.71.220.0/24')
# addr = ipaddress.ip_address('114.71.220.95')
# addr1 = ipaddress.ip_address('192.168.0.2')

# print(addr1 in net)

# # for x in net.hosts():
# #     print(x)

# print()


import socket

name = socket.gethostname()
print(name)

print(socket.gethostbyname(name))
print(socket.gethostbyname('homepage.sch.ac.kr'))

print(socket.gethostbyname_ex('homepage.sch.ac.kr'))
print(socket.gethostbyaddr('220.69.189.98'))
print(socket.getfqdn('220.69.189.98'))
print(socket.getfqdn('www.google.com'))


Host = [
    'www.sch.ac.kr',
    'homepage.sch.ac.kr',
    'www.naver.com',
    'iot'
]

for host in Host:
    try:
        print('{} : {}'.format(host,socket.gethostbyname(host)))
    except socket.error as msg:
        print('{} : {}'.format(host,msg))


print(socket.getservbyname('http'))
print(socket.getservbyport(80))


for port in [80,443,21,25,143,993,110,995]:
    url = '{}://example.com'.format(socket.getservbyport(port))
    print('{:4d} '.format(port),url)