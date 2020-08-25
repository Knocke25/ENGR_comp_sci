
import numpy as np
import matplotlib.pyplot as plt

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Aero_Demo_ui import Ui_Dialog
from Wing_Class import Wing


class main_window(QDialog):
    def __init__(self):
        super(main_window,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.wing=None
        self.show()

    def assign_widgets(self):
        self.ui.pushButton_Exit.clicked.connect(self.ExitApp)
        self.ui.pushButton_GetWing.clicked.connect(self.GetWing)         
        self.ui.pushButton_Plot.clicked.connect(self.PlotSomething)
    

    def GetWing(self):

        # get the filename using the OPEN dialog
        filename=QFileDialog.getOpenFileName()[0]
        if len(filename)==0: 
            no_file()
            return

        self.ui.textEdit_filename.setText(filename)
        app.processEvents()
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

        # Read the file
        f1 = open(filename, 'r')  # open the file for reading
        data = f1.readlines()  # read the entire file as a list of strings
        f1.close()  # close the file  ... very important

        self.wing=Wing()  # create a wing instance (object)

        try:
            self.wing.processWingData(data)
            self.ui.lineEdit_Height.setText('{:.2f}'.format(self.wing.sparH))
            self.ui.lineEdit_Width.setText('{:.2f}'.format(self.wing.sparW))
            QApplication.restoreOverrideCursor()
        except:
            QApplication.restoreOverrideCursor()
            bad_file()



    def PlotSomething(self):
        x=np.linspace(0,6*np.pi,300)
        y=np.zeros_like(x)
        for i in range(300):
            y[i]=np.exp(-x[i]/5)*np.sin(x[i])
        plt.plot(x,y)
        plt.show()
        return


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
    
 





