# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Verify.ui'
#
# Created: Tue Oct 27 12:10:50 2015
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

class Ui_Verify(object):
    def setupUi(self, Verify):
        Verify.setObjectName(_fromUtf8("Verify"))
        Verify.resize(417, 248)
        self.layoutWidget = QtGui.QWidget(Verify)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 150, 235, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.OtpLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.OtpLineEdit.setText(_fromUtf8(""))
        self.OtpLineEdit.setObjectName(_fromUtf8("OtpLineEdit"))
        self.horizontalLayout.addWidget(self.OtpLineEdit)
        self.VerifyButton = QtGui.QPushButton(self.layoutWidget)
        self.VerifyButton.setObjectName(_fromUtf8("VerifyButton"))
        self.horizontalLayout.addWidget(self.VerifyButton)

        self.retranslateUi(Verify)
        QtCore.QMetaObject.connectSlotsByName(Verify)

    def retranslateUi(self, Verify):
        Verify.setWindowTitle(_translate("Verify", "Form", None))
        self.OtpLineEdit.setPlaceholderText(_translate("Verify", "Enter OTP here ....", None))
        self.VerifyButton.setText(_translate("Verify", "Verify", None))

