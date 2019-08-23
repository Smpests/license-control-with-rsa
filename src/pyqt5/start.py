# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont

from MacGetter import get_mac_address


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(362, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 120, 71, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(QFont("宋体", 12, QFont.Normal))
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 120, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(QFont("宋体", 12, QFont.Bold))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mac获取器"))
        self.pushButton.setText(_translate("Form", "提取Mac"))

# 启动事件，验证key
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.lineEdit.setText(get_mac_address())