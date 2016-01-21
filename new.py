import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.0.3',9999))
getr=s.recvfrom(23344)
print getr