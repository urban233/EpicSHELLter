import os.path
import utils
import datetime
import shutil
from PyQt5 import QtWidgets, QtCore
from dialogs import DialogBackupExistsAlready


def chooseAnExistingFolder(self, statusBar, txtBox, message) -> None:
    """This function opens a file dialog and has the capability to select an existing folder
    and display the path in a textbox

    Args:
        self:
            self of the dialog where the function is used
        statusBar:
            statusbar object of the dialog where the function is used
        txtBox:
            text box (lineEdit) which is used to display the path
        message:
            string which describes the type of folder which needs to be opened
    """
    if self is None:
        raise ValueError
    if statusBar is None:
        raise ValueError
    if txtBox is None:
        raise ValueError
    if message is None:
        raise ValueError
    try:
        # open file dialog
        statusBar.showMessage(f"Open a folder to {message} ...")
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, f"Open Folder to {message}",
                                                              QtCore.QDir.homePath())
        if fileName == "":
            raise ValueError
        # display path in text box
        txtBox.setText(fileName)
        statusBar.showMessage("Selecting the folder was successful.")
    except FileNotFoundError:
        print("Selecting the folder failed!")
        statusBar.showMessage("Selecting the folder failed!")
    except ValueError:
        print("No file has been selected.")
        statusBar.showMessage("No file has been selected.")


def createBackupOfSingleDir(statusBar, pathOfBackup, pathToStorage, parentPath) -> None:
    """Copies one directory to another path with the filename *_backup_YYYYMMDD

    Args:
        statusBar:
            statusbar object of the main window
        pathOfBackup:
            full and absolute path of the folder to back up (entered in a textbox)
        pathToStorage:
            full and absolute path of the folder where to store the created backup (entered in a textbox)
        parentPath:
            full and absolute path of the folder where to store the backup
    """
    try:
        # check if the folder to back up exists
        if pathOfBackup is None:
            raise FileNotFoundError
        # check if the path to store the backup exists
        if pathToStorage is None:
            raise FileNotFoundError
        if pathOfBackup == pathToStorage:
            raise AttributeError

        # create a zip of the content in the folder to back up
        date = datetime.datetime.now()
        fDate = str(date.strftime("%x")).replace("/", "-")
        archiveName = f"backup_{fDate}"
        fullArchivePath = f"{parentPath}_{archiveName}"
        fullArchivePathWithExtension = f"{fullArchivePath}.zip"
        if os.path.exists(fullArchivePathWithExtension):
            raise FileExistsError
        utils.zipfolder(fullArchivePath, pathOfBackup)
        shutil.move(fullArchivePathWithExtension, pathToStorage)
        statusBar.showMessage(f"Successfully created the backup.")

    except FileNotFoundError:
        print(f"There is no folder with the absolute filepath {pathOfBackup} or {pathToStorage}!")
    except FileExistsError:
        print(f"The backup of {fullArchivePathWithExtension} already exists!")
        statusBar.showMessage(f"The backup of {fullArchivePathWithExtension} already exists!")
        dialog = DialogBackupExistsAlready.DialogBackupExistsAlready()
        dialog.exec_()
    except AttributeError:
        statusBar.showMessage(f"The backup path and storage path MUST be different.")
