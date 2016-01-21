from PyQt4.QtCore import *
from PyQt4.QtGui import *
from send import SendOtp
import random
import socket
import re
import time
import psutil
import sys
import Verify
import Login
import Function
import sqlite3
import os

class Main(QDialog,Login.Ui_Form):
    dbConn = sqlite3.connect("dbase.db")

    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS Sourcefinal(Name TEXT,Password TEXT,Phone TEXT,Otp TEXT)""")
        self.dbConn.commit()
        self.LoginButton.clicked.connect(self.add_button_clicked)

    def add_button_clicked(self):

        self.Name = str(self.NameEdit.text())
        print (self.Name)
        self.Password = str(self.PassEdit.text())
        print (self.Password)
        self.Phone = str(self.PhoneEdit.text())
        print (self.Phone)
        Otp = str(random.randint(0,99999))



        self.dbCursor.execute('''INSERT INTO Sourcefinal VALUES (?,?,?,?)''',[self.Name, self.Password,self.Phone,Otp])

        self.dbConn.commit()
        SendOtp(Otp,self.Phone)

        QMessageBox.information(self,"OTP message " , "OTP sent to mobile ...")
        self.hide()
        self.form = MainFormVerify()
        self.form.show()
class MainFormVerify(QDialog,Verify.Ui_Verify):
    Otpconfirmed = ""
    dbConn = sqlite3.connect("dbase.db")
    def __init__(self,parent=None):
        super(MainFormVerify,self).__init__(parent)
        self.setupUi(self)

        self.VerifyButton.clicked.connect(self.VerifyButton_clicked)
        #self.SignInButton.clicked.connect(self.SignInButton_clicked)


    def VerifyButton_clicked(self):
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute("""SELECT Otp FROM Sourcefinal""")
        self.OtpVerify = self.OtpLineEdit.text()
        self.Otp = self.dbCursor.fetchall()

        for self.OtpVer  in self.Otp:
            if self.OtpVerify in self.OtpVer:
                self.Otpconfirmed = str(self.OtpVerify)

        if self.Otpconfirmed == self.OtpVerify:
            QMessageBox.warning(self, "Confirmed", "Succesfully Log in and Signup !!!!")
            self.hide()
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
            '''arr = ""
            p = subprocess.Popen('ls',shell = True , stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
            '''
            s1.listen(5)
            while True:
                clientsocket,addr = s1.accept()
                print("Got a connection from %s" % str(addr))
                '''string1=clientsocket.recv(1024)
                string = (re.findall(r'RAM', string1))
                ''.join(string)
                if "RAM" in string:
                    print ("gotcha RAM")
                elif "PROCESSES" in string:
                    print ("Gotcha processes")
                elif "HARDISK" in string:
                    print ("Gotcha hardisk")
'''
                #For RamCheckform
                mem = (psutil.disk_usage('/'))
                clientsocket.send(str(mem))
                #time.sleep(1)

                #For Disk UsageForm
                disk = psutil.virtual_memory()
                clientsocket.send(str(disk))


        else:
            QMessageBox.warning(self, "Confirmed", "try again !")
        self.hide()
    '''def SignInButton_clicked(self):
        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute("""SELECT Name From Sourcefinal""")
        pass'''


app = QApplication(sys.argv)
form = MainFormVerify()
form.show()
app.exec_()
