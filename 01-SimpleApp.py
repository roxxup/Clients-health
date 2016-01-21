import socket
import re
import time
import psutil
class Gotcha:
    def __init__(self):

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

            s1.listen(5)
            while True:
                clientsocket,addr = s1.accept()
                print("Got a connection from %s" % str(addr))
                Gotcha()

                string1=clientsocket.recv(1024)
                string = (re.findall(r'RAM', string1))
                ''.join(string)
                if "RAM" in string:
                    print ("gotcha RAM")
                    self.RamHandler()
                elif "PROCESSES" in string:
                    print ("Gotcha processes")
                    self.ProcessHandler()
                elif "HARDISK" in string:
                    print ("Gotcha hardisk")
                    self.HardiskHandler()
    def RamHandler(self):
        mem = (psutil.virtual_memory())
        self.clientsocket.send(str(mem))
        time.sleep(1)
    def HardiskHandler(self):
                disk = (psutil.disk_usage('/'))
                self.clientsocket.send(str(disk))
                time.sleep(1)
    def ProcessHandler(self):
                process = (psutil.test())
                self.clientsocket.send(str(process))
                time.sleep(1)

if __name__ == '__main__':
    Gotcha()
