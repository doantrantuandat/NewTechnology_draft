# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\2019-2020\Ki1\CongNgheMoi\BaiTapLon\gui\test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog,QLabel,QWidget
from PyQt5.QtGui import QIcon, QPixmap,QImage
from PyQt5.uic import loadUi
import cv2
import os
from os.path import dirname, abspath
import numpy as np
from PIL import Image
import pickle
import os.path as path
import sys
import pyodbc
from PyQt5 import QtCore, QtGui, QtWidgets

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-JR11ETH\SQLEXPRESS;'
                      'Database=qlusername;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

current_id = 0
label_ids = {}
y_labels = []
x_train = []



face_cascade = cv2.CascadeClassifier(
    'cascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

cap = cv2.VideoCapture(0)


model_getImg = QtGui.QStandardItemModel()
model_getTrain = QtGui.QStandardItemModel()
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

        self.btn_train = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_train.setObjectName("btn_train")
        self.horizontalLayout.addWidget(self.btn_train)

        self.btn_refresh = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_refresh.setObjectName("btn_train")
        self.horizontalLayout.addWidget(self.btn_refresh)

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
        # self.frame.setStyleSheet("")
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

        # chinh bang
        
        model_getImg.setHorizontalHeaderLabels(['Tên', 'MSSV', 'Lớp'])
        model_getImg.setColumnCount(3)
        self.tbl_getIma.setModel(model_getImg)
        
        
        model_getTrain.setHorizontalHeaderLabels(['Tên', 'MSSV', 'Lớp'])
        model_getTrain.setColumnCount(3)
        self.tbl_train.setModel(model_getTrain)

        # gan su kien
        self.btn_layAnh.clicked.connect(self.getImg_student)

        self.btn_train.clicked.connect(self.faces_train)
        self.btn_refresh.clicked.connect(self.load_table_getImg)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Xóa"))
        self.btn_train.setText(_translate("MainWindow", "Train"))
        self.btn_layAnh.setText(_translate("MainWindow", "Lấy ảnh"))
        self.btn_refresh.setText(_translate("MainWindow","Refresh 2 bảng"))
        self.label_2.setText(_translate("MainWindow", "Họ và tên"))
        self.label.setText(_translate("MainWindow", "MSSV"))
        self.label_3.setText(_translate("MainWindow", "Lớp"))


    def getImg_student(self):
        title = self.txt_ten.text()+"_"+self.txt_mssv.text()+"_"+self.txt_lop.text()

        if self.txt_ten.text() == '':
            QtWidgets.QMessageBox.about(self, "Wanning", "Phai day du ten , mssv, lop")
            return
        if not os.path.exists('ima_student/'+title):
            print(title)
            os.mkdir('ima_student/'+ title)
            print("Directory " , 'ima_student/'+ title ,  " Created ")
            cursor.execute('INSERT INTO qlusername.dbo.student(ten,mssv,lop) values(?,?,?)',(self.txt_ten.text(), self.txt_mssv.text(), self.txt_lop.text()))
            cursor.commit()
        else:    
            QtWidgets.QMessageBox.about(self, "Wanning", "da ton tai sinh vien trong he thong")
            self.txt_ten.setText('')
            self.txt_mssv.setText('')
            self.txt_lop.setText('')
            return
        
        dem = 0
        while True:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                dem = dem + 1
                print(dem)
                label = str(title)

                label_ids[label] = 0
                id_ = label_ids[label]

                roi = gray[y:y+h, x:x+w]
                cv2.imwrite("ima_student/" + label + "/" + "." +
                            str(dem) + ".jpg", gray[y:y+h, x:x+w])

                x_train.append(roi)
                y_labels.append(id_)
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('frames', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if dem == 10:
                cv2.destroyAllWindows()
                break
        
        
    
    def faces_train(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_dir2 = dirname(str(BASE_DIR))
        image_dir = os.path.join(image_dir2, "ima_student")
        print("-----------------------------------------------")
        print(image_dir)
        print("-----------------------------------------------")
        
        current_id = 0
        labels_id = {}
        y_labels = []
        x_train = []
        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.endswith("png") or file.endswith("jpg"):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "-").lower()
                
                    if not label in labels_id:
                        labels_id[label] = current_id
                        current_id += 1
                    id_ = labels_id[label]
                    print(id_)
                
                pil_image = Image.open(path).convert("L")
                image_array = np.array(pil_image, "uint8")
                faces = face_cascade.detectMultiScale(image_array, 1.1, 4)
                for (x, y, w, h) in faces:
                    
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)
        with open("labels.pickle", "wb") as f:
            pickle.dump(labels_id, f)
        recognizer.train(x_train, np.array(y_labels))
        recognizer.save("facesAll_trainer.yml")

    def load_table_getImg(self):
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_dir2 = dirname(str(BASE_DIR))
        image_dir = os.path.join(image_dir2, "ima_student")
        print("-----------------------------------------------")
        print(image_dir)
        print("-----------------------------------------------")

        students = []
        
        model_getImg.clear()
        for root, dirs, files in os.walk(image_dir):
            for file in files:
                if file.endswith("png") or file.endswith("jpg"):
                    
                    label = os.path.basename(root)
                    info = label.split('_')
                    if not info in students:
                        students.append(info)
        print(students)
        for i in range(len(students)):
            
            model_getImg.setItem(i,0, QtGui.QStandardItem(str(students[i][0])))
            model_getImg.setItem(i,1,QtGui.QStandardItem(str(students[i][1])))
            model_getImg.setItem(i,2, QtGui.QStandardItem(str(students[i][2])))

            model_getTrain.setItem(i,0, QtGui.QStandardItem(str(students[i][0])))
            model_getTrain.setItem(i,1,QtGui.QStandardItem(str(students[i][1])))
            model_getTrain.setItem(i,2, QtGui.QStandardItem(str(students[i][2])))

        model_getImg.setHorizontalHeaderLabels(['Tên', 'MSSV', 'Lớp'])
        model_getTrain.setHorizontalHeaderLabels(['Tên', 'MSSV', 'Lớp'])
            
        

        
                    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())