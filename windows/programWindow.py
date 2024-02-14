from PyQt6 import QtCore, QtGui, QtWidgets


class UiProgramWindow(object):  # Класс, задающий параметры окна "О программе"
    def _setup_ui_(self, program_window):
        program_window.setObjectName("program_window")
        program_window.resize(745, 233)
        program_window.setMinimumSize(QtCore.QSize(745, 233))
        program_window.setMaximumSize(QtCore.QSize(745, 233))
        self.central_widget = QtWidgets.QWidget(parent=program_window)
        self.central_widget.setObjectName("central_widget")
        self.label_icon = QtWidgets.QLabel(parent=self.central_widget)
        self.label_icon.setGeometry(QtCore.QRect(10, 30, 181, 141))
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap("resources/splash_screen_pic.png"))
        self.label_icon.setObjectName("label_icon")
        self.groupBox_info = QtWidgets.QGroupBox(parent=self.central_widget)
        self.groupBox_info.setGeometry(QtCore.QRect(210, 30, 491, 141))
        self.groupBox_info.setTitle("")
        self.groupBox_info.setObjectName("groupBox_info")
        self.label_info = QtWidgets.QLabel(parent=self.groupBox_info)
        self.label_info.setGeometry(QtCore.QRect(10, 10, 471, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_info.setFont(font)
        self.label_info.setObjectName("label_info")
        self.groupBox_ver = QtWidgets.QGroupBox(parent=self.central_widget)
        self.groupBox_ver.setGeometry(QtCore.QRect(210, 190, 321, 21))
        self.groupBox_ver.setTitle("")
        self.groupBox_ver.setObjectName("groupBox_ver")
        self.label_ver = QtWidgets.QLabel(parent=self.groupBox_ver)
        self.label_ver.setGeometry(QtCore.QRect(120, 0, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_ver.setFont(font)
        self.label_ver.setObjectName("label_ver")
        self.exitButton = QtWidgets.QPushButton(parent=self.central_widget)
        self.exitButton.setGeometry(QtCore.QRect(580, 190, 75, 23))
        self.exitButton.setObjectName("exitButton")
        program_window.setCentralWidget(self.central_widget)

        self._retranslate_ui_(program_window)
        QtCore.QMetaObject.connectSlotsByName(program_window)
        self.exitButton.clicked.connect(program_window.close)

    def _retranslate_ui_(self, program_window):
        _translate = QtCore.QCoreApplication.translate
        program_window.setWindowTitle(_translate("program_window", "О программе"))
        self.label_info.setText(_translate("program_window",
                                           "<html><head/><body><p>Программа позволяет:</p><p>1. Строить графики функций(возможно несколько функций на одном графике)</p><p>2. Настройка отображения графиков</p><p>3. Сохранение графиков в виде изображения.</p></body></html>"))
        self.label_ver.setText(_translate("program_window", "Версия 1.0.0.2023"))
        self.exitButton.setText(_translate("program_window", "Выход"))
