# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'content.ui'
#
# Created: Mon Oct 26 01:30:56 2015
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

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName(_fromUtf8("mainDialog"))
        mainDialog.resize(380, 211)
        self.nameEdit = QtGui.QLineEdit(mainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(60, 110, 113, 27))
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.Button1 = QtGui.QPushButton(mainDialog)
        self.Button1.setGeometry(QtCore.QRect(180, 110, 98, 27))
        self.Button1.setObjectName(_fromUtf8("Button1"))

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(_translate("mainDialog", "Dialog", None))
        self.Button1.setText(_translate("mainDialog", "Show", None))

