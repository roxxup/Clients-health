# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Function.ui'
#
# Created: Mon Oct 26 14:59:58 2015
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

class Ui_Function(object):
    def setupUi(self, Function):
        Function.setObjectName(_fromUtf8("Function"))
        Function.resize(443, 303)
        self.verticalLayout = QtGui.QVBoxLayout(Function)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.PingClientButton = QtGui.QPushButton(Function)
        self.PingClientButton.setObjectName(_fromUtf8("PingClientButton"))
        self.verticalLayout.addWidget(self.PingClientButton)
        self.RamCheckButton = QtGui.QPushButton(Function)
        self.RamCheckButton.setObjectName(_fromUtf8("RamCheckButton"))
        self.verticalLayout.addWidget(self.RamCheckButton)
        self.HardriveCheckButton = QtGui.QPushButton(Function)
        self.HardriveCheckButton.setObjectName(_fromUtf8("HardriveCheckButton"))
        self.verticalLayout.addWidget(self.HardriveCheckButton)
        self.ProcessesCheckButton = QtGui.QPushButton(Function)
        self.ProcessesCheckButton.setObjectName(_fromUtf8("Log Viewer"))
        self.verticalLayout.addWidget(self.ProcessesCheckButton)

        self.retranslateUi(Function)
        QtCore.QMetaObject.connectSlotsByName(Function)

    def retranslateUi(self, Function):
        Function.setWindowTitle(_translate("Function", "FunctionCheck", None))
        self.PingClientButton.setText(_translate("Function", "Ping client ", None))
        self.RamCheckButton.setText(_translate("Function", "RAM Check", None))
        self.HardriveCheckButton.setText(_translate("Function", "HARDRIVE Check", None))
        self.ProcessesCheckButton.setText(_translate("Function", "Log Viewer", None))

