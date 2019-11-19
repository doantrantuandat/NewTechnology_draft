# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\2019-2020\Ki1\CongNgheMoi\BaiTapLon\gui\clgt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Test(object):
    def setupUi(self, Test):
        Test.setObjectName("Test")
        Test.resize(535, 320)
        self.widget_ngoai = QtWidgets.QWidget(Test)
        self.widget_ngoai.setGeometry(QtCore.QRect(140, 50, 281, 181))
        self.widget_ngoai.setObjectName("widget_ngoai")
        self.frame_trong = QtWidgets.QFrame(self.widget_ngoai)
        self.frame_trong.setGeometry(QtCore.QRect(80, 50, 120, 80))
        self.frame_trong.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_trong.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_trong.setObjectName("frame_trong")

        self.retranslateUi(Test)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Test = QtWidgets.QWidget()
    ui = Ui_Test()
    ui.setupUi(Test)
    Test.show()
    sys.exit(app.exec_())
