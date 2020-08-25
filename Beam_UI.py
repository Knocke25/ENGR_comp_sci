# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Beam_Demo_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(652, 604)
        self.pushButton_Exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_Exit.setGeometry(QtCore.QRect(250, 560, 140, 34))
        self.pushButton_Exit.setObjectName("pushButton_Exit")





        

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 601, 191))
        self.groupBox.setObjectName("groupBox")

        self.pushButton_GetBeam = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_GetBeam.setGeometry(QtCore.QRect(100, 30, 401, 34))
        self.pushButton_GetBeam.setObjectName("pushButton_GetBeam")

        self.textEdit_filename = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_filename.setGeometry(QtCore.QRect(70, 80, 461, 91))
        self.textEdit_filename.setReadOnly(True)
        self.textEdit_filename.setObjectName("textEdit_filename")

        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 230, 571, 281))
        self.groupBox_3.setObjectName("groupBox_3")



        self.lineEdit_maxMoment = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_maxMoment.setGeometry(QtCore.QRect(140, 120, 101, 25))
        self.lineEdit_maxMoment.setObjectName("lineEdit_MaxMoment")

        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(50, 120, 80, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")







        self.lineEdit_max_moment_location = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_max_moment_location.setGeometry(QtCore.QRect(450, 120, 101, 25))
        self.lineEdit_max_moment_location.setObjectName("lineEdit_max_moment_location")

        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(340, 120, 71, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")





        self.lineEdit_max_Slope = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_max_Slope.setGeometry(QtCore.QRect(140, 160, 101, 25))
        self.lineEdit_max_Slope.setObjectName("lineEdit_Slope")

        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(25, 160, 101, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")






        self.lineEdit_max_Slope_location = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_max_Slope_location.setGeometry(QtCore.QRect(450, 160, 101, 25))
        self.lineEdit_max_Slope_location.setObjectName("lineEdit_max_Slope_location")

        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(340, 160, 71, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")







        self.lineEdit_R1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_R1.setGeometry(QtCore.QRect(140, 40, 101, 25))
        self.lineEdit_R1.setObjectName("lineEdit_R1")

        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(50, 40, 71, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")





        self.lineEdit_R2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_R2.setGeometry(QtCore.QRect(450, 40, 101, 25))
        self.lineEdit_R2.setObjectName("lineEdit_R2")

        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(340, 40, 71, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")






        self.lineEdit_C1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_C1.setGeometry(QtCore.QRect(140, 80, 101, 25))
        self.lineEdit_C1.setObjectName("lineEdit_C1")

        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(50, 80, 71, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")





        self.lineEdit_C2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_C2.setGeometry(QtCore.QRect(450, 80, 101, 25))
        self.lineEdit_C2.setObjectName("lineEdit_C2")

        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(340, 80, 71, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")






        self.lineEdit_max_Deflection = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_max_Deflection.setGeometry(QtCore.QRect(140, 200, 101, 25))
        self.lineEdit_max_Deflection.setObjectName("lineEdit_max_Deflection")

        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(30, 200, 101, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")





        self.lineEdit_max_Deflection_location = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_max_Deflection_location.setGeometry(QtCore.QRect(450, 200, 101, 25))
        self.lineEdit_max_Deflection_location.setObjectName("lineEdit_max_Deflection_location")

        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(340, 200, 71, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")






        self.pushButton_Plot = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_Plot.setGeometry(QtCore.QRect(230, 250, 93, 28))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Beam Solver"))
        self.pushButton_Exit.setText(_translate("Dialog", "Exit"))
        self.groupBox.setTitle(_translate("Dialog", "Input"))
        self.pushButton_GetBeam.setText(_translate("Dialog", "Open and Read a Beam file"))
        self.groupBox_3.setTitle(_translate("Dialog", "Beam Values"))
        self.label.setText(_translate("Dialog", "Max Moment"))
        self.label_2.setText(_translate("Dialog", "Max Slope"))
        self.label_3.setText(_translate("Dialog", "R1"))
        self.label_4.setText(_translate("Dialog", "R2"))
        self.label_5.setText(_translate("Dialog", "C1"))
        self.label_6.setText(_translate("Dialog", "C2"))
        self.label_7.setText(_translate("Dialog", "Max Deflection"))
        self.label_8.setText(_translate("Dialog", "Location"))
        self.label_9.setText(_translate("Dialog", "Location"))
        self.label_10.setText(_translate("Dialog", "Location"))
        self.pushButton_Plot.setText(_translate("Dialog", "Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

