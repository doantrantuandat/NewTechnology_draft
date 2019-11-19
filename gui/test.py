# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\2019-2020\Ki1\CongNgheMoi\BaiTapLon\gui\test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QWidget, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.uic import loadUi
import cgi
import os
from tkinter import filedialog
import tkinter as tk


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 340, 541, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 10, 160, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_ten = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_ten.setText("")
        self.txt_ten.setObjectName("txt_ten")
        self.verticalLayout.addWidget(self.txt_ten)
        self.txt_mssv = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_mssv.setObjectName("txt_mssv")
        self.verticalLayout.addWidget(self.txt_mssv)
        self.txt_lop = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_lop.setObjectName("txt_lop")
        self.verticalLayout.addWidget(self.txt_lop)
        self.btn_layAnh = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_layAnh.setObjectName("btn_layAnh")
        self.verticalLayout.addWidget(self.btn_layAnh)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(510, 20, 61, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(-260, 370, 256, 192))
        self.tableView.setObjectName("tableView")
        self.tbl_getIma = QtWidgets.QTableView(self.centralwidget)
        self.tbl_getIma.setGeometry(QtCore.QRect(30, 210, 541, 121))
        self.tbl_getIma.setObjectName("tbl_getIma")
        self.tbl_train = QtWidgets.QTableView(self.centralwidget)
        self.tbl_train.setGeometry(QtCore.QRect(30, 380, 541, 121))
        self.tbl_train.setObjectName("tbl_train")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 10, 301, 191))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btn_layAnh.clicked.connect(self.browse_img)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Xóa"))
        self.pushButton.setText(_translate("MainWindow", "Train"))
        self.btn_layAnh.setText(_translate("MainWindow", "Lấy ảnh"))
        self.label_2.setText(_translate("MainWindow", "Họ và tên"))
        self.label.setText(_translate("MainWindow", "MSSV"))
        self.label_3.setText(_translate("MainWindow", "Lớp"))

    def browse_img(self):
        fileselect = filedialog.askopenfilename(initialdir=os.getcwd(), 
        title="Please select a file", filetypes=(('png files', '*.png'), ('jpeg files', '*.jpeg')))

        # print(file)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
