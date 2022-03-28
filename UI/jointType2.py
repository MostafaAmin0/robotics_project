# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jointType.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from dhWindow2 import Ui_dhWindow2

class Ui_jointWindow2(object):
    def openWindow(self):
        joint=self.textEdit.toPlainText()
        if(joint!=''):
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_dhWindow2(len(joint))
            self.ui.setupUi(self.window)
            self.window.show()


    def setupUi(self, jointWindow):
        jointWindow.setObjectName("jointWindow")
        jointWindow.resize(580, 504)
        jointWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(jointWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 150, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 160, 251, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.revoluteButton = QtWidgets.QPushButton(self.centralwidget,clicked= lambda:self.enterJoint("R"))
        self.revoluteButton.setGeometry(QtCore.QRect(160, 220, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        self.revoluteButton.setFont(font)
        self.revoluteButton.setStyleSheet("background-color: rgb(254, 233, 226);")
        self.revoluteButton.setObjectName("revoluteButton")
        self.prismaticButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked= lambda:self.enterJoint("P"))
        self.prismaticButton_2.setGeometry(QtCore.QRect(330, 220, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(10)
        self.prismaticButton_2.setFont(font)
        self.prismaticButton_2.setStyleSheet("background-color: rgb(222, 201, 254);")
        self.prismaticButton_2.setObjectName("prismaticButton_2")
        self.next = QtWidgets.QPushButton(self.centralwidget,clicked= lambda:self.openWindow())
        self.next.setGeometry(QtCore.QRect(470, 420, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.next.setFont(font)
        self.next.setStyleSheet("background-color: rgb(215, 228, 253);")
        self.next.setObjectName("next")
        jointWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(jointWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        jointWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(jointWindow)
        self.statusbar.setObjectName("statusbar")
        jointWindow.setStatusBar(self.statusbar)

        self.retranslateUi(jointWindow)
        QtCore.QMetaObject.connectSlotsByName(jointWindow)

    def retranslateUi(self, jointWindow):
        _translate = QtCore.QCoreApplication.translate
        jointWindow.setWindowTitle(_translate("jointWindow", "MainWindow"))
        self.label.setText(_translate("jointWindow", "Please enter joints type"))
        self.revoluteButton.setText(_translate("jointWindow", "Revolute"))
        self.prismaticButton_2.setText(_translate("jointWindow", "Prismatic"))
        self.next.setText(_translate("jointWindow", "Next"))
    
    joint=''
    def enterJoint(self,jointName):
        joint=self.textEdit.toPlainText()
        if(jointName=="R"):
            self.textEdit.setText(joint+'R')
        else :
            self.textEdit.setText(joint+'P')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jointWindow = QtWidgets.QMainWindow()
    ui = Ui_jointWindow2()
    ui.setupUi(jointWindow)
    jointWindow.show()
    sys.exit(app.exec_())
