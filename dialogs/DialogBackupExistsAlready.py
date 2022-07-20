from PyQt5 import QtWidgets
from forms.auto.auto_dialogBackupExistsAlready import Ui_Dialog


class DialogBackupExistsAlready(QtWidgets.QDialog):
    def __init__(self, parent=None):
        """Constructor

        Args:
            args
            kwargs
        """
        QtWidgets.QDialog.__init__(self, parent)
        # build ui object
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnCancel.clicked.connect(self.cancelDialog)
        self.setWindowTitle("Warning")

    #Slot
    def cancelDialog(self):
        self.close()
