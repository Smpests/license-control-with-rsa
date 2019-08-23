# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ActivateKey.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

from Analyzer import DecryptByPublicKey


class Ui_Dialog(object):
    pub_key = """MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAhYTLtE17h/MCghuNgNzCcCN77qPuonhv
EITRYw6fvJC0kNqjl9recncwsSPMWyzptj3y4O0C0rIYaZIMeDiGJYkaqz4caZ2i2xA5azmfwKjG
V01FejkIdiAzIh27z7k5xiYaTP8eKvz6Psb+DIR/3Lgo7gpFqR6acmsakL3v/I4dvMAJqqV2Ocyb
oeQ32ffiYBRuBX4/cZweyINg4piE7Ud7hfSYMpYLQBQMvLzqjtJ6ukZIoXKtS/jIdBJrbcxYM/0w
gm9/j+4BrF440XCs37NHZT1oQMqa+dk/vmwuQmBhMgzQc9FI3XRCvhMONF+EuG8RiJTq2ZodWBxi
8GM2wwIDAQAB"""

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 69)
        self.textEditKey = QtWidgets.QTextEdit(Dialog)
        self.textEditKey.setGeometry(QtCore.QRect(30, 10, 201, 41))
        self.textEditKey.setStyleSheet("font: 10pt \"宋体\";")
        self.textEditKey.setObjectName("textEditKey")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 10, 71, 41))
        self.pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "激活"))

    @pyqtSlot()
    def on_pushButton_clicked(self):
        code = self.textEditKey.toPlainText()
        print(code)
        result = DecryptByPublicKey(code, self.pub_key).validity()
        print(result)
        if result:
            QtWidgets.QMessageBox.information(self, "infomation", "激活成功")
        else:
            QtWidgets.QMessageBox.information(self, "infomation", "激活失败")