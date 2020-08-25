# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Aero_Demo_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(652, 504)
        self.pushButton_Exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_Exit.setGeometry(QtCore.QRect(250, 440, 112, 34))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 601, 191))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_GetWing = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_GetWing.setGeometry(QtCore.QRect(100, 30, 401, 34))
        self.pushButton_GetWing.setObjectName("pushButton_GetWing")
        self.textEdit_filename = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_filename.setGeometry(QtCore.QRect(70, 80, 461, 91))
        self.textEdit_filename.setReadOnly(True)
        self.textEdit_filename.setObjectName("textEdit_filename")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 230, 571, 181))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(50, 40, 71, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit_Height = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_Height.setGeometry(QtCore.QRect(140, 40, 101, 25))
        self.lineEdit_Height.setObjectName("lineEdit_Height")
        self.lineEdit_Width = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_Width.setGeometry(QtCore.QRect(450, 40, 101, 25))
        self.lineEdit_Width.setText("")
        self.lineEdit_Width.setObjectName("lineEdit_Width")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(340, 40, 91, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_Plot = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Plot.setGeometry(QtCore.QRect(230, 100, 93, 28))
        self.pushButton_Plot.setObjectName("pushButton_Plot")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wing Spar Structural Optimization"))
        self.pushButton_Exit.setText(_translate("Dialog", "Exit"))
        self.groupBox.setTitle(_translate("Dialog", "Input"))
        self.pushButton_GetWing.setText(_translate("Dialog", "Open and Read a Wing File a - as a Demo"))
        self.groupBox_3.setTitle(_translate("Dialog", "Spar I-beam Shape"))
        self.label.setText(_translate("Dialog", "Height"))
        self.label_2.setText(_translate("Dialog", "Width"))
        self.pushButton_Plot.setText(_translate("Dialog", "Plot Something"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

