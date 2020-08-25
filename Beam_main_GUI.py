import numpy as np
import matplotlib.pyplot as plt

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Beam_UI import Ui_Dialog
from whatever import Beam


class main_window(QDialog):
    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.beam = None
        self.show()

    def assign_widgets(self):
        self.ui.pushButton_Exit.clicked.connect(self.ExitApp)
        self.ui.pushButton_GetBeam.clicked.connect(self.GetBeam)
        self.ui.pushButton_Plot.clicked.connect(self.PlotSomething)

    def GetBeam(self):

        # get the filename using the OPEN dialog
        filename = QFileDialog.getOpenFileName()[0]
        if len(filename) == 0:
            no_file()
            return
        self.ui.textEdit_filename.setText(filename)
        app.processEvents()
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

        # Read the file
        f1 = open(filename, 'r')  # open the file for reading
        data = f1.readlines()  # read the entire file as a list of strings
        f1.close()  # close the file  ... very important

        self.beam = Beam()  # create a wing instance (object)

        try:
            self.beam.processBeamData(data)
            self.beam.solve()
            self.ui.lineEdit_maxMoment.setText('{:.7f}'.format(self.beam.maxMoment))
            self.ui.lineEdit_max_moment_location.setText('{:.7f}'.format(self.beam.maxM_location))
            self.ui.lineEdit_max_Deflection.setText('{:.7f}'.format(self.beam.maxDeflection))
            self.ui.lineEdit_max_Deflection_location.setText('{:.7f}'.format(self.beam.maxDeflection_location))
            self.ui.lineEdit_max_Slope.setText('{:.8f}'.format(self.beam.maxSlope))
            self.ui.lineEdit_max_Slope_location.setText('{:.7f}'.format(self.beam.maxSlope_location))
            self.ui.lineEdit_R1.setText('{:.7f}'.format(self.beam.R1))
            self.ui.lineEdit_R2.setText('{:.7f}'.format(self.beam.R2))
            self.ui.lineEdit_C1.setText('{:.7f}'.format(self.beam.C1))
            self.ui.lineEdit_C2.setText('{:.7f}'.format(self.beam.C2))
            QApplication.restoreOverrideCursor()
        except:
            QApplication.restoreOverrideCursor()
            bad_file()





    def PlotSomething(self):

        self.beam.plot(title=self.beam.title)


    def ExitApp(self):
        app.exit()


def no_file():
    msg = QMessageBox()
    msg.setText('There was no file selected')
    msg.setWindowTitle("No File")
    retval = msg.exec_()
    return None


def bad_file():
    msg = QMessageBox()
    msg.setText('Unable to process the selected file')
    msg.setWindowTitle("Bad File")
    retval = msg.exec_()
    return None


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())







