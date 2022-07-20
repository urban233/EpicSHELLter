import sys
from PyQt5 import QtWidgets, QtCore
from forms.auto.auto_mainWindow import Ui_MainWindow
import guiUtils


class MainWindow(QtWidgets.QMainWindow):
    """This class contains all information about the MainWindow in the
    application

    """
    def __init__(self, *args, **kwargs):
        """Constructor

        Args:
            args
            kwargs
        """
        super().__init__(*args, **kwargs)

        # build ui object
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Epic SHELLter Backup System")
        # self.ui.lblLogo.setPixmap(QtGui.QPixmap("assets/images/icon.jpg"))
        self.ui.lblLogo.hide()
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)

        self.ui.btnBackupDir.clicked.connect(self.chooseDirToBackup)
        self.ui.btnStoreDir.clicked.connect(self.chooseDirToStore)
        self.ui.btnCreateBackup.clicked.connect(self.createBackupOfSingleDir)

    #Slots
    def chooseDirToBackup(self):
        guiUtils.chooseAnExistingFolder(self, self.statusBar, self.ui.txtBackupDir, "backup")

    def chooseDirToStore(self):
        guiUtils.chooseAnExistingFolder(self, self.statusBar, self.ui.txtStoreDir, "store the backup")

    def createBackupOfSingleDir(self):
        parentPath = QtCore.QDir(self.ui.txtBackupDir.text())
        absPath = parentPath.absolutePath()
        guiUtils.createBackupOfSingleDir(self.statusBar, self.ui.txtBackupDir.text(), self.ui.txtStoreDir.text(), absPath)


if __name__ == '__main__':
    # Start point of the application
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
