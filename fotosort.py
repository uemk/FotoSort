#! /usr/bin/env python3

"""
This program is a GUI desktop application which main purpose is to rename
photo and video files by prepending datetime information (date of taking a photo/video)
in front of actual filename. In case of JPEG photo Exif datetime data is used
while in case of video - date modified file property.

This allows to sort media files chronologically by filename
even if file date changes after copying or moving between different locations.

Additionally, program allows also to modify Exif datetime information of jpg files
and date modified file property of video files.

Author: Emilia Dobkowska
"""
import sys
import os
import glob
import datetime
import time

import piexif
import webbrowser

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QFileDialog

from my_gui import main_window, dialog_about
import settings


class FotoSortApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self) -> None:
        """Initializes GUI and connects actions to specific buttons and checkboxes."""
        super(FotoSortApp, self).__init__()
        self.setupUi(self)

        self.files = []
        self.path_dir = ''
        self.files_temp = []

        # variables to store logs
        self.renamed = 0
        self.errors = 0
        self.unchanged = 0
        self.error_files = []

        # settings and about dialogs initialization
        self.about = QtWidgets.QDialog()
        self.settings = settings.Settings()
        self.settings.setupUi(self.settings)
        self.settings.init()

        # connect actions
        self.button_clear.clicked.connect(self.clear)
        self.button_simulate.clicked.connect(self.simulate)
        self.button_modify_date.clicked.connect(self.modify_date)
        self.button_date_from_name.clicked.connect(self.set_date_from_filename)
        self.button_rename.clicked.connect(self.rename_files)

        self.action_browse.triggered.connect(self.browse)
        self.action_settings.triggered.connect(self.show_settings)
        self.action_help.triggered.connect(self.show_help)
        self.action_about.triggered.connect(self.show_about)

        # handles launching an app with system arguments (directory path)
        self.open_with_path = ''
        if len(sys.argv) >= 2:
            self.open_with_path = ' '.join(sys.argv[1:])
            self.open_with(self.open_with_path)

    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
        """Accepts drag event if contains urls."""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        """Loads dragged & dropped photos/videos and displays them in the GUI table."""
        files = []
        for url in event.mimeData().urls():
            path = str(url)
            if is_windows():
                count_left = len("PyQt5.QtCore.QUrl('file:///")
            else:  # linux
                count_left = len("PyQt5.QtCore.QUrl('file://")
            count_right = len(path) - len("')")
            path = path[count_left:count_right]

            if self.settings.is_allowed_file(path):
                files.append(path)
            else:
                dir_path = path + '/'
                self.files_temp.clear()
                files_dir = self.find_files_in_dir(dir_path)
                files += files_dir

        self.fill_the_table(files)
        self.log_clear()

    def browse(self) -> None:
        """
        Implements 'Choose folder...' action in menu bar. Opens file dialog window to choose
        directory with photos/videos. Displays files from selected dir in the GUI table.
        """
        path = str(
            QFileDialog.getExistingDirectory(QFileDialog(),
                                             'Select a folder with photos or videos:', 'C:\\',
                                             QFileDialog.ShowDirsOnly))
        path_dir = path + "/"
        self.files_temp.clear()
        files_dir = self.find_files_in_dir(path_dir)
        self.fill_the_table(files_dir)
        self.log_clear()

    def clear(self) -> None:
        """
        Implements 'clear' button functionality.
        Removes files from the GUI table and clears logs
        """
        self.clear_table()
        self.log_clear()

    def simulate(self) -> None:
        """
        Implements 'simulate' button functionality.
        Displays the calculated new date of each file but does not modify the files.
        """
        if not self.files:
            self.set_statusbar('Please, add files!', 'red')
        elif not self.is_date_to_be_modified():
            self.set_statusbar('Please shift date/time!', 'red')
        else:
            for i, file in enumerate(self.files):
                simulation_result = ''
                if self.settings.is_exif_file(file):
                    time_exif = get_exif_time(file)
                    if time_exif:
                        shifted = self.get_shifted_exif_date(time_exif)
                        simulation_result = format_exif_datetime(shifted)
                    else:
                        simulation_result = '#error - no exif time'

                elif self.settings.is_nonexif_file(file):
                    shifted = self.get_shifted_file_date(file)
                    simulation_result = shifted.toString("yyyy-MM-dd HH:mm:ss")

                self.table_files.setItem(i, 0, QTableWidgetItem(simulation_result))

            self.table_files.setHorizontalHeaderLabels(['Simulated', 'Current date', 'File'])
            self.set_statusbar('Simulation performed!', 'blue')

    def modify_date(self) -> None:
        """
        Implements 'modify date' button functionality.
        Modifies Exif time field of jpeg photos and file modification date of video files.
        """
        self.log_clear()
        self.table_files.setHorizontalHeaderLabels(['[Error]', 'Current date', 'File'])

        if not self.files:
            self.set_statusbar('Please add files to modify!', 'red')
        elif not self.is_date_to_be_modified():
            self.set_statusbar('Please shift date/time!', 'red')
        else:
            self.setEnabled(False)
            self.set_statusbar('Please wait...', 'blue')
            self.statusbar.repaint()

            for index, file in enumerate(self.files):
                # prevents my_gui freeze during function execution
                QtCore.QCoreApplication.processEvents()
                current_date = ''
                error_msg = ''
                if self.settings.is_exif_file(file):
                    time_exif = get_exif_time(file)
                    fail = '#error - failed to modify exif time'
                    error_msg = '' if time_exif else fail
                    if time_exif:
                        shifted = self.get_shifted_exif_date(time_exif)
                        success = set_exif_time(file, shifted)
                        error_msg = '' if success else fail
                        current_date = exif_to_string(file)

                elif self.settings.is_nonexif_file(file):
                    self.change_file_date(file)
                    current_date = get_modification_date(file)

                date_cell = QTableWidgetItem(current_date)
                error_cell = QTableWidgetItem(error_msg)
                f_bold = QFont()
                f_bold.setBold(True)
                error_cell.setFont(f_bold)
                if not error_msg:
                    date_cell.setFont(f_bold)
                self.table_files.setItem(index, 1, date_cell)
                self.table_files.setItem(index, 0, error_cell)

            self.set_statusbar('Modify date executed!', 'blue')
            self.setEnabled(True)

    def set_date_from_filename(self) -> None:
        """
        Implements 'set date from name' button functionality.
        Sets the exif time field (for jpeg photo)and file modified date (for video)
        based on date included in the filename if exists.
        """
        self.log_clear()
        self.table_files.setHorizontalHeaderLabels(['[Error]', 'Current date', 'File'])
        self.setEnabled(False)
        self.set_statusbar('Please wait...', 'blue')
        self.statusbar.repaint()

        for i, file in enumerate(self.files):
            # prevents my_gui freeze during function execution
            QtCore.QCoreApplication.processEvents()
            original_name = str(os.path.basename(file))
            original_strip = str(original_name).replace('_', '').replace(' ', '')
            date = original_strip[:14]
            error_msg = ''
            current_date = ''
            try:
                if len(date) < 14 or not date.isdigit():
                    raise NoDateInFileName

                year = date[:4]
                month = date[4:6]
                day = date[6:8]
                hour = date[8:10]
                minute = date[10:12]
                second = date[12:14]

                if self.settings.is_exif_file(file):
                    time_exif = f'{year}:{month}:{day} {hour}:{minute}:{second}'
                    success = set_exif_time(file, time_exif)
                    error_msg = '' if success else '#error - failed to modify exif time'
                    current_date = exif_to_string(file)
                elif self.settings.is_nonexif_file(file):
                    date_from_filename = datetime.datetime(year=int(year),
                                                           month=int(month),
                                                           day=int(day),
                                                           hour=int(hour),
                                                           minute=int(minute),
                                                           second=int(second))
                    self.change_file_date_with_new_datetime(file, date_from_filename)
                    current_date = get_modification_date(file)
            except NoDateInFileName:
                error_msg = '#error - no date in filename'
                if self.settings.is_exif_file(file):
                    current_date = exif_to_string(file)
                elif self.settings.is_nonexif_file(file):
                    current_date = get_modification_date(file)
            finally:
                date_cell = QTableWidgetItem(current_date)
                error_cell = QTableWidgetItem(error_msg)
                f_bold = QFont()
                f_bold.setBold(True)
                error_cell.setFont(f_bold)
                if not error_msg:
                    date_cell.setFont(f_bold)
                self.table_files.setItem(i, 1, date_cell)
                self.table_files.setItem(i, 0, error_cell)

        self.set_statusbar('Set date based on filename executed!', 'blue') if self.files else \
            self.set_statusbar('Please add files to modify!', 'red')

        self.setEnabled(True)

    def rename_files(self) -> None:
        """
        Implements 'rename' button functionality. Main function of the application.
        Prepends the date of taking the photo or video (exif for jpeg, time modified for video)
        to the filename.
        """

        self.table_files.setHorizontalHeaderLabels(['[Error]', 'Current date', 'File'])

        self.text_logs.clear()
        self.renamed = 0
        self.errors = 0
        self.unchanged = 0
        self.error_files = []

        if not self.files:
            self.set_statusbar('Please, add files to rename!', 'red')
        else:
            self.setEnabled(False)
            self.set_statusbar('Please wait...', 'blue')
            self.statusbar.repaint()

            for file in self.files:
                # prevents my_gui freeze during function execution
                QtCore.QCoreApplication.processEvents()
                self.rename_single_file(file)

            self.set_statusbar('Rename files executed!', 'blue')

            self.text_logs.append('Total number of files: ' + str(len(self.files)))
            self.text_logs.append('Renamed: ' + str(self.renamed))
            self.text_logs.append('Unchanged: ' + str(self.unchanged))
            self.text_logs.append('Errors: ' + str(self.errors))
            if self.errors > 0:
                self.text_logs.append('\nFailed to rename the following files (none or wrong exif): ')
                for ph in self.error_files:
                    self.text_logs.append(ph)

            self.clear_table()
            self.setEnabled(True)

    def rename_single_file(self, file: str) -> None:
        """
        Renames single file with date information. Called by 'rename_files' function.
        :param file: file path (photo or video)
        """
        try:
            time_file = ''
            if self.settings.is_exif_file(file):
                time_exif = get_exif_time(file)
                if time_exif:
                    time_file = str(time_exif).replace(':', '').replace(' ', '')
                else:
                    raise KeyError

            elif self.settings.is_nonexif_file(file):
                time_file = get_modification_date(file).replace('-', '').replace(':', '').replace(' ', '')

            time_file = time_file[:14]  # get only digits from file datetime info

            if time_file == '0' * 14:  # zeros in exif date
                raise ValueError

            extension = str(settings.get_extension(file))
            time_sep = time_file[:8] + '_' + time_file[8:] + '_'
            path = str(os.path.dirname(file))
            original_name = str(os.path.basename(file))
            original_strip = str(original_name).replace('_', '').replace(' ', '')

            if time_sep == original_name[:len(time_sep)]:  # no need to change file name
                self.unchanged += 1
            else:
                if original_strip[:14].isdigit():
                    if len(original_name) > len(time_sep) + len('.') + len(extension):
                        file_ren = time_sep + original_name[len(time_sep):]
                    else:
                        file_ren = time_sep + extension
                else:  # exif date was not yet added to file name
                    file_ren = time_sep + original_name

                file_ren = os.path.join(path, file_ren)
                os.rename(file, file_ren)
                self.renamed += 1

        except (KeyError, ValueError):
            self.errors += 1
            self.error_files.append(file)

        except FileExistsError:
            self.unchanged += 1

    def find_files_in_dir(self, path_dir: str) -> list:
        """
        Finds all the photos and videos in a given directory. Called be 'browse' and 'dropEvent' functions.
        :param path_dir: path to directory containing photos/videos
        :return: list of found photos and videos
        """
        dir_files = []
        allowed_extensions = self.settings.file_extensions(file_type='ALL', accepted_only=True)

        for ext in allowed_extensions:
            # index for allowed files
            file_index_ext = filter(os.path.isfile, glob.glob(path_dir + '*.' + ext))
            dir_files_ext = [file for file in file_index_ext]
            dir_files += dir_files_ext

        for df in dir_files:
            df = str(df).replace('\\', '/')
            self.files_temp.append(df)

        if self.checkBox_subfolders.isChecked():
            subfolders = [item.path for item in os.scandir(path_dir) if item.is_dir()]
            for sf in subfolders:
                # recurrent function call
                self.find_files_in_dir(str(sf) + '/')

        return self.files_temp

    def fill_the_table(self, files: list) -> None:
        """
        Displays a given list of files in the GUI table. Called by 'browse' and 'dropEvent' functions.
        :param files: list of photos and/or videos
        """
        self.setEnabled(False)
        self.set_statusbar('Please wait...', 'blue')
        self.statusbar.repaint()

        for file in files:
            index = len(self.files)
            if file not in self.files:
                # prevents my_gui freeze during function execution
                QtCore.QCoreApplication.processEvents()
                self.files.append(str(file))
                self.table_files.setRowCount(index + 1)
                self.table_files.setItem(index, 2, QTableWidgetItem(str(file)))
                if self.settings.is_exif_file(file):
                    self.table_files.setItem(index, 1, QTableWidgetItem(exif_to_string(file)))
                elif self.settings.is_nonexif_file(file):
                    self.table_files.setItem(index, 1, QTableWidgetItem(get_modification_date(file)))

        self.statusbar.showMessage('')
        self.setEnabled(True)

    def change_file_date(self, file: str) -> None:
        """
        Changes access and modification date of file based on shifted date/time values.
        Called by 'modify_date' function.
        :param file: video file path
        """
        new = self.get_shifted_file_date(file)
        date_time = datetime.datetime.fromtimestamp(new.toTime_t())

        self.change_file_date_with_new_datetime(file, date_time)

    @staticmethod
    def change_file_date_with_new_datetime(file: str, date_time: datetime.datetime) -> None:
        """
        Changes access and modification date of file based on a given datetime.
        Called by 'set_date_from_filename' function.
        :param file: video file path
        :param date_time: new datetime
        """
        new_date = time.mktime(date_time.timetuple())
        os.utime(file, (new_date, new_date))  # change access and modification dates

    def get_shifted_exif_date(self, exif: str) -> str:
        """
        Returns properly formatted new exif datetime based on spin boxes values calculation.
        :param exif: current exif datetime (jpeg)
        :return: new exif datetime
        """
        current = QDateTime.fromString(exif, "yyyy:MM:dd HH:mm:ss")
        new = self.calculate_new_datetime(current)
        new_date_time = new.toString("yyyy:MM:dd HH:mm:ss")
        return new_date_time

    def get_shifted_file_date(self, file: str) -> QDateTime:
        """
        Returns new file modification date based on spin boxes values calculation.
        :param file: file path (video)
        :return: new datetime
        """
        current = QDateTime.fromSecsSinceEpoch(int(os.path.getmtime(file)))
        new = self.calculate_new_datetime(current)
        return new

    def calculate_new_datetime(self, current: QDateTime) -> QDateTime:
        """
        Calculates new datetime based on values in spin boxes.
        :param current: current datetime
        :return: new datetime
        """
        new = current \
            .addSecs(self.spinBox_seconds.value()) \
            .addSecs(self.spinBox_minutes.value() * 60) \
            .addSecs(self.spinBox_hours.value() * 3600) \
            .addDays(self.spinBox_days.value()) \
            .addMonths(self.spinBox_months.value()) \
            .addYears(self.spinBox_years.value())
        return new

    def is_date_to_be_modified(self) -> bool:
        """
        Indicates if date of the file shall be modified. Called by 'modify_date' function.
        :return: True if at least one of spin boxes values different than 0 (otherwise False)
        """
        if self.spinBox_years.value() != 0 \
                or self.spinBox_months.value() != 0 \
                or self.spinBox_days.value() != 0 \
                or self.spinBox_hours.value() != 0 \
                or self.spinBox_minutes.value() != 0 \
                or self.spinBox_seconds.value() != 0:
            return True
        else:
            return False

    def clear_table(self) -> None:
        """Removes files from the GUI table."""
        self.table_files.clear()
        self.table_files.setHorizontalHeaderLabels(['[Error]', 'Current date', 'File'])
        self.files.clear()
        self.files_temp.clear()

    def log_clear(self) -> None:
        """Resets the GUI statusbar and textBox 'text_logs'."""
        self.statusbar.showMessage('')
        self.text_logs.clear()

    def set_statusbar(self, message: str, color: str) -> None:
        """Sets the window statusbar message text and color."""
        self.statusbar.showMessage(message)
        self.statusbar.setStyleSheet(f'color: {color}')

    def open_with(self, path: str) -> None:
        """
        Called when program launched with system arguments.
        Loads photos and videos from a given directory while launching the application.
        :param path: directory path
        """
        dir_path = path + "/"
        print(dir_path)
        files = self.find_files_in_dir(dir_path)
        self.fill_the_table(files)

    def show_settings(self) -> None:
        """Shows settings dialog window"""
        self.settings.show()

    @staticmethod
    def show_help() -> None:
        """Displays help -> README document"""
        url = 'https://github.com/uemk/FotoSort/blob/main/README.md'
        webbrowser.open(url, new=2)  # open in new tab

    def show_about(self) -> None:
        """Shows 'About' dialog window"""
        self.about = QtWidgets.QDialog()
        ui = dialog_about.Ui_Dialog()
        ui.setupUi(self.about)
        self.about.show()


def get_exif_time(photo: str) -> str:
    """Returns exif datetime field of a given jpg photo."""
    time_exif = ''
    original = piexif.ExifIFD.DateTimeOriginal
    digitized = piexif.ExifIFD.DateTimeDigitized
    try:
        exif_dict = piexif.load(photo)
        try:
            time_exif = exif_dict['Exif'][original].decode('utf-8')
        except KeyError:
            time_exif = exif_dict['Exif'][digitized].decode('utf-8')
    except KeyError:
        print('No time info in exif')
    except Exception as exc:
        print(exc)
    finally:
        return time_exif


def set_exif_time(photo: str, exif_time: str) -> bool:
    """Sets exif datetime information for a jgp photo."""
    success = False
    original = piexif.ExifIFD.DateTimeOriginal
    digitized = piexif.ExifIFD.DateTimeDigitized
    try:
        exif_dict = piexif.load(photo)
        try:
            exif_dict['Exif'][original] = exif_time.encode()
        except KeyError:
            exif_dict['Exif'][digitized] = exif_time.encode()
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, photo)
    except (KeyError, ValueError):
        print('Error setting exif time')
    except Exception as exc:
        print(exc)
    else:
        success = True
    finally:
        return success


def exif_to_string(photo: str) -> str:
    """Formats exif datetime string for a given photo."""
    time_exif = get_exif_time(photo)
    if time_exif:
        return format_exif_datetime(time_exif)
    return ''


def format_exif_datetime(exif_str: str) -> str:
    """Formats exif datetime string: YYYY:MM:dd hh:mm:ss"""
    date = str(exif_str).split(' ', 1)
    return str(date[0].replace(':', '-') + ' ' + date[1])


def get_modification_date(filename: str) -> str:
    """Returns modification date of a given file."""
    t = os.path.getmtime(filename)
    return str(datetime.datetime.fromtimestamp(t))[:19]


def is_linux() -> bool:
    """Checks if current os platform is linux."""
    return True if sys.platform == 'linux' else False


def is_windows() -> bool:
    """Checks if current os platform is windows"""
    return True if sys.platform.startswith('win') else False


class NoDateInFileName(Exception):
    """No datetime information prepended to the filename"""
    pass


def main():

    app = QApplication(sys.argv)
    form = FotoSortApp()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
