# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PingChecker.ui'
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

class Ui_PingChecker(object):
    def setupUi(self, PingChecker):
        PingChecker.setObjectName(_fromUtf8("PingChecker"))
        PingChecker.resize(353, 45)
        self.verticalLayout = QtGui.QVBoxLayout(PingChecker)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.PingCheckEdit = QtGui.QLineEdit(PingChecker)
        self.PingCheckEdit.setObjectName(_fromUtf8("PingCheckEdit"))
        self.verticalLayout.addWidget(self.PingCheckEdit)

        self.retranslateUi(PingChecker)
        QtCore.QMetaObject.connectSlotsByName(PingChecker)

    def retranslateUi(self, PingChecker):
        PingChecker.setWindowTitle(_translate("PingChecker", "PingChecker", None))

