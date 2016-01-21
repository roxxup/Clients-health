#Alarm clock application 
from PySide.QtCore import *
from PySide.QtGui import *

import sys
import time

app = QApplication(sys.argv)

due = QTime.currentTime()
message = "Alert"

try:

    if len(sys.argv) < 2:
        raise ValueError

    hours , minutes  = sys.argv[1].split(":")
    due = QTime(int(hours), int(minutes))


    if not due.invalid():
    	raise ValueError
    if len(sys.argv) > 2:
    	message = " ".joind(sys.argv[2:])
except:
	print "Usage :python Simple aap"
	sys.exit(0)
while QTime.currentTime() < due:
	time.sleep(5)

label = Qlabel("<font color = red size =72 >" + message  + "</font>")
label.setWindowlags(QT.SplashScreen)
label.show()

QTimer.singleShot(10000,app.quit())
app.exec_()
