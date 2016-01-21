# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created: Tue Oct 27 01:36:33 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.NameEdit = QtGui.QLineEdit(Form)
        self.NameEdit.setGeometry(QtCore.QRect(130, 40, 113, 27))
        self.NameEdit.setObjectName(_fromUtf8("NameEdit"))
        self.PassEdit = QtGui.QLineEdit(Form)
        self.PassEdit.setGeometry(QtCore.QRect(130, 90, 113, 27))
        self.PassEdit.setObjectName(_fromUtf8("PassEdit"))
        self.LoginButton = QtGui.QPushButton(Form)
        self.LoginButton.setGeometry(QtCore.QRect(70, 200, 98, 27))
        self.LoginButton.setObjectName(_fromUtf8("LoginButton"))
        self.PhoneEdit = QtGui.QLineEdit(Form)
        self.PhoneEdit.setGeometry(QtCore.QRect(130, 140, 113, 27))
        self.PhoneEdit.setObjectName(_fromUtf8("PhoneEdit"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(250, 10, 51, 241))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.SignInButton = QtGui.QPushButton(Form)
        self.SignInButton.setGeometry(QtCore.QRect(290, 160, 98, 27))
        self.SignInButton.setObjectName(_fromUtf8("SignInButton"))
        self.AlreadyLabel = QtGui.QLabel(Form)
        self.AlreadyLabel.setGeometry(QtCore.QRect(300, 40, 66, 17))
        self.AlreadyLabel.setObjectName(_fromUtf8("AlreadyLabel"))
        self.MemberLabel = QtGui.QLabel(Form)
        self.MemberLabel.setGeometry(QtCore.QRect(300, 80, 66, 17))
        self.MemberLabel.setObjectName(_fromUtf8("MemberLabel"))
        self.QLabel = QtGui.QLabel(Form)
        self.QLabel.setGeometry(QtCore.QRect(320, 120, 66, 17))
        self.QLabel.setObjectName(_fromUtf8("QLabel"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 40, 91, 121))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.NameLabel = QtGui.QLabel(self.widget)
        self.NameLabel.setObjectName(_fromUtf8("NameLabel"))
        self.verticalLayout.addWidget(self.NameLabel)
        self.PassLabel = QtGui.QLabel(self.widget)
        self.PassLabel.setObjectName(_fromUtf8("PassLabel"))
        self.verticalLayout.addWidget(self.PassLabel)
        self.PassLabel_2 = QtGui.QLabel(self.widget)
        self.PassLabel_2.setObjectName(_fromUtf8("PassLabel_2"))
        self.verticalLayout.addWidget(self.PassLabel_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.LoginButton.setText(_translate("Form", "Log In", None))
        self.SignInButton.setText(_translate("Form", "SIGN IN ", None))
        self.AlreadyLabel.setText(_translate("Form", "ALREADY", None))
        self.MemberLabel.setText(_translate("Form", "MEMBER ", None))
        self.QLabel.setText(_translate("Form", "?", None))
        self.NameLabel.setText(_translate("Form", "Name", None))
        self.PassLabel.setText(_translate("Form", "Password", None))
        self.PassLabel_2.setText(_translate("Form", "Phone No -", None))

