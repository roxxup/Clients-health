# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RamChecker.ui'
#
# Created: Mon Oct 26 15:35:03 2015
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

class Ui_RamChecker(object):
    def setupUi(self, RamChecker):
        RamChecker.setObjectName(_fromUtf8("RamChecker"))
        RamChecker.resize(485, 81)
        self.horizontalLayout = QtGui.QHBoxLayout(RamChecker)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.RamCheckLabel = QtGui.QLabel(RamChecker)
        self.RamCheckLabel.setObjectName(_fromUtf8("RamCheckLabel"))
        self.horizontalLayout.addWidget(self.RamCheckLabel)
        self.RamCheckEdit = QtGui.QLineEdit(RamChecker)
        self.RamCheckEdit.setObjectName(_fromUtf8("RamCheckEdit"))
        self.horizontalLayout.addWidget(self.RamCheckEdit)

        self.retranslateUi(RamChecker)
        QtCore.QMetaObject.connectSlotsByName(RamChecker)

    def retranslateUi(self, RamChecker):
        RamChecker.setWindowTitle(_translate("RamChecker", "Form", None))
        self.RamCheckLabel.setText(_translate("RamChecker", "Client IP :>", None))

