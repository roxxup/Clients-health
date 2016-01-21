# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HardiskChecker.ui'
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

class Ui_HardiskChecker(object):
    def setupUi(self, HardiskChecker):
        HardiskChecker.setObjectName(_fromUtf8("HardiskChecker"))
        HardiskChecker.resize(410, 141)
        self.horizontalLayout = QtGui.QHBoxLayout(HardiskChecker)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.HardiskCheckLabel = QtGui.QLabel(HardiskChecker)
        self.HardiskCheckLabel.setObjectName(_fromUtf8("HardiskCheckLabel"))
        self.horizontalLayout.addWidget(self.HardiskCheckLabel)
        self.HardiskCheckEdit = QtGui.QLineEdit(HardiskChecker)
        self.HardiskCheckEdit.setObjectName(_fromUtf8("HardiskCheckEdit"))
        self.horizontalLayout.addWidget(self.HardiskCheckEdit)

        self.retranslateUi(HardiskChecker)
        QtCore.QMetaObject.connectSlotsByName(HardiskChecker)

    def retranslateUi(self, HardiskChecker):
        HardiskChecker.setWindowTitle(_translate("HardiskChecker", "Form", None))
        self.HardiskCheckLabel.setText(_translate("HardiskChecker", "Client IP :>", None))

