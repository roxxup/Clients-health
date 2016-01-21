# server.py
from subprocess import call 
import socket                                         
import time
import os
# creating chatclient
def chatclient(clisock):
  while 1:
    clisock.send(raw_input('chatting ==> '))
    print (clisock.recv(1024)).decode('ascii')
def ping(clisock):
   response = os.system("ping -c 1 " + clisock)
   if response == 0:
     print clisock , 'is up !'
   else: 
     print clisock, 'is down !'
def getls(clisock):
  print "list the content -->"
  print (clisock.recv(10000)).decode('ascii')
def ps(clisock):
  while 1:
    print (clisock.recv(34234)).decode('ascii')
# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = '192.168.0.3'
port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    #print addr[0]      

    print("Got a connection from %s" % str(addr))
    # currentTime = time.ctime(time.time()) + "\r\n"
    # clientsocket.send(currentTime.encode('ascii'))
    #chatclient(clientsocket)
    #ping(addr[0])
    #getls(clientsocket)
    ps(clientsocket)
