from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PingChecker
import sys
import os
class MainFormPing(QDialog,PingChecker.Ui_PingChecker):
    def __init__(self,parent=None):
        super(MainFormPing,self).__init__(parent)
        self.setupUi(self)

        self.connect(self.PingCheckEdit, SIGNAL("returnPressed()"), self.ping)

    def ping(self):
        response = os.system("ping -c 1 " + self.PingCheckEdit.text())
        if response == 0:
            QMessageBox.information(self,"PingForm","pinging host up !")
        else:
            QMessageBox.information(self,"PingForm","pinging host down !")
        print (self.PingCheckEdit.text())






app = QApplication(sys.argv)
form = MainFormPing()
form.show()
app.exec_()
