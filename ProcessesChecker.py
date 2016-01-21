# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProcessesChecker.ui'
#
# Created: Mon Oct 26 15:35:04 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ProcessesChecker(object):
    def setupUi(self, ProcessesChecker):
        ProcessesChecker.setObjectName(_fromUtf8("ProcessesChecker"))
        ProcessesChecker.resize(400, 300)
        self.ProcessesCheckLabel = QtGui.QLabel(ProcessesChecker)
        self.ProcessesCheckLabel.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.ProcessesCheckLabel.setObjectName(_fromUtf8("ProcessesCheckLabel"))
        self.ProcessesCheckEdit = QtGui.QLineEdit(ProcessesChecker)
        self.ProcessesCheckEdit.setGeometry(QtCore.QRect(110, 20, 241, 21))
        self.ProcessesCheckEdit.setObjectName(_fromUtf8("ProcessesCheckEdit"))
        self.ProcessesCheckBrowser = QtGui.QTextBrowser(ProcessesChecker)
        self.ProcessesCheckBrowser.setGeometry(QtCore.QRect(-5, 81, 411, 221))
        self.ProcessesCheckBrowser.setObjectName(_fromUtf8("ProcessesCheckBrowser"))

        self.retranslateUi(ProcessesChecker)
        QtCore.QMetaObject.connectSlotsByName(ProcessesChecker)

    def retranslateUi(self, ProcessesChecker):
        ProcessesChecker.setWindowTitle(_translate("ProcessesChecker", "Form", None))
        self.ProcessesCheckLabel.setText(_translate("ProcessesChecker", "Client IP:> ", None))

