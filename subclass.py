from PyQt4.QtCore import *
from PyQt4.QtGui import *
import socket
import Function
import ProcessesChecker
import HardiskChecker
import PingChecker
import RamChecker
import sys
import os
import time
import logging
class MainFormPing(QDialog,PingChecker.Ui_PingChecker):

    def __init__(self,parent=None):
        super(MainFormPing,self).__init__(parent)
        self.setupUi(self)

        self.connect(self.PingCheckEdit, SIGNAL("returnPressed()"), self.ping)


    def ping(self):
        response = os.system("ping -c 3 " + str(self.PingCheckEdit.text()))
        if response == 0:
            logging.basicConfig(filename='example.log',level=logging.DEBUG)
            logging.info(time.asctime(time.localtime(time.time())))
            QMessageBox.information(self,"PingForm","pinging host up !")


        else:
            QMessageBox.information(self,"PingForm","pinging host down !")
        print (self.PingCheckEdit.text())


class MainFormRam(QDialog,RamChecker.Ui_RamChecker):
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self,parent = None):
        super(MainFormRam,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.RamCheckEdit, SIGNAL("returnPressed()"), self.pingplusram)

    def pingplusram(self):
        response = os.system("ping -c 1 " + str(self.RamCheckEdit.text()))
        if response == 0:
            print (type(self.RamCheckEdit.text()))
            self.s1.connect((self.RamCheckEdit.text(),9999))
            #self.s.send(str('RAM'))
            got=self.s1.recv(1024).decode('ascii')
            QMessageBox.information(self,"PingForm",got)
            logging.basicConfig(filename='example.log',level=logging.DEBUG)
            logging.info(time.asctime(time.localtime(time.time())))

            self.s1.close()

        else:
            QMessageBox.information(self,"PingForm","Host down")

            #QMessageBox.information(self,"PingForm","pinging host down !")
        #print (self.RamCheckEdit.text())


class MainFormHardDisk(QDialog,HardiskChecker.Ui_HardiskChecker):
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self,parent = None):
        super(MainFormHardDisk,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.HardiskCheckEdit, SIGNAL("returnPressed()"), self.pingplusdisk)

    def pingplusdisk(self):
        response = os.system("ping -c 1 " + str(self.HardiskCheckEdit.text()))
        if response == 0:
            print (type(self.HardiskCheckEdit.text()))
            self.s2.connect((self.HardiskCheckEdit.text(),9999))
            #self.s2.send(str('HARDISK'))
            QMessageBox.information(self,"PingForm",self.s2.recv(1024).decode('ascii'))
            logging.basicConfig(filename='example.log',level=logging.DEBUG)
            logging.info(time.asctime(time.localtime(time.time())))

            self.s2.close()

        else:
            QMessageBox.information(self,"PingForm","Host down !")

            #QMessageBox.information(self,"PingForm","pinging host down !")
        #print (self.HardiskCheckEdit.text())


class MainFormProcesses(QDialog,ProcessesChecker.Ui_ProcessesChecker):
    arr = ""
    def __init__(self,parent = None):
        super(MainFormProcesses,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.ProcessesCheckEdit, SIGNAL("returnPressed()"), self.pingplusprocesses)
    def pingplusprocesses(self):
        myobj = open('example.log',"r")
        for l in myobj.readlines():
          self.arr +=l
        QMessageBox.information(self,"PingForm",self.arr)



            #QMessageBox.information(self,"PingForm","pinging host down !")
        #print (self.ProcessesCheckEdit.text())

class MainFormFunction(QDialog,Function.Ui_Function):
    def __init__(self,parent = None):
        super(MainFormFunction,self).__init__(parent)
        self.setupUi(self)
        self.ProcessesCheckButton.clicked.connect(self.ProcessesCheckButton_clicked)
        self.PingClientButton.clicked.connect(self.PingClientButton_clicked)
        self.RamCheckButton.clicked.connect(self.RamCheckButton_clicked)
        self.HardriveCheckButton.clicked.connect(self.HardriveCheckButton_clicked)


    def PingClientButton_clicked(self):
        self.form = MainFormPing()
        self.form.show()
    def RamCheckButton_clicked(self):
        self.form = MainFormRam()
        self.form.show()
    def HardriveCheckButton_clicked(self):
        self.form = MainFormHardDisk()
        self.form.show()
    def ProcessesCheckButton_clicked(self):
        self.form  = MainFormProcesses()
        self.form.show()





app = QApplication(sys.argv)
form = MainFormFunction()
form.show()
app.exec_()
