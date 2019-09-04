# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ActivationCodeGenerator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from rsa import common, transform, pkcs1, newkeys, PrivateKey
import base64
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from ActivationCodeFactory import ActivationCodeFactory
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 386)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(220, 100, 161, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 40, 161, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 200, 431, 161))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "激活码生成器"))
        self.label.setText(_translate("MainWindow", "绑定设备 MAC"))
        self.label_2.setText(_translate("MainWindow", "使用截止日期"))
        self.pushButton.setText(_translate("MainWindow", "生 成"))

    @pyqtSlot()
    def on_pushButton_clicked(self):
        try:
            # 工厂对象
            factory = ActivationCodeFactory()

            # 创建密钥仓库,密钥丢失时打开注释，将会在当前路径生成密钥文件
            # 运行一次后再注释，避免冲突
            # 密钥变更需及时更新替换开发包中的公钥文件
            # factory.create_key_pair()

            # 从表单获取加密信息
            mac = self.lineEdit.text()
            validity_date = self.dateEdit.text()
            print("mac:", mac)
            print("有效期:", validity_date)

            # 生成激活码
            code = factory.encrypt(mac + "&" + validity_date, "private.pem")
            # 保存激活码至当前路径txt文件，
            if code:
                self.textEdit.setText(code)
                factory.save_code(code, "ActivationCode.txt")
                QtWidgets.QMessageBox.information(self, "infomation", "激活码已成功生成并保存在程序所在目录")
                # print("激活码已保存")
            else:
                QtWidgets.QMessageBox.information(self, "infomation", "私钥文件读取错误")
        except:
            print("异常发生")
            QtWidgets.QMessageBox.information(self, "infomation", "异常发生")


class MainWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())
