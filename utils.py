import zipfile
import os


def zipfolder(foldername, target_dir):
    """Creates a zip folder of all files and subfolders

    Args:
        foldername:
            name of the zip file which should be created. MUST NOT contain the file extension
        target_dir:
            path of the parent folder which gets zipped
    """
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])
