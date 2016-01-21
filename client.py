# client.py  
import subprocess
import re
from psutil import test
import socket
import time 
# current processes 
a = test().hide()
 
# create a socket object
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = '192.168.0.3'
                         

port = 9999

# connection to hostname on the port.
s1.bind((host, port))



# Receive no more than 1024 bytes
#while 1:
   #print (s.recv(1024)).decode('ascii')
   #s.send(raw_input("Chatiing ==> "))
#print("The time got from the server is %s" % tm.decode('ascii'))
arr = ""
p = subprocess.Popen('ls',shell = True , stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

s1.listen(5)
while True:
    clientsocket,addr = s1.accept()
    print("Got a connection from %s" % str(addr))
    string1=clientsocket.recv(1024)
    string = (re.findall(r'RAM', string1))
    ''.join(string)
    if "RAM" in string:
        print ("gotcha RAM")
    elif "PROCESSES" in string:
        print ("Gotcha processes")
    elif "HARDISK" in string:
        print ("Gotcha hardisk")

    #For RamCheckform
    mem = (psutil.virtual_memory())
    clientsocket.send(str(mem))
    time.sleep(1)
    #For Disk UsageForm
    clientsocket.send(str(psutil.disk_usage('/')))
