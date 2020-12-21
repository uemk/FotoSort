# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_gui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 617)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("my_gui/../../.designer/backup/camera.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_table = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_table.setFont(font)
        self.groupBox_table.setObjectName("groupBox_table")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_table)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_subfolders = QtWidgets.QCheckBox(self.groupBox_table)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_subfolders.setFont(font)
        self.checkBox_subfolders.setObjectName("checkBox_subfolders")
        self.horizontalLayout.addWidget(self.checkBox_subfolders)
        self.button_clear = QtWidgets.QPushButton(self.groupBox_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_clear.sizePolicy().hasHeightForWidth())
        self.button_clear.setSizePolicy(sizePolicy)
        self.button_clear.setMinimumSize(QtCore.QSize(80, 25))
        self.button_clear.setMaximumSize(QtCore.QSize(80, 25))
        self.button_clear.setObjectName("button_clear")
        self.horizontalLayout.addWidget(self.button_clear)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.table_files = QtWidgets.QTableWidget(self.groupBox_table)
        self.table_files.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_files.sizePolicy().hasHeightForWidth())
        self.table_files.setSizePolicy(sizePolicy)
        self.table_files.setAcceptDrops(True)
        self.table_files.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_files.setObjectName("table_files")
        self.table_files.setColumnCount(3)
        self.table_files.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_files.setItem(2, 1, item)
        self.table_files.horizontalHeader().setHighlightSections(False)
        self.table_files.horizontalHeader().setStretchLastSection(True)
        self.table_files.verticalHeader().setVisible(True)
        self.table_files.verticalHeader().setDefaultSectionSize(35)
        self.verticalLayout_5.addWidget(self.table_files)
        self.verticalLayout.addWidget(self.groupBox_table)
        self.groupBox_modify_date = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_modify_date.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_modify_date.setFont(font)
        self.groupBox_modify_date.setCheckable(True)
        self.groupBox_modify_date.setChecked(False)
        self.groupBox_modify_date.setObjectName("groupBox_modify_date")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_modify_date)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_shift = QtWidgets.QHBoxLayout()
        self.horizontalLayout_shift.setObjectName("horizontalLayout_shift")
        self.label_shift = QtWidgets.QLabel(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_shift.sizePolicy().hasHeightForWidth())
        self.label_shift.setSizePolicy(sizePolicy)
        self.label_shift.setObjectName("label_shift")
        self.horizontalLayout_shift.addWidget(self.label_shift)
        self.verticalLayout_years = QtWidgets.QVBoxLayout()
        self.verticalLayout_years.setObjectName("verticalLayout_years")
        self.label_years = QtWidgets.QLabel(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_years.sizePolicy().hasHeightForWidth())
        self.label_years.setSizePolicy(sizePolicy)
        self.label_years.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_years.setObjectName("label_years")
        self.verticalLayout_years.addWidget(self.label_years)
        self.spinBox_years = QtWidgets.QSpinBox(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_years.sizePolicy().hasHeightForWidth())
        self.spinBox_years.setSizePolicy(sizePolicy)
        self.spinBox_years.setMinimum(-100)
        self.spinBox_years.setMaximum(100)
        self.spinBox_years.setObjectName("spinBox_years")
        self.verticalLayout_years.addWidget(self.spinBox_years)
        self.horizontalLayout_shift.addLayout(self.verticalLayout_years)
        self.verticalLayout_months = QtWidgets.QVBoxLayout()
        self.verticalLayout_months.setObjectName("verticalLayout_months")
        self.label_months = QtWidgets.QLabel(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_months.sizePolicy().hasHeightForWidth())
        self.label_months.setSizePolicy(sizePolicy)
        self.label_months.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_months.setObjectName("label_months")
        self.verticalLayout_months.addWidget(self.label_months)
        self.spinBox_months = QtWidgets.QSpinBox(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_months.sizePolicy().hasHeightForWidth())
        self.spinBox_months.setSizePolicy(sizePolicy)
        self.spinBox_months.setMinimum(-11)
        self.spinBox_months.setMaximum(11)
        self.spinBox_months.setObjectName("spinBox_months")
        self.verticalLayout_months.addWidget(self.spinBox_months)
        self.horizontalLayout_shift.addLayout(self.verticalLayout_months)
        self.verticalLayout_days = QtWidgets.QVBoxLayout()
        self.verticalLayout_days.setObjectName("verticalLayout_days")
        self.label_days = QtWidgets.QLabel(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_days.sizePolicy().hasHeightForWidth())
        self.label_days.setSizePolicy(sizePolicy)
        self.label_days.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_days.setObjectName("label_days")
        self.verticalLayout_days.addWidget(self.label_days)
        self.spinBox_days = QtWidgets.QSpinBox(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_days.sizePolicy().hasHeightForWidth())
        self.spinBox_days.setSizePolicy(sizePolicy)
        self.spinBox_days.setMinimum(-30)
        self.spinBox_days.setMaximum(30)
        self.spinBox_days.setObjectName("spinBox_days")
        self.verticalLayout_days.addWidget(self.spinBox_days)
        self.horizontalLayout_shift.addLayout(self.verticalLayout_days)
        self.verticalLayout_hours = QtWidgets.QVBoxLayout()
        self.verticalLayout_hours.setObjectName("verticalLayout_hours")
        self.label_hours = QtWidgets.QLabel(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_hours.sizePolicy().hasHeightForWidth())
        self.label_hours.setSizePolicy(sizePolicy)
        self.label_hours.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_hours.setObjectName("label_hours")
        self.verticalLayout_hours.addWidget(self.label_hours)
        self.spinBox_hours = QtWidgets.QSpinBox(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_hours.sizePolicy().hasHeightForWidth())
        self.spinBox_hours.setSizePolicy(sizePolicy)
        self.spinBox_hours.setMinimum(-23)
        self.spinBox_hours.setMaximum(23)
        self.spinBox_hours.setObjectName("spinBox_hours")
        self.verticalLayout_hours.addWidget(self.spinBox_hours)
        self.horizontalLayout_shift.addLayout(self.verticalLayout_hours)
        self.verticalLayout_minutes = QtWidgets.QVBoxLayout()
        self.verticalLayout_minutes.setObjectName("verticalLayout_minutes")
        self.label_minutes = QtWidgets.QLabel(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_minutes.sizePolicy().hasHeightForWidth())
        self.label_minutes.setSizePolicy(sizePolicy)
        self.label_minutes.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_minutes.setObjectName("label_minutes")
        self.verticalLayout_minutes.addWidget(self.label_minutes)
        self.spinBox_minutes = QtWidgets.QSpinBox(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_minutes.sizePolicy().hasHeightForWidth())
        self.spinBox_minutes.setSizePolicy(sizePolicy)
        self.spinBox_minutes.setMinimum(-59)
        self.spinBox_minutes.setMaximum(59)
        self.spinBox_minutes.setObjectName("spinBox_minutes")
        self.verticalLayout_minutes.addWidget(self.spinBox_minutes)
        self.horizontalLayout_shift.addLayout(self.verticalLayout_minutes)
        self.verticalLayout_seconds = QtWidgets.QVBoxLayout()
        self.verticalLayout_seconds.setObjectName("verticalLayout_seconds")
        self.label_seconds = QtWidgets.QLabel(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_seconds.sizePolicy().hasHeightForWidth())
        self.label_seconds.setSizePolicy(sizePolicy)
        self.label_seconds.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_seconds.setObjectName("label_seconds")
        self.verticalLayout_seconds.addWidget(self.label_seconds)
        self.spinBox_seconds = QtWidgets.QSpinBox(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_seconds.sizePolicy().hasHeightForWidth())
        self.spinBox_seconds.setSizePolicy(sizePolicy)
        self.spinBox_seconds.setMinimum(-59)
        self.spinBox_seconds.setMaximum(59)
        self.spinBox_seconds.setObjectName("spinBox_seconds")
        self.verticalLayout_seconds.addWidget(self.spinBox_seconds)
        self.horizontalLayout_shift.addLayout(self.verticalLayout_seconds)
        self.verticalLayout_buttons = QtWidgets.QVBoxLayout()
        self.verticalLayout_buttons.setObjectName("verticalLayout_buttons")
        self.button_simulate = QtWidgets.QPushButton(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_simulate.sizePolicy().hasHeightForWidth())
        self.button_simulate.setSizePolicy(sizePolicy)
        self.button_simulate.setMinimumSize(QtCore.QSize(111, 25))
        self.button_simulate.setMaximumSize(QtCore.QSize(111, 25))
        self.button_simulate.setObjectName("button_simulate")
        self.verticalLayout_buttons.addWidget(self.button_simulate)
        self.button_modify_date = QtWidgets.QPushButton(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_modify_date.sizePolicy().hasHeightForWidth())
        self.button_modify_date.setSizePolicy(sizePolicy)
        self.button_modify_date.setMinimumSize(QtCore.QSize(111, 25))
        self.button_modify_date.setMaximumSize(QtCore.QSize(111, 25))
        self.button_modify_date.setObjectName("button_modify_date")
        self.verticalLayout_buttons.addWidget(self.button_modify_date)
        self.horizontalLayout_shift.addLayout(self.verticalLayout_buttons)
        self.verticalLayout_2.addLayout(self.horizontalLayout_shift)
        self.gridLayout_date_from_name = QtWidgets.QGridLayout()
        self.gridLayout_date_from_name.setObjectName("gridLayout_date_from_name")
        self.label_date_from_name = QtWidgets.QLabel(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date_from_name.sizePolicy().hasHeightForWidth())
        self.label_date_from_name.setSizePolicy(sizePolicy)
        self.label_date_from_name.setObjectName("label_date_from_name")
        self.gridLayout_date_from_name.addWidget(self.label_date_from_name, 0, 0, 1, 1)
        self.button_date_from_name = QtWidgets.QPushButton(self.groupBox_modify_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_date_from_name.sizePolicy().hasHeightForWidth())
        self.button_date_from_name.setSizePolicy(sizePolicy)
        self.button_date_from_name.setObjectName("button_date_from_name")
        self.gridLayout_date_from_name.addWidget(self.button_date_from_name, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_date_from_name)
        self.verticalLayout.addWidget(self.groupBox_modify_date)
        self.groupBox_rename = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_rename.setFont(font)
        self.groupBox_rename.setFocusPolicy(QtCore.Qt.NoFocus)
        self.groupBox_rename.setObjectName("groupBox_rename")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_rename)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.button_rename = QtWidgets.QPushButton(self.groupBox_rename)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_rename.sizePolicy().hasHeightForWidth())
        self.button_rename.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button_rename.setFont(font)
        self.button_rename.setObjectName("button_rename")
        self.verticalLayout_4.addWidget(self.button_rename)
        self.text_logs = QtWidgets.QTextBrowser(self.groupBox_rename)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_logs.sizePolicy().hasHeightForWidth())
        self.text_logs.setSizePolicy(sizePolicy)
        self.text_logs.setStyleSheet("color: rgb(32, 74, 135);")
        self.text_logs.setObjectName("text_logs")
        self.verticalLayout_4.addWidget(self.text_logs)
        self.verticalLayout.addWidget(self.groupBox_rename)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_browse = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.action_browse.setFont(font)
        self.action_browse.setObjectName("action_browse")
        self.action_quit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.action_quit.setFont(font)
        self.action_quit.setObjectName("action_quit")
        self.action_help = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.action_help.setFont(font)
        self.action_help.setObjectName("action_help")
        self.action_about = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.action_about.setFont(font)
        self.action_about.setObjectName("action_about")
        self.action_settings = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.action_settings.setFont(font)
        self.action_settings.setObjectName("action_settings")
        self.menuFile.addAction(self.action_browse)
        self.menuFile.addAction(self.action_settings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)
        self.menuHelp.addAction(self.action_help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action_about)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.action_quit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FotoSort"))
        self.groupBox_table.setTitle(_translate("MainWindow", "Add JPEG photos and/or video files:"))
        self.checkBox_subfolders.setText(_translate("MainWindow", "Include subfolders"))
        self.button_clear.setText(_translate("MainWindow", "CLEAR"))
        item = self.table_files.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.table_files.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.table_files.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.table_files.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.table_files.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.table_files.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.table_files.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.table_files.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.table_files.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.table_files.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.table_files.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "[Error]"))
        item = self.table_files.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Current date"))
        item = self.table_files.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "File"))
        __sortingEnabled = self.table_files.isSortingEnabled()
        self.table_files.setSortingEnabled(False)
        self.table_files.setSortingEnabled(__sortingEnabled)
        self.groupBox_modify_date.setTitle(_translate("MainWindow", "Enable date-time modifications:"))
        self.label_shift.setText(_translate("MainWindow", "<html><head/><body><p>Shift<br/>date-<br/>time:</p></body></html>"))
        self.label_years.setText(_translate("MainWindow", "Years:"))
        self.spinBox_years.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_months.setText(_translate("MainWindow", "Months:"))
        self.label_days.setText(_translate("MainWindow", "Days:"))
        self.label_hours.setText(_translate("MainWindow", "Hours:"))
        self.label_minutes.setText(_translate("MainWindow", "Min:"))
        self.label_seconds.setText(_translate("MainWindow", "Sec:"))
        self.button_simulate.setText(_translate("MainWindow", "Simulate"))
        self.button_modify_date.setText(_translate("MainWindow", "MODIFY DATE"))
        self.label_date_from_name.setText(_translate("MainWindow", "Set file date-time from filename:"))
        self.button_date_from_name.setText(_translate("MainWindow", "DATE FROM FILENAME"))
        self.groupBox_rename.setTitle(_translate("MainWindow", "Rename media files (format: date_time_originalName):"))
        self.button_rename.setText(_translate("MainWindow", "RENAME"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.action_browse.setText(_translate("MainWindow", "Choose folder..."))
        self.action_quit.setText(_translate("MainWindow", "Quit"))
        self.action_quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_help.setText(_translate("MainWindow", "Help"))
        self.action_help.setShortcut(_translate("MainWindow", "F1"))
        self.action_about.setText(_translate("MainWindow", "About"))
        self.action_settings.setText(_translate("MainWindow", "Settings"))
