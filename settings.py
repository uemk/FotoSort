import os
import sys
import ctypes

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QCheckBox
from my_gui import dialog_settings


class Settings(QtWidgets.QDialog, dialog_settings.Ui_DialogSettings):
    def init(self) -> None:
        super(Settings, self).__init__()
        self.setupUi(self)

        self.checkBox_check_all.stateChanged.connect(self.check_all)

        if is_windows():
            self.lineEdit_path.setText(str(os.getcwd())+"\\fotosort.exe")
            admin = is_user_admin()
            if not admin:
                self.pushButton_add.setEnabled(False)
                self.pushButton_del.setEnabled(False)
                self.label_log.setText('Please, run the application as administrator!')
                self.label_log.setStyleSheet('color: red')

            self.pushButton_add.clicked.connect(self.add_registry)
            self.pushButton_del.clicked.connect(self.del_registry)
        else:
            self.tab_context_menu.setEnabled(False)
            self.label_log.setText('Function available only on Windows OS')
            self.label_log.setStyleSheet('color: red')

    def add_registry(self) -> None:
        """
        Add program to Windows registry (show in folder context menu)
        """
        import winreg

        root_registry = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
        contex_menu_key = winreg.OpenKey(root_registry, r'Directory\shell\\')
        try:
            fotosort_key = winreg.CreateKey(contex_menu_key, r'Open with FotoSort\\')
            value = '\"' + os.getcwd() + '\\fotosort.exe\" \"%1\"'
            winreg.SetValue(fotosort_key, r'command', winreg.REG_SZ, value)
        except OSError:
            self.label_log.setText('Error while adding FotoSort to Windows registry!')
            self.label_log.setStyleSheet('color: red')
        else:
            self.label_log.setText('FotoSort successfully added to Windows registry!')
            self.label_log.setStyleSheet('color: blue')

        # ALTERNATIVE VERSION TO ADD KEY TO WIN REGISTRY:
        # with open('register.reg', 'w') as file:
        #     file.write('Windows Registry Editor Version 5.00\n')
        #     file.write('[HKEY_CLASSES_ROOT\Directory\shell\Open with FotoSort]\n')
        #     file.write('[HKEY_CLASSES_ROOT\Directory\shell\Open with FotoSort\command]\n')
        #     value = '@=' + "\"" + os.getcwd() + "\\fotosort.exe %1\""
        #     new_value = str(value).replace("\\", "\\"+"\\")
        #     file.write(new_value)
        #
        # cmd_line = 'regedit.exe ' + os.getcwd() + '/register.reg'
        # os.system(cmd_line)
        # os.system('del register.reg')

    def del_registry(self) -> None:
        """
        Remove program from Windows registry (delete from floder context menu)
        """
        import winreg

        root_registry = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
        contex_menu_key = winreg.OpenKey(root_registry, r'Directory\shell\\')
        try:
            fotosort_key = winreg.OpenKey(contex_menu_key, r'Open with FotoSort\\')
        except OSError:
            self.label_log.setText('Nothing to delete!')
            self.label_log.setStyleSheet('color: red')
        else:
            index = 0
            while True:
                try:
                    subkey = winreg.EnumKey(fotosort_key, index)
                    winreg.DeleteKey(fotosort_key, subkey)
                    index += 1
                except OSError:
                    break
            try:
                winreg.DeleteKey(contex_menu_key, r'Open with FotoSort')
            except OSError:
                self.label_log.setText('Error while deleting FotoSort from Windows registry!')
                self.label_log.setStyleSheet('color: red')
            else:
                self.label_log.setText('FotoSort successfully deleted from Windows registry!')
                self.label_log.setStyleSheet('color: blue')

    def file_extensions(self, file_type: str, accepted_only: bool) -> list:
        """
        Returns the list of file extensions from File extensions settings tab.
        :param file_type: should be 'EXIF', 'NON_EXIF' or 'ALL'
        :param accepted_only: if set True then only 'checked' extensions are returned
        :return: list of file extensions ('checked' or all) for a given file_type
        """
        extensions = []

        if file_type == 'EXIF':
            checkboxes = self.groupBox_exif.findChildren(QCheckBox)
        elif file_type == 'NON_EXIF':
            checkboxes = self.groupBox_nonexif.findChildren(QCheckBox)
        elif file_type == 'ALL':
            checkboxes = self.groupBox_exif.findChildren(QCheckBox) + \
                         self.groupBox_nonexif.findChildren(QCheckBox)
        else:
            return extensions

        if accepted_only:
            allowed_checkboxes = [box for box in checkboxes if box.isChecked()]
        else:
            allowed_checkboxes = checkboxes

        for check in allowed_checkboxes:
            values = check.text().split(',')
            for val in values:
                extensions.append(val.strip().lower())
                extensions.append(val.strip().upper())

        return extensions

    def is_exif_file(self, file_path: str) -> bool:
        """
        Returns True if file belongs to exif file group (e.g. jpeg photo).
        """
        ext = get_extension(file_path)
        exif_extensions = self.file_extensions(file_type='EXIF', accepted_only=False)
        return True if ext in exif_extensions else False

    def is_nonexif_file(self, file_path: str) -> bool:
        """
        Returns True if file belongs to non-exif file group (e.g. video)
        """
        ext = get_extension(file_path)
        nonexif_extensions = self.file_extensions(file_type='NON_EXIF', accepted_only=False)
        return True if ext in nonexif_extensions else False

    def is_allowed_file(self, file_path: str) -> bool:
        """
        Returns True if file has accepted ('checked') extension in Settings window.
        """
        ext = get_extension(file_path)
        allowed_extensions = self.file_extensions(file_type='ALL', accepted_only=True)
        return True if ext in allowed_extensions else False

    def check_all(self) -> None:
        """Marks all below checkBoxes according to the state of checkBox_check_all."""
        checked = True if self.checkBox_check_all.isChecked() else False

        exif_ext = self.groupBox_exif.findChildren(QCheckBox)
        non_exif_ext = self.groupBox_nonexif.findChildren(QCheckBox)

        for ext in exif_ext + non_exif_ext:
            ext.setCheckState(checked)


class AdminStateUnknownError(Exception):
    """Cannot determine whether the user is an admin."""
    pass


def get_extension(file: str) -> str:
    """Returns extensions of a given file."""
    basename = os.path.basename(file)
    extension = str(basename.split('.')[-1])
    return extension


def is_user_admin() -> bool:
    """
    Returns True if user has admin privileges.
    :raises AdminStateUnknownError
    """
    try:
        return os.getuid() == 0
    except AttributeError:
        pass
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() == 1
    except AttributeError:
        raise AdminStateUnknownError


def is_windows() -> bool:
    """Checks if current os platform is windows"""
    return True if sys.platform.startswith('win') else False
