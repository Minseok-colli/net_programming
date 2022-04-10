import socket
import struct
import binascii

class Iphdr:
    def __init__(self, sourceport, DestPort, length, Checksum):
        self.SourcePort = sourceport
        self.DestPort = DestPort
        self.length = length
        self.Checksum = Checksum

    def pack_Iphdr(self):
        packed = b''
        packed += struct.pack('!HH',self.SourcePort,self.DestPort)
        packed += struct.pack('!HH',self.length,self.Checksum)
        return packed
    
def unpack_Iphdr(buffer):
    unpacked = struct.unpack('!HHHH',buffer[:16])
    return unpacked

def getSrcPort(unpacked_ipheader):
    return unpacked_ipheader[0]

def getDstPort(unpacked_ipheader):
    return unpacked_ipheader[1]

def getLength(unpacked_ipheader):
    return unpacked_ipheader[2]

def getChecksum(unpacked_ipheader):
    return unpacked_ipheader[3]

ip = Iphdr(5555,80,1000,0xFFFF)
packed_iphdr = ip.pack_Iphdr()
print(binascii.b2a_hex(packed_iphdr))

unpacked_iphdr = unpack_Iphdr(packed_iphdr)
print(unpacked_iphdr)
print('Source Port:{} Destination Port:{} Length:{} CheckSum:{}'.format(getSrcPort(unpacked_iphdr),getDstPort(unpacked_iphdr),getLength(unpacked_iphdr),getChecksum(unpacked_iphdr)))