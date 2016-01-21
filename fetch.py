import platform
import re

a = str(platform.platform())
print (a)

print (re.split)






'''import sqlite3 as lt
import sys
con = lt.connect("students.db")
with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM Eng")
	rows = cur.fetchall()
	for x in rows:
		print(x)

con.close()'''''

class MainFormProcesses(QDialog,ProcessesChecker.Ui_ProcessesChecker):
    def __init__(self,parent = None):
        super(MainFormProcesses,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.ProcessesCheckEdit , SIGNAL("returnPressed()"), self.pingplusprocesses)
    def pingplusprocesses(self):
        response = os.system("ping -c 1 " + str(self.pingplusprocesses))
        if response == 0:
            print (type(self.ProcessesCheckEdit.text()))
            s.connect((self.ProcessesCheckEdit.text(),9999))
            s.send(str('PROCESSES'))
            QMessageBox.information(self,"PingForm",s.recv(32423).decode('ascii'))

        else:
            QMessageBox.information(self,"PingForm","Host down !")

            #QMessageBox.information(self,"PingForm","pinging host down !")
        print (self.ProcessesCheckEdit.text())